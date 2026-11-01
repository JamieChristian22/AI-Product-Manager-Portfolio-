"""Exact CSV/HTML parity and accessible offline dashboard regression tests."""
from __future__ import annotations
import csv
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

from tools.validate_ai_products import ROOT, PROJECTS

HTML=ROOT/"demo/ai-product-evidence.html"
SECTIONS={
    "dataset":"Data_Analytics/dataset.csv",
    "model_metrics":"AI_Model/evaluation_metrics.csv",
    "monitoring":"Monitoring/monitoring_thresholds.csv",
    "risks":"AI_Risk_Management/risk_register.csv",
    "acceptance":"Testing/acceptance_tests.csv",
}

class HTMLAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set()
        self.labels=set()
        self.external_scripts=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if "id" in a:
            if a["id"] in self.ids:
                raise AssertionError("Duplicate element ID")
            self.ids.add(a["id"])
        if tag=="label" and "for" in a:
            self.labels.add(a["for"])
        if tag=="script" and "src" in a:
            self.external_scripts.append(a["src"])

class EvidenceDashboardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page=HTML.read_text(encoding="utf-8")
        match=re.search(r'<script id="evidence-data" type="application/json">(.*?)</script>',cls.page,re.DOTALL)
        if not match:
            raise AssertionError("Dashboard embedded evidence missing")
        cls.data=json.loads(match.group(1))

    def test_exact_committed_csv_parity_every_project_and_category(self):
        self.assertEqual(set(self.data["projects"]),set(PROJECTS))
        for project,fields in self.data["projects"].items():
            with self.subTest(project=project):
                for kind,relative in SECTIONS.items():
                    path=ROOT/project/relative
                    if path.is_file():
                        with path.open(encoding="utf-8-sig",newline="") as f:
                            source=list(csv.DictReader(f))
                    else:
                        source=[]
                    self.assertEqual(fields[kind],source,(project,kind))
        self.assertEqual(self.data["schema_version"],1)

    def test_dashboard_reports_reused_samples_and_unverified_results(self):
        self.assertIn("reused",self.page)
        self.assertIn("not independently executed",self.page)
        self.assertIn("no live deployment",self.data["disclosure"].lower())
        self.assertEqual(len(self.data["projects"][PROJECTS[3]]["acceptance"]),12)

    def test_safe_offline_rendering_and_accessible_filters(self):
        audit=HTMLAudit()
        audit.feed(self.page)
        self.assertTrue({"project","section","search"}.issubset(audit.labels))
        self.assertTrue({"project","section","search"}.issubset(audit.ids))
        self.assertTrue({"records","sources"}.issubset(audit.ids))
        self.assertIn('aria-live="polite"',self.page)
        self.assertIn("textContent",self.page)
        self.assertIn("replaceChildren",self.page)
        self.assertNotIn("innerHTML",self.page)
        self.assertNotIn("fetch(",self.page)
        self.assertFalse(audit.external_scripts)
