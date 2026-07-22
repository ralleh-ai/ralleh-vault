# Runbook: vault.status

Report current vault health in a compact snapshot.

## Output

- Inbox item count + oldest item age
- Raw source count by bucket
- Canonical wiki note count by type
- Frontmatter compliance summary
- Broken wikilink count
- Approval-gate compliance for active/stable decisions/procedures
- Last 10 entries from `wiki/log.md`
- Recommended next actions

## Procedure

1. Count files in `Inbox/`, `raw/`, and `wiki/` subfolders.
2. Run doctor checks (`scripts/vault_doctor.py`).
3. Read and include recent entries from `wiki/log.md`.
4. Return concise summary with blockers first.
