#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
import re
import sys
from typing import Dict, List, Optional, Tuple

REQUIRED_FIELDS = {
    "created",
    "updated",
    "type",
    "status",
    "title",
    "sources",
    "related",
    "owner",
    "confidence",
}

VALID_TYPES = {
    "entity",
    "concept",
    "decision",
    "procedure",
    "project",
    "area",
    "resource",
    "meeting",
    "insight",
    "other",
}

VALID_STATUS = {"draft", "active", "stable", "archived", "deprecated"}
VALID_CONFIDENCE = {"high", "medium", "low"}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
LOG_LINE_RE = re.compile(r"^-\s+(\d{4}-\d{2}-\d{2}):", re.MULTILINE)
APPROVAL_HEADING_RE = re.compile(r"^##\s+Approval\s*$", re.MULTILINE)
APPROVED_BY_RE = re.compile(r"^[-*]?\s*Approved by:\s*(.+?)\s*$", re.MULTILINE)

TYPE_DIR_EXPECTATION = {
    "entity": "Entities",
    "concept": "Concepts",
    "decision": "Decisions",
    "procedure": "Procedures",
    "project": "Projects",
    "area": "Areas",
    "resource": "Resources",
    "meeting": "Meetings",
    "insight": "Insights",
}


def parse_frontmatter(text: str) -> Tuple[Optional[Dict[str, str]], str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text

    block = text[4:end]
    body = text[end + 5 :]
    data: Dict[str, str] = {}

    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip()

    return data, body


def as_date(v: str) -> Optional[dt.date]:
    if not DATE_RE.match(v):
        return None
    try:
        return dt.date.fromisoformat(v)
    except ValueError:
        return None


def scan(vault_root: Path, inbox_max_age_hours: int, log_max_age_days: int, strict: bool) -> int:
    wiki = vault_root / "wiki"
    inbox = vault_root / "Inbox"
    raw = vault_root / "raw"

    issues: List[str] = []
    warnings: List[str] = []

    index = wiki / "index.md"
    log = wiki / "log.md"

    if not wiki.exists():
        issues.append("missing required folder: wiki/")
    if not raw.exists():
        issues.append("missing required folder: raw/")
    if not inbox.exists():
        warnings.append("missing recommended folder: Inbox/")

    if not index.exists():
        issues.append("missing required file: wiki/index.md")
    if not log.exists():
        issues.append("missing required file: wiki/log.md")

    notes = sorted(wiki.rglob("*.md")) if wiki.exists() else []
    all_stems = {p.stem for p in notes}

    moc_files = [p for p in notes if p.name.endswith(" MOC.md")]

    coverage_docs = []
    if index.exists():
        coverage_docs.append(index.read_text(encoding="utf-8"))
    for m in moc_files:
        coverage_docs.append(m.read_text(encoding="utf-8"))
    coverage_text = "\n".join(coverage_docs)

    decision_proc_count = 0
    decision_proc_approval_fail = 0

    for note in notes:
        text = note.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)

        if note.name in {"index.md", "log.md"}:
            continue

        if fm is None:
            issues.append(f"missing frontmatter: {note}")
            continue

        missing = sorted(REQUIRED_FIELDS - set(fm))
        if missing:
            issues.append(f"missing required fields {missing}: {note}")

        for k in ("created", "updated"):
            if k in fm and as_date(fm[k]) is None:
                issues.append(f"invalid {k} date format in {note}: {fm[k]}")

        note_type = fm.get("type", "").strip().lower()
        note_status = fm.get("status", "").strip().lower()
        confidence = fm.get("confidence", "").strip().lower()
        owner = fm.get("owner", "").strip()

        if note_type and note_type not in VALID_TYPES:
            issues.append(f"invalid type in {note}: {note_type}")
        if note_status and note_status not in VALID_STATUS:
            issues.append(f"invalid status in {note}: {note_status}")
        if confidence and confidence not in VALID_CONFIDENCE:
            issues.append(f"invalid confidence in {note}: {confidence}")

        if owner == "":
            issues.append(f"empty owner in {note}")

        is_moc = note.name.endswith(" MOC.md") or note.name == "Vault Index.md"

        if fm.get("sources", "") == "[]" and not is_moc:
            warnings.append(f"empty sources in {note}")

        if fm.get("related", "") == "[]" and not is_moc:
            warnings.append(f"empty related links in {note}")

        expected_dir = TYPE_DIR_EXPECTATION.get(note_type)
        if expected_dir and expected_dir not in note.parts and not is_moc:
            warnings.append(
                f"type-directory mismatch in {note}: type={note_type} expected under wiki/{expected_dir}/"
            )

        if not is_moc and f"[[{note.stem}]]" not in coverage_text:
            warnings.append(f"note not referenced by index/MOC coverage: {note}")

        if (
            note_type in {"decision", "procedure"}
            and note_status in {"active", "stable"}
            and not is_moc
        ):
            decision_proc_count += 1
            has_heading = bool(APPROVAL_HEADING_RE.search(body))
            approved_match = APPROVED_BY_RE.search(body)
            approved_value = approved_match.group(1).strip() if approved_match else ""
            if not has_heading or not approved_value or approved_value.lower() in {"tbd", "n/a", "none"}:
                decision_proc_approval_fail += 1
                issues.append(
                    f"approval gate unmet for {note} (active/stable decision/procedure requires Approval section and non-empty Approved by)"
                )

    for note in notes:
        text = note.read_text(encoding="utf-8")
        for link in WIKILINK_RE.findall(text):
            target = link.split("|")[0].strip()
            if target and target not in all_stems:
                issues.append(f"broken wikilink [[{target}]] in {note}")

    inbox_files = list(inbox.rglob("*.md")) if inbox.exists() else []
    oldest_age_hours: Optional[float] = None
    if inbox_files:
        now = dt.datetime.now(dt.UTC).timestamp()
        oldest_mtime = min(f.stat().st_mtime for f in inbox_files)
        oldest_age_hours = (now - oldest_mtime) / 3600.0
        if oldest_age_hours > inbox_max_age_hours:
            issues.append(
                f"stale Inbox: oldest markdown item age {oldest_age_hours:.1f}h exceeds threshold {inbox_max_age_hours}h"
            )

    raw_files = [p for p in raw.rglob("*") if p.is_file()] if raw.exists() else []

    log_freshness_days: Optional[int] = None
    if log.exists():
        log_text = log.read_text(encoding="utf-8")
        dates = [dt.date.fromisoformat(d) for d in LOG_LINE_RE.findall(log_text) if as_date(d)]
        if dates:
            newest = max(dates)
            log_freshness_days = (dt.date.today() - newest).days
            if log_freshness_days > log_max_age_days:
                warnings.append(
                    f"log appears stale: newest entry {newest.isoformat()} is {log_freshness_days} days old"
                )
        else:
            warnings.append("wiki/log.md has no parseable '- YYYY-MM-DD:' entries")

    if strict and warnings:
        issues.extend([f"[strict] {w}" for w in warnings])

    print(f"vault_root: {vault_root}")
    print(f"wiki_notes: {len(notes)}")
    print(f"moc_files: {len(moc_files)}")
    print(f"inbox_markdown_count: {len(inbox_files)}")
    print(f"raw_file_count: {len(raw_files)}")
    if oldest_age_hours is not None:
        print(f"inbox_oldest_age_hours: {oldest_age_hours:.1f}")
    if log_freshness_days is not None:
        print(f"log_freshness_days: {log_freshness_days}")
    print(f"decision_procedure_active_or_stable_count: {decision_proc_count}")
    print(f"decision_procedure_approval_failures: {decision_proc_approval_fail}")
    print(f"checked_at: {dt.datetime.now(dt.UTC).isoformat()}")

    if warnings:
        print("\nwarnings:")
        for w in sorted(set(warnings)):
            print(f"- {w}")

    if issues:
        print("\nissues:")
        for i in sorted(set(issues)):
            print(f"- {i}")
        return 1

    print("\nstatus: ok")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Ralleh Vault health and consistency checks")
    parser.add_argument("--vault-root", default="vault", help="Path to vault root")
    parser.add_argument(
        "--inbox-max-age-hours",
        type=int,
        default=72,
        help="Fail if oldest Inbox markdown file exceeds this age",
    )
    parser.add_argument(
        "--log-max-age-days",
        type=int,
        default=30,
        help="Warn if newest log entry is older than this",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat all warnings as errors",
    )

    args = parser.parse_args()
    root = Path(args.vault_root)
    if not root.exists():
        print(f"vault root not found: {root}")
        return 2

    return scan(
        root,
        inbox_max_age_hours=args.inbox_max_age_hours,
        log_max_age_days=args.log_max_age_days,
        strict=args.strict,
    )


if __name__ == "__main__":
    sys.exit(main())
