# TOOLS.md — VAULT Tool Posture

## Tooling Principles

- Use the smallest deterministic tool that proves correctness. Read the file; don't rely on memory.
- Validate with the doctor script before marking any batch complete — never skip this step.
- Prefer file/read/doctor evidence over in-context claims.
- Treat JSON API contracts as typed — never omit required fields from a BRAIN response.
- Check that `sources` paths are real files before committing a canonical note.

## Integrations

### Vault skill contract
Primary operational contract: `skills/vault/SKILL.md`

### Validation tool
```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root vault/ --strict
```
Run strict mode after every crystallization batch. Non-strict mode is for exploratory checks only.

### Runbooks (authoritative step-by-step procedures)
- `skills/vault/runbooks/crystallize.md` — finalize canonical notes from drafts
- `skills/vault/runbooks/query.md` — retrieve with citations
- `skills/vault/runbooks/maintain.md` — hygiene, archival, link repair
- `skills/vault/runbooks/status.md` — health report generation
- `skills/vault/runbooks/promote.md` — promote material to Engram or BRAIN registry

### Templates
- `skills/vault/templates/` — type templates for concept, decision, entity, insight, meeting, procedure, project

### Frontmatter schema
- `skills/vault/schemas/frontmatter.md` — required fields, valid enum values, constraints

### BRAIN integration API

**Inbound query (BRAIN → VAULT):**
```json
{
  "caller": "ralleh-brain-core",
  "entity_id": "...",
  "query_type": "verify | crystallize | resolve_conflict",
  "context": "...",
  "classification_required": "public | internal | confidential | restricted"
}
```

**Response (VAULT → BRAIN):**
```json
{
  "source_path": "vault/wiki/path/to/note.md",
  "summary": "1-3 sentence summary of canonical content",
  "classification": "public | internal | confidential | restricted",
  "last_verified_at": "ISO-8601 timestamp",
  "confidence": 0.85,
  "redacted": false
}
```

Confidence scoring guide:
- `0.9–1.0`: complete frontmatter, non-empty sources, no conflicts, strict doctor passes
- `0.6–0.89`: minor gaps (missing related links, 1 weak source), no approval failures
- `0.3–0.59`: draft status, partial sources, or open conflicts noted in note body
- `0.0–0.29`: unresolvable conflict, missing evidence, or classification block — escalate

## What Does Not Belong Here

- Personal reminders or calendar items unrelated to knowledge quality.
- Client secrets, API keys, or credentials.
- Workflow policy (belongs in `GUIDELINES.md` and `WORKFLOWS.md`).
- Operational runbook text (belongs in `skills/vault/runbooks/`).
