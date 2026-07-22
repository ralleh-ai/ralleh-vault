# Getting Started (First Day)

A practical first-day rollout for Ralleh Vault.

## Goal

Have a working vault with:
- validated structure
- first ingestion batch
- first canonical notes
- successful retrieval with citations

## 0) Preconditions

- Python 3 available (`python3 --version`)
- OpenClaw workspace access
- source materials ready (transcripts/docs/notes)

## 1) Scaffold and validate

```bash
cp -R scaffold/vault /path/to/workspace/vault
python3 skills/vault/scripts/vault_doctor.py --vault-root /path/to/workspace/vault --strict
```

## 2) Ingest first sources

Put originals in:
- `vault/raw/transcripts/`
- `vault/raw/documents/`
- `vault/raw/research/`

Create one Inbox batch:
- `vault/Inbox/YYYY-MM-DD-batch-<topic>.md`

## 3) Process with VAULT-FAST

Run a processing pass to:
- classify notes
- normalize frontmatter
- generate candidate links
- escalate uncertain items

## 4) Crystallize with VAULT

For escalated and high-value items:
- produce canonical notes in `wiki/`
- ensure `sources` and `related` are meaningful
- update `wiki/index.md`
- append `wiki/log.md`

## 5) Validate health gates

```bash
make validate
```

Success conditions:
- strict doctor passes
- no broken wikilinks
- no approval-gate violations

## 6) Prove retrieval

Run a retrieval request such as:
- "What was decided for Project X and why?"

Expected response format:
- short answer
- confidence level
- cited note/source paths

## 7) Set ongoing rhythm

- Daily: process Inbox
- Weekly: crystallize high-value drafts and run strict doctor
- Monthly: archive and graph hygiene review
