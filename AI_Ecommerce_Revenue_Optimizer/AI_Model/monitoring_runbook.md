# Model Monitoring & Operations Runbook

## Daily Automated Checks
Data freshness, schema compatibility, missingness, duplicates, scoring volume, latency, failed predictions, blocked-price rate, intervention frequency, policy violations, and GenAI filter failures.

## Weekly Product/Model Review
Recommendation NDCG@10/CTR/coverage/concentration; abandonment AUC/calibration/precision/recall/intervention conversion; pricing MAPE/revenue lift/margin lift/override rate; GenAI grounding/policy rates; complaint and support-contact trends; seller-impact indicators.

## Monthly Governance Review
Feature drift, proxy-risk audit, segment performance, data-retention audit, model/rules change log, incidents, retraining decision, access review, and experiment learnings.

## Trigger Matrix
| Trigger | Severity | Immediate Action | Recovery Gate |
|---|---|---|---|
| Sensitive/prohibited feature detected | SEV-1 | stop affected scoring | root cause + clean retrain + governance approval |
| Pricing bound/margin violation delivered | SEV-1 | disable pricing optimizer | policy fix + replay test + approval |
| Demand MAPE >15% | SEV-2 | disable affected category recommendations | <=12% on fresh validation |
| Abandonment AUC <0.78 | SEV-2 | revert to rule fallback | >=0.80 for two review windows |
| Recommendation NDCG drop >10% | SEV-2 | reduce/rollback treatment | root cause + restored quality |
| Critical-field missingness >2% | SEV-2 | stop affected pipeline | <1% and backfill validated |
| Complaint rate +20% vs 28-day baseline | SEV-2 | pause experiment | review shows no product harm |
| GenAI unsupported claims >2% | SEV-2 | require 100% human review | <1% on 500-case re-test |

## Rollback Procedure
Freeze traffic to affected model, route to last approved model or non-ML rules, preserve logs/model version/data snapshot, notify accountable owners, open incident record, validate recovery, then re-enable gradually at 10%/25%/50%/100% traffic only after gates pass.
