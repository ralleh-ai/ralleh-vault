# Data Ingestion Guide

How to feed Ralleh Vault so retrieval quality stays high.

## Ingestion objective

Move source material into Vault with maximum provenance and minimum distortion.

## Data classes

### A) Immutable source data (`raw/`)

Use for:
- call transcripts
- exported docs
- research captures
- system exports

Paths:
- `vault/raw/transcripts/`
- `vault/raw/documents/`
- `vault/raw/research/`
- `vault/raw/exports/`

Rules:
- Do not modify files after ingest.
- Preserve source filenames when possible.
- Keep directory naming predictable.

### B) Working triage data (`Inbox/`)

Use for:
- fresh notes and observations
- unresolved meeting summaries
- ambiguity packets for processing

Path:
- `vault/Inbox/`

## Suggested naming conventions

### Raw files

`YYYY-MM-DD_<source>_<topic>.<ext>`

Examples:
- `2026-07-22_zoom_client-alpha-kickoff.txt`
- `2026-07-22_notion_pricing-notes.md`

### Inbox files

`YYYY-MM-DD-batch-<topic>.md`

Examples:
- `2026-07-22-batch-client-alpha.md`
- `2026-07-22-batch-oncall-retro.md`

## Ingestion checklist

1. Land all originals in `raw/` first.
2. Create inbox batch note with intent and scope.
3. Run `vault.process` for normalization.
4. Run `vault.crystallize` for canonicalization.
5. Confirm `sources` in canonical notes reference real raw paths.
6. Run strict doctor validation.

## Anti-patterns to avoid

- writing canonical notes with empty `sources`
- deleting rough notes before provenance is captured
- mixing client data in one batch without explicit approval
- letting Inbox age exceed policy thresholds
