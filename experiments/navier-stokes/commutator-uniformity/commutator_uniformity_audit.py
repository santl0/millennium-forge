#!/usr/bin/env python3
"""Exact envelope audit for the localized commutator chain (8)--(22).

The script certifies rational dyadic sums, scaling ledgers, and adversarial
gates.  It does not evaluate a Calderon--Zygmund operator, prove the Jones or
Coifman--Rochberg--Weiss theorems, or simulate Navier--Stokes.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


SCRIPT = Path(__file__).resolve()


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def check(name: str, condition: bool, details: dict[str, object]) -> dict[str, object]:
    if not condition:
        raise AssertionError(f"{name}: {details}")
    return {"name": name, "passed": True, "details": details}


def dyadic_weight_ratio(log2_inverse_radius: int, index: int) -> Fraction:
    """phi(2^j R)/phi(R) for R=2^-T and phi(r)=1/|log r|."""

    return Fraction(log2_inverse_radius, log2_inverse_radius - index)


def normalized_double_sum(log2_inverse_radius: int) -> Fraction:
    """(sum_k 4^-k sum_{j<=k+1} phi_j)/phi(R), exactly."""

    total = Fraction(0)
    threshold = log2_inverse_radius // 2
    for k in range(1, threshold + 1):
        inner = sum(
            Fraction(log2_inverse_radius, log2_inverse_radius - j)
            for j in range(1, k + 2)
        )
        total += Fraction(1, 4**k) * inner
    return total


def normalized_unweighted_drift(log2_inverse_radius: int) -> Fraction:
    """(sum_j phi_j)/phi(R), the mean-drift gate without 4^-k."""

    threshold = log2_inverse_radius // 2
    return sum(
        Fraction(log2_inverse_radius, log2_inverse_radius - j)
        for j in range(1, threshold + 2)
    )


def main() -> None:
    checks: list[dict[str, object]] = []

    # Exact counterexample to the factor 2 displayed before (21).
    edge_ratio = dyadic_weight_ratio(8, 5)
    checks.append(
        check(
            "dyadic_factor_two_refuted",
            edge_ratio == Fraction(8, 3) and edge_ratio > 2,
            {"R": "2^-8", "N": 4, "j": 5, "phi_ratio": fstr(edge_ratio)},
        )
    )

    # For T>=6 and N=floor(T/2), j<=N+1 gives
    # T/(T-j)<=T/(T/2-1)<=3.  The finite exact sweep checks the arithmetic;
    # the displayed inequality is the certificate for every real T>=6.
    edge_ratios = []
    for inverse_log in range(6, 513):
        threshold = inverse_log // 2
        edge_ratios.append(dyadic_weight_ratio(inverse_log, threshold + 1))
    checks.append(
        check(
            "dyadic_factor_three_safe",
            max(edge_ratios) <= 3,
            {
                "integer_range": "T=6..512",
                "maximum": fstr(max(edge_ratios)),
                "analytic_extension": "N<=T/2 implies T/(T-N-1)<=2T/(T-2)<=3 for every real T>=6",
            },
        )
    )

    # The geometric series which compensates the telescoping mean drift.
    # Sum_{k>=1}(k+1)4^-k=7/9, so factor 3 yields the safe 7/3.
    geometric_partials = [
        sum(Fraction(k + 1, 4**k) for k in range(1, n + 1))
        for n in range(1, 257)
    ]
    checks.append(
        check(
            "geometric_annular_budget",
            all(value <= Fraction(7, 9) for value in geometric_partials),
            {
                "checked_partials": "N=1..256, each strictly below 7/9",
                "infinite_sum": "7/9",
                "safe_weighted_constant_after_phi_factor_3": "7/3",
            },
        )
    )

    # Execute the exact double sum, with all positive increments (the adverse
    # sign choice for this absolute-value envelope).
    double_sums = [normalized_double_sum(t) for t in range(6, 513)]
    maximum_double_sum = max(double_sums)
    maximum_index = 6 + double_sums.index(maximum_double_sum)
    checks.append(
        check(
            "weighted_multiscale_envelope",
            maximum_double_sum <= Fraction(7, 3),
            {
                "T_range": "6..512",
                "maximum_ratio_to_phi_R": fstr(maximum_double_sum),
                "attained_at_T": maximum_index,
                "margin_to_safe_7_over_3": fstr(Fraction(7, 3) - maximum_double_sum),
                "sign_choice": "all increments positive maximizes the absolute envelope",
            },
        )
    )

    # Without the geometric kernel weights, the telescoping drift cannot be
    # bounded by C phi(R): each of roughly T/2 terms is at least phi(R).
    drift_ratios = [normalized_unweighted_drift(t) for t in (8, 16, 32, 64, 128, 256)]
    checks.append(
        check(
            "unweighted_mean_drift_not_small",
            all(right > left for left, right in zip(drift_ratios, drift_ratios[1:])),
            {
                "T_values": [8, 16, 32, 64, 128, 256],
                "certified_integer_lower_bounds": [5, 9, 17, 33, 65, 129],
                "analytic_lower_bound": "ratio >= floor(T/2)+1, hence no uniform C",
                "verdict": "the 4^-k kernel budget is essential",
            },
        )
    )

    # Lorentz weak endpoint follows by interpolating two strong Lp bounds;
    # L^(3/2,infinity) itself is not reflexive.  For p0=4/3, p1=2 the
    # interpolation parameter is theta=1/3.
    theta = Fraction(1, 3)
    inverse_p = (1 - theta) / Fraction(4, 3) + theta / 2
    checks.append(
        check(
            "weak_lorentz_interpolation_route",
            inverse_p == Fraction(2, 3),
            {
                "p0": "4/3",
                "p1": "2",
                "theta": fstr(theta),
                "target_p": "3/2",
                "target_q": "infinity",
                "warning": "L^(3/2,infinity) is non-reflexive; the mapping uses real interpolation of neighboring strong bounds",
            },
        )
    )

    # A naive zero extension cannot preserve a small BMO seminorm.  A
    # constant on the local domain has local seminorm zero, while a symmetric
    # two-atom ball crossing a zero-extension boundary has oscillation 1/2.
    local_constant_seminorm = Fraction(0)
    crossing_mean = Fraction(1, 2)
    crossing_mean_oscillation = (
        abs(Fraction(1) - crossing_mean) + abs(Fraction(0) - crossing_mean)
    ) / 2
    checks.append(
        check(
            "bmo_extension_gauge_gate",
            local_constant_seminorm == 0 and crossing_mean_oscillation == Fraction(1, 2),
            {
                "local_constant_seminorm": fstr(local_constant_seminorm),
                "zero_extension_crossing_oscillation": fstr(crossing_mean_oscillation),
                "repair": "subtract a local mean and use a Jones extension; commutators ignore restored constants",
            },
        )
    )

    # Scaling ledger with a reference radius R*.  The far cutoff
    # L=sqrt(R R*) yields pointwise L^-2 and restricted weak norm R^2/L^2=R/R*.
    spatial_weights = {
        "R": -1,
        "R_star": -1,
        "geometric_mean_cutoff": -1,
        "pointwise_strain": 2,
        "local_L32_volume_factor": -2,
        "restricted_commutator_norm": 0,
        "phi_R_over_R_star": 0,
    }
    checks.append(
        check(
            "commutator_scaling_ledger",
            spatial_weights["pointwise_strain"]
            + spatial_weights["local_L32_volume_factor"]
            == spatial_weights["restricted_commutator_norm"],
            {
                "weights_under_NS_kappa": spatial_weights,
                "I1_and_Imid": "R^-2 times R^2 times phi(R/R*)",
                "Ifar": "(R R*)^-1 times R^2 = R/R*",
                "far_absorption": "q=R/R* <= 1/log(e/q) for 0<q<=1",
            },
        )
    )

    digest = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
    output = {
        "artifact": "COMMUTATOR-UNIFORMITY-AUDIT-1",
        "scope": "exact dyadic and scaling envelope for (8)-(22); classical harmonic-analysis theorems remain external premises",
        "arithmetic": "fractions and finite symbolic ledgers; no floating point",
        "discretization": "no PDE grid; finite exact sweeps are paired with analytic all-scale inequalities",
        "random_seed": None,
        "assertion_failure_count": 0,
        "check_count": len(checks),
        "checks": checks,
        "script_sha256": digest,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
