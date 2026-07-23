# WORKFLOWS.md — VAULT-FAST

## Workflow Index

### vault.capture — Ingest source material to raw/ or Inbox/

1. Receive the inbound artifact: transcript, document, export, or meeting note.
2. Determine destination:
   - Durable source artifact → `vault/raw/<bucket>/` (transcripts, documents, research, exports)
   - Fleeting or unresolved note → `vault/Inbox/<slug>-<date>.md`
3. Save without editing content. Raw files are immutable after ingest.
4. Record minimal context in filename: origin type and date at minimum.
5. Confirm the file is saved before reporting capture complete.

### vault.process — High-throughput classification and draft generation

1. Measure Inbox state: count items and find oldest item age. Record before-state.
2. Sort by oldest age (process oldest first).
3. Pick a bounded batch (10–20 items, or all if smaller).
4. For each item:
   a. Read the full source file.
   b. Classify into `concept | decision | entity | insight | meeting | procedure | project`.
   c. If type is unclear or content triggers escalation criteria (see `GUIDELINES.md`): create escalation packet, skip draft generation.
   d. Open the matching template from `skills/vault/templates/`.
   e. Populate required frontmatter: `created`, `updated`, `type`, `status: draft`, `title`, `sources`, `related` (candidates), `owner`, `confidence`.
   f. Write key bullet points. Add open questions block if unresolved items exist.
   g. Save draft to `vault/wiki/<type>/<title>.md`.
5. Validate frontmatter on completed drafts:
   ```bash
   python3 skills/vault/scripts/vault_doctor.py --vault-root vault/ --strict
   ```
6. Fix schema errors before reporting batch complete.
7. Move processed Inbox items to `vault/wiki/` or mark as escalated.
8. Report: items processed, items escalated, Inbox count and oldest age before/after.

### vault.status — Backlog health snapshot

1. Count `Inbox/` items and find oldest age.
2. Run doctor (normal mode for speed, strict if full check requested):
   ```bash
   python3 skills/vault/scripts/vault_doctor.py --vault-root vault/
   ```
3. Sample 5 most recent drafts for schema compliance.
4. Report: Inbox count, oldest age, doctor summary, batch compliance rate.
5. Classify backlog risk: `green` (count < 20, age < 3d), `yellow` (count 20–50 or age 3–7d), `red` (count > 50 or age > 7d).

### vault.maintain — Lightweight cleanup and archival prep

1. Run doctor strict. Review full output.
2. Fix obviously broken draft frontmatter (missing fields, invalid enums).
3. Remove noise from Inbox: duplicates, zero-content files, test artifacts.
4. Identify drafts older than 30 days with `status: draft` — flag for review or escalate to VAULT.
5. Confirm Inbox trend is flat or decreasing before completing the session.

## What Belongs in examples/

- Inbox triage batch examples: before-state, classification decisions, after-state report
- Low/high confidence classification examples with reasoning
- Escalation handoff packet examples for VAULT
- Before/after draft normalization: raw messy note → template-compliant draft
- BRAIN batch query/response examples (bulk_draft, inbox_scan)
