# Runbook: vault.maintain

1. Check Inbox count and oldest item age.
2. Run doctor checks (strict for release branches).
3. Fix missing frontmatter and stale `updated` fields.
4. Repair broken links or park unresolved links in a backlog note.
5. Archive stale notes with `status: archived` and links to replacements.
6. Keep `wiki/index.md` and `wiki/log.md` coherent.
7. For client-scoped roots, run per-client and report per-client deltas.
