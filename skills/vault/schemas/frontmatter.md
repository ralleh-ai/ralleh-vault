# Vault Frontmatter Schema

All canonical notes in `vault/wiki/` require YAML frontmatter.

```yaml
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | decision | procedure | project | area | resource | meeting | insight | other
status: draft | active | stable | archived | deprecated
title: Human readable title
sources: []
related: []
owner: human | VAULT | VAULT-FAST | other-agent
confidence: high | medium | low
tags: []
clients: []
projects: []
---
```

## Field rules

- `created` and `updated` are ISO dates.
- `type` must match the note’s semantic purpose.
- `sources` contains file paths (`raw/...`), URLs, IDs, or event refs.
- `related` contains `[[wikilinks]]` to canonical notes.
- `tags` optional and sparse; do not replace links with tags.
- `owner` indicates the actor most responsible for the current note state.
- `confidence` reflects evidence quality, not writing confidence.

## Status meaning

- `draft`: initial pass; likely incomplete.
- `active`: currently maintained and in use.
- `stable`: mature and trusted.
- `archived`: retained but inactive.
- `deprecated`: superseded; leave pointer to replacement.
