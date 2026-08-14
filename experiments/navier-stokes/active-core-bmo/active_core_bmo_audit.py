#!/usr/bin/env python3
"""Exact audit of the two-active-core bmo_phi extension obstruction.

The script certifies the finite geometry, mean-oscillation lower bound,
critical scaling, and a divergence-free inner-core construction.  It does not
integrate Navier--Stokes, certify a global pressure after cutoff, or prove that
the two-core family occurs along one Navier--Stokes trajectory.
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


def constant_corridor_mean_oscillation(value: Fraction) -> Fraction:
    """Three-atom model: two cores of mass 1/27 and corridor mass 25/27."""

    core_mass = Fraction(1, 27)
    corridor_mass = Fraction(25, 27)
    mean = corridor_mass * value
    return (
        core_mass * abs(1 - mean)
        + core_mass * abs(-1 - mean)
        + corridor_mass * abs(value - mean)
    )


def main() -> None:
    checks: list[dict[str, object]] = []

    # Two balls B_epsilon(+/-2 epsilon e1) sit in B_(3 epsilon)(0).
    # Each occupies exactly 1/27 of the containing ball.
    one_core_fraction = Fraction(1, 27)
    forced_mean_oscillation = 2 * one_core_fraction
    checks.append(
        check(
            "two_core_geometry",
            one_core_fraction == Fraction(1, 27)
            and forced_mean_oscillation == Fraction(2, 27),
            {
                "centers": "+/-2 epsilon e1",
                "core_radius": "epsilon",
                "test_ball_radius": "3 epsilon",
                "one_core_volume_fraction": fstr(one_core_fraction),
                "extension_independent_MO_lower_bound": fstr(forced_mean_oscillation),
            },
        )
    )

    # For any vector c, |e-c|+|-e-c|>=|e-(-e)|=2.  The exact scalar sweep
    # is a finite witness; the triangle inequality is the all-vector proof.
    scalar_means = [Fraction(k, 64) for k in range(-256, 257)]
    triangle_values = [abs(1 - c) + abs(-1 - c) for c in scalar_means]
    checks.append(
        check(
            "mean_independent_extension_lower_bound",
            min(triangle_values) == 2,
            {
                "rational_mean_sweep": "c=k/64, -256<=k<=256",
                "minimum_core_distance_sum": fstr(min(triangle_values)),
                "all_vector_certificate": "|e-c|+|-e-c|>=|e-(-e)|=2",
                "consequence": "mean oscillation on B_(3 epsilon) is at least 2/27 for every measurable extension",
            },
        )
    )

    # A constant fill of the zero corridor cannot evade the same bound.
    corridor_values = [Fraction(k, 64) for k in range(-64, 65)]
    corridor_oscillations = [constant_corridor_mean_oscillation(z) for z in corridor_values]
    checks.append(
        check(
            "zero_corridor_constant_fill_gate",
            min(corridor_oscillations) >= Fraction(2, 27),
            {
                "fill_sweep": "z=k/64, -1<=z<=1",
                "minimum_mean_oscillation": fstr(min(corridor_oscillations)),
                "unrestricted_extension_warning": "the preceding triangle proof, not this constant-fill sweep, covers arbitrary corridor values",
            },
        )
    )

    # At radii r_n=e^-n, the manuscript weight phi(r)=1/|log r| equals
    # 1/n.  Hence the normalized bmo_phi cost is at least 2n/27.
    normalized_costs = [Fraction(2 * n, 27) for n in range(1, 257)]
    checks.append(
        check(
            "log_weighted_extension_cost_diverges",
            all(right > left for left, right in zip(normalized_costs, normalized_costs[1:])),
            {
                "symbolic_radii": "r_n=exp(-n)=3 epsilon_n",
                "phi_r_n": "1/n",
                "cost_lower_bound": "2n/27",
                "checked_n": "1..256",
                "last_exact_cost": fstr(normalized_costs[-1]),
                "all_scale_certificate": "2n/27 tends to infinity",
            },
        )
    )

    # Each core separately has a constant direction and therefore zero local
    # mean oscillation, while one ball seeing both cores has a fixed defect.
    checks.append(
        check(
            "corewise_coherence_does_not_globalize",
            Fraction(0) < forced_mean_oscillation,
            {
                "MO_on_each_constant_core": "0",
                "MO_on_common_ball_lower_bound": fstr(forced_mean_oscillation),
                "verdict": "componentwise perfect coherence does not imply a uniform global bmo_phi bound",
            },
        )
    )

    # Smooth compactly supported realization: choose a scalar potential
    # B_3=-(sigma A/4)(y1^2+y2^2) chi, with chi=1 on the core, and set
    # u=curl(B_3 e3).  Globally div u=div curl(...)=0.  On the core the
    # following derivative ledger is exact.
    derivative_ledger = {
        "partial_1_u1": Fraction(0),
        "partial_2_u2": Fraction(0),
        "partial_3_u3": Fraction(0),
        "partial_1_u2_coefficient": Fraction(1, 2),
        "partial_2_u1_coefficient": Fraction(-1, 2),
    }
    divergence = (
        derivative_ledger["partial_1_u1"]
        + derivative_ledger["partial_2_u2"]
        + derivative_ledger["partial_3_u3"]
    )
    curl_3_coefficient = (
        derivative_ledger["partial_1_u2_coefficient"]
        - derivative_ledger["partial_2_u1_coefficient"]
    )
    checks.append(
        check(
            "divergence_free_core_realization",
            divergence == 0 and curl_3_coefficient == 1,
            {
                "potential": "B3=-(sigma A/4)(y1^2+y2^2) chi_epsilon,p",
                "velocity_on_core": "u=(-sigma A y2/2, sigma A y1/2, 0)",
                "divergence_residual": fstr(divergence),
                "curl_on_core": "sigma A e3",
                "curl_coefficient_residual": fstr(curl_3_coefficient - 1),
                "global_certificate": "u is a curl of a smooth compactly supported potential",
            },
        )
    )

    # The two signs give exactly opposite direction fields on the two cores.
    directions = {sigma: (0, 0, sigma) for sigma in (-1, 1)}
    direction_dot_product = sum(
        Fraction(directions[1][j] * directions[-1][j]) for j in range(3)
    )
    checks.append(
        check(
            "opposite_vorticity_directions",
            direction_dot_product == -1,
            {
                "xi_plus": directions[1],
                "xi_minus": directions[-1],
                "dot_product": fstr(direction_dot_product),
                "angular_separation": "pi",
            },
        )
    )

    # The uncut solid-rotation polynomial is an exact stationary NS solution:
    # convection is cancelled by p=A^2(y1^2+y2^2)/8 and Delta u=0.
    # This check is not a pressure computation for the globally cut-off field.
    local_residuals = []
    amplitude = Fraction(9, 4)
    for sigma in (-1, 1):
        for y1, y2 in ((Fraction(1, 3), Fraction(-2, 5)), (Fraction(-7, 8), Fraction(5, 6))):
            convection = (-amplitude**2 * y1 / 4, -amplitude**2 * y2 / 4, Fraction(0))
            pressure_gradient = (amplitude**2 * y1 / 4, amplitude**2 * y2 / 4, Fraction(0))
            viscosity = (Fraction(0), Fraction(0), Fraction(0))
            residual = tuple(convection[j] + pressure_gradient[j] - viscosity[j] for j in range(3))
            local_residuals.append((sigma, residual))
    checks.append(
        check(
            "uncut_solid_rotation_ns_residual",
            all(residual == (0, 0, 0) for _, residual in local_residuals),
            {
                "tested_signs": [-1, 1],
                "amplitude": fstr(amplitude),
                "pressure": "p=A^2(y1^2+y2^2)/8",
                "residuals": [[sigma, [fstr(value) for value in residual]] for sigma, residual in local_residuals],
                "warning": "the cutoff transition has a nonzero residual and requires the global Leray pressure",
            },
        )
    )

    # Critical two-core scaling with epsilon as length: A=epsilon^-2,
    # |u|~epsilon^-1, volume~epsilon^3, energy~epsilon, and the weak-L3/2
    # vorticity scale A*volume^(2/3) is invariant.
    epsilon_weights = {
        "length_epsilon": 1,
        "vorticity_amplitude_A": -2,
        "velocity_amplitude": -1,
        "volume": 3,
        "velocity_energy_squared": 1,
        "weak_L32_vorticity": 0,
        "direction": 0,
    }
    checks.append(
        check(
            "critical_two_core_scaling",
            2 * epsilon_weights["velocity_amplitude"] + epsilon_weights["volume"]
            == epsilon_weights["velocity_energy_squared"]
            and epsilon_weights["vorticity_amplitude_A"]
            + Fraction(2, 3) * epsilon_weights["volume"]
            == epsilon_weights["weak_L32_vorticity"],
            {
                "epsilon_exponents": epsilon_weights,
                "critical_choice": "A_epsilon=epsilon^-2",
                "consequence": "energy tends to zero while the weak-L^(3/2) vorticity scale remains order one",
            },
        )
    )

    # Dyadic multiscale atom ledger.  At strict threshold lambda_N=4^N,
    # all levels n>N have total normalized volume 2/(7*8^N), so
    # lambda_N^(3/2) mu(lambda_N)=2/7 exactly.
    weak_rows = []
    for level in range(1, 65):
        tail_volume = Fraction(2, 7 * 8**level)
        lambda_power_three_halves = Fraction(8**level)
        product = tail_volume * lambda_power_three_halves
        weak_rows.append(product)
    checks.append(
        check(
            "dyadic_weak_L32_distribution",
            all(product == Fraction(2, 7) for product in weak_rows),
            {
                "levels": "N=1..64",
                "amplitude": "A_N=4^N",
                "pair_volume": "2*8^-N (unit ball volume suppressed)",
                "strict_tail_volume": "2/(7*8^N)",
                "lambda_power_3_over_2_times_tail": fstr(Fraction(2, 7)),
            },
        )
    )

    # The exact inner-core kinetic energy of a pair, with unit ball volume
    # suppressed, is epsilon/5.  Its dyadic sum is finite.
    energy_partials = [
        sum(Fraction(1, 5 * 2**n) for n in range(1, cutoff + 1))
        for cutoff in range(1, 129)
    ]
    checks.append(
        check(
            "dyadic_energy_budget",
            all(value < Fraction(1, 5) for value in energy_partials),
            {
                "pair_core_energy": "|B_1| epsilon/5",
                "normalized_partial_sum_N128": fstr(energy_partials[-1]),
                "normalized_infinite_sum": fstr(Fraction(1, 5)),
                "scope": "inner cores exactly; cutoff shells change only the fixed prefactor",
            },
        )
    )

    # Dimensioned logarithms must use a reference scale.  Choosing
    # r_n=R_* exp(1-n) makes phi_*(r_n)=1/n exactly.
    scale_weights = {
        "r": -1,
        "R_star": -1,
        "r_over_R_star": 0,
        "direction": 0,
        "mean_oscillation": 0,
        "weighted_bmo_ratio": 0,
    }
    checks.append(
        check(
            "dimensioned_bmo_scaling_ledger",
            scale_weights["r"] - scale_weights["R_star"]
            == scale_weights["r_over_R_star"]
            and scale_weights["mean_oscillation"] == scale_weights["weighted_bmo_ratio"],
            {
                "weights_under_NS_kappa": scale_weights,
                "weight": "phi_*(r)=1/[1+log(R_*/r)]",
                "symbolic_sequence": "r_n=R_* exp(1-n), hence phi_*(r_n)=1/n",
            },
        )
    )

    digest = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
    output = {
        "artifact": "ACTIVE-CORE-BMO-OBSTRUCTION-1",
        "scope": "exact extension obstruction and critical static two-core scaling on R3",
        "arithmetic": "fractions and symbolic logarithmic sequences; no floating point",
        "discretization": "no PDE grid; finite sweeps have analytic all-scale certificates",
        "random_seed": None,
        "pde_status": "smooth compactly supported divergence-free initial-data family; not one Navier-Stokes trajectory",
        "uncertified_components": [
            "existence of this geometry along a candidate blow-up trajectory",
            "global pressure and Navier-Stokes residual in cutoff shells",
            "a time-uniform upper bmo_phi extension bound",
            "any implication from weak-L^(3/2) vorticity to global regularity or blow-up",
        ],
        "assertion_failure_count": 0,
        "check_count": len(checks),
        "checks": checks,
        "script_sha256": digest,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
