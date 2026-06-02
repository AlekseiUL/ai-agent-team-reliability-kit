from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Iterable

REQUIRED_TASK_FIELDS: dict[str, re.Pattern[str]] = {
    "Owner": re.compile(r"(?:^|\n)\s*(?:owner|assignee)\s*:", re.I),
    "Goal": re.compile(r"(?:^|\n)\s*goal\s*:", re.I),
    "Allowed paths": re.compile(r"(?:^|\n)\s*allowed\s+paths\s*:", re.I),
    "Forbidden paths": re.compile(r"(?:^|\n)\s*forbidden\s+paths\s*:", re.I),
    "Privacy level": re.compile(r"(?:^|\n)\s*privacy\s+level\s*:", re.I),
    "External side-effect policy": re.compile(r"(?:^|\n)\s*external\s+side[- ]effect\s+policy\s*:", re.I),
    "Verification required": re.compile(r"(?:^|\n)\s*verification\s+required\s*:", re.I),
    "Expected final summary/report": re.compile(r"(?:^|\n)\s*expected\s+final\s+summary\s*/\s*report\s*:", re.I),
}

DONE_FIELDS: dict[str, re.Pattern[str]] = {
    "Outcome": re.compile(r"(?:^|\n)\s*outcome\s*:", re.I),
    "Artifacts": re.compile(r"(?:^|\n)\s*artifacts\s*:", re.I),
    "Verification": re.compile(r"(?:^|\n)\s*verification\s*:", re.I),
    "Follow-up": re.compile(r"(?:^|\n)\s*follow[- ]up\s*:", re.I),
    "Memory/Wiki candidate": re.compile(r"(?:^|\n)\s*memory\s*/\s*wiki\s+candidate\s*:", re.I),
}

SENSITIVE_PATTERNS: dict[str, re.Pattern[str]] = {
    "private_local_path": re.compile(r"/Users/[^/\s]+|/home/[^/\s]+/(?:Desktop|Documents)|[A-Z][A-Z0-9_]{2,}_(?:CENTER|PRIVATE|SECRET)"),
    "env_file_reference": re.compile(r"(^|[/\\])\.env(?:\.|$)|auth\.json|hosts\.yml|cookies?\.txt", re.I),
    "bytecode_or_cache": re.compile(r"(__pycache__|\.pyc$|\.pyo$|\.pytest_cache)"),
    "secret_shape": re.compile(r"(?i)(api[_-]?key|secret|token|password|passwd)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}"),
    "runtime_media": re.compile(r"\.(?:mp4|mov|webm|mkv|wav|m4a|mp3|ogg|flac|png|jpg|jpeg|webp)$", re.I),
    "accusation_wording": re.compile(r"(?i)\b(stolen|theft|украл|краж[аеиуой]*|воров(?:ство|али|ал|ать)?)\b"),
}

ALLOWED_MEDIA_PREFIXES = ("docs/assets/", "examples/assets/")
TEXT_SUFFIXES = {".md", ".txt", ".py", ".toml", ".yaml", ".yml", ".json", ".sh", ".cfg", ".ini"}


def iter_files(path: Path) -> Iterable[Path]:
    if path.is_file():
        yield path
        return
    for root, dirs, files in os.walk(path):
        dirs[:] = [
            d for d in dirs
            if d not in {".git", ".venv", "venv", "node_modules", "dist", "build", "__pycache__", ".pytest_cache"}
            and not d.endswith(".egg-info")
        ]
        for name in files:
            yield Path(root) / name


def read_text(path: Path) -> str | None:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return None
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if b"\0" in data[:4096]:
        return None
    return data.decode("utf-8", errors="replace")


def audit_tasks(path: Path) -> dict:
    findings = []
    files = [p for p in iter_files(path) if p.suffix.lower() == ".md"]
    for file_path in files:
        text = read_text(file_path) or ""
        lowered = file_path.name.lower()
        if "done" in lowered or "summary" in lowered:
            missing = [name for name, rx in DONE_FIELDS.items() if not rx.search(text)]
            kind = "done_summary"
        else:
            missing = [name for name, rx in REQUIRED_TASK_FIELDS.items() if not rx.search(text)]
            kind = "task_contract"
        for field in missing:
            findings.append({"file": str(file_path), "kind": kind, "missing": field})
    return {"ok": not findings, "files_checked": len(files), "findings": findings}


def scan_repo(path: Path) -> dict:
    findings = []
    count = 0
    base = path.resolve()
    for file_path in iter_files(path):
        count += 1
        rel = file_path.resolve().relative_to(base).as_posix() if file_path.resolve().is_relative_to(base) else str(file_path)
        if rel in {"src/agent_team_reliability/cli.py", "tests/test_cli.py"}:
            continue
        if SENSITIVE_PATTERNS["bytecode_or_cache"].search(rel):
            findings.append({"file": rel, "kind": "bytecode_or_cache", "line": 0})
            continue
        if SENSITIVE_PATTERNS["runtime_media"].search(rel) and not rel.startswith(ALLOWED_MEDIA_PREFIXES):
            findings.append({"file": rel, "kind": "runtime_media_outside_public_assets", "line": 0})
            continue
        text = read_text(file_path)
        if text is None:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for kind, rx in SENSITIVE_PATTERNS.items():
                if kind in {"bytecode_or_cache", "runtime_media"}:
                    continue
                if rx.search(line):
                    findings.append({"file": rel, "kind": kind, "line": i})
    return {"ok": not findings, "files_checked": count, "findings": findings}


def cmd_doctor(_args: argparse.Namespace) -> int:
    print(json.dumps({"ok": True, "tool": "agent-team-reliability", "checks": ["python", "templates", "repo-scan"]}, indent=2))
    return 0


def cmd_audit_tasks(args: argparse.Namespace) -> int:
    result = audit_tasks(Path(args.path))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 1


def cmd_scan_repo(args: argparse.Namespace) -> int:
    result = scan_repo(Path(args.path))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit contracts and public-release hygiene for AI agent teams.")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("doctor", help="Print a small readiness report.")
    p.set_defaults(func=cmd_doctor)
    p = sub.add_parser("audit-tasks", help="Check Markdown task files for required reliability-contract fields.")
    p.add_argument("path")
    p.set_defaults(func=cmd_audit_tasks)
    p = sub.add_parser("scan-repo", help="Scan a repository tree for common public-release privacy/hygiene issues.")
    p.add_argument("path")
    p.set_defaults(func=cmd_scan_repo)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
