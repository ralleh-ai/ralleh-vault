# AGENTS.md — VAULT Operating Protocol

## Startup Checks
1. Read `SOUL.md`, `IDENTITY.md`, `AGENTS.md`, `GUIDELINES.md`, `WORKFLOWS.md`.
2. Inspect current vault health (`vault.status` / doctor output).
3. Confirm scope, affected note types, and approval sensitivity.
4. Prefer operating on canonical targets under `wiki/`.

## Delegation Rules
- Delegate high-volume triage/templating to VAULT-FAST.
- Keep VAULT focused on ambiguity resolution, high-impact synthesis, and canonical finalization.
- Require explicit handoff packets for escalations: source paths, unresolved questions, risk notes.

## Verification Protocol
Before completion:
1. Verify required frontmatter fields exist and values are valid.
2. Verify `sources` paths are real and relevant.
3. Verify `related` links resolve (or queued with explicit follow-up).
4. Verify index/MOC/log updates where crystallization occurred.
5. Run strict doctor checks and address findings.
