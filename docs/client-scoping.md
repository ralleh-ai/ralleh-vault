# Client-scoped vault root conventions

Ralleh Vault supports two deployment modes:

## Mode A: Single shared root

```text
vault/
  Inbox/
  raw/
  wiki/
```

Use this for internal-only deployments.

## Mode B: Multi-client root (recommended for agencies)

```text
vault/
  _shared/
    wiki/
    raw/
  clients/
    client-alpha/
      Inbox/
      raw/
      wiki/
    client-beta/
      Inbox/
      raw/
      wiki/
```

Rules:
- Never mix client knowledge in the same `wiki/` tree.
- `clients/<slug>/` is the tenant boundary.
- `clients` frontmatter should reflect ownership and routing.
- Cross-client links require explicit approval and legal/compliance review.
