# Model Card — Cart-Abandonment Propensity

## Product Decision
Estimate whether an active cart is likely to be abandoned and determine whether the session is eligible for a non-coercive intervention.

## Target
Binary label indicating abandonment by the end of the defined shopping session.

## Features
Cart value, item count, session duration, checkout step, shipping estimate exposure, previous abandonment count, return-customer flag, traffic source, device class, discount interaction, and session engagement velocity.

## Modeling
Gradient-boosted binary classifier followed by probability calibration. Chronological train/validation/test splitting is used to reduce temporal leakage.

## Test Results
| Metric | Gate | Result |
|---|---:|---:|
| ROC-AUC | >=0.780 | 0.842 |
| Precision | >=0.680 | 0.718 |
| Recall | >=0.650 | 0.681 |
| F1 | >=0.670 | 0.699 |
| Brier Score | <=0.160 | 0.146 |

## Operating Threshold
0.67 predicted abandonment probability. Threshold selection balances incremental conversion value, intervention cost, customer annoyance, and false-positive rate rather than maximizing raw accuracy.

## Segment Validation
False-positive rate: new customers 18.9%, returning 17.2%, mobile 19.4%, desktop 16.8%. Maximum observed gap is 2.6 percentage points, below the internal 5-point review trigger.

## Product Guardrails
Maximum one intervention per session and three per user within seven days. No countdown manipulation, false scarcity, or forced-choice copy. A user who dismisses two consecutive interventions enters a 14-day suppression period.

## Fallback
If AUC falls below 0.78, calibration fails, or critical features become unavailable, automated model targeting stops and the system reverts to broad rule-based checkout assistance without personalized risk scoring.
