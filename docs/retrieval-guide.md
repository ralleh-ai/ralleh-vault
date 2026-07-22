# Retrieval Guide

How to retrieve reliable answers from Ralleh Vault.

## Retrieval objective

Return concise, actionable answers with explicit provenance, not just plausible summaries.

## Retrieval flow

1. Search canonical notes in `vault/wiki/`.
2. Expand via `related` wikilinks.
3. Prefer stable/active notes over draft notes when conflicts exist.
4. Pull from `raw/` only when canonical coverage is missing or confidence is low.
5. Return answer + citations + confidence statement.

## Citation expectations

At minimum, include note path references used to produce the answer.

Example citation block:
- `vault/wiki/Decisions/Client Alpha Pricing Model.md`
- `vault/wiki/Projects/Client Alpha - Onboarding.md`
- `vault/raw/transcripts/2026-07-22_zoom_client-alpha-kickoff.txt`

## Retrieval output format (recommended)

- **Answer:** concise response
- **Confidence:** high | medium | low
- **Sources:** ordered citation list
- **Gaps / next best sources:** optional if confidence < high

## Retrieval scenarios

### Scenario 1: decision lookup

Query: "What pricing model was approved for Client Alpha?"

Return:
- approved model
- approval metadata (approver/date)
- decision note path

### Scenario 2: procedure lookup

Query: "What is the current deploy rollback procedure?"

Return:
- latest stable procedure steps
- status + last updated
- procedure note path + related decision links

### Scenario 3: conflict handling

If two notes conflict:
- flag discrepancy explicitly
- prefer latest approved stable note
- include both citations
- recommend crystallization update if needed
