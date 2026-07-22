# FAQ

## Why Markdown instead of a database?

Markdown keeps source-of-truth simple, local, inspectable, and Git-native.

## When do we use VAULT vs VAULT-FAST?

- VAULT-FAST: high-volume triage, formatting, baseline structuring.
- VAULT: high-judgment synthesis, decisions, procedures, graph quality.

## What is a canonical note?

A note under `wiki/` with valid frontmatter, explicit sources, and meaningful links.

## Are tags required?

No. Use tags sparingly. Prefer explicit `[[wikilinks]]`.

## What does `confidence` mean?

Evidence quality, not writing confidence:
- `high`: strong, corroborated evidence
- `medium`: useful but partial evidence
- `low`: uncertain or provisional

## Why can strict doctor fail while normal doctor passes?

`--strict` promotes warnings to failures to enforce release-grade quality.

## Why can't we edit files in `raw/`?

`raw/` preserves provenance and auditability. Transformations belong in `wiki/` notes.

## How do approval gates work?

Active/stable `decision` and `procedure` notes must include an Approval section and `Approved by` value.

## Can we link across clients?

Only with explicit approval and policy review.
