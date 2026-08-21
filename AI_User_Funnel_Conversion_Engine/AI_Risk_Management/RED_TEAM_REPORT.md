# Red-Team Report

## Scope
80 synthetic scenarios across:
- consent bypass
- sensitive inference
- manipulative copy
- experiment contamination
- event poisoning
- prompt injection
- PII leakage
- intervention fatigue
- cancellation obstruction
- pricing misuse

## Initial Result
72/80 passed.

## Initial Failures
1. lifecycle and in-product caps not shared
2. pricing-page interest could influence aggressive conversion prompt
3. prompt injection in help content
4. stale consent cached for 5 minutes
5. repeated activation reminder after two dismissals
6. intervention copy used unsupported “most popular” claim
7. score generated despite >8% missing features
8. control assignment lost after anonymous→logged-in transition

## Remediation
- shared intervention ledger
- price-blind action policy
- untrusted-content isolation
- real-time consent invalidation
- dismissal suppression
- catalog claim validation
- hard feature-readiness gate
- persistent identity-safe experiment mapping

## Final Result
80/80 scenarios passed acceptance criteria.
