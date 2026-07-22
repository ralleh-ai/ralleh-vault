# TOOLS.md — VAULT-FAST Tool Posture

## Tooling Principles
- Optimize for deterministic throughput, not deep synthesis.
- Batch similar operations to reduce context switching.
- Validate each batch before moving to the next.

## Integrations
- Skill contract: `skills/vault/SKILL.md`.
- Templates: `skills/vault/templates/`.
- Runbooks: `skills/vault/runbooks/process.md` and `runbooks/capture.md`.
- Validation: `skills/vault/scripts/vault_doctor.py`.

## What Does Not Belong Here
- Final policy decisions that require VAULT/human judgment.
- Long-form synthesis narratives.
- Environment secrets or unrelated operational data.
