# AI Observability Specification

## Request-Level Telemetry
- model_version
- feature_version
- policy_version
- latency_ms
- fallback_used
- candidate_count
- selected_count
- experiment_arm
- consent_state
- error_code

## Aggregate Dashboards
### Model Quality
Precision@10, NDCG@10, AUC, calibration, diversity, coverage.

### Business
EAR, conversion, revenue per active user, repeat purchase.

### User Experience
negative feedback, hide rate, opt-out, session abandonment.

### Reliability
p50/p95/p99 latency, timeout rate, fallback rate, error rate.

### Risk
cohort quality gaps, exposure concentration, GenAI hallucination/unsafe-output samples.

## Alert Routing
SEV-1 → Pager: PM + MLOps + Security/Privacy.
SEV-2 → MLOps + PM within 15 minutes.
SEV-3 → business-hours triage.
