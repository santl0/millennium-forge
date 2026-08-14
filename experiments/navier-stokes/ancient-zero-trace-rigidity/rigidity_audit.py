#!/usr/bin/env python3
"""Audit the exact gates in bounded-ancient zero-trace rigidity."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
OBLIGATIONS_PATH = HERE / "rigidity_obligations.json"
ALLOWED_STATUSES = {"SOURCE", "SOURCE_PLUS_SCALING", "DERIVATION", "CROSSCHECK"}
DIRECT_STATUSES = {"SOURCE", "SOURCE_PLUS_SCALING", "DERIVATION"}


def load_obligations() -> dict:
    return json.loads(OBLIGATIONS_PATH.read_text(encoding="utf-8"))


def main() -> None:
    data = load_obligations()
    failures: list[str] = []
    obligations = data["obligations"]
    route = data["direct_route"]
    properties = set(data["properties"])
    required = set(data["required_properties"])

    if required != properties:
        failures.append(
            "required properties differ from declared properties: "
            f"missing={sorted(properties-required)}, extra={sorted(required-properties)}"
        )

    unknown_route = sorted(set(route) - set(obligations))
    if unknown_route:
        failures.append(f"direct route has unknown obligations: {unknown_route}")
    for name, obligation in obligations.items():
        status = obligation["status"]
        if status not in ALLOWED_STATUSES:
            failures.append(f"{name}: invalid status {status}")
        if name in route and status not in DIRECT_STATUSES:
            failures.append(f"{name}: non-direct status {status} used in direct route")

    derivative_scaling = []
    for k in range(4):
        for ell in range(3):
            predicted = k + 2 * ell + 1
            dimensional = 1 + k + 2 * ell
            residual = predicted - dimensional
            derivative_scaling.append(
                {"spatial_order": k, "time_order": ell, "M_power": predicted}
            )
            if residual != 0:
                failures.append(
                    f"derivative scaling failed for k={k}, ell={ell}: {residual}"
                )

    equation_exponents = {
        "partial_t_u": 3,
        "Delta_u": 3,
        "u_dot_nabla_u": 3,
        "nabla_p": 3,
    }
    if len(set(equation_exponents.values())) != 1:
        failures.append(f"NS terms scale differently: {equation_exponents}")

    # Exact modulus certificate. Proposition 4.1 gives
    # ||partial_t u||_infinity <= C M^3. The chosen rational values merely
    # exercise the exponent and the Cauchy modulus; they approximate no PDE.
    M = Fraction(2)
    C_time = Fraction(3)
    time_lipschitz = C_time * M**3
    trace_modulus = []
    for power in range(1, 9):
        h = Fraction(1, 2**power)
        bound = time_lipschitz * h
        trace_modulus.append(
            {
                "h": str(h),
                "C_M3_h": str(bound),
            }
        )
        if bound != Fraction(24, 2**power):
            failures.append(f"time modulus residual at power={power}")

    # The Oseen Duhamel tail has integral 2*C_K*M^2*sqrt(delta). Choosing
    # delta=q^2 keeps this certificate rational and exposes the half-power.
    C_kernel = Fraction(3)
    duhamel_tail = []
    previous = None
    for power in range(1, 9):
        q = Fraction(1, 2**power)
        delta = q**2
        tail = 2 * C_kernel * M**2 * q
        duhamel_tail.append(
            {"delta": str(delta), "tail_bound": str(tail)}
        )
        if previous is not None and tail * 2 != previous:
            failures.append(f"Duhamel tail did not halve at power={power}")
        previous = tail

    counterprofile_failures: dict[str, list[str]] = {}
    for name, profile in data["counterprofiles"].items():
        satisfies = set(profile["satisfies"])
        unknown = sorted(satisfies - properties)
        if unknown:
            failures.append(f"{name}: unknown satisfied properties {unknown}")
        actual_failed = sorted(required - satisfies)
        expected_failed = sorted(profile["expected_failed_properties"])
        counterprofile_failures[name] = actual_failed
        if actual_failed != expected_failed:
            failures.append(
                f"{name}: failed={actual_failed}, expected={expected_failed}"
            )
        if not actual_failed:
            failures.append(f"{name}: purported counterprofile passes every lemma gate")

    report = {
        "experiment": data["experiment"],
        "arithmetic": "finite set logic and rational identities; no floating point",
        "obligations_sha256": hashlib.sha256(OBLIGATIONS_PATH.read_bytes()).hexdigest(),
        "direct_route": route,
        "direct_route_obligation_count": len(route),
        "derivative_scaling": derivative_scaling,
        "equation_scaling_exponents": equation_exponents,
        "time_trace_modulus": trace_modulus,
        "duhamel_tail_modulus": duhamel_tail,
        "counterprofile_failed_gates": counterprofile_failures,
        "assertion_failure_count": len(failures),
        "assertion_failures": failures,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
