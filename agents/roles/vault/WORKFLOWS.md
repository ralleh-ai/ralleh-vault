# WORKFLOWS.md — VAULT

## Workflow Index

### vault.crystallize — Finalize canonical notes from draft or handoff input

1. Read the source handoff packet: source paths, candidate type, unresolved questions, risk notes.
2. Open each referenced `raw/` or `Inbox/` file. Read fully before writing anything.
3. Identify note type from content. Choose the matching template from `skills/vault/templates/`.
4. Resolve all conflicts across sources: rank by authority (transcripts > docs > exports > memory), document the resolution.
5. Write the canonical note under the appropriate `wiki/` subdirectory.
6. Populate all required frontmatter fields. Set `confidence` based on source quality (see `GUIDELINES.md`).
7. For `type: decision` or `type: procedure` with `status: active` or `stable`: confirm approval metadata exists. Block if missing.
8. Add or repair bidirectional `[[wikilinks]]` to related notes.
9. Append a new entry to `wiki/log.md`.
10. Update `wiki/index.md` if this is a new note or type category.
11. Run strict doctor: `python3 skills/vault/scripts/vault_doctor.py --vault-root vault/ --strict`
12. Fix any errors reported. Re-run until clean.
13. Remove source item from `Inbox/` after successful crystallization.

### vault.retrieve — Cited answer from canonical graph

1. Parse the query: entity name, topic, date range, or note type filter.
2. Search `wiki/` directory matching on filename and frontmatter title.
3. Follow `related` wikilinks to expand relevant context.
4. Fall back to `raw/` only if canonical coverage is weak or absent — note this explicitly.
5. Compose answer: short answer paragraph, then citation block listing source note paths.
6. Label confidence: `high` (complete canonical coverage), `medium` (partial), `low` (raw-only or conflicts present).
7. For BRAIN responses: serialize using the typed response schema from `TOOLS.md`.
8. State explicit gaps if confidence is `low` or `medium` — do not suppress uncertainty.

### vault.maintain — Graph hygiene, index/log upkeep, archival

1. Run doctor in strict mode. Review full output before touching files.
2. Fix broken wikilinks first (highest blast radius): find the moved/renamed target, update all references.
3. Fix missing required frontmatter (second priority): open the note, populate fields from source evidence.
4. Audit `wiki/index.md` against actual `wiki/` directory contents. Add missing entries; remove dead ones.
5. Check `wiki/log.md` is append-only and reflects recent crystallizations.
6. Review notes not updated in >90 days with `status: active`. Flag for review or archive.
7. Archive deprecated notes: set `status: deprecated`, add `superseded_by` if applicable, move to `wiki/Archive/`.
8. Check `Inbox/` age. Items older than policy threshold should be processed or explicitly escalated.
9. Re-run doctor strict. Confirm zero errors.

### vault.status — Health report and risk detection

1. Run doctor in both normal and strict modes. Capture full output.
2. Count: total `wiki/` notes, broken wikilinks, missing frontmatter, approval gate violations, `Inbox/` count and oldest age.
3. Classify risk level: `green` (zero issues), `yellow` (warnings only), `red` (errors present).
4. Report findings: summary metrics, issue list by severity, recommended next action.
5. Identify the single highest-blast-radius issue if any and surface it first.
6. For BRAIN callers: include `vault_health` summary in any query response where errors are present.

## What Belongs in examples/

- Escalation handoff packets from VAULT-FAST to VAULT (before/after format)
- Before/after crystallization examples showing ambiguity resolution decisions
- Retrieval answer examples with confidence label and citation block
- Conflict resolution examples — two conflicting sources, ranked resolution, documented outcome
- Doctor-failure remediation examples with minimal corrective edits
- BRAIN query/response examples (verify, crystallize, resolve_conflict)
