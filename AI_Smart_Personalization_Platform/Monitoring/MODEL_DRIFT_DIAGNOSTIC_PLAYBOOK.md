# Model Drift Diagnostic Playbook

## When PSI > 0.25 or performance drops
1. Identify top drifting features.
2. Compare source-system health.
3. Check seasonal/event effects.
4. Review cohort distribution changes.
5. Compare champion vs challenger.
6. Validate labels and attribution logic.
7. Re-run calibration.
8. Determine whether retraining is appropriate.

## Do Not Retrain Automatically When
- source data is corrupted,
- consent logic changed unexpectedly,
- label generation is broken,
- incident investigation is active.

Retraining bad data converts an operational incident into a model defect.
