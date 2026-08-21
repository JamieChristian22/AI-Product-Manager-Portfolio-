# AI Personalization On-Call Runbook

## Common Alerts

### High Latency
Check model server CPU/memory, feature-store latency, downstream catalog service, cache hit rate.
Mitigation: increase capacity or activate fallback.

### Precision Drop
Check feature freshness, model version, catalog changes, cohort distribution.
Mitigation: revert champion or disable affected feature.

### Consent Mismatch
Immediately disable personalization for impacted path, preserve logs, notify Privacy, open SEV-1/2 depending on exposure.

### GenAI Unsafe Output
Disable generation feature flag, revert to templated explanations, preserve prompt/output trace with privacy controls.

### Exposure Concentration
Increase diversity lambda, verify candidate source, inspect popularity feedback loop.
