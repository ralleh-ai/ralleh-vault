# Runbook: vault.query / vault.retrieve

## Purpose
Return concise, reliable answers from canonical knowledge with explicit confidence and citations.

## Retrieval Order
1. Search canonical `vault/wiki/` first.
2. Expand through `related` wikilinks.
3. Pull `vault/raw/` only when canonical coverage is missing or low confidence.

## Output Contract
Return:
- short direct answer
- confidence (`high|medium|low`)
- cited note/source paths
- explicit unknowns when confidence is not high

## Quality Rules
- Prefer canonical notes over re-summarizing long raw text.
- Do not hide uncertainty.
- Do not infer beyond cited evidence.

## Escalate When
- conflicting canonical notes imply governance drift
- user request would require non-approved cross-client synthesis
