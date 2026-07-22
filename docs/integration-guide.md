# Integration Guide (OpenClaw + Ralleh Vault)

This guide explains how to wire Ralleh Vault into an OpenClaw environment for reliable, repeatable knowledge operations.

## 1) Integration goals

- Keep knowledge local-first and inspectable.
- Separate high-throughput processing from high-judgment synthesis.
- Enforce deterministic quality checks before release merges.

## 2) Components to integrate

- Skill package: `skills/vault/`
- Role package (synthesis): `agents/roles/vault/`
- Role package (throughput): `agents/roles/vault-fast/`
- Working data root: `vault/` (from `scaffold/vault/`)

## 3) Role responsibilities

### VAULT-FAST

Use for:
- inbox triage
- type classification
- template normalization
- handoff creation when confidence is low or ambiguity is high

### VAULT

Use for:
- conflict resolution across sources
- decision/procedure crystallization
- canonical graph integrity
- final quality gate before operational reliance

## 4) Recommended operational choreography

1. `vault.capture` lands raw source + inbox note.
2. `vault.process` runs in VAULT-FAST.
3. Escalation handoffs are produced for uncertainty.
4. `vault.crystallize` runs in VAULT.
5. `vault.retrieve` serves cited answers.
6. `vault.maintain` and `vault.status` keep system health visible.

## 5) Tenant and boundary model

- Single-tenant: one shared `vault/` root.
- Multi-tenant: client-scoped roots under approved boundary rules.

See `docs/client-scoping.md`.

## 6) Integration acceptance checks

- strict doctor passes
- canonical notes have non-empty `sources`
- no broken wikilinks
- approval gates met for active/stable decisions and procedures
- inbox age remains under threshold
