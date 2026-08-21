# Drift Root-Cause Matrix

| Signal | Likely Cause | Investigation |
|---|---|---|
| PSI spike | seasonality / source change | compare feature distribution |
| AUC drop, PSI stable | concept drift | inspect label relationship |
| calibration worsens | base-rate shift | recalibrate |
| activation drops across all cohorts | product issue | review release/error logs |
| one cohort degrades | proxy/data sparsity | cohort feature analysis |
| intervention acceptance drops | fatigue/content issue | message/frequency review |
| conversion up, retention down | over-optimization | stop rollout, review incentives |
