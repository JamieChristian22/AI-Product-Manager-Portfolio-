# Data Dictionary & Quality Contract

## Key Entities
**Session:** pseudonymous browsing period tied to a rotating session identifier. **Product:** catalog item with approved commercial metadata. **Order:** synthetic completed purchase event. **Impression:** eligible product exposure. **Intervention:** checkout assistance event. **Price Recommendation:** model-generated candidate that has passed the policy engine.

## Required Fields and Rules
| Field | Type | Rule | Failure Action |
|---|---|---|---|
| event_timestamp | UTC timestamp | non-null; not >5 min future | quarantine event |
| session_id | string | non-null pseudonymous ID | drop from modeling stream |
| product_id | string | valid active catalog key | exclude record |
| event_type | enum | view/cart/checkout/purchase/impression | reject unknown value |
| reference_price | decimal | >0 and approved catalog value | block pricing score |
| unit_cost | decimal | >=0 and < reference price for optimizer | block pricing score |
| inventory_band | enum | low/normal/high | fallback to normal only in offline simulation; production would block |
| checkout_step | integer | 0–5 | quarantine invalid event |

## Pipeline SLOs
Event freshness <=30 minutes; duplicate rate <=1%; critical-field missingness <=2%; schema compatibility 100%; daily row-count deviation alert at +/-25% from trailing 28-day weekday median.

## Leakage Controls
Future purchase outcomes are never included as features for earlier prediction times. Post-checkout events are excluded from abandonment features. Target-derived statistics are generated within training folds. Price outcome evaluation uses chronological holdout windows.
