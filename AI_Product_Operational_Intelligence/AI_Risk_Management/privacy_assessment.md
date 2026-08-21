# Privacy & Data Protection Assessment

## Purpose Limitation
Behavioral and transaction-derived features are used only to improve relevance, estimate checkout risk, evaluate bounded commercial scenarios, and measure product experiments.

## Data Minimization
Modeling uses pseudonymous session/user identifiers rather than direct identity. Precise address, payment-card data, government identifiers, private messages, health data, and protected attributes are excluded.

## Retention
Web/session behavior: 90 days; commerce-derived aggregates: up to 365 days; model monitoring aggregates: 365 days; raw GenAI evaluation prompts: 30 days in the simulation unless retained as de-identified benchmark examples.

## Access
Role-based access separates commercial cost data from general product analytics. Model developers receive the minimum data required. Administrative access is logged and reviewed monthly.

## User Controls
Personalized interventions respect suppression rules. Recommendation explanations can reference broad signals such as recent browsing or category interest. A production implementation should support applicable privacy rights and preference controls according to jurisdiction and company policy.

## Privacy Incident Trigger
Unexpected direct identifiers in model datasets, unauthorized access, retention beyond policy, or sensitive data appearing in GenAI prompts is treated as SEV-1: stop affected processing, preserve evidence, revoke access, assess scope, remove data, and require privacy/security approval before restart.
