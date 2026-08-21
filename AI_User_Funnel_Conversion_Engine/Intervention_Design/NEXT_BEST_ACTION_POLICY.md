# Next-Best-Action Policy

## Candidate Generation
Only interventions approved for the user's funnel stage are considered.

## Scoring
Illustrative:
0.30 predicted helpful response
+ 0.25 activation opportunity
+ 0.20 churn mitigation
+ 0.15 relevance
+ 0.10 recency
- dismissal penalty
- fatigue penalty

## Mandatory Candidate
“No intervention” is always included.

## Overrides
Policy engine may suppress all actions for:
- opt-out
- excessive frequency
- recent complaint
- insufficient confidence
- stale features
