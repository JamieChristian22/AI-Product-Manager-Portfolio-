# Model Card — Recommendation Ranking

## Product Decision
Rank up to 10 eligible products that are most relevant to the current shopper/session.

## Features
Category affinity, recent product views, cart interactions, prior purchases, price-band preference, promotion interaction, session recency/frequency, product popularity, product age, inventory availability, and category metadata.

## Training / Validation Design
120,000 synthetic user-product impressions are ordered chronologically and split 70% train, 15% validation, 15% test. Items from future periods are not allowed to leak into earlier training windows. Negative examples are sampled from eligible impressions that were shown but not clicked/purchased.

## Model Approach
Gradient-boosted relevance scoring combined with collaborative behavioral features. Eligibility rules run before ranking; diversity and exploration adjustments run after raw scoring.

## Validation Results
| Metric | Baseline/Gate | Result |
|---|---:|---:|
| Precision@10 | 0.280 | 0.312 |
| Recall@10 | 0.400 | 0.428 |
| NDCG@10 | 0.350 | 0.387 |
| Simulated CTR | 7.4% baseline | 8.6% |
| Coverage | >=70% eligible catalog | 76.4% |
| Top-category concentration | <=38% impressions | 34.1% |

## Segment Check
NDCG@10: new users 0.361; returning users 0.401; mobile 0.379; desktop 0.394. All segments remain above the 0.350 release gate except no materially undersized cohort is treated as conclusive.

## Controls
Unavailable/restricted products are removed before ranking. Same-product exposure is capped at three impressions per seven days unless the user re-engages. At least 10% of recommendation inventory is reserved for controlled exploration among eligible items. Category concentration above 38% triggers ranking review.

## Failure Modes
Cold-start users may receive less personalized results; fallback uses contextual popularity and category signals. Popular products may dominate; diversity reranking and exploration reduce concentration. Missing event history falls back to session/context features.
