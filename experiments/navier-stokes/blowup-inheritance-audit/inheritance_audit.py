#!/usr/bin/env python3
"""Validate that rigidity hypotheses come from one audited blow-up chain."""

from __future__ import annotations

import hashlib
import json
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
MATRIX_PATH = HERE / "inheritance_matrix.json"
POSITIVE = {"SOURCE", "INFERENCE"}
ALLOWED = POSITIVE | {"NOT_PROVIDED", "CONTRADICTED", "NOT_APPLICABLE"}


def load_matrix() -> dict:
    return json.loads(MATRIX_PATH.read_text(encoding="utf-8"))


def chain_supports(chain: dict, requirements: list[str]) -> bool:
    return all(chain["values"][key] in POSITIVE for key in requirements)


def minimal_union_covers(chains: dict, requirements: list[str]) -> list[list[str]]:
    names = sorted(chains)
    covers: list[list[str]] = []
    for size in range(2, len(names) + 1):
        for selected in combinations(names, size):
            if all(
                any(chains[name]["values"][key] in POSITIVE for name in selected)
                for key in requirements
            ):
                covers.append(list(selected))
        if covers:
            return covers
    return []


def main() -> None:
    matrix = load_matrix()
    properties = set(matrix["properties"])
    chains = matrix["chains"]
    gates = matrix["gates"]
    failures: list[str] = []

    for chain_name, chain in chains.items():
        keys = set(chain["values"])
        if keys != properties:
            failures.append(
                f"{chain_name}: property keys differ: "
                f"missing={sorted(properties - keys)}, extra={sorted(keys - properties)}"
            )
        invalid = sorted(set(chain["values"].values()) - ALLOWED)
        if invalid:
            failures.append(f"{chain_name}: invalid statuses {invalid}")
        values = chain["values"]
        if (
            values["limit_equation_obtained_is_viscous_ns"] in POSITIVE
            and values["limit_equation_obtained_is_euler"] in POSITIVE
        ):
            failures.append(f"{chain_name}: both viscous NS and inviscid Euler are positive")
        zero_trace = (
            values["terminal_zero_L2loc"] in POSITIVE
            or values["terminal_zero_Sprime"] in POSITIVE
        )
        if zero_trace and values["terminal_point_nonzero"] in POSITIVE:
            failures.append(f"{chain_name}: zero and nonzero terminal traces are both positive")

    matches: dict[str, list[str]] = {}
    union_only: dict[str, list[list[str]]] = {}
    for gate_name, requirements in gates.items():
        unknown = sorted(set(requirements) - properties)
        if unknown:
            failures.append(f"{gate_name}: unknown properties {unknown}")
            continue
        matches[gate_name] = sorted(
            name for name, chain in chains.items() if chain_supports(chain, requirements)
        )
        expected = sorted(matrix["expected_single_chain_matches"][gate_name])
        if matches[gate_name] != expected:
            failures.append(
                f"{gate_name}: matches={matches[gate_name]} expected={expected}"
            )
        if not matches[gate_name]:
            union_only[gate_name] = minimal_union_covers(chains, requirements)

    hybrid = "HYBRID_BOUNDED_MILD_ZERO_TRACE"
    hybrid_requirements = gates[hybrid]
    property_sources = {
        key: sorted(
            name
            for name, chain in chains.items()
            if chain["values"][key] in POSITIVE
        )
        for key in hybrid_requirements
    }
    expected_union = sorted(
        sorted(selected) for selected in matrix["expected_hybrid_minimal_union_covers"]
    )
    actual_union = sorted(sorted(selected) for selected in union_only.get(hybrid, []))
    if actual_union != expected_union:
        failures.append(
            f"{hybrid}: minimal union covers={actual_union} expected={expected_union}"
        )

    report = {
        "experiment": "BLOWUP-INHERITANCE-AUDIT-1",
        "arithmetic": "finite exact set containment; no floating point",
        "matrix_sha256": hashlib.sha256(MATRIX_PATH.read_bytes()).hexdigest(),
        "chain_count": len(chains),
        "property_count": len(properties),
        "gate_count": len(gates),
        "single_chain_matches": matches,
        "unsupported_hybrid_gate": hybrid,
        "unsupported_hybrid_single_chain_matches": matches.get(hybrid, []),
        "unsupported_hybrid_minimal_union_covers": actual_union,
        "unsupported_hybrid_property_sources": property_sources,
        "assertion_failure_count": len(failures),
        "assertion_failures": failures,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
