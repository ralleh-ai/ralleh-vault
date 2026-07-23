# VAULT-FAST Role Package

## Purpose

VAULT-FAST is the high-throughput normalization and triage role for Ralleh Vault. It transforms noisy inbound material into schema-valid knowledge drafts and clean escalation packets, and serves as BRAIN's bulk entity seeding pipeline.

Primary outcomes:
- Inbox velocity with low rework rate
- Schema-compliant drafts with real provenance on first pass
- Clean, complete escalation packets for VAULT
- Typed BRAIN batch query responses with 100% path coverage

## When to use VAULT-FAST

Use VAULT-FAST for:
- Inbox triage and batch normalization
- Type classification and template application
- BRAIN `bulk_draft`, `inbox_scan`, `normalize_batch` queries
- Routine frontmatter generation for clearly-scoped source material

Do **not** use VAULT-FAST for:
- Conflict resolution requiring cross-source judgment (use VAULT)
- Finalizing active/stable decisions or procedures (use VAULT)
- Deep synthesis or canonical note finalization (use VAULT)

## How it fits the system

```
Inbound material (raw/, Inbox/)
  └─ vault.capture → VAULT-FAST (triage + normalize)
       ├─ clean drafts → wiki/ (draft status, for VAULT finalization)
       └─ escalations → Inbox/escalation-* → VAULT (judgment)

BRAIN (bulk entity seeding)
  └─ bulk_draft / inbox_scan / normalize_batch → VAULT-FAST
       └─ processed + escalations → BRAIN (entity registry update)
```

## Quick reference

| Operation | Workflow | Runbook |
|-----------|----------|---------|
| Ingest source artifact | `vault.capture` | `runbooks/capture.md` |
| Process Inbox batch | `vault.process` | `runbooks/process.md` |
| Check backlog health | `vault.status` | `runbooks/status.md` |
| Lightweight cleanup | `vault.maintain` | `runbooks/maintain.md` |

## Required files in this package

README.md, SOUL.md, IDENTITY.md, AGENTS.md, TOOLS.md, DOCTOR.md, GUIDELINES.md, WORKFLOWS.md, MEMORY.md, USER.md, PATTERNS.md

## Validation

```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root vault/ --strict
python3 scripts/audit_roles.py
```
