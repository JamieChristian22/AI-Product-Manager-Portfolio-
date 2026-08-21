# Bias Testing Methodology

## Objective
Detect material differences in recommendation quality and exposure across operational cohorts while avoiding sensitive-feature use in production scoring.

## Tests
1. Metric parity: Precision@10, NDCG@10, CTR, conversion.
2. Exposure parity: category and catalog coverage.
3. Calibration parity for propensity scores.
4. Missing-feature parity.
5. Cold-start performance.
6. Counterfactual feature ablation.
7. Proxy sensitivity analysis.

## Threshold
A >10 percentage-point quality gap triggers formal review.
A >15% relative exposure gap for comparable catalogs triggers investigation.

## Remediation
Data validation → feature ablation → reweighting → exploration increase → re-ranking constraint → feature removal → model pause.

## Documentation
Every fairness test records dataset version, model version, cohort definition, metrics, owner, decision, and remediation if needed.
