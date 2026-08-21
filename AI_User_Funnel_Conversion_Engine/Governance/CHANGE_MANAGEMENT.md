# AI Change Management

## Patch
Bug fix with no intended decision behavior change.
Requires regression tests.

## Minor
Threshold, hyperparameter, feature weighting, or retraining change.
Requires offline validation and version update.

## Major
New objective, new model family, new data source, new intervention class, or materially changed label.
Requires full model card refresh, risk review, fairness/privacy review, experiment, and release gate.

## Emergency
Safety, privacy, or security mitigation.
May bypass normal experiment sequencing but requires retrospective documentation within one business day.
