# Runbook: vault.process (VAULT-FAST)

## Purpose
Convert high-volume Inbox/raw intake into schema-valid drafts and clean escalation packets.

## Inputs
- `vault/Inbox/*.md`
- newly landed references in `vault/raw/*`
- templates in `skills/vault/templates/`

## Procedure
1. Enumerate Inbox + new raw refs.
2. Remove obvious duplicates/noise (do not delete outside Inbox).
3. Classify note type (`project|area|resource|entity|meeting|insight|other`).
4. Apply template and fill baseline frontmatter.
5. Add concise factual bullets and unresolved questions.
6. Add candidate `related` wikilinks.
7. Build escalation packet for ambiguous/high-risk items.
8. Move processed Inbox items out of active queue.

## Output Contract
- Draft notes are frontmatter-complete and source-traceable.
- Escalations include:
  - item path(s)
  - candidate type
  - unresolved questions
  - risk/impact note

## Validation Gates
- required frontmatter present
- `sources` populated
- `related` links syntactically valid
- no unsupported synthesis claims

## Escalate When
- source conflict cannot be resolved safely
- decision/procedure finalization is implied
- legal/compliance-sensitive classification is uncertain
