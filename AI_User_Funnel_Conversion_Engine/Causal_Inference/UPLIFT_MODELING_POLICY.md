# Uplift Modeling Policy

## Problem
Propensity models identify who is likely to activate or convert. They do not identify who is caused to activate by an intervention.

## Future-State Approach
For mature deployment, use uplift / treatment-effect modeling to estimate:
P(outcome | treatment) - P(outcome | control)

## Why It Matters
High-propensity users may convert without help. Targeting them can waste interventions and inflate attribution.

## Required Guardrails
- randomized historical data
- treatment/control balance
- no post-treatment features
- calibration by uplift decile
- Qini / uplift curve
- incremental outcome measurement
- no sensitive targeting
