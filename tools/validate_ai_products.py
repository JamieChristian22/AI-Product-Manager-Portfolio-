#!/usr/bin/env python3
"""Validate synthetic AI PM examples against their *committed* source artifacts.

This verifies reproducibility and internal arithmetic, not real-world model
quality, causal experiment effects, safe deployment or live user outcomes.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sqlite3
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = (
    "AI_Ecommerce_Revenue_Optimizer",
    "AI_Product_Operational_Intelligence",
    "AI_Smart_Personalization_Platform",
    "AI_User_Funnel_Conversion_Engine",
)
MODELS = PROJECTS[:2]
MONITORING = PROJECTS[2:]
DATA_COLUMNS = {"user_id", "session_length", "conversion", "revenue", "retention_flag"}
MODEL_COLUMNS = {"model", "metric", "gate", "result", "status"}
MONITOR_COLUMNS = {"Metric", "Current", "Warning", "Critical", "Cadence", "Owner"}


def read_csv(path: Path, required: set[str]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, strict=True)
        fields = reader.fieldnames or []
        if len(fields) != len(set(fields)) or not required.issubset(fields):
            raise ValueError(f"{path}: missing or duplicate CSV headers")
        rows = list(reader)
    if not rows:
        raise ValueError(f"{path}: no records")
    for line, row in enumerate(rows, 2):
        if None in row or any(x is None for x in row.values()):
            raise ValueError(f"{path}:{line}: extra or missing fields")
        if any(not row[k].strip() for k in required):
            raise ValueError(f"{path}:{line}: missing mandatory cell")
    return rows


def finite(value: str, context: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{context}: invalid number") from exc
    if not math.isfinite(number):
        raise ValueError(f"{context}: non-finite number")
    return number


def validate_sessions(rows: list[dict[str, str]]) -> dict:
    ids = set()
    sessions = []
    conversions = 0
    retained = 0
    revenue_cents = 0
    for row in rows:
        if row["user_id"] in ids:
            raise ValueError("Duplicate sample user ID")
        ids.add(row["user_id"])
        session = finite(row["session_length"], "session_length")
        if session < 0:
            raise ValueError("Negative sample session")
        sessions.append(session)
        if row["conversion"] not in ("0", "1") or row["retention_flag"] not in ("0", "1"):
            raise ValueError("Conversion and retention flags must be binary")
        conversions += int(row["conversion"])
        retained += int(row["retention_flag"])
        amount = finite(row["revenue"], "revenue")
        if amount < 0 or int(round(amount * 100)) != round(amount * 100):
            raise ValueError("Revenue must be nonnegative and quantized to cents")
        if row["conversion"] == "0" and amount != 0:
            raise ValueError("Nonconverting sample row has positive revenue")
        revenue_cents += int(round(amount * 100))
    return {
        "sample_sessions": len(rows),
        "sample_conversions": conversions,
        "conversion_rate": round(conversions / len(rows), 6),
        "mean_session_length": round(sum(sessions) / len(rows), 6),
        "retention_share": round(retained / len(rows), 6),
        "revenue": round(revenue_cents / 100, 2),
    }


def evaluate_gate(gate: str, result: str) -> bool:
    match = re.fullmatch(r"\s*(>=|<=|>|<|==|=)?\s*(-?\d+(?:\.\d+)?)\s*", gate)
    if not match:
        raise ValueError(f"Unsupported model metric gate {gate!r}")
    operator, threshold = match.groups()
    observed = finite(result, "model metric result")
    limit = float(threshold)
    return {
        ">=": lambda: observed >= limit,
        "<=": lambda: observed <= limit,
        ">": lambda: observed > limit,
        "<": lambda: observed < limit,
        "==": lambda: observed == limit,
        "=": lambda: observed == limit,
    }[operator or "="]()


def validate_model_metrics(rows: list[dict[str, str]]) -> dict:
    seen = set()
    actual = Counter()
    for row in rows:
        key = (row["model"], row["metric"])
        if key in seen:
            raise ValueError("Duplicate model/metric gate")
        seen.add(key)
        claimed = row["status"].strip().lower()
        if claimed not in ("pass", "fail"):
            raise ValueError(f"Unknown model evaluation status {claimed}")
        measured = evaluate_gate(row["gate"], row["result"])
        if measured != (claimed == "pass"):
            raise ValueError(f"{key}: documented outcome conflicts with gate calculation")
        actual["passes" if measured else "failures"] += 1
    return {"gate_count": len(rows), "calculated_passes": actual["passes"],
            "calculated_failures": actual["failures"]}


def validate_monitor(rows: list[dict[str, str]]) -> dict:
    names = set()
    levels = Counter()
    for row in rows:
        name = row["Metric"]
        if name in names:
            raise ValueError(f"Duplicate monitor metric {name}")
        names.add(name)
        current = finite(row["Current"], name)
        warn = finite(row["Warning"], name)
        critical = finite(row["Critical"], name)
        if warn == critical:
            raise ValueError(f"{name}: ambiguous equal warning/critical boundaries")
        if warn < critical:
            state = "critical" if current >= critical else "warning" if current >= warn else "within_sample_threshold"
        else:
            state = "critical" if current <= critical else "warning" if current <= warn else "within_sample_threshold"
        levels[state] += 1
    return {"metric_count": len(rows), "sample_severity_counts": dict(levels),
            "scope": "Illustrative table entries only, not live drift or uptime monitoring"}


def validate_risks(rows: list[dict[str, str]]) -> dict:
    ids = set()
    for row in rows:
        rid = row["Risk_ID"]
        if rid in ids:
            raise ValueError(f"Duplicate risk ID {rid}")
        ids.add(rid)
        likelihood = int(row["Likelihood"])
        impact = int(row["Impact"])
        score = int(row["Score"])
        if not 1 <= likelihood <= 5 or not 1 <= impact <= 5 or score != likelihood * impact:
            raise ValueError(f"{rid}: inconsistent likelihood × impact risk score")
    return {"registered_risk_rows": len(rows), "risk_scores_reconciled": len(rows)}


def sql_verify(root: Path, rows: list[dict[str, str]], expected: dict) -> int:
    sql = (root / "Data_Analytics/queries.sql").read_text(encoding="utf-8")
    con = sqlite3.connect(":memory:")
    try:
        con.execute("CREATE TABLE dataset (user_id INTEGER, session_length REAL, conversion INTEGER, revenue REAL, retention_flag INTEGER)")
        con.executemany("INSERT INTO dataset VALUES (?, ?, ?, ?, ?)",
            [(int(r["user_id"]), float(r["session_length"]), int(r["conversion"]),
              float(r["revenue"]), int(r["retention_flag"])) for r in rows])
        statements = [s.strip() for s in sql.split(";") if s.strip()]
        if len(statements) != 4:
            raise ValueError("Expected four authored independent SQL checks")
        values = [con.execute(s).fetchall() for s in statements]
        checks = (
            abs(values[0][0][0] - expected["mean_session_length"]) < 1e-6,
            values[1][0][0] == expected["sample_conversions"],
            abs(values[2][0][0] - expected["revenue"]) < 1e-6,
            dict(values[3]) == {0: len(rows)-int(sum(int(x["retention_flag"]) for x in rows)),
                                1: int(sum(int(x["retention_flag"]) for x in rows))},
        )
        if not all(checks):
            raise ValueError(f"{root.name}: SQL values do not reconcile to Python aggregates")
        return len(checks)
    finally:
        con.close()


def validate() -> dict:
    projects = {}
    sample_digests = {}
    for name in PROJECTS:
        root = ROOT / name
        dataset = root / "Data_Analytics/dataset.csv"
        rows = read_csv(dataset, DATA_COLUMNS)
        stats = validate_sessions(rows)
        stats["sql_reconciliation_checks"] = sql_verify(root, rows, stats)
        digest = hashlib.sha256(dataset.read_bytes()).hexdigest()
        sample_digests[name] = digest
        stats["dataset_sha256"] = digest
        projects[name] = stats

    model_digests = {}
    for name in MODELS:
        model_path = ROOT / name / "AI_Model/evaluation_metrics.csv"
        rows = read_csv(model_path, MODEL_COLUMNS)
        projects[name]["model_evaluation"] = validate_model_metrics(rows)
        model_digests[name] = hashlib.sha256(model_path.read_bytes()).hexdigest()

    for name in MONITORING:
        root = ROOT / name
        projects[name]["monitoring"] = validate_monitor(read_csv(root / "Monitoring/monitoring_thresholds.csv", MONITOR_COLUMNS))
        risks = read_csv(root / "AI_Risk_Management/risk_register.csv",
                         {"Risk_ID", "Likelihood", "Impact", "Score"})
        projects[name]["risk_register"] = validate_risks(risks)
        config_path = root / "Governance/governance_config.json"
        config = json.loads(config_path.read_text(encoding="utf-8"))
        if "Synthetic" not in config.get("portfolio_disclosure", ""):
            raise ValueError(f"{name}: missing synthetic-data disclosure")
        if not config.get("fallback"):
            raise ValueError(f"{name}: no documented fallback")
        projects[name]["governance"] = {"fallback": config["fallback"], "model_policy_documented": True}

    acceptance = read_csv(ROOT / PROJECTS[3] / "Testing/acceptance_tests.csv",
                          {"Test_ID", "Scenario", "Expected", "Result"})
    if len(set(x["Test_ID"] for x in acceptance)) != len(acceptance):
        raise ValueError("Duplicate acceptance scenario ID")
    statuses = dict(Counter(row["Result"] for row in acceptance))
    if any(status not in {"PASS", "FAIL", "NOT_RUN", "BLOCKED"} for status in statuses):
        raise ValueError("Unknown authored acceptance result")
    projects[PROJECTS[3]]["documented_acceptance"] = {
        "scenario_count": len(acceptance), "authored_results": statuses,
        "execution_evidence": "UNVERIFIED: no executable product acceptance harness in this repository"
    }
    return {
        "schema_version": 1,
        "status": "PASS_SOURCE_RECONCILIATION",
        "provenance": "Synthetic/modelled case-study records, not independent production/ML/A-B evaluation",
        "projects": projects,
        "shared_five_row_sample_across_all_projects": len(set(sample_digests.values())) == 1,
        "shared_evaluation_table_in_first_two_projects": len(set(model_digests.values())) == 1,
        "sql_check_total": sum(v["sql_reconciliation_checks"] for v in projects.values()),
        "live_model_validation": False,
        "live_experiment_outcomes_verified": False,
        "live_security_privacy_assessment_verified": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "reports/source-evidence.json")
    args = parser.parse_args()
    evidence = validate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))


if __name__ == "__main__":
    main()
