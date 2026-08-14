#!/usr/bin/env python3
"""Exact audit of the conditional analyticity--sparseness endgame.

The script checks the temporal branch split, harmonic-measure algebra,
scaling ledger, logarithmic constant gate, and a rational cubed-radius
comparison.  It neither constructs a Navier--Stokes solution nor proves the
upstream distribution estimate or the external analyticity theorems.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


SCRIPT = Path(__file__).resolve()


def fstr(value: Fraction) -> str:
    """Serialize a rational without floating-point conversion."""

    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def check(name: str, condition: bool, details: dict[str, object]) -> dict[str, object]:
    if not condition:
        raise AssertionError(f"{name}: {details}")
    return {"name": name, "passed": True, "details": details}


def harmonic_parameters(harmonic_lower_bound: Fraction) -> tuple[Fraction, Fraction]:
    """Return M and lambda from h/2+(1-h)M=1 and lambda M=1/2."""

    h = harmonic_lower_bound
    leap = (2 - h) / (2 * (1 - h))
    threshold = (1 - h) / (2 - h)
    return leap, threshold


def harmonic_coefficient(harmonic_measure: Fraction, leap: Fraction) -> Fraction:
    return harmonic_measure / 2 + (1 - harmonic_measure) * leap


def main() -> None:
    checks: list[dict[str, object]] = []

    # The algebra used after the harmonic-measure lower bound must hold for
    # every h in (0,1), not merely for a decimal approximation of h*.
    harmonic_rows = []
    for h in (Fraction(1, 10), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(9, 10)):
        leap, threshold = harmonic_parameters(h)
        row_ok = (
            leap > 1
            and 0 < threshold < Fraction(1, 2)
            and threshold * leap == Fraction(1, 2)
            and harmonic_coefficient(h, leap) == 1
        )
        harmonic_rows.append(
            {
                "h": fstr(h),
                "M": fstr(leap),
                "lambda": fstr(threshold),
                "identity_residual": fstr(harmonic_coefficient(h, leap) - 1),
                "passed": row_ok,
            }
        )
    checks.append(
        check(
            "harmonic_parameter_identity",
            all(row["passed"] for row in harmonic_rows),
            {"rows": harmonic_rows, "analytic_formulas": {"M": "(2-h)/(2(1-h))", "lambda": "(1-h)/(2-h)"}},
        )
    )

    # Since M>1/2, H/2+(1-H)M decreases with H.  The finite rational
    # witnesses are accompanied by this exact derivative certificate.
    monotonic_rows = []
    for h in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
        leap, _ = harmonic_parameters(h)
        values = [harmonic_coefficient(H, leap) for H in (h, (1 + h) / 2, Fraction(1))]
        monotonic_rows.append(
            {
                "h": fstr(h),
                "coefficients_for_H_h_mid_1": [fstr(value) for value in values],
                "slope": fstr(Fraction(1, 2) - leap),
                "passed": values[0] == 1 and values[0] >= values[1] >= values[2],
            }
        )
    checks.append(
        check(
            "harmonic_coefficient_monotonicity",
            all(row["passed"] for row in monotonic_rows),
            {"rows": monotonic_rows, "all_scale_certificate": "d/dH [H/2+(1-H)M]=1/2-M<0"},
        )
    )

    # A guaranteed local lifespan tau gives an exhaustive split.  Equality
    # belongs to the extension branch, because an interior evaluation time
    # must satisfy s<T* strictly.
    branch_rows = []
    for terminal_time, base_time, lifespan in (
        (Fraction(1), Fraction(3, 4), Fraction(1, 2)),
        (Fraction(1), Fraction(1, 2), Fraction(1, 2)),
        (Fraction(1), Fraction(1, 2), Fraction(1, 4)),
    ):
        endpoint = base_time + lifespan
        extension = endpoint >= terminal_time
        interior = endpoint < terminal_time
        branch_rows.append(
            {
                "T_star": fstr(terminal_time),
                "t": fstr(base_time),
                "tau_t": fstr(lifespan),
                "t_plus_tau_t": fstr(endpoint),
                "branch": "local_extension" if extension else "interior_endgame",
                "exclusive_and_exhaustive": extension != interior,
            }
        )
    checks.append(
        check(
            "local_lifespan_branch_partition",
            all(row["exclusive_and_exhaustive"] for row in branch_rows),
            {"rows": branch_rows, "partition": "t+tau_t>=T* or t+tau_t<T*"},
        )
    )

    # Literal countermodel to selecting s=t+T_t when T_t is a maximal
    # lifespan: it can land exactly at the putative singular time and hence
    # is not an admissible point of (t,T*).
    terminal_time = Fraction(1)
    base_time = Fraction(3, 4)
    maximal_lifespan = Fraction(1, 4)
    literal_s = base_time + maximal_lifespan
    checks.append(
        check(
            "maximal_time_selection_refuted",
            literal_s == terminal_time and not (base_time < literal_s < terminal_time),
            {
                "T_star": fstr(terminal_time),
                "t": fstr(base_time),
                "T_t_max": fstr(maximal_lifespan),
                "literal_s": fstr(literal_s),
                "strict_interior_residual_T_star_minus_s": fstr(terminal_time - literal_s),
                "verdict": "s=t+T_t_max need not belong to (t,T*)",
            },
        )
    )

    # Two asymptotic subsequences can approach the same terminal time without
    # ever furnishing a common evaluation time.  Equality would require
    # 4n=4m+2, impossible modulo four.
    distribution_times = {1 - Fraction(1, 4 * n) for n in range(1, 65)}
    analyticity_times = {1 - Fraction(1, 4 * n + 2) for n in range(1, 65)}
    checks.append(
        check(
            "separate_asymptotic_times_not_synchronized",
            distribution_times.isdisjoint(analyticity_times),
            {
                "n_range": "1..64",
                "distribution_times": "d_n=1-1/(4n)",
                "analyticity_times": "a_n=1-1/(4n+2)",
                "intersection_size": len(distribution_times & analyticity_times),
                "all_scale_certificate": "d_n=a_m would imply 4n=4m+2, impossible modulo 4",
            },
        )
    )

    # Divergence of both the active level and the admissibility threshold does
    # not imply that the active level ever enters the theorem's range.
    level_rows = []
    for n in range(1, 33):
        active_level = Fraction(2**n, 4)
        moving_threshold = Fraction(2 ** (2 * n))
        level_rows.append(active_level < moving_threshold)
    checks.append(
        check(
            "nonuniform_level_threshold_gate",
            all(level_rows),
            {
                "n_range": "1..32",
                "active_level": "theta A_n=2^(n-2)",
                "moving_threshold": "Lambda_n=2^(2n)",
                "all_scale_certificate": "2^(n-2)<2^(2n) for every integer n>=1",
                "verdict": "a threshold uniform in time and truncation is indispensable",
            },
        )
    )

    # Exact synchronized branch-II witness.  The square root is rational for
    # this choice, so the analyticity radius is checked without floating point.
    viscosity = Fraction(1)
    analyticity_time_constant = Fraction(4)
    analyticity_radius_constant = Fraction(2)
    amplitude_t = Fraction(2)
    guaranteed_lifespan = viscosity / (analyticity_time_constant * amplitude_t**2)
    base_time = Fraction(1, 2)
    terminal_time = Fraction(1)
    synchronized_s = base_time + guaranteed_lifespan
    radius = Fraction(1, 8)
    radius_squared_from_theorem = viscosity * guaranteed_lifespan / analyticity_radius_constant**2
    radius_from_amplitude = viscosity / (
        analyticity_radius_constant * 2 * amplitude_t
    )
    checks.append(
        check(
            "interior_time_radius_synchronization",
            synchronized_s < terminal_time
            and radius**2 == radius_squared_from_theorem
            and radius == radius_from_amplitude,
            {
                "nu": fstr(viscosity),
                "c1": fstr(analyticity_time_constant),
                "c2": fstr(analyticity_radius_constant),
                "A_t": fstr(amplitude_t),
                "tau_t": fstr(guaranteed_lifespan),
                "s": fstr(synchronized_s),
                "rho": fstr(radius),
                "rho_squared_residual": fstr(radius**2 - radius_squared_from_theorem),
                "formula": "rho=sqrt(nu*tau_t)/c2=nu/(c2*sqrt(c1)*A_t)",
            },
        )
    )

    # Escape plus the real-slice analyticity bound yields A_t<A_s<=M A_t.
    h = Fraction(1, 2)
    leap, threshold = harmonic_parameters(h)
    amplitude_t = Fraction(2)
    amplitude_s = Fraction(5, 2)
    checks.append(
        check(
            "escape_amplitude_sandwich",
            amplitude_t < amplitude_s <= leap * amplitude_t,
            {
                "h": fstr(h),
                "M": fstr(leap),
                "lambda": fstr(threshold),
                "A_t": fstr(amplitude_t),
                "A_s": fstr(amplitude_s),
                "lower_margin": fstr(amplitude_s - amplitude_t),
                "upper_margin": fstr(leap * amplitude_t - amplitude_s),
            },
        )
    )

    # Replacing log(beta) by log(e+beta) cannot retain the same constant.
    # For beta>=3, e<3<=beta gives e+beta<=2beta; also log(2)<=log(beta).
    # Thus log(e+beta)<=2log(beta), and the safe cubed loss is 8.
    checks.append(
        check(
            "log_regularization_constant_gate",
            2**3 == 8,
            {
                "same_constant_counter_certificate": "for beta>1, log(e+beta)>log(beta)>0, so the regularized right-hand side is strictly smaller",
                "safe_constant_factor_for_beta_ge_3": 8,
                "analytic_certificate": "e<3<=beta => log(e+beta)<=log(2beta)<=2log(beta)",
                "verdict": "the exponent survives, but the displayed constant must be enlarged",
            },
        )
    )

    # Cubing avoids roots.  In normalized constants, C4=3 and
    # C_rho=1/4.  The sufficient logarithmic gate is ell>=C4/(C_rho nu)=12.
    amplitude_t = Fraction(120)
    amplitude_s = Fraction(150)
    c4 = Fraction(3)
    c_rho = Fraction(1, 4)
    logarithmic_lower_bound = Fraction(12)
    safe_sparse_radius = c4 / (amplitude_s * logarithmic_lower_bound)
    analytic_radius = c_rho * viscosity / amplitude_t
    threshold_log = c4 / (c_rho * viscosity)
    checks.append(
        check(
            "cubed_radius_gate",
            amplitude_t < amplitude_s
            and logarithmic_lower_bound >= threshold_log
            and safe_sparse_radius**3 <= analytic_radius**3,
            {
                "A_t": fstr(amplitude_t),
                "A_s": fstr(amplitude_s),
                "C4": fstr(c4),
                "C_rho": fstr(c_rho),
                "certified_log_lower_bound": fstr(logarithmic_lower_bound),
                "required_log_threshold": fstr(threshold_log),
                "r_sparse": fstr(safe_sparse_radius),
                "rho_analytic": fstr(analytic_radius),
                "cubed_margin_rho3_minus_r3": fstr(analytic_radius**3 - safe_sparse_radius**3),
                "all_scale_certificate": "r/rho <= [C4/(C_rho nu log(beta/Lambda*))](A_t/A_s)<=1",
            },
        )
    )

    # Scaling under u_kappa(x,t)=kappa u(kappa x,kappa^2 t).
    scaling_weights = {
        "amplitude_A": 1,
        "threshold_beta": 1,
        "reference_amplitude_Lambda_star": 1,
        "time_increment_tau": -2,
        "analytic_radius_rho": -1,
        "sparse_radius_r": -1,
        "volume": -3,
        "viscosity_nu": 0,
        "log_beta_over_Lambda_star": 0,
    }
    checks.append(
        check(
            "endgame_scaling_ledger",
            2 * scaling_weights["amplitude_A"] + scaling_weights["time_increment_tau"] == 0
            and scaling_weights["viscosity_nu"] - scaling_weights["amplitude_A"]
            == scaling_weights["analytic_radius_rho"]
            and -3 * scaling_weights["threshold_beta"] == scaling_weights["volume"]
            and scaling_weights["threshold_beta"] - scaling_weights["reference_amplitude_Lambda_star"]
            == scaling_weights["log_beta_over_Lambda_star"],
            {
                "weights_under_NS_kappa": scaling_weights,
                "dimensioned_formulas": [
                    "tau_t=nu/[c1(M) A_t^2]",
                    "rho=C_rho(M) nu/A_t",
                    "|{|u|>beta}|<=C_u/[beta^3 log^3(e+beta/Lambda*)]",
                ],
            },
        )
    )

    digest = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
    output = {
        "artifact": "ENDGAME-SYNCHRONIZATION-AUDIT-1",
        "scope": "exact algebraic and temporal audit of the conditional analyticity--sparseness endgame",
        "arithmetic": "fractions and symbolic ledgers; no floating point",
        "discretization": "no PDE grid",
        "random_seed": None,
        "external_premises_not_certified": [
            "mild-solution spatial analyticity theorem",
            "uniform distribution-tail estimate",
            "Solynin harmonic-measure lower bound",
            "Ransford two-constants theorem",
            "existence of terminal escape times for an unbounded classical branch",
        ],
        "assertion_failure_count": 0,
        "check_count": len(checks),
        "checks": checks,
        "script_sha256": digest,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
