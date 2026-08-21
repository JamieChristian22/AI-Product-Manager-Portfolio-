# AI Product Decision Log

## D-01 — Optimize Contribution Margin, Not Revenue Alone
**Decision:** Price model optimizes expected contribution margin. **Reason:** pure revenue optimization could drive excessive discounting or seller harm. **Guardrail:** 22% margin floor. **Status:** Approved.

## D-02 — Reject Lower Cart Threshold
**Decision:** use 0.67 rather than 0.55. **Reason:** 0.55 raised recall but reduced precision and increased intervention volume by 31%, creating higher annoyance risk. **Status:** Approved.

## D-03 — Maintain 10% Recommendation Exploration
**Decision:** reserve controlled exploration for eligible products. **Reason:** limits popularity feedback loops and supports cold-start products. **Status:** Approved.

## D-04 — Human Approval for GenAI Campaign Copy
**Decision:** generated campaign-level copy cannot auto-publish. **Reason:** residual hallucination/brand risk remains even with a 98.7% grounded-claim rate. **Status:** Approved.

## D-05 — Controlled Launch Simulation
**Decision:** all three predictive models pass technical gates and can proceed to a simulated controlled experiment; GenAI remains limited with human approval. **Reason:** metrics pass and risk controls/fallbacks are defined. **Status:** Approved 2026-08-18.
