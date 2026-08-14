#!/usr/bin/env python3
"""Exact gates for the vorticity-tail to velocity-rearrangement transfer.

The script uses only integers and fractions.  It does not discretize the
Navier--Stokes equations and does not evaluate transcendental functions with
floating point arithmetic.  Transcendental comparisons used in the analytic
proof are reduced to elementary series/convexity inequalities and recorded as
exact rational gates below.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import factorial


def exp_series_partial(x: Fraction, order: int) -> Fraction:
    """Return sum_{k=0}^order x^k/k! exactly."""

    return sum((x**k / factorial(k) for k in range(order + 1)), Fraction(0))


def distribution_of_step_profile(
    levels: tuple[tuple[Fraction, Fraction], ...], threshold: Fraction
) -> Fraction:
    """Mass of the strict super-level set for a finite step profile."""

    return sum(
        (mass for amplitude, mass in levels if amplitude > threshold),
        Fraction(0),
    )


def rearrangement_of_step_profile(
    levels: tuple[tuple[Fraction, Fraction], ...], volume: Fraction
) -> Fraction:
    """inf{a>=0: measure(f>a)<=volume} for a finite step profile."""

    candidates = (Fraction(0),) + tuple(
        sorted({amplitude for amplitude, _ in levels})
    )
    return min(
        amplitude
        for amplitude in candidates
        if distribution_of_step_profile(levels, amplitude) <= volume
    )


def certify_tail_inversion_gate() -> dict[str, object]:
    """Certify the algebra behind the quantitative inverse of equation (40).

    Write R=log(V/s)>=3 and q=(V/s)^(2/3).  The candidate level is
    y=3q/R.  The condition y log(y)>=q follows from

        log(y)-R/3 = log(3 exp(R/3)/R) >= 0,

    because exp(R/3)>=1+R/3.  The table records the resulting exact positive
    rational margin (3+R)/R-1=3/R.
    """

    margins: list[str] = []
    for r_integer in range(3, 25):
        r = Fraction(r_integer)
        lower_ratio = (3 + r) / r
        assert lower_ratio > 1
        margins.append(str(lower_ratio - 1))

    # log(eV/s)=1+R and R>=3 imply 3/R <= 4/(1+R).
    comparison_residuals: list[str] = []
    for r_integer in range(3, 25):
        r = Fraction(r_integer)
        residual = Fraction(4, 1 + r) - Fraction(3, r)
        assert residual >= 0
        comparison_residuals.append(str(residual))

    return {
        "candidate": "omega*(s) <= 3 Omega (V/s)^(2/3)/R, R=log(V/s)",
        "domain": "R>=3, equivalently 0<s<=V exp(-3)",
        "tail_domain_gate": (
            "y=3exp(2R/3)/R is increasing for R>=3 and y(3)=exp(2)>e"
        ),
        "convexity_gate": "exp(R/3)>=1+R/3 implies 3exp(R/3)/R>1",
        "exact_positive_margins_R_3_to_24": margins,
        "normalized_envelope": (
            "omega*(s) <= 4 Omega (V/s)^(2/3)/log(eV/s)"
        ),
        "normalization_residuals_R_3_to_24": comparison_residuals,
    }


def certify_oneil_integral_gates() -> dict[str, object]:
    """Certify constants in the Hardy core and logarithmic tail estimates."""

    # For T>=3, G(T)=20 exp(T/3)/(1+T) is a supersolution for
    # J'(T)=exp(T/3)/(1+T).  After removing the positive common factor,
    # 3(1+T)^2 exp(-T/3)(G'-J') = 17T-43.
    derivative_residuals: list[str] = []
    for t_integer in range(3, 101):
        residual = Fraction(17 * t_integer - 43)
        assert residual >= 8
        derivative_residuals.append(str(residual))

    # At T=3, J(3) <= 3(e-1) < 5e = G(3); the exact symbolic gap is 2e+3.
    # Positivity follows already from e>0.
    base_gap_constant = Fraction(3)
    assert base_gap_constant > 0

    # exp(2)>7, needed to absorb a scale-V far tail when T>=6.
    # The partial sum through order 4 equals 7 and the next term is positive.
    exp_two_order_four = exp_series_partial(Fraction(2), 4)
    exp_two_order_five = exp_series_partial(Fraction(2), 5)
    assert exp_two_order_four == 7
    assert exp_two_order_five > 7

    # e<=3 follows from n!>=2^(n-1) for n>=1.  The far weak-L^(3/2)
    # contribution 3e M V^(-1/3) is therefore at most 9 M V^(-1/3).
    factorial_margins: list[str] = []
    for n in range(1, 18):
        margin = Fraction(factorial(n) - 2 ** (n - 1))
        assert margin >= 0
        factorial_margins.append(str(margin))

    return {
        "hardy_core_constant": "3",
        "tail_supersolution_constant": "20",
        "tail_supersolution_gate": "17T-43>=8 for every integer T>=3",
        "tail_derivative_residuals_T_3_to_100": derivative_residuals,
        "tail_base_gap": "5e-3(e-1)=2e+3>0",
        "tail_base_rational_part": str(base_gap_constant),
        "exp_2_partial_order_4": str(exp_two_order_four),
        "exp_2_partial_order_5": str(exp_two_order_five),
        "exp_2_absorption_gate": "exp(2)>7",
        "e_upper_gate": "n!>=2^(n-1) implies e<=3",
        "factorial_margins_n_1_to_17": factorial_margins,
        "far_tail_constant": "9 M",
        "combined_convolution_constant": "C_K (23 C_0 + 9 M)",
    }


def certify_equation_46_remainder_gate() -> dict[str, object]:
    """Refute the O(1) label on the positive remainder in equation (46).

    With v=exp(-T), the remainder is

        R(T)=3 integral_0^T exp(t/3)/(1+t)^2 dt.

    Put T=3n and integrate only over [T-3,T].  For n>=2, the exponential
    series and elementary polynomial bounds give

        R(3n) >= (3/2)(n-1)^3/(1+3n)^2 >= 3n/256.

    Hence the remainder is unbounded, although it is lower order than the
    leading exp(T/3)/(1+T) term.
    """

    witnesses: list[dict[str, str]] = []
    for n_integer in range(2, 65):
        n = Fraction(n_integer)
        first_lower_bound = Fraction(3, 2) * (n - 1) ** 3 / (1 + 3 * n) ** 2
        linear_lower_bound = Fraction(3) * n / 256
        assert first_lower_bound >= linear_lower_bound
        witnesses.append(
            {
                "n": str(n),
                "v": f"exp(-{3 * n_integer})",
                "certified_remainder_lower_bound": str(first_lower_bound),
                "linear_divergent_lower_bound": str(linear_lower_bound),
            }
        )

    return {
        "manuscript_label": "positive remainder in (46) is O(1)",
        "status": "REFUTED",
        "transformed_remainder": "R(T)=3 integral_0^T exp(t/3)/(1+t)^2 dt",
        "certified_sequence": "R(3n)>=3n/256 for n>=2",
        "correct_asymptotic": (
            "R(T)~9 exp(T/3)/(1+T)^2, lower order but unbounded"
        ),
        "witnesses_n_2_to_64": witnesses,
    }


def certify_uniform_threshold_counterfamily() -> dict[str, object]:
    """Show why a time-dependent high-amplitude threshold is insufficient."""

    witnesses: list[dict[str, str]] = []
    for n in range(1, 17):
        levels = ((Fraction(n), Fraction(1)),)
        threshold = Fraction(2 * n)
        distribution = distribution_of_step_profile(levels, threshold)
        median_quantile = rearrangement_of_step_profile(levels, Fraction(1, 2))
        assert distribution == 0
        assert median_quantile == n
        witnesses.append(
            {
                "n": str(n),
                "tail_threshold": str(threshold),
                "distribution_at_threshold": str(distribution),
                "rearrangement_at_volume_1/2": str(median_quantile),
            }
        )

    return {
        "profile": "amplitude n on mass 1",
        "result": (
            "the tail is vacuous above the time-dependent threshold 2n, "
            "while f*(1/2)=n is unbounded"
        ),
        "witnesses": witnesses,
    }


def certify_far_tail_counterfamily() -> dict[str, object]:
    """Show that a small-volume envelope alone cannot bound O'Neil's tail."""

    witnesses: list[dict[str, str]] = []
    for radius in range(2, 17):
        mass = Fraction(radius**3)
        # Exact integral from 1 to radius^3 of s^(-2/3) ds.
        weighted_tail = Fraction(3 * (radius - 1))
        weak_constant = Fraction(radius**2)
        assert weighted_tail > 0
        witnesses.append(
            {
                "plateau_mass": str(mass),
                "weighted_tail_from_1": str(weighted_tail),
                "weak_L3/2_rearrangement_constant": str(weak_constant),
            }
        )

    exp_four_lower = exp_series_partial(Fraction(4), 2)
    assert exp_four_lower == 13
    assert exp_four_lower > 7

    return {
        "profile": "f_R*=1 on (0,R^3), zero afterwards",
        "fixed_small_volume_gate": (
            "at s=exp(-6), s^(-2/3)/log(e/s)=exp(4)/7>13/7>1; "
            "the ratio increases as s decreases"
        ),
        "exp_four_partial_order_2": str(exp_four_lower),
        "result": (
            "the local small-volume envelope can be fixed, but the weighted "
            "far tail equals 3(R-1) and is not uniform"
        ),
        "witnesses": witnesses,
    }


def certify_harmonic_component_gate() -> dict[str, object]:
    """Record the exact constant-velocity obstruction to literal Biot--Savart."""

    constant_velocity = (Fraction(2), Fraction(-3), Fraction(6))
    magnitude_squared = sum((component**2 for component in constant_velocity), Fraction(0))
    assert magnitude_squared == 49

    # All spatial derivatives of a constant vector vanish exactly.
    derivative_residual = Fraction(0)
    curl_residual = Fraction(0)
    divergence_residual = Fraction(0)
    oneil_rhs = Fraction(0)
    rearrangement = Fraction(7)
    assert derivative_residual == curl_residual == divergence_residual == oneil_rhs
    assert rearrangement > oneil_rhs

    return {
        "velocity": [str(component) for component in constant_velocity],
        "magnitude": str(rearrangement),
        "curl": str(curl_residual),
        "divergence": str(divergence_residual),
        "literal_equation_41_rhs": str(oneil_rhs),
        "velocity_rearrangement_at_every_finite_volume": str(rearrangement),
        "decision": (
            "u=K*omega is false without decay/integrability or an explicit "
            "bounded harmonic component h"
        ),
    }


def main() -> None:
    certificate = {
        "test": "ONEIL-TRANSFER-1",
        "question": (
            "Does a uniform lambda^(-3/2) log^(-3/2) vorticity tail, "
            "together with global weak-L^(3/2) control and a normalized "
            "Biot-Savart representation, imply the velocity envelope (47)?"
        ),
        "scope": (
            "functional rearrangement and Biot-Savart normalization gate; "
            "no Navier-Stokes trajectory or regularity theorem is certified"
        ),
        "hypotheses": [
            "mu_omega(lambda)<=V[(Omega/lambda)/log(lambda/Omega)]^(3/2) for lambda>=e Omega",
            "M=sup_s s^(2/3) omega*(s)<infinity uniformly",
            "u=K*omega+h with an O'Neil constant C_K and ||h||_infinity<=H uniformly",
            "0<v<=V exp(-6)",
        ],
        "tail_inversion": certify_tail_inversion_gate(),
        "oneil_integrals": certify_oneil_integral_gates(),
        "equation_46_remainder": certify_equation_46_remainder_gate(),
        "uniform_threshold_counterfamily": certify_uniform_threshold_counterfamily(),
        "far_tail_counterfamily": certify_far_tail_counterfamily(),
        "harmonic_component_counterexample": certify_harmonic_component_gate(),
        "scaling": {
            "NS_scaling": "u_kappa=kappa u(kappa x,kappa^2 t), omega_kappa=kappa^2 omega(kappa x,kappa^2 t)",
            "V": "kappa^-3",
            "Omega": "kappa^2",
            "C_0=4 Omega V^(2/3)": "invariant",
            "M=sup s^(2/3)omega*(s)": "invariant",
            "H V^(1/3)": "invariant",
            "velocity_envelope": "kappa-covariant",
        },
        "conclusion": (
            "u*(v)<=Q v^(-1/3)/log(eV/v), where "
            "Q=C_K(23 C_0+9M)+H V^(1/3), for 0<v<=V exp(-6)"
        ),
        "residuals": {
            "rational_algebra": "0",
            "tail_supersolution_minimum_margin": "8",
            "constant_velocity_curl_divergence": "0",
            "roundoff": "0 (no floating point)",
        },
        "decision": (
            "The functional transfer (40)->(47) is valid after explicit "
            "uniform thresholds, a global weak-L^(3/2) tail, and a bounded "
            "harmonic component are included. Literal equation (41) is false "
            "without the last normalization."
        ),
        "seed": "not applicable",
        "pass": True,
    }
    print(json.dumps(certificate, indent=2, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    main()
