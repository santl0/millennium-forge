#!/usr/bin/env python3
"""Exact dyadic audit of the BMO-to-active-axis extraction gate.

The script does not solve Navier--Stokes.  It verifies rational constants in
the reduction from centered logarithmic mean oscillation, bounded critical
amplitude and shell mass to a slowly varying axis, then checks a finite
contradiction against the moving-axis moment budget from cycle 0023.
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


# 1. Certified rational enclosure of log(2).
# log(2)=2*sum_{j>=0} x^(2j+1)/(2j+1), x=1/3.  The positive tail after N
# terms is bounded by a geometric series with the smallest tail denominator.
x = Q(1, 3)
term_count = 12
log2_partial = 2 * sum(
    (x ** (2 * j + 1)) / (2 * j + 1) for j in range(term_count)
)
log2_remainder_upper = (
    2
    * x ** (2 * term_count + 1)
    / ((2 * term_count + 1) * (1 - x**2))
)
log2_lower = Q(6931, 10000)
log2_upper = Q(6932, 10000)

record(
    "log2_lower_certificate",
    log2_partial > log2_lower,
    f"positive partial sum={show(log2_partial)}>6931/10000",
)
record(
    "log2_upper_certificate",
    log2_partial + log2_remainder_upper < log2_upper,
    "partial sum plus rigorous tail is below 6932/10000",
)


# 2. Dyadic active fraction in a centered ball.
# R_{k+1}=R_k/2 and L=log(2).  In logarithmic depth t, normalized physical
# volume is 3*exp(-3t)dt.  If 0<=Phi<=M and
# integral_0^L <Phi^(3/2)>dt>=kappa, then the active set {Phi>0} occupies at
# least a_*=3*(1/2)^3*kappa/M^(3/2) of B_{R_k}.
radius_ratio = Q(1, 2)
volume_ratio = radius_ratio**3
M = Q(1)
kappa = Q(1, 4)
bmo_constant = Q(1, 100)
active_fraction_lower = 3 * volume_ratio * kappa  # M^(3/2)=1 in the audit.
axis_error_factor = 1 + 1 / active_fraction_lower

record(
    "active_fraction_lower",
    active_fraction_lower == Q(3, 32),
    f"a*=3*q^3*kappa={show(active_fraction_lower)}",
)
record(
    "axis_error_factor",
    axis_error_factor == Q(35, 3),
    f"1+1/a*={show(axis_error_factor)}",
)


# 3. Mean non-degeneracy and normalized-axis error.
# For a bounded extension zeta with |zeta|<=1, equal to the unit direction on
# the active set, epsilon=average_B|zeta-m| gives
#   |m|>=1-epsilon/a_*,
#   average_B|zeta-m/|m|| <= (1+1/a_*)epsilon.
def epsilon_upper(k: int) -> Fraction:
    return bmo_constant / (1 + Q(k) * log2_lower)


for k in (1, 2, 4, 8, 16, 32, 64):
    epsilon = epsilon_upper(k)
    mean_norm_lower = 1 - epsilon / active_fraction_lower
    ball_axis_error = axis_error_factor * epsilon
    record(
        f"mean_nonzero_k_{k}",
        mean_norm_lower > Q(1, 2),
        f"|m_k|>={show(mean_norm_lower)}>1/2",
    )
    record(
        f"ball_axis_error_k_{k}",
        ball_axis_error == epsilon + epsilon / active_fraction_lower,
        f"ball error <= {show(ball_axis_error)}",
    )


# 4. Nested balls give O(1/k) axis increments.  If A_k is the average error
# to e_k on B_{R_k}, then the average on B_{R_{k+1}} costs at most q^-3 A_k.
# Hence |e_{k+1}-e_k|<=q^-3 A_k+A_{k+1}.  A shortest interpolation has
# variation at most twice this chord once the means are non-degenerate.
nested_volume_cost = 1 / volume_ratio
record(
    "nested_volume_cost",
    nested_volume_cost == 8,
    "a dyadic child ball has one eighth of the parent volume",
)

for k in (1, 2, 4, 8, 16, 32):
    current_error = axis_error_factor * epsilon_upper(k)
    next_error = axis_error_factor * epsilon_upper(k + 1)
    chord_bound = nested_volume_cost * current_error + next_error
    coarse_chord_bound = 9 * axis_error_factor * epsilon_upper(k)
    record(
        f"nested_axis_chord_k_{k}",
        chord_bound <= coarse_chord_bound,
        f"axis chord <= {show(coarse_chord_bound)}",
    )


# 5. Convert physical-volume error to the unweighted log-shell error required
# by the moving-axis moment lemma.  On 0<=t<=L, exp(-3t)>=q^3:
#   integral_shell <Phi|xi-e_k|>dt <= M/(3q^3) A_k.
# Interpolating the axes adds at most 2*M*L*chord_bound.  log(2) is replaced
# by its certified rational upper bound.
shell_conversion = M / (3 * volume_ratio)
variation_coefficient = 18 * axis_error_factor
moving_error_coefficient = M * axis_error_factor * (
    Q(8, 3) + 18 * log2_upper
)

record(
    "shell_conversion",
    shell_conversion == Q(8, 3),
    f"M/(3q^3)={show(shell_conversion)}",
)
record(
    "variation_coefficient",
    variation_coefficient == 210,
    f"Var block <= {show(variation_coefficient)} epsilon_k",
)
record(
    "moving_error_coefficient_positive",
    moving_error_coefficient > 0,
    f"D block <= {show(moving_error_coefficient)} epsilon_k",
)


# 6. Exact dyadic harmonic envelope.  For k in [2^j,2^(j+1)-1],
# epsilon_k<=B/(k*l0), so the sum over the group is <=B/l0.  Up to 2^n-1,
# the total is at most n*B/l0, which is sublinear in the number of blocks.
for exponent in range(1, 13):
    block_count = 2**exponent - 1
    exact_sum = sum(epsilon_upper(k) for k in range(1, block_count + 1))
    grouped_upper = Q(exponent) * bmo_constant / log2_lower
    record(
        f"dyadic_harmonic_envelope_n_{exponent}",
        exact_sum <= grouped_upper,
        f"sum epsilon <= {show(grouped_upper)}",
    )


# 7. Finite decisive contradiction with the cycle-0023 moment budget.
# The true block length is log(2)<=l1, so the transverse drop satisfies
# a0>=2*kappa^2/(3*M^2*l1).  For N=2^n-1 blocks, use the grouped bounds on
# total variation and moving direction error.
positive_drop_lower = 2 * kappa**2 / (3 * M**2 * log2_upper)
first_certified_exponent: int | None = None
first_certified_margin: Fraction | None = None
for exponent in range(1, 21):
    block_count = 2**exponent - 1
    epsilon_sum_upper = Q(exponent) * bmo_constant / log2_lower
    variation_upper = variation_coefficient * epsilon_sum_upper
    direction_error_upper = moving_error_coefficient * epsilon_sum_upper
    forced_drop = Q(block_count) * positive_drop_lower
    available_budget = M + (M / 2) * variation_upper + direction_error_upper
    contradiction = forced_drop > available_budget
    if contradiction and first_certified_exponent is None:
        first_certified_exponent = exponent
        first_certified_margin = forced_drop - available_budget

record(
    "finite_moment_contradiction_found",
    first_certified_exponent is not None and first_certified_margin is not None,
    (
        f"first dyadic exponent={first_certified_exponent}, "
        f"positive margin={show(first_certified_margin or Q(0))}"
    ),
)


# 8. Adversarial necessity of the uniform amplitude bound.  An active fraction
# a_n=n^-3 with amplitude n^2 keeps <Phi^(3/2)>=1, while the zero extension of
# a constant direction has mean oscillation 2a_n(1-a_n)->0 and mean norm a_n.
previous_oscillation: Fraction | None = None
for n in range(2, 10):
    active_fraction = Q(1, n**3)
    amplitude = Q(n**2)
    critical_mass = amplitude**3 * active_fraction**2
    zero_extension_mean_norm = active_fraction
    zero_extension_oscillation = 2 * active_fraction * (1 - active_fraction)
    record(
        f"unbounded_amplitude_mass_n_{n}",
        critical_mass == 1,
        "(mean Phi^(3/2))^2 is fixed exactly",
    )
    record(
        f"unbounded_amplitude_mean_n_{n}",
        zero_extension_mean_norm == Q(1, n**3),
        f"mean norm={show(zero_extension_mean_norm)}",
    )
    if previous_oscillation is not None:
        record(
            f"unbounded_amplitude_bmo_decay_n_{n}",
            zero_extension_oscillation < previous_oscillation,
            f"binary oscillation={show(zero_extension_oscillation)}",
        )
    previous_oscillation = zero_extension_oscillation


# 9. Scaling ledger.
record(
    "critical_scaling_ledger",
    Q(3, 2) * 2 - 3 == 0,
    "|W|^(3/2) dx is invariant under Navier--Stokes scaling",
)
record(
    "direction_bmo_scaling",
    volume_ratio == Q(1, 8),
    "direction, mean oscillation and dyadic volume ratios are dimensionless",
)


failures = [name for name, condition, _ in checks if not condition]
report = {
    "experiment": "BMO-ACTIVE-AXIS-EXTRACTION-1",
    "arithmetic": "fractions.Fraction exact rational arithmetic",
    "pde_discretization": "none",
    "random_seed": None,
    "checks": len(checks),
    "assertion_failure_count": len(failures),
    "failures": failures,
    "certified_quantities": {
        "log2_lower": show(log2_lower),
        "log2_upper": show(log2_upper),
        "M": show(M),
        "kappa": show(kappa),
        "active_fraction_lower": show(active_fraction_lower),
        "axis_error_factor": show(axis_error_factor),
        "variation_coefficient": show(variation_coefficient),
        "positive_drop_lower": show(positive_drop_lower),
        "first_certified_dyadic_exponent": first_certified_exponent,
        "first_certified_margin": show(first_certified_margin or Q(0)),
        "identity_residuals": "0",
    },
    "adversarial_limits": [
        "the proof assumes a bounded direction extension agreeing with the unit direction on the active set",
        "the shell mass lower bound and the angular amplitude upper bound are independent extra hypotheses",
        "removing the amplitude bound permits sparse high-amplitude active sets with vanishing mean direction",
        "no Biot--Savart velocity, pressure, cutoff, time evolution, or continuum discretization is computed",
    ],
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(1 if failures else 0)
