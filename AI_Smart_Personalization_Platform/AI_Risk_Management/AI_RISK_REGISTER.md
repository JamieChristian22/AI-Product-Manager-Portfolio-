# Enterprise AI Risk Register

Scoring: Likelihood 1–5 × Impact 1–5.

| ID | Risk | L | I | Score | Primary Control | Residual | Owner |
|---|---|---:|---:|---:|---|---|---|
| R01 | Popularity bias | 4 | 3 | 12 | diversity + coverage constraints | Medium | Ranking Lead |
| R02 | Filter bubble | 4 | 4 | 16 | novelty quota + exploration | Medium | AI PM |
| R03 | Historical feedback loop | 4 | 4 | 16 | randomized exposure + debiasing | Medium | ML |
| R04 | Proxy discrimination | 3 | 5 | 15 | feature review + cohort tests | Medium | ML/Privacy |
| R05 | Sensitive inference | 2 | 5 | 10 | inference prohibition | Low | Privacy |
| R06 | Consent bypass | 2 | 5 | 10 | hard consent gate | Low | Platform |
| R07 | Cold-start degradation | 4 | 3 | 12 | generic fallback + exploration | Low | AI PM |
| R08 | Feature drift | 4 | 3 | 12 | PSI monitoring | Low | MLOps |
| R09 | Concept drift | 3 | 4 | 12 | KPI monitoring + retraining review | Medium | ML |
| R10 | Data leakage | 2 | 5 | 10 | chronological split + timestamp checks | Low | ML |
| R11 | Data-quality corruption | 3 | 4 | 12 | SLAs + pipeline validation | Low | Data Eng |
| R12 | Click optimization harms retention | 3 | 4 | 12 | EAR + long-term guardrails | Medium | AI PM |
| R13 | Merchant/category concentration | 3 | 4 | 12 | exposure constraints | Medium | Marketplace PM |
| R14 | Latency degradation | 3 | 3 | 9 | caching + fallback | Low | Platform |
| R15 | Experiment harm | 2 | 5 | 10 | staged rollout + kill switch | Low | Experiment Lead |
| R16 | Reward hacking | 3 | 4 | 12 | composite reward | Medium | ML |
| R17 | Hallucinated GenAI claim | 3 | 4 | 12 | retrieval grounding | Low | GenAI |
| R18 | Prompt injection | 3 | 4 | 12 | content isolation | Medium | Security |
| R19 | PII in prompt/output | 2 | 5 | 10 | PII filtering | Low | Privacy |
| R20 | Model extraction | 2 | 3 | 6 | rate limiting | Low | Security |
| R21 | Event poisoning | 3 | 4 | 12 | anomaly detection | Medium | Security/Data |
| R22 | Item metadata manipulation | 3 | 3 | 9 | catalog validation | Low | Catalog |
| R23 | Silent retraining degradation | 3 | 4 | 12 | champion/challenger gate | Low | MLOps |
| R24 | Dark-pattern personalization | 2 | 5 | 10 | UX ethics policy | Low | Design/PM |
| R25 | Opt-out failure | 2 | 5 | 10 | automated preference test | Low | Platform |
| R26 | Stale inventory recommendation | 3 | 3 | 9 | serve-time availability check | Low | Backend |
| R27 | Overfitting high-value users | 3 | 3 | 9 | segment-weighted metrics | Low | ML |
| R28 | Model-version traceability loss | 2 | 4 | 8 | required decision logging | Low | MLOps |
| R29 | Unapproved feature addition | 2 | 4 | 8 | feature registry/change control | Low | Data Gov |
| R30 | Fallback also fails | 2 | 5 | 10 | independent fallback health checks | Low | Platform |
