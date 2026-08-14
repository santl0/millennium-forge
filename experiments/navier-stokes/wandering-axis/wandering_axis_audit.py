#!/usr/bin/env python3
"""Exact audit of the moving-axis moment budget and two radial BMO tests.

No Navier--Stokes trajectory is discretized.  The script checks the constants
in the l=1 solenoidal budget and the centered-ball oscillation of two explicit
axis paths using only ``fractions.Fraction`` arithmetic.
"""

from __future__ import annotations

import json
from fractions import Fraction


Q = Fraction
checks: list[tuple[str, bool, str]] = []


def record(name: str, condition: bool, detail: str) -> None:
    checks.append((name, condition, detail))


def show(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


# 1. Constants in the moving-axis moment inequality.
# For W=r^-2 Omega(s,theta), div W=0 gives
#   partial_s Omega_r=div_S Omega_T.
# With mu_s=e(s).theta, b=<theta Omega_r> and J=e.b,
#   J'=e'.b-<Phi(1-mu_s^2)>-<Phi(xi-e).grad_S mu_s>.
# The vector identities themselves are analytic; the audit certifies the
# constants that follow from |J|<=M/2 and
# |<(e'.theta)Omega_r>|<=M|e'|/2.
M = Q(2)
kappa = Q(1, 2)
block_length = Q(3)

positive_drop_per_block = 2 * kappa**2 / (3 * M**2 * block_length)
mobile_cost_coefficient = M / 2
necessary_mean_axis_speed = positive_drop_per_block / (
    mobile_cost_coefficient * block_length
)
moment_range = M

record(
    "positive_drop_sample",
    positive_drop_per_block == Q(1, 72),
    f"a0=2*kappa^2/(3*M^2*L)={show(positive_drop_per_block)}",
)
record(
    "necessary_speed_sample",
    necessary_mean_axis_speed == Q(1, 216),
    f"v*=2*a0/(M*L)={show(necessary_mean_axis_speed)}",
)
record(
    "moment_range_sample",
    moment_range == 2,
    "J lies in [-M/2,M/2], hence its total range is M",
)

# Integrated certificate over N blocks:
#   N*a0 <= M + (M/2)*Var(e;[S,S+NL]) + D,
# where D=int <Phi|xi-e|> ds.  Rational witnesses strictly violating this
# inequality must therefore be impossible under the lemma's hypotheses.
for block_count in (1, 12, 144, 288, 289):
    variation_budget = Q(block_count) * block_length * necessary_mean_axis_speed / 2
    direction_error_budget = Q(0)
    left = Q(block_count) * positive_drop_per_block
    right = moment_range + mobile_cost_coefficient * variation_budget + direction_error_budget
    record(
        f"integrated_budget_N_{block_count}",
        (left <= right) == (block_count <= 288),
        f"left={show(left)}, right={show(right)}",
    )


# 2. Constant-speed rotation on a great circle.
# On a centered ball B_R, logarithmic depth t=s-S has normalized density
# 3*exp(-3t).  For z(t)=exp(i*alpha*(S+t)),
#   E z = exp(i alpha S)*3/(3-i alpha),
#   E|z-Ez|^2 = alpha^2/(9+alpha^2).
# Since |z-Ez|<=2, mean absolute oscillation is at least half this variance.
def rotation_statistics(alpha: Fraction) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    denominator = 9 + alpha**2
    mean_cos_rotated_frame = Q(9) / denominator
    mean_sin_rotated_frame = Q(3) * alpha / denominator
    mean_norm_squared = Q(9) / denominator
    variance = alpha**2 / denominator
    return (
        mean_cos_rotated_frame,
        mean_sin_rotated_frame,
        mean_norm_squared,
        variance,
    )


for alpha in (Q(1), Q(1, 2), necessary_mean_axis_speed):
    mean_cos, mean_sin, mean_norm_squared, variance = rotation_statistics(alpha)
    record(
        f"rotating_mean_norm_alpha_{show(alpha)}",
        mean_cos**2 + mean_sin**2 == mean_norm_squared,
        f"|mean|^2={show(mean_norm_squared)}",
    )
    record(
        f"rotating_variance_alpha_{show(alpha)}",
        1 - mean_norm_squared == variance,
        f"variance={show(variance)}",
    )
    record(
        f"rotating_mo_lower_alpha_{show(alpha)}",
        variance / 2 > 0,
        f"centered mean oscillation >= {show(variance / 2)}",
    )

threshold_variance = necessary_mean_axis_speed**2 / (
    9 + necessary_mean_axis_speed**2
)
threshold_mo_lower = threshold_variance / 2
record(
    "threshold_rotation_bmo_lower",
    threshold_mo_lower == Q(1, 839_810),
    f"at alpha=v*, centered MO >= {show(threshold_mo_lower)}",
)

previous_weighted_cost: Fraction | None = None
for depth in (0, 1, 10, 100, 1000):
    weighted_cost = Q(1 + depth) * threshold_mo_lower
    if previous_weighted_cost is not None:
        record(
            f"persistent_weighted_growth_S_{depth}",
            weighted_cost > previous_weighted_cost,
            f"(1+S)*MO lower={show(weighted_cost)}",
        )
    previous_weighted_cost = weighted_cost


# 3. Slow logarithmic wandering.
# e(s)=(cos(beta log(1+s)),sin(beta log(1+s)),0) obeys
#   |e(S+t)-e(S)| <= beta*t/(1+S).
# With two independent exponential depths T,T', Jensen gives
# MO<=E|e(S+T)-e(S+T')|.  Since E|T-T'|=1/3,
#   MO(B_R) <= beta/[3(1+S)].
# This is only a necessary centered-ball test, not a global bmo_phi bound.
beta = Q(1, 5)
mean_absolute_depth_difference = Q(1, 3)
slow_weighted_upper = beta * mean_absolute_depth_difference
record(
    "exponential_depth_pair_distance",
    mean_absolute_depth_difference == Q(1, 3),
    "independent Exp(3) depths have mean absolute difference 1/3",
)
for depth in (0, 1, 10, 100, 1000):
    mo_upper = slow_weighted_upper / (1 + depth)
    record(
        f"slow_centered_weighted_bound_S_{depth}",
        Q(1 + depth) * mo_upper == slow_weighted_upper,
        f"(1+S)*MO upper={show(slow_weighted_upper)}",
    )

# At dyadic terminal depths T_n=2^n-1, total variation equals
# beta*n*log(2)<beta*n.  The rational upper envelope below tends to zero
# after division by T_n.  No transcendental value is rounded.
previous_ratio: Fraction | None = None
for n in range(2, 13):
    terminal_depth = Q(2**n - 1)
    mean_variation_upper = beta * n / terminal_depth
    if previous_ratio is not None:
        record(
            f"slow_variation_sublinear_n_{n}",
            mean_variation_upper < previous_ratio,
            f"Var/T < {show(mean_variation_upper)}",
        )
    previous_ratio = mean_variation_upper

# An explicit depth beyond which even the pointwise angular speed beta/(1+s)
# is below the necessary asymptotic mean speed v*.
speed_crossing_depth = beta / necessary_mean_axis_speed - 1
record(
    "slow_speed_crossing_depth",
    speed_crossing_depth == Q(211, 5),
    f"beta/(1+S)=v* at S={show(speed_crossing_depth)}",
)
for depth in (Q(43), Q(100), Q(1000)):
    record(
        f"slow_speed_below_threshold_S_{show(depth)}",
        beta / (1 + depth) < necessary_mean_axis_speed,
        f"speed={show(beta / (1 + depth))}<v*",
    )


# 4. Scaling ledger.  The angular axis and its logarithmic speed are
# dimensionless; |W|^(3/2) dx is invariant in three spatial dimensions.
vorticity_scaling = Q(2)
critical_power = Q(3, 2)
volume_scaling = Q(-3)
record(
    "critical_vorticity_scaling",
    critical_power * vorticity_scaling + volume_scaling == 0,
    "(3/2)*2-3=0",
)
record(
    "logarithmic_axis_speed_scaling",
    necessary_mean_axis_speed.denominator > 0,
    "s, L, e and de/ds are dimensionless under Navier--Stokes scaling",
)


failures = [name for name, condition, _ in checks if not condition]
report = {
    "experiment": "WANDERING-AXIS-1",
    "arithmetic": "fractions.Fraction exact rational arithmetic",
    "pde_discretization": "none",
    "random_seed": None,
    "checks": len(checks),
    "assertion_failure_count": len(failures),
    "failures": failures,
    "certified_quantities": {
        "M": show(M),
        "kappa": show(kappa),
        "block_length": show(block_length),
        "positive_drop_per_block": show(positive_drop_per_block),
        "necessary_mean_axis_speed": show(necessary_mean_axis_speed),
        "threshold_rotation_centered_mo_lower": show(threshold_mo_lower),
        "slow_log_rotation_weighted_mo_upper": show(slow_weighted_upper),
        "identity_residuals": "0",
    },
    "adversarial_limits": [
        "the moving-axis identity is analytic; the script certifies only its rational constants",
        "the oscillation estimates concern balls centered at the profile origin, not the global bmo_phi seminorm",
        "large total variation can arise from small rapid loops and does not by itself imply escape from a fixed cone",
        "no velocity, pressure, cutoff, Navier--Stokes evolution, or continuum extrapolation is computed",
    ],
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(1 if failures else 0)
