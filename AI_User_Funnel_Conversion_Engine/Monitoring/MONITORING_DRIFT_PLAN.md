# Monitoring & Drift Plan

| Metric | Current | Warning | Critical | Cadence |
|---|---:|---:|---:|---|
| Activation AUC | 0.86 | <0.82 | <0.78 | daily |
| Churn AUC | 0.88 | <0.84 | <0.80 | daily |
| Conversion AUC | 0.85 | <0.82 | <0.79 | daily |
| Intervention Response AUC | 0.82 | <0.79 | <0.75 | daily |
| F1 | 0.81 | <0.77 | <0.74 | daily |
| Calibration Error | 0.033 | >0.06 | >0.08 | daily |
| PSI | 0.08 | >0.15 | >0.25 | daily |
| p95 Latency | 126ms | >200ms | >250ms | 15m |
| Error Rate | 0.7% | >1% | >2% | 15m |
| Opt-out Delta | +0.2pp | +0.7pp | +1.0pp | daily |
| Complaint Delta | +0.1pp | +0.5pp | +1.0pp | daily |
| 7-Day Retention Delta | +4% | <0% | <-3% | daily |
| Dismissal Rate | 22% | >35% | >45% | daily |
| Experiment Contamination | 1.2% | >3% | >5% | daily |
