# Model Card — Funnel Friction Classifier

## Purpose
Classify the most likely reason a user has not progressed to the next funnel stage.

## Classes
- setup incomplete
- feature discovery gap
- integration friction
- unclear value
- task failure
- pricing uncertainty
- inactive / no clear friction

## Synthetic Evaluation
- Macro F1: 0.79
- Weighted F1: 0.82
- Accuracy: 0.84
- Lowest class recall: 0.73

## Product Use
Select appropriate education or assistance, not pressure.

## Risk
Incorrect classification can produce irrelevant or repetitive prompts.

## Mitigation
Confidence threshold of 0.60; below threshold, route to generic help or no intervention.
