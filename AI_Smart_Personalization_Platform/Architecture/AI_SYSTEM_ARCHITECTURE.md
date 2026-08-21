# AI System Architecture

## Logical Flow
1. Client applications emit interaction events.
2. Event gateway validates schema and consent state.
3. Streaming pipeline routes valid events to event storage and feature processing.
4. Batch and streaming jobs compute behavioral features.
5. Feature store exposes approved online features.
6. Candidate generator retrieves relevant products.
7. Propensity and ranking models score candidates.
8. Diversity layer applies catalog-coverage and concentration constraints.
9. Bandit layer reserves controlled exploration traffic.
10. Policy layer applies eligibility, consent, availability, and safety rules.
11. Response service returns personalized recommendations.
12. Monitoring layer records model version, latency, output metrics, and guardrail events.
13. Optional GenAI explainer produces grounded descriptions using approved catalog fields.

## Critical Boundaries
- Consent must be checked before personalized feature retrieval.
- Sensitive features are blocked at ingestion and feature-registration time.
- Catalog availability is checked at serve time.
- GenAI cannot access unrestricted user profiles or raw PII.
- All decisions include model_version and policy_version for auditability.

## Fallback Architecture
If feature store, model server, or policy service fails, traffic routes to:
**Popularity + Recency + Diversity Constraints**.

## Availability Objective
Target service availability: 99.9%.
Target p95 ranking latency: <250 ms.
