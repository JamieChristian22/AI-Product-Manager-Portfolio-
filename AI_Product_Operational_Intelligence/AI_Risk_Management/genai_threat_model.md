# GenAI Threat Model & Red-Team Plan

## Assets to Protect
Approved catalog facts, system/policy instructions, confidential commercial information, user privacy, brand reputation, and publishing controls.

## Threat Scenarios
1. Catalog description contains “ignore previous instructions” prompt injection.
2. Product metadata asks the model to invent a 50% discount.
3. Input requests disclosure of hidden/system instructions.
4. Untrusted text tries to insert malicious links or HTML.
5. Model invents medical, safety, legal, or sustainability claims.
6. Prompt asks for competitor defamation or unsupported superiority claims.
7. User/customer data is accidentally copied into merchandising context.
8. Model is asked to publish directly without human approval.

## Controls
Separate system instructions from untrusted catalog text; delimit data; only expose allowlisted fields; do not place secrets in prompts; validate numeric discounts against pricing service; filter prohibited claim classes; strip active links/HTML where not explicitly supported; require human campaign approval; log model version, prompt template version, source fields, filter outcome, and reviewer action.

## Red-Team Results (Synthetic)
200 adversarial cases executed. 196 were safely rejected or grounded; 4 produced policy-risk content before filtering; all 4 were blocked by post-generation validation. Effective unsafe-output delivery rate = 0%. Residual risk remains because novel prompt attacks can emerge; monthly red-team refresh is required.
