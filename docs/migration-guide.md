# Migration Guide: Ad-hoc Notes → Ralleh Vault

This guide moves an existing note pile into a structured Vault with minimal risk.

## Goals

- Preserve all source material.
- Separate raw capture from canonical knowledge.
- Establish repeatable processing and crystallization flow.

## Safety-first migration rules

1. Never edit original source exports directly.
2. Keep a full backup before transformations.
3. Migrate in small batches with validation after each batch.

## Step 0 — Backup and inventory

```bash
cp -R <your-notes-root> <your-notes-root>.backup
find <your-notes-root> -type f | wc -l
```

Create a lightweight inventory by source kind:
- transcripts
- documents
- research
- meeting notes
- project notes

## Step 1 — Scaffold Vault root

```bash
cp -R scaffold/vault /path/to/workspace/vault
python3 skills/vault/scripts/vault_doctor.py --vault-root /path/to/workspace/vault --strict
```

## Step 2 — Land originals into `raw/`

- Place immutable originals under:
  - `vault/raw/transcripts/`
  - `vault/raw/documents/`
  - `vault/raw/research/`
  - `vault/raw/exports/`

Do not rewrite content during this step.

## Step 3 — Create Inbox processing batches

- Create one batch note per domain in `vault/Inbox/`, for example:
  - `2026-07-22-batch-project-atlas.md`
  - `2026-07-22-batch-sales-handoffs.md`

Include:
- source file list
- initial type guess
- confidence estimate

## Step 4 — Run `vault.process` (VAULT-FAST)

Expected outputs:
- drafts under `wiki/<Type>/`
- valid baseline frontmatter
- unresolved ambiguity captured as handoff notes

## Step 5 — Run `vault.crystallize` (VAULT)

Expected outputs:
- canonical notes with complete provenance
- resolved conflicts where possible
- index/MOC updates and log entries

## Step 6 — Validate after each batch

```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root /path/to/workspace/vault
python3 skills/vault/scripts/vault_doctor.py --vault-root /path/to/workspace/vault --strict
```

## Step 7 — Activate operating rhythm

- Daily: process inbox.
- Weekly: crystallize high-value drafts and run strict doctor.
- Monthly: archive deprecated notes and review link graph quality.

## Common migration anti-patterns

- Writing canonical notes directly from memory without `sources`.
- Mixing multiple clients in one wiki tree.
- Leaving `Inbox/` to accumulate for weeks.
- Bulk deleting “messy” notes before provenance is preserved.
