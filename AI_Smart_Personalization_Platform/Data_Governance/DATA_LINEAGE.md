# Data Lineage

| Source | Event/Data | Transformation | Feature | Model Consumer | Retention |
|---|---|---|---|---|---|
| Web/App Events | page_view | 30d aggregation | session_count_30d | segmentation/propensity | 90d |
| Web/App Events | add_to_cart | rate calculation | add_to_cart_rate | propensity | 90d |
| Orders | order_complete | 90d aggregation | purchase_count_90d | all models | 180d |
| Orders | order_total | mean aggregation | avg_order_value_90d | segmentation/ranking | 180d |
| Search | query event | category mapping | search_category_affinity | ranking | 90d |
| Catalog | product metadata | taxonomy validation | product_category | ranking | active catalog |
| Feedback | dislike/hide | suppression feature | negative_feedback_rate | ranking/bandit | 90d |
| Consent Store | personalization flag | no transform | consent_personalization | policy gate | current state |

## Lineage Controls
- Every production feature has a source owner.
- Feature definitions are versioned.
- Event timestamp and processing timestamp are preserved.
- Training snapshots are reproducible.
- Data-quality alerts block model promotion when critical fields fail.
