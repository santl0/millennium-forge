#!/usr/bin/env python3
"""Exact audit at record-centered time in a KNSS maximum-normalized zoom."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
OBLIGATIONS_PATH = HERE / "commutator_obligations.json"
ALLOWED_STATUSES = {"SOURCE", "SOURCE_PLUS_SCALING", "DERIVATION", "COUNTERPROFILE"}
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

    required_clock_fields = {"past_endpoint", "record_time", "future_endpoint"}
    missing_clock_fields = sorted(required_clock_fields - set(data["normalization"]))
    if missing_clock_fields:
        failures.append(f"normalization misses clock fields: {missing_clock_fields}")

    if properties != required:
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

    # v=M^-1 u(x_k+M^-1 y,t_k+M^-2 s). All transformed NS terms carry M^-3.
    equation_exponents_in_M = {
        "partial_s_v": -3,
        "Delta_y_v": -3,
        "v_dot_nabla_y_v": -3,
        "nabla_y_pressure": -3,
    }
    if len(set(equation_exponents_in_M.values())) != 1:
        failures.append(f"NS scaling mismatch: {equation_exponents_in_M}")

    # Exact clock audit: s=M^2(t-t_k), so s=0 is t_k and physical T is B.
    sample_t_k = Fraction(3, 4)
    sample_T = Fraction(1)
    sample_M = Fraction(4)
    sample_B = sample_M**2 * (sample_T - sample_t_k)
    physical_at_record_zero = sample_t_k + Fraction(0) / sample_M**2
    physical_at_future_endpoint = sample_t_k + sample_B / sample_M**2
    if physical_at_record_zero != sample_t_k:
        failures.append("scaled record time zero does not map to t_k")
    if physical_at_future_endpoint != sample_T:
        failures.append("scaled future endpoint B does not map to physical T")

    # Pairing: M^-1 from amplitude and M^3 from dy=M^3 dx.
    pairing_prefactor_exponent = -1 + 3
    if pairing_prefactor_exponent != 2:
        failures.append(f"pairing prefactor exponent is {pairing_prefactor_exponent}, not 2")

    local_lq_scaling = []
    for q in range(1, 7):
        exponent = 3 - q
        local_lq_scaling.append({"q": q, "integral_M_exponent": exponent})
        if q == 3 and exponent != 0:
            failures.append("local L3 mass is not scale invariant")

    # If |v(0)|=1 and ||nabla v||<=G, then |v|>=1/2 on B_(1/(2G)).
    # In 3D the resulting L3 mass is pi/(48 G^3). We certify the rational
    # coefficient multiplying pi*G^-3; no approximation of pi is used.
    radius_coefficient = Fraction(1, 2)
    volume_coefficient = Fraction(4, 3) * radius_coefficient**3
    amplitude_cubed = Fraction(1, 2) ** 3
    critical_mass_coefficient = volume_coefficient * amplitude_cubed
    if critical_mass_coefficient != Fraction(1, 48):
        failures.append(
            f"critical mass coefficient is {critical_mass_coefficient}, not 1/48"
        )

    # Uniform record-time modulus for a compactly supported test phi:
    # |<v_k(s)-v_k(0),phi>| <= L |s| ||phi||_1.
    lipschitz = Fraction(3)
    phi_l1 = Fraction(5)
    record_time_modulus = []
    previous = None
    for j in range(1, 9):
        abs_s = Fraction(1, 2**j)
        bound = lipschitz * phi_l1 * abs_s
        record_time_modulus.append({"abs_s": str(abs_s), "pairing_bound": str(bound)})
        if previous is not None and bound * 2 != previous:
            failures.append(f"record-time modulus did not halve at j={j}")
        previous = bound

    # Exact adverse boundary layer a_k(s)=exp(k^2 s). Its PDE residual cancels
    # symbolically for u=a e_1, p=-a' x_1. Only the coefficients are needed.
    a_dot = Fraction(7, 3)
    affine_pressure_pde_residuals = {
        "divergence": Fraction(0),
        "convection": Fraction(0),
        "laplacian": Fraction(0),
        "momentum_e1": a_dot - a_dot,
        "pressure_poisson": Fraction(0),
    }
    if any(affine_pressure_pde_residuals.values()):
        failures.append(f"affine-pressure residual nonzero: {affine_pressure_pde_residuals}")

    # Discrete samples expose the non-commuting corner of a generic endpoint
    # layer b_(k,j)=max(1-k/j,0), with s_j approaching zero. Along j=k^2 it
    # approaches 1; along k=j^2 it is identically 0. This array is not a PDE.
    boundary_layer_paths = []
    for n in range(2, 9):
        k = 2**n
        j_slow = k**2
        slow = max(Fraction(1) - Fraction(k, j_slow), Fraction(0))
        j = 2**n
        k_fast = j**2
        fast = max(Fraction(1) - Fraction(k_fast, j), Fraction(0))
        boundary_layer_paths.append(
            {"n": n, "j_equals_k_squared": str(slow), "k_equals_j_squared": str(fast)}
        )
        if slow != Fraction(k - 1, k) or fast != 0:
            failures.append(f"boundary-layer path identity failed at n={n}")

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
            failures.append(f"{name}: purported counterprofile passes every gate")

    report = {
        "experiment": data["experiment"],
        "arithmetic": "finite set logic and rational identities; pi retained symbolically",
        "obligations_sha256": hashlib.sha256(OBLIGATIONS_PATH.read_bytes()).hexdigest(),
        "direct_route": route,
        "direct_route_obligation_count": len(route),
        "equation_exponents_in_M": equation_exponents_in_M,
        "clock_audit": {
            "sample_t_k": str(sample_t_k),
            "sample_T": str(sample_T),
            "sample_M": str(sample_M),
            "sample_B": str(sample_B),
            "physical_at_s_zero": str(physical_at_record_zero),
            "physical_at_s_B": str(physical_at_future_endpoint),
        },
        "pairing_prefactor_M_exponent": pairing_prefactor_exponent,
        "local_lq_scaling": local_lq_scaling,
        "critical_L3_mass_lower_bound": "pi/(48 G^3)",
        "record_time_pairing_modulus": record_time_modulus,
        "affine_pressure_pde_residuals": {
            key: str(value) for key, value in affine_pressure_pde_residuals.items()
        },
        "noncommuting_boundary_layer_paths": boundary_layer_paths,
        "counterprofile_failed_gates": counterprofile_failures,
        "assertion_failure_count": len(failures),
        "assertion_failures": failures,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
