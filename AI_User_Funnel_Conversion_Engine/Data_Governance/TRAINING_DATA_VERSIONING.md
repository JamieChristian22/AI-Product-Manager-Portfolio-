# Training Data Versioning

Every training snapshot includes:
- dataset_id
- extraction timestamp
- schema version
- label version
- feature registry version
- consent filtering logic version
- excluded cohort rules
- row count
- date range
- hash/checksum

Example:
dataset_id: funnel_train_2026_08_01_v3
schema_version: 2.2
label_version: activation_v4
feature_registry: 3.1
consent_policy: 1.4
