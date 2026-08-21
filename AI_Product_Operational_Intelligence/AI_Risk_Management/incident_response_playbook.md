# AI Incident Response Playbook

## Severity
**SEV-1:** sensitive/protected data use, discriminatory behavior, privacy/security breach, uncontrolled pricing outside hard bounds, or unsafe GenAI output delivered at scale.
**SEV-2:** material model degradation, repeated incorrect targeting, margin violations caught before delivery, complaint spike, or GenAI quality breach.
**SEV-3:** localized drift/quality issue with no material customer harm.

## First 30 Minutes — Simulated Operational Standard
Disable affected feature or route to fallback; preserve logs and model/rule/prompt versions; stop automatic retraining/deployment; identify incident owner; notify product, MLOps, risk/privacy/security as applicable.

## Investigation
Determine first bad event, affected users/products/categories, model and data versions, trigger source, policy-control behavior, customer/seller impact, and whether experiment results are contaminated.

## Recovery
Fix source issue; replay affected test cases; rerun release checklist; compare fresh validation with release gates; obtain accountable approvals; ramp traffic gradually; monitor elevated metrics for seven days.

## Post-Incident Review
Document root cause, impact, detection gap, why preventive controls did/did not work, corrective actions, owners, dates, and whether the risk register or monitoring thresholds require revision.
