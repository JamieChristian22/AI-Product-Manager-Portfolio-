# Model Selection Rationale

## Behavioral Segmentation
**Chosen:** K-Means.
**Compared:** rule-based RFM, Gaussian Mixture.
**Why:** simple, interpretable, fast to retrain, adequate separation for portfolio use.

## Conversion Propensity
**Chosen:** Gradient-boosted trees.
**Compared:** logistic regression.
**Why:** nonlinear feature interactions improved AUC while maintaining explainability through feature importance.

## Ranking
**Chosen:** weighted learning-to-rank style scoring + diversity re-ranker.
**Compared:** popularity baseline and pure relevance score.
**Why:** materially improved ranking quality without allowing excessive category concentration.

## Exploration
**Chosen:** bounded multi-armed bandit.
**Compared:** fixed randomized exploration.
**Why:** adapts allocation while preserving explicit exposure floors/caps.

## GenAI
**Chosen:** retrieval-grounded response generation.
**Compared:** free-form generation and fixed templates.
**Why:** retains flexibility while reducing unsupported claims.
