# Model Card — Intervention Response Model

## Purpose
Estimate whether a user is likely to respond positively to an approved intervention.

## Key Rule
Response probability does not equal incremental causal effect. This model may prioritize experiments but cannot establish business lift by itself.

## Synthetic Metrics
- ROC-AUC: 0.82
- F1: 0.77
- Calibration Error: 0.049

## Features
- prior intervention response
- funnel stage
- product friction class
- time since last nudge
- prior dismissals
- session recency
- activation/churn scores

## Exclusions
No sensitive traits, financial hardship signals, or private communications.

## Guardrail
If prior dismissals >=2 in 7 days, predicted response cannot override suppression policy.
