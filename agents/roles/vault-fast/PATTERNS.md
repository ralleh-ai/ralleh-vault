# PATTERNS.md — Shared Patterns

## Batch Processing Pattern
1. collect bounded batch
2. classify + template
3. validate frontmatter
4. generate candidate links
5. emit escalations

## Escalation Packet Pattern
Include:
- source path(s)
- candidate type
- reason for escalation
- unresolved questions
- risk/impact note

## Backlog Control Pattern
Track backlog count and oldest age every run; reduce oldest-age risk before volume optimization.
