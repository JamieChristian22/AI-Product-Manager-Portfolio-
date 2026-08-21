# AI Model Validation Report

## Validation Scope
The portfolio validation evaluates predictive quality, calibration, business utility, segment consistency, data leakage, policy compliance, and robustness under degraded inputs.

## Recommendation Validation
NDCG@10 = 0.387, Precision@10 = 0.312, Recall@10 = 0.428. Removing behavioral history reduces NDCG@10 to 0.354, demonstrating dependence on personalization but preserving acceptable cold-start fallback quality. With 10% random event loss, NDCG@10 declines to 0.366 and remains above the release gate.

## Abandonment Validation
ROC-AUC = 0.842 and Brier = 0.146 at the calibrated model level. At threshold 0.67, precision = 0.718 and recall = 0.681. Threshold 0.55 increased recall to 0.754 but reduced precision to 0.621 and increased simulated intervention volume by 31%; it was rejected because the customer-annoyance tradeoff outweighed incremental coverage.

## Price-Response Validation
Demand MAPE = 8.9% overall. Category MAPE ranges from 7.2% to 11.8%. Stress testing a 15% demand shock raises MAPE to 14.6%, still under the 15% shutdown threshold but close enough to trigger enhanced monitoring. Every candidate is tested against +/-8% price bounds and a 22% margin floor; 7.3% of raw candidates are blocked by the policy layer, yielding zero post-rule violations.

## GenAI Validation
Across 1,000 test prompts, grounded-claim rate = 98.7%, unsupported-claim rate = 0.8%, tone compliance = 96.9%, and policy violation rate = 0.3%. All policy-violating outputs are treated as failed cases even if the prose is otherwise useful.

## Segment/Fairness Review
No protected attributes are present. Proxy-risk review focuses on traffic source, device class, cart value, and historical behavior. The largest abandonment false-positive-rate gap across defined operational cohorts is 2.6 percentage points, below the 5-point review trigger. Recommendation NDCG gap between new and returning users is 0.040; exploration and contextual fallback are retained to reduce cold-start disadvantage.

## Validation Decision
**Approved for controlled portfolio launch simulation** because all model gates pass, policy violations are blocked before decision delivery, segment gaps remain below review thresholds, and rollback/fallback paths are documented.
