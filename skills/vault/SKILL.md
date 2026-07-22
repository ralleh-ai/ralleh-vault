---
name: vault
description: "Capture, process, crystallize, retrieve, and maintain a local-first Markdown knowledge vault with strict provenance and linking."
---

# Ralleh Vault

Use when working with durable organizational knowledge in Markdown form.

## Scope

- Build and maintain a vault rooted at `vault/`.
- Keep `raw/` immutable.
- Keep durable knowledge under `wiki/`.
- Maintain provenance (`sources`) and graph quality (`related` wikilinks).

## Capability map

- `vault.capture`: land signals into `Inbox/` or `raw/`.
- `vault.process`: triage and normalize high-volume inputs (VAULT-FAST default).
- `vault.crystallize`: produce high-judgment canonical knowledge notes (VAULT default).
- `vault.query` / `vault.retrieve`: return cited context packs from canonical notes.
- `vault.maintain`: clean inbox, fix links, archive stale docs, run health checks.
- `vault.status`: report vault health (inbox size, missing frontmatter, broken links).
- `vault.promote`: stub for future Engram/source promotion into vault workflows.

## Vault root modes

### Mode A — Single shared root

```text
vault/
├── Inbox/
├── Daily/
├── raw/
├── wiki/
├── Templates/
└── Attachments/
```

### Mode B — Client-scoped root

```text
vault/
├── _shared/
│   ├── raw/
│   └── wiki/
└── clients/
    └── <client-slug>/
        ├── Inbox/
        ├── Daily/
        ├── raw/
        ├── wiki/
        ├── Templates/
        └── Attachments/
```

Rules:
- Client roots are hard boundaries.
- No cross-client linking without explicit approval.
- Set frontmatter `clients:` consistently for tenant routing.

## Hard rules

- Never edit files in `raw/` after ingest.
- Never store durable canonical notes outside `wiki/`.
- Use `[[wikilinks]]` for relationships; tags are optional and sparse.
- Every crystallized `wiki/` note must have required frontmatter.

## Required frontmatter

Use schema in `schemas/frontmatter.md`.

Minimum fields:
- `created`, `updated`, `type`, `status`, `title`
- `sources`, `related`, `owner`, `confidence`
- Optional: `tags`, `clients`, `projects`

## Workflow

### 1) Capture

1. Receive source material.
2. Save immutable source to `raw/<bucket>/...`.
3. Save fleeting notes to `Inbox/...`.
4. Record minimal context (origin/time).

### 2) Process (VAULT-FAST)

1. Scan `Inbox/` and newly landed raw files.
2. Remove obvious noise/duplicates.
3. Classify into `project|area|resource|entity|meeting|insight|other`.
4. Draft note from template with baseline frontmatter.
5. Add key bullets, open questions, and candidate links.
6. Escalate complex/ambiguous/high-risk items to VAULT.

### 3) Crystallize (VAULT)

1. Resolve ambiguity and conflicts across sources.
2. Write canonical note under `wiki/` with full provenance.
3. Add/repair bidirectional links for related notes.
4. Update `wiki/index.md` and append event to `wiki/log.md`.
5. Mark status correctly (`draft|active|stable|archived|deprecated`).

## Query / retrieve behavior

- Search canonical `wiki/` first, then contextual sources.
- Return short answer + cited note paths.
- Prefer linking canonical note over re-summarizing raw text.
- If confidence is low, surface uncertainty and next best sources.

## Approval gates (must ask first)

Ask for explicit approval before:
- Writing/changing major `Decision` and production `Procedure` notes.
- Deleting anything outside `Inbox/`.
- Cross-client links or merges.
- Client-sensitive classification with legal/compliance impact.
- Large archival moves that alter active project visibility.

## Maintenance and doctor standards

- Keep `Inbox/` trending to zero.
- Keep `wiki/index.md` current.
- Keep `wiki/log.md` append-only.
- Run doctor checks from `scripts/vault_doctor.py`.
- Use strict mode for CI and release gates:
  - `python3 skills/vault/scripts/vault_doctor.py --vault-root <root> --strict`

## Git conventions

- Commit style:
  - `feat(vault): ...`
  - `fix(vault): ...`
  - `docs(vault): ...`
  - `chore(vault): ...`
- Validate before commit with doctor.

## Collaboration model

- VAULT-FAST handles throughput and structure.
- VAULT handles quality, synthesis, and final graph integrity.
- Other agents can request `vault.*` operations or hand off to VAULT / VAULT-FAST.

## Verification checklist (per operation)

- Frontmatter valid and complete.
- `sources` populated and real.
- `related` wikilinks resolve or are queued for creation.
- `updated` changed.
- index/log updated for crystallization operations.
