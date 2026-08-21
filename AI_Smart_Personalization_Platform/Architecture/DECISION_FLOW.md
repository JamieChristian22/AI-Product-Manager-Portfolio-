# Personalization Decision Flow

## Decision Sequence
**Step 1: Consent**
If personalization consent = false → generic ranking.

**Step 2: Eligibility**
Remove unavailable, restricted, previously blocked, and policy-ineligible items.

**Step 3: Feature Readiness**
If feature freshness > SLA or missingness >5% → fallback ranking.

**Step 4: Candidate Generation**
Retrieve up to 500 candidates using category affinity, collaborative similarity, and popularity.

**Step 5: Model Scoring**
Apply propensity and relevance scores.

**Step 6: Diversity Re-Ranking**
Enforce category exposure and novelty constraints.

**Step 7: Exploration**
Apply bounded exploration budget.

**Step 8: Policy Guardrails**
Check suppression, negative feedback, inventory, and unsafe content rules.

**Step 9: Serve**
Return top-K recommendations.

**Step 10: Log**
Persist model version, decision timestamp, candidate set hash, selected items, latency, experiment assignment, and policy result.
