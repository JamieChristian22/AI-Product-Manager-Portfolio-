# Model Card — Price-Response Optimization

## Product Decision
Recommend a bounded price or offer adjustment that maximizes expected contribution margin while satisfying policy, fairness, seller, and customer-trust constraints.

## Inputs
Approved reference price, product cost, category, inventory band, synthetic historical demand, prior promotion response, seasonality, demand-elasticity estimate, and simulated competitor-price index.

## Optimization Objective
Expected contribution margin = predicted units × (candidate price − unit cost − variable fulfillment cost). Revenue is monitored but is not the sole objective.

## Candidate Policy
Candidate recommendations are limited to +/-8% from the approved reference price. Gross margin cannot fall below 22%. Products identified as essential/emergency categories are excluded from dynamic price optimization in the portfolio design.

## Validation Results
| Metric | Gate | Result |
|---|---:|---:|
| Demand MAPE | <=15.0% | 8.9% |
| Revenue Lift vs static baseline | >=5.0% | +7.8% |
| Contribution Margin Lift | >=4.0% | +6.4% |
| Post-rule margin violations | 0 | 0 |
| Price-bound violations | 0 | 0 |

## Fairness/Trust Policy
Protected traits and inferred protected-trait scores are prohibited. Pricing is based on product/context economics, not person-level willingness-to-pay using sensitive characteristics. Segment monitoring checks whether contextual features produce unexplained price outcome disparities.

## Human Oversight
The model only recommends. The policy engine can block recommendations automatically; commercial/product owners approve material rule changes. Any proposed relaxation of +/-8% or 22% margin floor requires explicit governance approval and a new risk review.
