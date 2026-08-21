# Data Quality SLA

| Check | Warning | Critical | Action |
|---|---:|---:|---|
| Missing key features | >2% | >5% | fallback / investigate |
| Late events | >5% | >10% | freeze retraining |
| Schema violations | >0.5% | >1% | block ingest |
| Duplicate events | >1% | >3% | dedupe / investigate |
| Invalid product IDs | >0.2% | >0.5% | filter / catalog incident |
| Consent mismatch | any trend | >0.1% | disable personalization |
| Feature freshness | >15 min late | >30 min late | fallback |

Critical data-quality failures block model promotion.
