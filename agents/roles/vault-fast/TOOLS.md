# TOOLS.md — VAULT-FAST Tool Posture

## Tooling Principles

- Optimize for deterministic throughput, not deep synthesis. Templates encode the structure; follow them.
- Batch similar operations. Switching between note types mid-batch increases error rate.
- Validate each batch before moving to the next — don't wait until the end.
- For BRAIN responses: serialize exactly to the typed schema. Missing fields cause BRAIN parse failures.
- Never populate `sources` with placeholder text. If the real path is unknown, escalate.

## Integrations

### Vault skill contract
Primary operational contract: `skills/vault/SKILL.md`

### Validation tool
```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root vault/ --strict
```

### Templates (apply before any custom content)
- `skills/vault/templates/concept.md`
- `skills/vault/templates/decision.md`
- `skills/vault/templates/entity.md`
- `skills/vault/templates/insight.md`
- `skills/vault/templates/meeting.md`
- `skills/vault/templates/procedure.md`
- `skills/vault/templates/project.md`

### Runbooks
- `skills/vault/runbooks/capture.md` — ingest source to raw/inbox
- `skills/vault/runbooks/process.md` — high-throughput normalization procedure

### Frontmatter schema
- `skills/vault/schemas/frontmatter.md` — required fields, valid enums

### BRAIN integration API

**Inbound query (BRAIN → VAULT-FAST):**
```json
{
  "caller": "ralleh-brain-core",
  "query_type": "bulk_draft | inbox_scan | normalize_batch",
  "vault_paths": ["vault/path/to/source.md"],
  "output_format": "entity_card | frontmatter_draft",
  "target_domain": "client | product | employee | project | general"
}
```

**Response (VAULT-FAST → BRAIN):**
```json
{
  "processed": [
    {
      "source_path": "vault/path/to/source.md",
      "draft": { "type": "entity", "title": "...", "confidence": "medium", "sources": ["vault/path/to/source.md"] },
      "candidate_classification": "internal",
      "confidence": 0.72
    }
  ],
  "escalations": [
    {
      "source_path": "vault/path/to/ambiguous.md",
      "reason": "Candidate type unclear",
      "candidate_type": "unknown",
      "unresolved_questions": ["Is this a project or a concept?"]
    }
  ]
}
```

**Coverage rule:** every path in `vault_paths` must appear in exactly one of `processed` or `escalations`.

## What Does Not Belong Here

- Policy decisions requiring VAULT or human judgment.
- Long-form synthesis or conflict resolution — that is VAULT's scope.
- Environment secrets, credentials, or client-specific configuration.
- Workflow policy (belongs in `GUIDELINES.md` and `WORKFLOWS.md`).
