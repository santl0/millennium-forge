#!/usr/bin/env python3
"""Validate canonical claims and the problem registry with the standard library."""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import re
import sys
from typing import Any


def load_json(path: pathlib.Path) -> tuple[Any | None, list[str]]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except (OSError, json.JSONDecodeError) as exc:
        return None, [f"{path}: invalid JSON: {exc}"]


def validate_string_list(path: pathlib.Path, field: str, value: Any) -> list[str]:
    if not isinstance(value, list):
        return [f"{path}: {field} must be a list"]
    if not all(isinstance(item, str) for item in value):
        return [f"{path}: every {field} entry must be a string"]
    return []


def validate_claim(path: pathlib.Path, schema: dict[str, Any]) -> list[str]:
    data, errors = load_json(path)
    if errors:
        return errors
    if not isinstance(data, dict):
        return [f"{path}: claim must be an object"]

    properties = schema["properties"]
    required = set(schema["required"])
    missing = sorted(required - data.keys())
    extra = sorted(data.keys() - properties.keys())
    if missing:
        errors.append(f"{path}: missing fields: {', '.join(missing)}")
    if extra:
        errors.append(f"{path}: unknown fields: {', '.join(extra)}")

    claim_id = data.get("id")
    id_pattern = properties["id"]["pattern"]
    if not isinstance(claim_id, str) or re.fullmatch(id_pattern, claim_id) is None:
        errors.append(f"{path}: invalid id: {claim_id!r}")

    for field in ("problem", "status"):
        if data.get(field) not in properties[field]["enum"]:
            errors.append(f"{path}: invalid {field}: {data.get(field)!r}")

    statement = data.get("statement")
    minimum = properties["statement"]["minLength"]
    if not isinstance(statement, str) or len(statement) < minimum:
        errors.append(f"{path}: statement must contain at least {minimum} characters")

    errors.extend(validate_string_list(path, "hypotheses", data.get("hypotheses")))
    errors.extend(validate_string_list(path, "dependencies", data.get("dependencies")))
    dependencies = data.get("dependencies")
    if isinstance(dependencies, list):
        if len(dependencies) != len(set(map(str, dependencies))):
            errors.append(f"{path}: dependencies must be unique")
        for dependency in dependencies:
            if not isinstance(dependency, str) or re.fullmatch(id_pattern, dependency) is None:
                errors.append(f"{path}: invalid dependency id: {dependency!r}")

    evidence = data.get("evidence")
    evidence_schema = properties["evidence"]["items"]
    if not isinstance(evidence, list):
        errors.append(f"{path}: evidence must be a list")
    else:
        for index, item in enumerate(evidence):
            prefix = f"{path}: evidence[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{prefix} must be an object")
                continue
            missing_evidence = set(evidence_schema["required"]) - item.keys()
            extra_evidence = item.keys() - evidence_schema["properties"].keys()
            if missing_evidence:
                errors.append(f"{prefix} missing: {', '.join(sorted(missing_evidence))}")
            if extra_evidence:
                errors.append(f"{prefix} unknown: {', '.join(sorted(extra_evidence))}")
            if item.get("kind") not in evidence_schema["properties"]["kind"]["enum"]:
                errors.append(f"{prefix} has invalid kind: {item.get('kind')!r}")
            if not isinstance(item.get("reference"), str) or not item.get("reference"):
                errors.append(f"{prefix} requires a non-empty reference")
            sha256 = item.get("sha256")
            if sha256 is not None and re.fullmatch(r"[a-f0-9]{64}", str(sha256)) is None:
                errors.append(f"{prefix} has invalid sha256")

    for field in ("provenance", "review"):
        value = data.get(field)
        field_schema = properties[field]
        if not isinstance(value, dict):
            errors.append(f"{path}: {field} must be an object")
            continue
        missing_nested = set(field_schema["required"]) - value.keys()
        extra_nested = value.keys() - field_schema["properties"].keys()
        if missing_nested:
            errors.append(f"{path}: {field} missing: {', '.join(sorted(missing_nested))}")
        if extra_nested:
            errors.append(f"{path}: {field} unknown: {', '.join(sorted(extra_nested))}")

    provenance = data.get("provenance")
    if isinstance(provenance, dict):
        if provenance.get("producer_type") not in properties["provenance"]["properties"]["producer_type"]["enum"]:
            errors.append(f"{path}: invalid provenance.producer_type")
        try:
            dt.date.fromisoformat(provenance.get("created_at", ""))
        except (TypeError, ValueError):
            errors.append(f"{path}: provenance.created_at must be an ISO date")

    review = data.get("review")
    if isinstance(review, dict) and review.get("status") not in properties["review"]["properties"]["status"]["enum"]:
        errors.append(f"{path}: invalid review.status")

    return errors


def validate_problem_index(root: pathlib.Path, schema: dict[str, Any]) -> list[str]:
    path = root / "problems" / "index.json"
    data, errors = load_json(path)
    if errors:
        return errors
    if not isinstance(data, dict) or not isinstance(data.get("problems"), list):
        return [f"{path}: problems must be a list"]

    expected = set(schema["properties"]["problem"]["enum"]) - {"cross-cutting"}
    found: set[str] = set()
    for index, item in enumerate(data["problems"]):
        prefix = f"{path}: problems[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        if set(item) != {"slug", "path", "official"}:
            errors.append(f"{prefix} must contain only slug, path and official")
        slug = item.get("slug")
        relative = item.get("path")
        official = item.get("official")
        if slug in found:
            errors.append(f"{prefix} duplicates slug {slug!r}")
        if isinstance(slug, str):
            found.add(slug)
        if not isinstance(relative, str) or not (root / "problems" / relative / "README.md").is_file():
            errors.append(f"{prefix} points to a missing problem README")
        if not isinstance(official, str) or not official.startswith("https://www.claymath.org/"):
            errors.append(f"{prefix} must reference an official Clay URL")

    missing = sorted(expected - found)
    unexpected = sorted(found - expected)
    if missing:
        errors.append(f"{path}: missing problem slugs: {', '.join(missing)}")
    if unexpected:
        errors.append(f"{path}: unexpected problem slugs: {', '.join(unexpected)}")
    return errors


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    schema_path = root / "schemas" / "claim.schema.json"
    schema, errors = load_json(schema_path)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    if not isinstance(schema, dict):
        print(f"ERROR: {schema_path}: schema must be an object")
        return 1

    claims = sorted((root / "claims").rglob("*.json"))
    examples = sorted((root / "schemas" / "examples").glob("*.json"))
    errors = [error for path in claims + examples for error in validate_claim(path, schema)]
    errors.extend(validate_problem_index(root, schema))
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"claims ok: {len(claims)} canonical, {len(examples)} example(s), 6 problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
