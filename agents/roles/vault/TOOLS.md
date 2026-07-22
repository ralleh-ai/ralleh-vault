# TOOLS.md — VAULT Tool Posture

## Tooling Principles
- Use the smallest deterministic tool that proves correctness.
- Prefer file/read/doctor evidence over memory-only claims.
- Validate after each meaningful crystallization batch.

## Integrations
- Vault root layout from `scaffold/vault/`.
- Skill contract: `skills/vault/SKILL.md`.
- Validation tool: `skills/vault/scripts/vault_doctor.py`.
- Retrieval and operating runbooks: `skills/vault/runbooks/*`.

## What Does Not Belong Here
- Personal reminders unrelated to knowledge quality.
- Client secrets or credentials.
- Workflow policy that belongs in `GUIDELINES.md` / `WORKFLOWS.md`.
