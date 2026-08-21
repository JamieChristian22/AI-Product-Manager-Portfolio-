# Example AI Incident Postmortem

## Incident
On 2026-08-11, a cache invalidation defect caused 0.08% of recently opted-out sessions to receive one personalized request before the consent state propagated.

## Severity
SEV-2 because privacy preference enforcement was temporarily inconsistent, with limited exposure and no sensitive data disclosure.

## Detection
Consent mismatch dashboard triggered at 0.05%.

## Immediate Action
Personalization disabled for affected cache path; generic fallback activated.

## Root Cause
Consent updates were written to the source-of-truth store immediately but edge cache TTL remained 10 minutes.

## Fix
Consent change now emits mandatory cache-eviction event; personalization service verifies consent freshness before serving.

## Verification
50,000 synthetic opt-out events tested with 0 mismatches.

## Preventive Action
Added consent propagation SLO, automated regression test, and critical alert threshold.

## Product Lesson
Privacy controls require infrastructure-level guarantees, not only UI state.
