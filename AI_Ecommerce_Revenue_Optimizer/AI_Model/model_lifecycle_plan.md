# AI Model Lifecycle Plan

## Discover
Define business decision, user value, harms, non-goals, affected stakeholders, and measurable success/guardrails.

## Develop
Use approved features only; version data, feature logic, prompts, policy rules, and model artifacts. Document assumptions and synthetic-data limitations.

## Validate
Run offline quality, calibration, leakage, robustness, fairness/segment, privacy, policy, and rollback tests. Product and risk owners review evidence.

## Experiment
Use pre-registered randomized experiments. Ramp 10% -> 25% -> 50% treatment exposure while checking guardrails before broader exposure.

## Operate
Monitor technical/model/business/risk KPIs. Maintain an auditable model registry, change log, incident record, and decision log.

## Retrain
Retrain when performance/drift triggers fire, feature definitions materially change, new categories shift demand behavior, or quarterly review identifies degradation. Retraining requires the same validation gates as a new release.

## Retire
Retire a model when it no longer adds measurable value, creates unresolved risk, has a safer/better replacement, or depends on deprecated data. Archive its model card, validation record, decision memo, and final monitoring snapshot.
