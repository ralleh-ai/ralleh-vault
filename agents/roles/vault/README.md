# VAULT Role Package

## Purpose

VAULT is the high-judgment knowledge steward for Ralleh Vault. It converts ambiguous drafts, handoff packets, and conflicting sources into canonical, source-grounded wiki notes that are safe to rely on for retrieval, audit, and downstream agent consumption.

VAULT is BRAIN's **L3 source-of-truth layer** — the deepest and most authoritative tier in the Ralleh retrieval hierarchy. When BRAIN cannot verify an entity from its hot cache or Engram, it calls VAULT.

## When to use VAULT

Use VAULT for:
- Crystallizing high-stakes drafts: decisions, procedures, complex entities
- Resolving conflicts between sources that VAULT-FAST escalated
- Responding to BRAIN `verify`, `crystallize`, or `resolve_conflict` queries
- Graph maintenance: broken links, approval gate violations, stale note review
- Final quality gate before operational reliance on any canonical note

Do **not** use VAULT for:
- High-volume inbox triage (use VAULT-FAST)
- Simple template normalization with no ambiguity (use VAULT-FAST)
- Raw file ingestion (use `vault.capture`)

## How it fits the system

```
BRAIN (entity registry)
  └─ L3 verify → VAULT (canonical source-of-truth)
                   └─ upstream triage → VAULT-FAST (inbox/bulk processing)
```

VAULT-FAST processes inbound material and escalates uncertain items. VAULT crystallizes escalated items and serves BRAIN queries. BRAIN caches VAULT responses with a TTL.

## Quick reference

| Operation | Workflow | Runbook |
|-----------|----------|---------|
| Finalize a draft note | `vault.crystallize` | `runbooks/crystallize.md` |
| Answer a BRAIN query | `vault.retrieve` | `runbooks/query.md` |
| Fix broken links, stale notes | `vault.maintain` | `runbooks/maintain.md` |
| Check vault health | `vault.status` | `runbooks/status.md` |

## Required files in this package

README.md, SOUL.md, IDENTITY.md, AGENTS.md, TOOLS.md, DOCTOR.md, GUIDELINES.md, WORKFLOWS.md, MEMORY.md, USER.md, PATTERNS.md

## Validation

```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root vault/ --strict
```

Both roles (vault, vault-fast) must pass `golden` verdict in CI:
```bash
python3 scripts/audit_roles.py
```
