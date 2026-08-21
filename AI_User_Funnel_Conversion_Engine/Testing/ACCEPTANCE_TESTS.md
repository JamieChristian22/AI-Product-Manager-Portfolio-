# Filled Acceptance Tests

| ID | Scenario | Expected | Result |
|---|---|---|---|
| AT01 | personalization opt-out | no AI intervention | PASS |
| AT02 | feature missingness 7% | fallback | PASS |
| AT03 | two dismissals | 7-day suppression | PASS |
| AT04 | p95 latency >250ms | rollback trigger | PASS |
| AT05 | control user | static experience | PASS |
| AT06 | pricing interest high | no individualized price action | PASS |
| AT07 | stale activation label schema | block promotion | PASS |
| AT08 | anonymous→login | experiment preserved | PASS |
| AT09 | prompt injection in help content | ignored/isolated | PASS |
| AT10 | complaint submitted | 30-day suppression | PASS |
| AT11 | consent cache stale | immediate invalidation | PASS |
| AT12 | model service down | static fallback | PASS |
