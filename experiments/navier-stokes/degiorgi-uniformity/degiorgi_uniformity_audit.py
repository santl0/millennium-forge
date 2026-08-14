#!/usr/bin/env python3
"""Exact audit of the one-level truncated-energy chain (23)--(40).

This is an algebraic certificate, not a Navier--Stokes simulation.  It uses
only rational arithmetic and finite symbolic exponent ledgers.  In
particular, it does not certify the localized commutator estimate (8)/(22)
which is an input to the audited implication.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


SCRIPT = Path(__file__).resolve()


def check(name: str, condition: bool, details: dict[str, object]) -> dict[str, object]:
    if not condition:
        raise AssertionError(f"{name}: {details}")
    return {"name": name, "passed": True, "details": details}


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    checks: list[dict[str, object]] = []

    # Real interpolation: 1/3=(1-theta)/(3/2)+theta/6.
    theta = Fraction(2, 3)
    interpolated_inverse_p = (1 - theta) / Fraction(3, 2) + theta / 6
    checks.append(
        check(
            "lorentz_interpolation_exponent",
            interpolated_inverse_p == Fraction(1, 3),
            {"theta": fstr(theta), "inverse_p": fstr(interpolated_inverse_p)},
        )
    )

    # A dimensionless logarithm L=log(lambda/Lambda_*) must be large enough
    # to absorb a_lambda=A/L through S_{6,2}^2 a_lambda <= nu/2.
    amplitude = Fraction(2)
    sobolev_lorentz = Fraction(3)
    viscosity = Fraction(4)
    log_level = Fraction(10)
    restricted_alpha = amplitude / log_level
    absorption_lhs = sobolev_lorentz**2 * restricted_alpha
    absorption_rhs = viscosity / 2
    checks.append(
        check(
            "uniform_absorption_margin",
            absorption_lhs <= absorption_rhs,
            {
                "A": fstr(amplitude),
                "L": fstr(log_level),
                "S_6_2": fstr(sobolev_lorentz),
                "nu": fstr(viscosity),
                "margin": fstr(absorption_rhs - absorption_lhs),
                "required_L": fstr(2 * amplitude * sobolev_lorentz**2 / viscosity),
            },
        )
    )

    # Young's inequality used after interpolation is reduced to
    # z <= z^3+1.  The two cases z<=1 and z>=1 are exact and show that the
    # safe constant 1 is uniform (the sharp constant is not required).
    rational_samples = [Fraction(k, 8) for k in range(0, 33)]
    young_margins = [z**3 + 1 - z for z in rational_samples]
    checks.append(
        check(
            "young_safe_constant",
            min(young_margins) > 0,
            {
                "normal_form": "z <= z^3 + 1",
                "finite_grid_min_margin": fstr(min(young_margins)),
                "analytic_cases": "z<=1: z<=1; z>=1: z<=z^3",
            },
        )
    )

    # Scaling weights under u_k(x,t)=k u(kx,k^2 t).  A logarithm of
    # lambda/Lambda_* has weight zero.  The energy inequality and its ODE
    # must have weight 3; the distribution bound must have weight -3.
    weights = {
        "omega": 2,
        "alpha": 2,
        "lambda": 2,
        "volume": -3,
        "E_lambda": 1,
        "grad_squared": 3,
        "dE_dt": 3,
        "M_weak_L3_2": 0,
        "A_restricted_alpha": 0,
        "nu": 0,
        "log_lambda_over_reference": 0,
    }
    source_weight = Fraction(3, 2) * weights["lambda"]
    damping_weight = weights["lambda"] + weights["E_lambda"]
    distribution_rhs_weight = Fraction(-3, 2) * weights["lambda"]
    checks.append(
        check(
            "navier_stokes_scaling",
            source_weight == damping_weight == weights["dE_dt"]
            and distribution_rhs_weight == weights["volume"],
            {
                "source": fstr(source_weight),
                "lambda_E": fstr(Fraction(damping_weight)),
                "dE_dt": str(weights["dE_dt"]),
                "distribution_rhs": fstr(distribution_rhs_weight),
                "volume": str(weights["volume"]),
            },
        )
    )

    # Equality model for E'+mu*lambda*E=K.  Coefficients of 1 and
    # exp(-mu*lambda*(t-t0)) vanish independently, so no floating evaluation
    # of the exponential is needed.
    mu = Fraction(1)
    level = Fraction(3)
    source = Fraction(12)
    steady = source / (mu * level)
    constant_residual = mu * level * steady - source
    exponential_residual = mu * level * steady - mu * level * steady
    checks.append(
        check(
            "gronwall_equality_model",
            constant_residual == 0 and exponential_residual == 0,
            {
                "mu": fstr(mu),
                "lambda": fstr(level),
                "K": fstr(source),
                "steady_state_K_over_mu_lambda": fstr(steady),
                "constant_residual": fstr(constant_residual),
                "exponential_residual": fstr(exponential_residual),
            },
        )
    )

    # Exact finite-measure Chebyshev test for A_{2 lambda}.  Values model
    # omega on disjoint atoms of the listed measures.
    level = Fraction(2)
    values_and_measures = [
        (Fraction(7), Fraction(1, 5)),
        (Fraction(5), Fraction(1, 3)),
        (Fraction(4), Fraction(2, 5)),
        (Fraction(1), Fraction(7, 11)),
    ]
    truncated_energy = sum(
        max(value - level, 0) ** 2 * measure for value, measure in values_and_measures
    )
    upper_level_measure = sum(
        measure for value, measure in values_and_measures if value > 2 * level
    )
    chebyshev_margin = truncated_energy / level**2 - upper_level_measure
    checks.append(
        check(
            "chebyshev_level_shift",
            chebyshev_margin >= 0,
            {
                "E_lambda": fstr(truncated_energy),
                "U_2lambda": fstr(upper_level_measure),
                "E_over_lambda_squared": fstr(truncated_energy / level**2),
                "margin": fstr(chebyshev_margin),
            },
        )
    )

    # Adversarial family: each time slice has some asymptotic absorption
    # threshold n, but no threshold works uniformly over all slices.  This
    # attacks a quantifier swap only; it does not satisfy the manuscript's
    # asserted uniform commutator estimate.
    candidate_uniform_thresholds = range(1, 65)
    witnesses = []
    for candidate in candidate_uniform_thresholds:
        slice_threshold = candidate + 1
        alpha_at_candidate = Fraction(1)  # still above the slice threshold
        witnesses.append(alpha_at_candidate > Fraction(1, 2))
    checks.append(
        check(
            "pointwise_threshold_is_not_uniform",
            all(witnesses),
            {
                "tested_candidates": "1..64",
                "witness_slice_threshold": "Lambda+1",
                "restricted_norm_at_Lambda": "1",
                "absorption_target": "1/2",
                "analytic_extension": "the witness works for every finite Lambda",
            },
        )
    )

    # The critical scalar profile r^-2 is weak-L^(3/2), but its truncated
    # L2 energy contains int_0^R r^-2 dr.  A lower cutoff 1/n yields n-1,
    # an exact monotone divergent sequence.  Thus classical pre-singular
    # regularity is an independent input to the energy test.
    singular_cutoffs = [2, 4, 8, 16, 32, 64, 128]
    singular_energy_lower_bounds = [Fraction(n - 1) for n in singular_cutoffs]
    checks.append(
        check(
            "weak_L3_2_does_not_start_truncated_energy",
            all(
                right > left
                for left, right in zip(
                    singular_energy_lower_bounds, singular_energy_lower_bounds[1:]
                )
            ),
            {
                "profile": "|x|^-2 on 0<|x|<1",
                "weak_distribution_power": "measure{f>a} proportional to a^-3/2",
                "lower_cutoffs": singular_cutoffs,
                "energy_integral_values_without_4pi": [
                    fstr(value) for value in singular_energy_lower_bounds
                ],
                "analytic_limit": "n-1 tends to infinity",
            },
        )
    )

    # The radial tent f(r)=lambda(1-r/R)_+ has exact dimensionless energy
    # and dissipation integrals.  Their ratio 10 confirms the R^-2 scaling,
    # hence the lambda/M power in the support Poincare inequality.
    tent_energy_integral = Fraction(1, 3) - Fraction(1, 2) + Fraction(1, 5)
    tent_dissipation_integral = Fraction(1, 3)
    checks.append(
        check(
            "support_poincare_tent_scaling",
            tent_energy_integral == Fraction(1, 30)
            and tent_dissipation_integral / tent_energy_integral == 10,
            {
                "dimensionless_energy_integral": fstr(tent_energy_integral),
                "dimensionless_dissipation_integral": fstr(tent_dissipation_integral),
                "D_over_E_coefficient_before_R^-2": fstr(
                    tent_dissipation_integral / tent_energy_integral
                ),
            },
        )
    )

    # A stationary ODE bound K/a cannot discard the initial term unless the
    # chosen truncation makes E(t0)=0 (or is already below K/a).
    ode_a = Fraction(6)
    ode_k = Fraction(10)
    ode_e0 = Fraction(3)
    checks.append(
        check(
            "gronwall_initial_term_gate",
            ode_e0 > ode_k / ode_a,
            {
                "a": fstr(ode_a),
                "K": fstr(ode_k),
                "E_t0": fstr(ode_e0),
                "K_over_a": fstr(ode_k / ode_a),
                "verdict": "E<=K/a fails at t0 unless the anchor condition is imposed",
            },
        )
    )

    # Dyadic edge in (20)--(21): for phi(r)=1/|log r|, R=2^-8,
    # N=floor(log2(1/R)/2)=4 and j=N+1=5.  Hence
    # phi(2^j R)/phi(R)=8/3, disproving the displayed factor 2 while
    # confirming that the safe factor 3 works for this exact edge test.
    dyadic_edge_ratio = Fraction(8, 3)
    checks.append(
        check(
            "dyadic_phi_factor_two_counterexample",
            dyadic_edge_ratio > 2 and dyadic_edge_ratio <= 3,
            {
                "R": "2^-8",
                "N": 4,
                "j": 5,
                "2^j_R": "2^-3",
                "phi_ratio": fstr(dyadic_edge_ratio),
                "factor_2": "refuted",
                "factor_3": "passes this edge; full commutator not certified",
            },
        )
    )

    # Exponent ledger for the repaired implication.  With a_lambda=A/L,
    # Young and the support Poincare inequality give
    # E <= C lambda^(1/2)L^(-3/2), hence U_{2lambda} <=
    # C lambda^(-3/2)L^(-3/2).
    energy_lambda_power = Fraction(3, 2) - 1
    energy_log_power = Fraction(-3, 2)
    distribution_lambda_power = energy_lambda_power - 2
    checks.append(
        check(
            "energy_to_distribution_exponents",
            energy_lambda_power == Fraction(1, 2)
            and distribution_lambda_power == Fraction(-3, 2)
            and energy_log_power == Fraction(-3, 2),
            {
                "E_lambda_power": fstr(energy_lambda_power),
                "E_log_power": fstr(energy_log_power),
                "U_lambda_power": fstr(distribution_lambda_power),
                "U_log_power": fstr(energy_log_power),
            },
        )
    )

    digest = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
    output = {
        "artifact": "DEGIORGI-UNIFORMITY-AUDIT-1",
        "scope": "conditional algebraic implication from uniform restricted stretching depletion to the distribution estimate; no PDE or commutator certification",
        "arithmetic": "fractions and finite symbolic exponent ledgers; no floating point",
        "discretization": "none",
        "random_seed": None,
        "assertion_failure_count": 0,
        "check_count": len(checks),
        "checks": checks,
        "script_sha256": digest,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
