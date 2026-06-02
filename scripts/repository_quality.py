#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check_python_syntax() -> list[str]:
    bad = []
    for path in ROOT.rglob("*.py"):
        if any(part in {".git", ".venv", "venv", "build", "dist"} for part in path.parts):
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as exc:
            bad.append(f"python syntax: {path}:{exc.lineno}: {exc.msg}")
    return bad


def check_json() -> list[str]:
    bad = []
    for path in ROOT.rglob("*.json"):
        if ".git" in path.parts:
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            bad.append(f"json parse: {path}: {exc}")
    return bad


def main() -> int:
    bad = []
    bad.extend(check_python_syntax())
    bad.extend(check_json())
    if bad:
        print("repository quality: FAIL")
        for item in bad:
            print(item)
        return 1
    print("repository quality: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
