# Fairness & Proxy-Risk Assessment

## Scope
Because the portfolio system affects recommendations, interventions, and price/offer suggestions, fairness is treated as an outcome and process requirement even though the models are not used for legally regulated eligibility decisions.

## Protected Data Policy
Race, ethnicity, religion, disability, health status, sexual orientation, political affiliation, precise location, and other protected/sensitive traits are prohibited as decision features. The simulation does not infer these attributes for personalization.

## Operational Cohorts Reviewed
New vs returning shoppers, mobile vs desktop, traffic source, cart-value bands, category, price bands, and product/seller age. These are used to detect operationally meaningful disparities, not to infer protected status.

## Results
Abandonment false-positive rates: new 18.9%, returning 17.2%, mobile 19.4%, desktop 16.8%. Largest gap = 2.6 percentage points, below the internal 5-point review trigger. Recommendation NDCG@10 is 0.361 for new users and 0.401 for returning users; the 0.040 gap is accepted with contextual fallback and 10% exploration because no user is denied access to products and the gap is monitored.

Price outcomes are reviewed for unexplained differences by operational context. No individualized sensitive-trait pricing exists. Any segment price-outcome gap above 5 percentage points after controlling for product/category context triggers review and potential suspension.

## Mitigation Strategy
Use minimum-necessary features, review proxies, limit behavioral-history dependence, preserve exploration for cold-start users/items, constrain pricing by policy rather than inferred willingness-to-pay, and treat customer trust metrics as release guardrails.
