#!/usr/bin/env python3
import argparse
import pathlib
import sys

REQUIRED_FILES = [
    "AGENTS.md",
    "docs/contexte.md",
    "docs/decisions.md",
    "docs/todo.md",
    "docs/governance.md",
    "problems/index.json",
    "schemas/claim.schema.json",
    "agents/PROTOCOL_AUTONOME.md",
]

GITHUB_FILES = [
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/codex-task.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/workflows/repo-hygiene.yml",
]

REQUIRED_TERM_GROUPS = {
    "AGENTS.md": [["branch", "branche"], ["codex"], ["validation", "validations"]],
    "docs/contexte.md": [["github", "repo", "dépôt", "branche", "branch"]],
    "docs/decisions.md": [["décision", "décisions", "validée", "validated"]],
    "docs/todo.md": [["todo", "priorité", "questions ouvertes"]],
}


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.repo).resolve()
    errors = []

    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.exists():
            errors.append(f"missing required file: {rel}")
            continue
        text = read_text(path).lower()
        if not text.strip():
            errors.append(f"empty required file: {rel}")
        for group in REQUIRED_TERM_GROUPS.get(rel, []):
            if not any(term in text for term in group):
                errors.append(f"{rel} does not mention: {', '.join(group)}")

    for rel in GITHUB_FILES:
        if not (root / rel).exists():
            errors.append(f"missing GitHub file: {rel}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"repo contract ok: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
