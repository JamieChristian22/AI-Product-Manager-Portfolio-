"""Fail-closed validation of synthetic AI PM examples and their numerical gates."""
from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from tools.validate_ai_products import (
    ROOT, PROJECTS, MODEL_COLUMNS, DATA_COLUMNS, MONITOR_COLUMNS,
    evaluate_gate, read_csv, validate_sessions, validate_model_metrics,
    validate_monitor, validate_risks, sql_verify, validate,
)

class AIProductEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sessions=read_csv(ROOT / PROJECTS[0] / "Data_Analytics/dataset.csv", DATA_COLUMNS)
        cls.model_rows=read_csv(ROOT / PROJECTS[0] / "AI_Model/evaluation_metrics.csv", MODEL_COLUMNS)
        cls.monitor_rows=read_csv(ROOT / PROJECTS[2] / "Monitoring/monitoring_thresholds.csv", MONITOR_COLUMNS)

    def test_four_projects_and_reused_synthetic_fixtures_disclosed(self):
        result=validate()
        self.assertEqual(len(result["projects"]),4)
        self.assertTrue(result["shared_five_row_sample_across_all_projects"])
        self.assertTrue(result["shared_evaluation_table_in_first_two_projects"])
        self.assertEqual(result["sql_check_total"],16)
        self.assertFalse(result["live_model_validation"])
        self.assertFalse(result["live_experiment_outcomes_verified"])

    def test_independently_calculated_kpis(self):
        k=validate_sessions(self.sessions)
        self.assertEqual(k["sample_sessions"],5)
        self.assertEqual(k["sample_conversions"],3)
        self.assertEqual(k["conversion_rate"],0.6)
        self.assertEqual(k["mean_session_length"],356)
        self.assertEqual(k["retention_share"],0.6)
        self.assertEqual(k["revenue"],460.49)

    def test_committed_sql_agrees_with_python_for_all_four_projects(self):
        for p in PROJECTS:
            with self.subTest(project=p):
                rows=read_csv(ROOT / p / "Data_Analytics/dataset.csv",DATA_COLUMNS)
                self.assertEqual(sql_verify(ROOT / p,rows,validate_sessions(rows)),4)

    def test_duplicate_sample_user_is_rejected(self):
        rows=copy.deepcopy(self.sessions)
        rows[1]["user_id"]=rows[0]["user_id"]
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            validate_sessions(rows)

    def test_nonbinary_conversion_and_revenue_on_nonconversion_are_rejected(self):
        rows=copy.deepcopy(self.sessions)
        rows[1]["conversion"]="3"
        with self.assertRaisesRegex(ValueError,"binary"):
            validate_sessions(rows)
        rows=copy.deepcopy(self.sessions)
        rows[1]["revenue"]="5"
        with self.assertRaisesRegex(ValueError,"Nonconverting"):
            validate_sessions(rows)

    def test_invalid_negative_or_nonfinite_session_rejected(self):
        for val in ["-1","NaN","Infinity"]:
            rows=copy.deepcopy(self.sessions)
            rows[0]["session_length"]=val
            with self.assertRaises(ValueError):
                validate_sessions(rows)

    def test_model_gates_derived_not_accepted_at_face_value(self):
        r=validate_model_metrics(self.model_rows)
        self.assertEqual(r["gate_count"],18)
        self.assertEqual(r["calculated_passes"],18)
        self.assertEqual(r["calculated_failures"],0)

    def test_strict_comparisons_and_zero_policy_violations(self):
        self.assertTrue(evaluate_gate(">=0.28","0.28"))
        self.assertFalse(evaluate_gate(">0.28","0.28"))
        self.assertTrue(evaluate_gate("<=0.16","0.146"))
        self.assertTrue(evaluate_gate("0","0"))
        self.assertFalse(evaluate_gate("0","1"))

    def test_model_metric_false_pass_fails_closed(self):
        rows=copy.deepcopy(self.model_rows)
        rows[0]["result"]="0.001"
        with self.assertRaisesRegex(ValueError,"conflicts"):
            validate_model_metrics(rows)

    def test_duplicate_model_gate_fails_closed(self):
        rows=copy.deepcopy(self.model_rows)
        rows.append(copy.deepcopy(rows[0]))
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            validate_model_metrics(rows)

    def test_bad_gate_string_rejected(self):
        with self.assertRaisesRegex(ValueError,"Unsupported"):
            evaluate_gate("run_eval()","1")

    def test_monitor_thresholds_validate(self):
        m=validate_monitor(self.monitor_rows)
        self.assertEqual(m["metric_count"],11)
        self.assertEqual(sum(m["sample_severity_counts"].values()),11)

    def test_monitor_duplicate_and_ambiguous_boundaries_rejected(self):
        rows=copy.deepcopy(self.monitor_rows)
        rows[0]["Critical"]=rows[0]["Warning"]
        with self.assertRaisesRegex(ValueError,"ambiguous"):
            validate_monitor(rows)
        rows=copy.deepcopy(self.monitor_rows)
        rows.append(copy.deepcopy(rows[0]))
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            validate_monitor(rows)

    def test_risk_scores_are_recomputed(self):
        rows=read_csv(ROOT / PROJECTS[3] / "AI_Risk_Management/risk_register.csv",
                      {"Risk_ID","Likelihood","Impact","Score"})
        self.assertEqual(validate_risks(rows)["risk_scores_reconciled"],36)
        bad=copy.deepcopy(rows)
        bad[0]["Score"]="3"
        with self.assertRaisesRegex(ValueError,"inconsistent"):
            validate_risks(bad)

    def test_duplicate_risk_ids_rejected(self):
        rows=read_csv(ROOT / PROJECTS[2] / "AI_Risk_Management/risk_register.csv",
                      {"Risk_ID","Likelihood","Impact","Score"})
        rows.append(copy.deepcopy(rows[0]))
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            validate_risks(rows)

    def test_acceptance_results_accurately_labelled_as_unverified(self):
        result=validate()
        acceptance=result["projects"][PROJECTS[3]]["documented_acceptance"]
        self.assertEqual(acceptance["scenario_count"],12)
        self.assertEqual(acceptance["authored_results"],{"PASS":12})
        self.assertIn("UNVERIFIED",acceptance["execution_evidence"])

    def test_csv_extra_cells_fail_without_silent_drop(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"bad.csv"
            p.write_text("a,b\n1,2,3\n")
            with self.assertRaisesRegex(ValueError,"extra"):
                read_csv(p,{"a","b"})

    def test_duplicate_csv_headers_fail_without_ambiguous_columns(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"bad.csv"
            p.write_text("a,a\n1,2\n")
            with self.assertRaisesRegex(ValueError,"duplicate"):
                read_csv(p,{"a"})
