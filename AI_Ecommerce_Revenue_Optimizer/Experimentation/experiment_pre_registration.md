# Experiment Pre-Registration — AI Revenue Optimizer

## Hypothesis
Providing AI-ranked recommendations, targeted checkout assistance, and policy-constrained price/offer recommendations will increase revenue per active user without materially worsening contribution margin, complaints, repeat purchase, seller outcomes, or fairness indicators.

## Design
Randomized 50/50 control vs treatment allocation at stable pseudonymous user ID. Control receives existing rule/static experience. Treatment receives AI decisioning. Assignment remains sticky during the experiment.

## Primary Metric
Revenue per active user (RPAU).

## Secondary Metrics
Conversion rate, average order value, cart abandonment rate, repeat purchase rate, recommendation CTR, contribution margin per active user.

## Guardrails
Complaint rate must not rise >20% vs 28-day baseline; contribution margin per active user must not fall >2%; repeat purchase must not fall >2 percentage points; pricing policy violations = 0; abandonment intervention cap compliance = 100%; no fairness review trigger >5 percentage points without investigation.

## Statistical Decision Rule
Require 95% confidence on primary metric improvement, no sample-ratio mismatch, and no critical guardrail breach. Multiple secondary metrics are directional/supporting and do not override a failed primary metric or breached guardrail.

## Ramp
10% treatment smoke test -> 25% -> 50%, with guardrail review at each stage. Full simulated launch only after final decision memo.
