# PATTERNS.md — Shared Patterns

# PATTERNS.md — Shared Patterns

## Pattern: Batch Processing

**Input:** Bounded set of `Inbox/` items or `vault_paths` from a BRAIN query.

**Logic:**
1. Sort by oldest age. Process oldest first.
2. Group by candidate type where possible (type-homogenous batches are faster and lower error rate).
3. For each item: read → classify → template → populate frontmatter → generate candidate links → validate.
4. If any item triggers escalation criteria: create escalation packet immediately. Do not attempt to process.
5. Validate batch before reporting complete. Fix schema errors in the same session.

**Output:** Schema-valid drafts in `wiki/` + escalation packets in `Inbox/escalation-*.md` + before/after Inbox count report.

**Failure signal:** Batch reported complete but doctor returns frontmatter errors, or Inbox oldest age increases.

---

## Pattern: Escalation Packet

**Input:** Item that exceeds VAULT-FAST's judgment scope.

**Logic:**
1. Collect: source path, candidate type (best guess), reason for escalation, unresolved questions, risk/impact note.
2. Write to `Inbox/escalation-<slug>-<date>.md` using draft frontmatter.
3. Set `type: insight` or `type: decision` as appropriate for the escalation type.
4. Set `status: draft`, `confidence: low`, `owner: vault`.
5. Include all open questions as a numbered list in the note body.
6. Do not attempt to answer the open questions. Leave them verbatim for VAULT.

**Output:** Escalation draft with complete context. VAULT can process without re-reading the original source.

**Failure signal:** Escalation packet missing source path, reason, or unresolved questions.

---

## Pattern: Backlog Control

**Input:** Current Inbox state (count + oldest age).

**Logic:**
1. Measure oldest age. If >7 days, this is the top priority — reduce before processing newer items.
2. Measure count. If >50, operate in triage mode: classify first, draft second.
3. Triage mode: classify all items, create escalation packets for VAULT-scope items, draft only clearly in-scope items.
4. Report before/after state every session. Track trend over time in `MEMORY.md`.
5. Never process a batch so large that per-item validation becomes impractical.

**Output:** Inbox state report. Oldest age must not increase after a session.

**Failure signal:** Inbox count grows session over session without explanation.

---

## Pattern: BRAIN Seeding (bulk_draft / inbox_scan / normalize_batch)

**Input:** BRAIN query with `vault_paths` list and `output_format`.

**Logic:**
1. Read each file in `vault_paths`. Do not skip unreadable files — add them to escalations.
2. For each readable file: classify, apply template logic, populate draft frontmatter.
3. Assign `candidate_classification` based on content context (default: `internal`).
4. Assign numeric `confidence` based on source quality: 0.7–0.9 for clean templates, 0.3–0.6 for partial sources, 0.0–0.2 for missing or ambiguous data.
5. Every path must appear in `processed` or `escalations` — no silent drops.
6. Serialize response using the typed schema from `TOOLS.md`.

**Output:** Typed JSON response with `processed` and `escalations` arrays covering 100% of input paths.

**Failure signal:** `vault_paths` has 10 items but response has 8 entries. Silent drops break BRAIN's coverage tracking.
