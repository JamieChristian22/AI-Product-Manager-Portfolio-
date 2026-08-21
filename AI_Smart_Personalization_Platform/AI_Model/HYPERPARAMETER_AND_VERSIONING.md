# Hyperparameter & Versioning Record

## Behavioral Segmenter v1.2
- k = 4
- initialization = k-means++
- max_iter = 300
- random_seed = 42

## Conversion Propensity v1.4
- estimators = 300
- max_depth = 5
- learning_rate = 0.05
- subsample = 0.8
- probability calibration = isotonic

## Ranking v2.1
- candidate pool = 500
- final K = 20
- diversity lambda = 0.18
- novelty minimum = 15%
- max category concentration = 65%

## Bandit v1.0
- exploration default = 10%
- min exploration = 5%
- max exploration = 25%
- reward delay window = 24h

## Versioning Policy
MAJOR: objective/model-family change.
MINOR: meaningful feature, parameter, or training-data change.
PATCH: bug fix without intended behavior change.
