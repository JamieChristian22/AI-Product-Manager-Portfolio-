# Calibration & Threshold Policy

## Why Calibration Matters
Product actions depend on probability bands, so a predicted 0.70 should approximately correspond to a 70% observed rate in a comparable cohort.

## Monitoring
Expected Calibration Error (ECE)
Brier score
reliability curves
segment-level calibration

## Thresholds
Critical ECE: >0.08
Warning ECE: >0.06

## Action Bands
Activation risk:
- >=0.75 likely activate: low-intervention
- 0.45–0.75 uncertain: contextual support
- <0.45 high friction: eligible for guided intervention

Churn risk:
- <0.30 low
- 0.30–0.60 medium
- >0.60 high

Thresholds are illustrative and must be validated through experiments before production use.
