# PATTERNS.md — Shared Patterns

# PATTERNS.md — Shared Patterns

## Pattern: Crystallization

**Input:** Draft note or handoff packet with source paths, candidate type, unresolved questions.

**Logic:**
1. Identify the dominant source (most authoritative, most recent).
2. Extract key claims, decisions, or facts. One claim per bullet in the note body.
3. For each claim, cite the source path inline or in frontmatter `sources`.
4. Assign `status: draft` initially. Upgrade to `active` only after all required fields pass doctor check.
5. For decisions/procedures: requires explicit approval before `active` or `stable`.

**Output:** Canonical `wiki/` note with complete frontmatter, cited body, and resolved wikilinks.

**Failure signal:** `sources` empty, `confidence` unset, or doctor returns errors.

---

## Pattern: Conflict Resolution

**Input:** Two or more sources with contradicting claims about the same entity or fact.

**Logic:**
1. Identify the conflict explicitly. Write it in the note as an open question.
2. Rank sources by authority: primary transcripts > formal documents > exports/secondary docs > agent memory.
3. Rank by freshness: newer source wins unless older source is the authoritative record (e.g., a signed decision).
4. If resolvable: state the resolution and cite all governing evidence. Mark which source was overridden and why.
5. If not resolvable: set `confidence: low`, document the conflict with all source paths, and escalate to human.

**Output:** Note with explicit resolution or documented escalation. Never silently pick one source.

**Failure signal:** Note finalized with `confidence: high` despite conflicting sources.

---

## Pattern: Retrieval

**Input:** Query — entity name, topic, question, or date range.

**Logic:**
1. Search `wiki/` first. Title match, then frontmatter `tags` and `type` filter.
2. Follow `related` wikilinks to expand context. Max 2 hops unless query is explicitly broad.
3. If canonical coverage is weak: check `raw/` as secondary evidence. Flag this explicitly.
4. Compose: short answer (1–3 sentences), then citations (note paths).

**Confidence assignment:**
- `high`: full canonical coverage, no conflicts, `status: stable` or `active`
- `medium`: partial coverage, minor gaps
- `low`: raw-only, draft status, or unresolved conflicts

**Output:** Answer + confidence label + citation list. State gaps explicitly when confidence < high.

---

## Pattern: BRAIN Query Response

**Input:** Typed BRAIN query — `verify`, `crystallize`, or `resolve_conflict`.

**Logic:**
1. Read the query `entity_id` and `query_type`. Locate the canonical note.
2. Apply the matching workflow: retrieval for `verify`, crystallization for `crystallize`, conflict resolution for `resolve_conflict`.
3. Serialize response using the typed schema from `TOOLS.md`.
4. Set `confidence` numerically (0.0–1.0) based on source quality and doctor status.
5. If classification is higher than `classification_required`: set `redacted: true` and omit body from summary.

**Output:** Typed JSON response. Never omit `source_path` (use `null` if not found), `confidence`, or `summary`.

**Failure signal:** Response with `confidence: 0.9` and `source_path: null`. That is contradictory.

---

## Pattern: Escalation Packet

**Input:** Item that VAULT cannot resolve safely without human input.

**Logic:**
1. Collect: source path(s), candidate type, reason for escalation, unresolved questions, risk/impact note.
2. Write to `Inbox/escalation-<slug>-<date>.md` using draft frontmatter.
3. Notify the appropriate owner (human or orchestrator) with the escalation file path.
4. Do not finalize the note until escalation is resolved.
5. When resolved: incorporate the resolution, update `updated`, upgrade `status`, re-run doctor.

**Output:** Escalation draft in `Inbox/` with complete context for human or orchestrator review.

**Failure signal:** Escalation created but no owner assigned or no follow-up path recorded.
