#!/usr/bin/env python3
"""Audit VAULT role packages against ralleh-agents-style golden standards."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

ROLE_IDS = ("vault", "vault-fast")

EXPECTED_FILES = (
    "README.md",
    "SOUL.md",
    "IDENTITY.md",
    "AGENTS.md",
    "TOOLS.md",
    "DOCTOR.md",
    "GUIDELINES.md",
    "WORKFLOWS.md",
    "MEMORY.md",
    "USER.md",
    "PATTERNS.md",
)

SIZE_CAPS = {
    "SOUL.md": 2000,
    "AGENTS.md": 3500,
    "TOOLS.md": 3500,
    "WORKFLOWS.md": 3000,
    "DOCTOR.md": 1800,
    "MEMORY.md": 3000,
    "USER.md": 1200,
    "PATTERNS.md": 3000,
    "README.md": 2500,
    "IDENTITY.md": 1800,
    "GUIDELINES.md": 2000,
}

REQUIRED_SECTIONS = {
    "README.md": ("## Purpose",),
    "SOUL.md": (
        "## Core Identity",
        "## Role",
        "## Operating Principles",
        "## Boundaries",
        "## Continuity",
    ),
    "IDENTITY.md": ("## Mission", "## Core Responsibilities", "## Success Measures"),
    "AGENTS.md": ("## Startup Checks", "## Delegation Rules", "## Verification Protocol"),
    "TOOLS.md": ("## Tooling Principles", "## Integrations", "## What Does Not Belong Here"),
    "DOCTOR.md": (
        "## Purpose",
        "## Fast Triage",
        "## Common Failure Modes",
        "## Escalation",
        "## Doctor Report Format",
    ),
    "GUIDELINES.md": ("## Source of Truth Rules", "## Quality Bar"),
    "WORKFLOWS.md": ("## Workflow Index", "## What Belongs in examples/"),
    "MEMORY.md": ("# MEMORY.md — Lessons & Patterns",),
    "USER.md": ("## Identity", "## Values", "## Style Preferences"),
    "PATTERNS.md": ("# PATTERNS.md — Shared Patterns",),
}

WORD_RE = re.compile(r"\b\w+[\w'-]*\b")


@dataclass
class Issue:
    level: str  # error|warn
    file: str
    message: str


def count_words(text: str) -> int:
    return len(WORD_RE.findall(text))


def verdict_for(issues: list[Issue]) -> str:
    if any(i.level == "error" and "missing required file" in i.message for i in issues):
        return "misplaced"
    if any(i.level == "error" and "missing required section" in i.message for i in issues):
        return "misplaced"
    if any(i.level == "error" and "exceeds size cap" in i.message for i in issues):
        return "bloated"
    if any(i.level == "error" for i in issues):
        return "risky"
    if any(i.level == "warn" for i in issues):
        return "usable"
    return "golden"


def audit_role(repo_root: Path, role_id: str) -> tuple[list[str], list[Issue], str]:
    role_dir = repo_root / "agents" / "roles" / role_id
    summaries: list[str] = []
    issues: list[Issue] = []

    for file_name in EXPECTED_FILES:
        file_path = role_dir / file_name
        if not file_path.exists():
            issues.append(Issue("error", file_name, "missing required file"))
            continue

        text = file_path.read_text(encoding="utf-8")
        words = count_words(text)
        cap = SIZE_CAPS[file_name]
        summaries.append(f"{file_name}: {words} words")

        if words > cap:
            issues.append(Issue("error", file_name, f"exceeds size cap ({words} > {cap})"))

        for section in REQUIRED_SECTIONS.get(file_name, ()):
            if section not in text:
                issues.append(Issue("error", file_name, f"missing required section '{section}'"))

    return summaries, issues, verdict_for(issues)


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    has_error = False

    for role_id in ROLE_IDS:
        summaries, issues, verdict = audit_role(repo_root, role_id)
        print(f"ROLE {role_id}")
        print(f"  Verdict: {verdict}")
        for line in summaries:
            print(f"  {line}")
        if not issues:
            print("  OK")
            continue
        for issue in issues:
            print(f"  {issue.level.upper()}: {issue.file} - {issue.message}")
            if issue.level == "error":
                has_error = True

    return 1 if has_error else 0


if __name__ == "__main__":
    sys.exit(main())
