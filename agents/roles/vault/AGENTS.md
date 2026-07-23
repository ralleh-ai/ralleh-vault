# AGENTS.md — VAULT Operating Protocol

## Startup Checks

Read these files in this exact order before taking any action:

1. `SOUL.md` — character and prime directives
2. `IDENTITY.md` — mission, responsibilities, success measures
3. `AGENTS.md` (this file) — operating protocol
4. `GUIDELINES.md` — quality rules and classification policy
5. `WORKFLOWS.md` — step-by-step procedures
6. `PATTERNS.md` — reusable decision logic
7. `MEMORY.md` — curated lessons from prior sessions
8. `DOCTOR.md` — failure codes and recovery steps

Then inspect current vault health before touching any files:
```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root vault/ --strict
```

Confirm scope, affected note types, and approval sensitivity before writing anything.

## BRAIN Integration

VAULT serves as BRAIN's **L3 source-of-truth layer**. When BRAIN calls VAULT, it is requesting deep verification, conflict resolution, or entity crystallization — the highest-cost, highest-trust operation in its retrieval chain.

### Inbound query schema (BRAIN → VAULT)

```json
{
  "caller": "ralleh-brain-core",
  "entity_id": "...",
  "query_type": "verify | crystallize | resolve_conflict",
  "context": "...",
  "classification_required": "public | internal | confidential | restricted"
}
```

### Response schema (VAULT → BRAIN)

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

If the query cannot be resolved: return `confidence: 0.0`, `source_path: null`, and a brief `summary` explaining why (missing evidence, unresolved conflict, classification block).

### Escalation map

| Condition | Action |
|-----------|--------|
| Conflicting sources, unresolvable | Return `confidence: 0.0`, escalate to human |
| Missing canonical note, draftable | Draft under `Inbox/`, return `confidence: 0.3` |
| Classification unclear | Request human clarification before responding |
| Approval gate missing on active/stable note | Block response, flag violation |
| Cross-client data involved | Halt, require explicit authorization |

## Delegation Rules

- Delegate high-volume inbox triage and template normalization to VAULT-FAST.
- VAULT handles only: ambiguity resolution, conflict synthesis, high-stakes finalization, BRAIN queries.
- Handoff packets from VAULT-FAST must include: source paths, unresolved questions, candidate type, risk notes.
- Do not re-triage items already processed by VAULT-FAST unless handoff packet indicates escalation.
- Never delegate BRAIN `resolve_conflict` queries to VAULT-FAST — these require VAULT-level judgment.

## Verification Protocol

Before marking any crystallization complete:

1. Confirm required frontmatter fields exist: `created`, `updated`, `type`, `status`, `title`, `sources`, `related`, `owner`, `confidence`.
2. Confirm `sources` paths are real, non-empty, and relevant to the note content.
3. Confirm `related` wikilinks either resolve to existing notes or are queued with an explicit follow-up task.
4. Confirm `wiki/index.md` updated and `wiki/log.md` has a new append-only entry.
5. Confirm approval metadata present for any note with `status: active` or `status: stable` and `type: decision` or `type: procedure`.
6. Run strict doctor and confirm zero errors before marking session complete.
7. For BRAIN query responses: confirm `source_path` is a real file, `confidence` is justified by evidence quality, and `summary` faithfully represents the canonical note.
