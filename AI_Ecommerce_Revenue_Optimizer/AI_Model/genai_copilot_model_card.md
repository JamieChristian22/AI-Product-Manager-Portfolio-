# Model Card — Generative Merchandising Copilot

## Purpose
Draft concise merchandising copy from approved product catalog attributes to accelerate internal content workflows.

## Allowed Inputs
Product name, category, material, dimensions, approved features, approved benefits, brand tone, shipping facts, and approved promotion terms.

## Prohibited Inputs/Outputs
No fabricated specifications, health claims, legal guarantees, counterfeit claims, unsupported sustainability claims, competitor defamation, or unapproved pricing promises. Raw customer private data is not inserted into prompts.

## Evaluation Set
1,000 synthetic product-copy prompts spanning apparel, electronics, home, beauty, accessories, and seasonal merchandise. Outputs are reviewed against structured source attributes.

## Results
| Metric | Gate | Result |
|---|---:|---:|
| Grounded Claim Rate | >=98.0% | 98.7% |
| Unsupported Claim Rate | <=2.0% | 0.8% |
| Brand Tone Compliance | >=95.0% | 96.9% |
| Policy Violation Rate | <=1.0% | 0.3% |
| Human Acceptance w/minor edits | >=85.0% | 89.4% |

## Controls
Catalog text is treated as untrusted data and delimited separately from instructions. The model receives no secrets and no open-ended tool access. High-risk or unsupported claims are blocked. Campaign-level copy requires human approval before publication.

## Red-Team Focus
Prompt injection embedded in catalog text, attempts to reveal system instructions, fabricated discounts, unsupported product benefits, malicious HTML/links, and instructions to ignore brand/policy constraints.
