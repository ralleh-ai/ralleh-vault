# Runbook: vault.crystallize (VAULT)

## Purpose
Produce durable canonical knowledge from drafts/escalations while preserving provenance and graph integrity.

## Inputs
- escalation packet(s) from VAULT-FAST
- relevant canonical notes in `vault/wiki/`
- supporting source artifacts in `vault/raw/`

## Procedure
1. Gather all cited source references and related canonical notes.
2. Resolve conflicts explicitly; preserve uncertainty when unresolved.
3. Write/update canonical note in `vault/wiki/<Type>/`.
4. Set correct `status` and `confidence`.
5. Add/repair bidirectional links and nearby MOC references.
6. Update `vault/wiki/index.md` and append `vault/wiki/log.md`.
7. Trigger approval gate for major active/stable Decisions/Procedures.

## Output Contract
- Canonical note is schema-valid and citation-backed.
- Graph remains navigable (no broken references introduced).
- Change is reflected in index + log.

## Validation Gates
- frontmatter completeness + valid enums/dates
- meaningful `sources` and `related`
- approval metadata present when required
- strict doctor passes on target vault root

## Stop Conditions
Pause for approval before:
- major decision/procedure changes
- cross-client linking/merging
- deletions outside Inbox
