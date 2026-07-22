# Role Quality Contract (VAULT / VAULT-FAST)

This repo enforces ralleh-agents-style role precision for Vault roles.

## Scope
Audited roles:
- `agents/roles/vault`
- `agents/roles/vault-fast`

## Required Files
Each role must include:
- `README.md`
- `SOUL.md`
- `IDENTITY.md`
- `AGENTS.md`
- `TOOLS.md`
- `DOCTOR.md`
- `GUIDELINES.md`
- `WORKFLOWS.md`
- `MEMORY.md`
- `USER.md`
- `PATTERNS.md`

## Required Sections
Key section headers are enforced per file (startup checks, delegation rules, verification protocol, quality rules, etc.).

## Size Discipline
Word caps are enforced to prevent role bloat and preserve execution focus.

## Audit Command
```bash
python3 scripts/audit_roles.py
```

## Verdicts
- `golden` — no issues
- `usable` — warnings only
- `bloated` — size-cap violations
- `risky` — other errors
- `misplaced` — missing required files/sections

## CI Gate
`validate-vault` runs role audit in CI. `make validate` enforces the same gate locally.
