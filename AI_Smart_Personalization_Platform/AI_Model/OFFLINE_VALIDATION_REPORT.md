# Offline Validation Report

## Dataset
Synthetic, time-ordered e-commerce interaction dataset with modeled sessions, searches, carts, orders, catalog metadata, and consent states.

## Holdout Strategy
70% train / 15% validation / 15% chronological holdout.

## Ranking Results
| Metric | Baseline | Candidate | Delta |
|---|---:|---:|---:|
| Precision@10 | 0.69 | 0.84 | +0.15 |
| Recall@10 | 0.64 | 0.79 | +0.15 |
| NDCG@10 | 0.70 | 0.82 | +0.12 |
| Catalog Coverage | 0.48 | 0.71 | +0.23 |
| Diversity | 0.44 | 0.68 | +0.24 |

## Propensity Results
| Metric | Logistic Baseline | GBT Candidate |
|---|---:|---:|
| ROC-AUC | 0.78 | 0.86 |
| F1 | 0.72 | 0.81 |
| Brier | 0.148 | 0.118 |
| Calibration Error | 0.061 | 0.031 |

## Segmentation
Silhouette score: 0.57.
30-day reassignment stability: 87%.

## Decision
Candidate models pass offline release thresholds and may proceed to controlled experiment.
