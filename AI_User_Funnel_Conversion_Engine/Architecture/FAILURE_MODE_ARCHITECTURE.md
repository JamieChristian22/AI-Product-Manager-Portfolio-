# Failure-Mode Architecture

## Feature Store Failure
Action: bypass predictive scoring.
Fallback: static onboarding and generic lifecycle messages.

## Model Service Timeout
Action: timeout at 150 ms internal budget.
Fallback: no personalized intervention.

## Experiment Service Failure
Action: preserve prior persistent assignment if available.
Fallback: control experience.

## Consent Service Failure
Action: fail closed for personalization.
Fallback: non-personalized experience.

## Catalog / Content Service Failure
Action: do not serve dependent intervention.

## Monitoring Pipeline Failure
Action: freeze promotion and new experiments until observability restored.

## GenAI Failure
Action: revert to approved deterministic templates.
