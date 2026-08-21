# Feature Governance Policy

## Feature Admission Checklist
A new feature must have:
- Product rationale
- Data owner
- Source system
- Allowed use
- Retention period
- Privacy classification
- Proxy-risk assessment
- Leakage assessment
- Missingness threshold
- Freshness SLA
- Monitoring owner

## Prohibited Features
Protected traits, precise geolocation, raw payment details, health information, political affiliation, biometric identifiers, private communications, government identifiers, and inferred sensitive traits.

## High-Risk Features Requiring Review
Broad geography, device class, discount affinity, spend level, and inferred behavioral segments.

## Feature Change Control
Material feature changes require:
1. updated feature documentation,
2. offline backtest,
3. fairness re-test,
4. privacy review when necessary,
5. model version increment,
6. experiment or shadow validation,
7. change-log entry.
