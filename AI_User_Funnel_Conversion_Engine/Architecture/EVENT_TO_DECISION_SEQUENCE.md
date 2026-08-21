# Event-to-Decision Sequence

1. User event arrives.
2. Schema validator checks event structure.
3. Consent service verifies allowed personalization state.
4. Event is written to event store.
5. Feature pipelines update rolling aggregates.
6. Feature store exposes approved snapshot.
7. Model gateway loads active champion versions.
8. Activation, churn, and conversion scores are generated.
9. Funnel-friction classifier identifies likely barrier.
10. Policy engine checks eligibility, frequency, prior dismissals, and safety rules.
11. Next-best-action ranker scores approved interventions.
12. Experiment service assigns control/treatment.
13. Intervention is served or suppressed.
14. Decision metadata is logged.
15. Outcome events return to analytics.
16. Causal experiment analysis determines whether intervention should scale.
