#!/usr/bin/env python3
"""Exact audit of the Lorentz cone-compensation gate.

No Navier--Stokes solution is computed.  Rational atomic models certify the
constant in the weak-L^(3/2) set and weighted estimates, the induced
cone/mean-oscillation bound under zero vector mean, and a two-amplitude family
showing that the cubic exponent is sharp at the measure-theoretic level.
"""

from __future__ import annotations

import json
from fractions import Fraction


Q = Fraction
checks: list[tuple[str, bool, str]] = []


def show(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def record(name: str, condition: bool, detail: str) -> None:
    checks.append((name, condition, detail))


def weak_l32_cube(weights: list[Fraction], magnitudes: list[Fraction]) -> Fraction:
    """Return K^3 for K=sup_lambda lambda |{f>lambda}|^(2/3)."""

    levels = sorted(set(magnitudes))
    return max(
        level**3
        * sum(weight for weight, value in zip(weights, magnitudes) if value >= level) ** 2
        for level in levels
        if level > 0
    )


def signed_direction_mo(weights: list[Fraction], values: list[Fraction]) -> Fraction:
    directions = [Q(1) if value > 0 else Q(-1) if value < 0 else Q(0) for value in values]
    mean = sum(weight * direction for weight, direction in zip(weights, directions))
    return sum(weight * abs(direction - mean) for weight, direction in zip(weights, directions))


# 1. Exact scaling and Lorentz constant.  For p=3/2,
# integral_E f <= 3 K |E|^(1/3), hence (integral_E f)^3<=27 K^3 |E|.
record(
    "lorentz_integration_constant",
    Q(3, 2) / (Q(3, 2) - 1) == 3,
    "p/(p-1)=3 at p=3/2",
)
record(
    "critical_scaling_of_K",
    Q(-2) + Q(3) / Q(3, 2) == 0,
    "the weak-L^(3/2) vorticity quasinorm is scale invariant",
)
record(
    "critical_scaling_of_m3_over_volume",
    3 * (-2 + 3) - 3 == 0,
    "m scales like length, so m^3/|D| is invariant",
)


# Exhaustive subset audit on twelve deterministic atomic distributions.
for profile in range(1, 13):
    raw_weights = [Q(profile + j, 1) for j in range(1, 5)]
    total_weight = sum(raw_weights)
    weights = [weight / total_weight for weight in raw_weights]
    magnitudes = [Q((profile + 2 * j) ** 2, profile + j + 1) for j in range(1, 5)]
    k_cube = weak_l32_cube(weights, magnitudes)
    for mask in range(1, 1 << len(weights)):
        set_measure = sum(weights[j] for j in range(len(weights)) if mask & (1 << j))
        set_mass = sum(
            weights[j] * magnitudes[j]
            for j in range(len(weights))
            if mask & (1 << j)
        )
        record(
            f"lorentz_subset_profile_{profile}_mask_{mask}",
            set_mass**3 <= 27 * k_cube * set_measure,
            f"mass^3={show(set_mass**3)}, bound={show(27*k_cube*set_measure)}",
        )
    q_weights = [Q(profile + j, profile + 5) for j in range(1, 5)]
    weighted_mass = sum(
        weight * magnitude * q
        for weight, magnitude, q in zip(weights, magnitudes, q_weights)
    )
    q_integral = sum(weight * q for weight, q in zip(weights, q_weights))
    record(
        f"lorentz_weighted_profile_{profile}",
        weighted_mass**3 <= 27 * k_cube * q_integral,
        f"weighted_mass^3={show(weighted_mass**3)}, bound={show(27*k_cube*q_integral)}",
    )


# 2. Cone compensation theorem in cubed form.
# If int_D W=0, G={xi.e>=alpha}, m=int_G|W| and N={xi.e<=0}, then
# The weighted negative projection q=(-xi.e)_+ satisfies
# int |W|q<=3K(int q)^(1/3).  Cancellation gives int |W|q>=alpha*m,
# and balance of positive/negative deviations then forces
# MO_D(zeta)>=2*alpha^3*m^3/(27*K^3*|D|).
alpha = Q(3, 4)
k_cube_demo = Q(125, 8)
conical_mass_demo = Q(5, 7)
domain_volume_demo = Q(11, 6)
cone_lower_demo = (
    2 * alpha**3 * conical_mass_demo**3
    / (27 * k_cube_demo * domain_volume_demo)
)
record(
    "cone_bound_positive",
    cone_lower_demo > 0,
    f"sample scale-invariant lower bound={show(cone_lower_demo)}",
)


# Deterministic signed profiles with exact zero mean test the final inequality.
for positive_weight_numerator in range(2, 18):
    positive_weight = Q(positive_weight_numerator, 20)
    negative_weight = 1 - positive_weight
    positive_amplitude = Q(20 - positive_weight_numerator, positive_weight_numerator + 3)
    negative_amplitude = positive_weight * positive_amplitude / negative_weight
    weights = [positive_weight, negative_weight]
    values = [positive_amplitude, -negative_amplitude]
    magnitudes = [abs(value) for value in values]
    k_cube = weak_l32_cube(weights, magnitudes)
    conical_mass = positive_weight * positive_amplitude
    mean_residual = sum(weight * value for weight, value in zip(weights, values))
    direction_mo = signed_direction_mo(weights, values)
    theorem_lower = 2 * conical_mass**3 / (27 * k_cube)
    record(
        f"signed_zero_mean_{positive_weight_numerator}",
        mean_residual == 0,
        "weighted vector mean is exactly zero",
    )
    record(
        f"signed_cone_bound_{positive_weight_numerator}",
        direction_mo >= theorem_lower,
        f"MO={show(direction_mo)}, lower={show(theorem_lower)}",
    )


# 3. Sharp two-amplitude family.
# epsilon=n^-3, W=a_n e on 1-epsilon and W=-n^2 e on epsilon,
# a_n=n^2/(n^3-1).  Then mean W=0, K=1, conical L1 mass=1/n,
# direction MO=4 epsilon(1-epsilon)~4m^3, and the negative phase alone has
# critical L^(3/2) mass exactly one.
first_n = 2
last_n = 64
for n in range(first_n, last_n + 1):
    epsilon = Q(1, n**3)
    positive_fraction = 1 - epsilon
    positive_amplitude = Q(n**2, n**3 - 1)
    negative_amplitude = Q(n**2)
    weights = [positive_fraction, epsilon]
    values = [positive_amplitude, -negative_amplitude]
    magnitudes = [positive_amplitude, negative_amplitude]
    mean_residual = sum(weight * value for weight, value in zip(weights, values))
    k_cube = weak_l32_cube(weights, magnitudes)
    conical_mass = positive_fraction * positive_amplitude
    direction_mo = signed_direction_mo(weights, values)
    theorem_lower = 2 * conical_mass**3 / (27 * k_cube)
    cubic_ratio = direction_mo / conical_mass**3
    negative_critical_mass = n**3 * epsilon

    record(
        f"sharp_mean_zero_{n}",
        mean_residual == 0,
        "positive and negative vector moments cancel exactly",
    )
    record(
        f"sharp_weak_norm_{n}",
        k_cube == 1,
        "K^3=1 exactly",
    )
    record(
        f"sharp_conical_mass_{n}",
        conical_mass == Q(1, n),
        f"m={show(conical_mass)}",
    )
    record(
        f"sharp_direction_mo_{n}",
        direction_mo == 4 * epsilon * (1 - epsilon),
        f"MO={show(direction_mo)}",
    )
    record(
        f"sharp_cone_bound_{n}",
        direction_mo >= theorem_lower,
        f"lower={show(theorem_lower)}",
    )
    record(
        f"sharp_cubic_exponent_{n}",
        cubic_ratio == 4 * (1 - epsilon),
        f"MO/m^3={show(cubic_ratio)}",
    )
    record(
        f"sharp_critical_mass_{n}",
        negative_critical_mass == 1 and positive_amplitude <= 1,
        "negative L^(3/2) mass is one and total mass lies in [1,2]",
    )


# A simple spatial realization with a regular interface does not inherit its
# small domain-average MO locally: a half-ball with directions +/-e has MO=1.
record(
    "regular_interface_local_mo",
    signed_direction_mo([Q(1, 2), Q(1, 2)], [Q(1), Q(-1)]) == 1,
    "a resolved two-phase interface has order-one local oscillation",
)


failures = [name for name, condition, _detail in checks if not condition]
report = {
    "experiment": "LORENTZ-CONE-COMPENSATION-1",
    "arithmetic": "fractions.Fraction exact rational arithmetic",
    "pde_discretization": "none",
    "random_seed": None,
    "checks": len(checks),
    "assertion_failure_count": len(failures),
    "failures": failures,
    "certified_quantities": {
        "lorentz_set_constant": "3",
        "weighted_lorentz_constant": "3",
        "cone_MO_constant": "2/27",
        "cone_power_in_alpha": "3",
        "sharp_family_epsilon": "n^-3",
        "sharp_family_weak_L32_K": "1",
        "sharp_family_conical_L1_mass": "1/n",
        "sharp_family_direction_MO": "4 n^-3 (1-n^-3)",
        "sharp_family_negative_L32_mass": "1",
        "identity_residuals": "0",
    },
    "adversarial_limits": [
        "the cone theorem is measure-theoretic and uses zero vector mean; it does not construct a compact curl",
        "without zero mean the canonical bound uses the negative projected mass nu_e explicitly",
        "the two-amplitude sharp family has no spatial arrangement, divergence constraint, velocity, pressure, or evolution",
        "a regular interface between the two phases has order-one local BMO despite small whole-domain oscillation",
        "critical L^(3/2) mass does not give a lower bound for the conical L1 mass",
        "a log-BMO-compatible lift would require a nested non-Dini transition across additional subscales",
    ],
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(1 if failures else 0)
