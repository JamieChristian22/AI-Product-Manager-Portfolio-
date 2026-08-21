# Audit Trail Requirements

Every served decision should be traceable to:
- request/session ID
- pseudonymous user key
- consent status
- model version
- policy version
- feature snapshot timestamp
- experiment assignment
- candidate-set hash
- selected item IDs
- latency
- fallback flag
- suppression events

Every model release should preserve:
- code commit
- training dataset version
- feature schema
- hyperparameters
- validation report
- risk review
- approvers
- deployment timestamp
- rollback target
