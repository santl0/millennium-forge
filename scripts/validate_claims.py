#!/usr/bin/env python3
"""Validate claim JSON files using only the Python standard library."""

from __future__ import annotations

import json
import pathlib
import sys

ALLOWED_STATUSES = {
    "SPECULATION",
    "COMPUTATION_ONLY",
    "SOURCE_VERIFIED",
    "PAPER_PROOF",
    "FORMALIZED",
    "REFUTED",
    "SUPERSEDED",
}

REQUIRED_FIELDS = {
    "id",
    "problem",
    "statement",
    "status",
    "hypotheses",
    "dependencies",
    "evidence",
    "review",
}


def validate(path: pathlib.Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: invalid JSON: {exc}"]

    missing = sorted(REQUIRED_FIELDS - data.keys())
    if missing:
        errors.append(f"{path}: missing fields: {', '.join(missing)}")
    if data.get("status") not in ALLOWED_STATUSES:
        errors.append(f"{path}: invalid status: {data.get('status')!r}")
    if not isinstance(data.get("hypotheses"), list):
        errors.append(f"{path}: hypotheses must be a list")
    if not isinstance(data.get("dependencies"), list):
        errors.append(f"{path}: dependencies must be a list")
    if not isinstance(data.get("evidence"), list):
        errors.append(f"{path}: evidence must be a list")
    if not isinstance(data.get("review"), dict):
        errors.append(f"{path}: review must be an object")
    return errors


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    paths = sorted((root / "claims").rglob("*.json")) if (root / "claims").exists() else []
    errors = [error for path in paths for error in validate(path)]
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"claims ok: {len(paths)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
