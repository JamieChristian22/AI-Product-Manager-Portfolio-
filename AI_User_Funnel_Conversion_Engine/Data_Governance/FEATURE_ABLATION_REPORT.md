# Feature Ablation Report

## Objective
Determine whether high-risk or proxy-prone features are necessary.

| Feature Removed | Activation AUC Change | Churn AUC Change | Conversion AUC Change | Decision |
|---|---:|---:|---:|---|
| device_class | -0.004 | -0.003 | -0.002 | remove from conversion model |
| acquisition_channel | -0.006 | -0.005 | -0.007 | retain with monitoring |
| pricing_page_views | -0.001 | 0.000 | -0.021 | retain for conversion only |
| help_views_7d | -0.013 | -0.018 | -0.004 | retain |
| lifecycle_engagement | -0.008 | -0.009 | -0.010 | retain with intervention-bias caution |

## Product Decision
Device class was removed from paid-conversion scoring because the incremental lift was negligible relative to proxy-risk concerns.
