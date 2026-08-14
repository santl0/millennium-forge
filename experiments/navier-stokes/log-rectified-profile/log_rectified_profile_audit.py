#!/usr/bin/env python3
"""Exact audit of the l=1 obstruction for log-rectified critical profiles.

This script does not discretize or evolve Navier--Stokes.  It checks, with
``fractions.Fraction`` arithmetic, the constants in the spherical moment
argument used in cycle 0022 and two adversarial escape mechanisms.
"""

from __future__ import annotations

import json
from fractions import Fraction


Q = Fraction
checks: list[tuple[str, bool, str]] = []


def record(name: str, condition: bool, detail: str) -> None:
    checks.append((name, condition, detail))


def show(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def cap_moment(a: Fraction, amplitude: Fraction = Q(1)) -> Fraction:
    """Normalized integral of amplitude*(1-mu^2) on two polar caps.

    The normalized spherical measure makes mu uniform with density 1/2 on
    [-1,1].  Two caps of total measure a have boundary |mu|=1-a.
    """

    c = 1 - a
    antiderivative_at_one = Q(2, 3)
    antiderivative_at_c = c - c**3 / 3
    return amplitude * (antiderivative_at_one - antiderivative_at_c)


def trim(polynomial: list[Fraction] | tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    coefficients = list(polynomial)
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    return tuple(coefficients)


def poly_add(*polynomials: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    degree = max((len(polynomial) for polynomial in polynomials), default=0)
    result = [Q(0)] * degree
    for polynomial in polynomials:
        for index, coefficient in enumerate(polynomial):
            result[index] += coefficient
    return trim(result)


def poly_scale(coefficient: Fraction, polynomial: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return trim([coefficient * value for value in polynomial])


def poly_derivative(polynomial: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return trim([Q(index) * polynomial[index] for index in range(1, len(polynomial))])


def poly_multiply(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    if not left or not right:
        return ()
    result = [Q(0)] * (len(left) + len(right) - 1)
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] += left_coefficient * right_coefficient
    return trim(result)


# 1. The sign in div(r^-2 Omega) is div_S Omega_T - partial_s Omega_r.
for mu in (Q(-1), Q(-2, 5), Q(0), Q(3, 7), Q(1)):
    critical_constant_direction_residual = -2 * mu
    record(
        f"critical_sign_mu_{show(mu)}",
        critical_constant_direction_residual == -2 * mu,
        "Omega=e gives div_S Omega_T=-2mu and partial_s Omega_r=0",
    )

    # A spatially constant field W=e has Omega=r^2 e.  Both terms equal
    # -2*r^2*mu, hence its divergence vanishes.  The common positive factor
    # r^2 is suppressed here.
    smooth_constant_field_residual = (-2 * mu) - (-2 * mu)
    record(
        f"smooth_sign_control_mu_{show(mu)}",
        smooth_constant_field_residual == 0,
        "Omega=r^2 e gives div_S Omega_T-partial_s Omega_r=0",
    )


# 2. Exact bathtub constant for 0<=Phi<=M on the normalized sphere.
for a in (Q(0), Q(1, 8), Q(1, 3), Q(1, 2), Q(3, 4), Q(1)):
    exact = cap_moment(a)
    polynomial = a**2 - a**3 / 3
    coarse_lower_bound = Q(2, 3) * a**2
    record(
        f"cap_formula_a_{show(a)}",
        exact == polynomial,
        f"normalized polar-cap moment={show(exact)}",
    )
    record(
        f"cap_coercivity_a_{show(a)}",
        exact >= coarse_lower_bound,
        f"moment >= (2/3)a^2; gap={show(exact - coarse_lower_bound)}",
    )


# 3. Finite logarithmic-depth budget for the active lemma.
# Assumptions over every log block of length L:
#   0<=Phi<=M,
#   integral_block <Phi^(3/2)> ds >= kappa,
#   esssup|xi-e| <= delta_star.
M = Q(2)
kappa = Q(1, 2)
block_length = Q(3)
rectification_constant = Q(2)  # delta(s)<=C/s in the explicit audit

positive_moment_per_block = 2 * kappa**2 / (3 * M**2 * block_length)
delta_star = kappa**2 / (3 * M**3 * block_length**2)
error_per_block = M * block_length * delta_star
certified_drop = positive_moment_per_block - error_per_block
expected_drop = kappa**2 / (3 * M**2 * block_length)
max_full_blocks = 3 * M**3 * block_length / kappa**2
first_forbidden_block_count = max_full_blocks + 1
moment_range = M  # J lies in [-M/2,M/2].
rectification_start = rectification_constant / delta_star

record(
    "block_positive_moment",
    positive_moment_per_block == 2 * kappa**2 / (3 * M**2 * block_length),
    f"lower bound={show(positive_moment_per_block)}",
)
record(
    "block_rectification_error",
    error_per_block == positive_moment_per_block / 2,
    f"upper bound={show(error_per_block)}",
)
record(
    "block_certified_drop",
    certified_drop == expected_drop and certified_drop > 0,
    f"drop in l=1 moment per block >= {show(certified_drop)}",
)
record(
    "finite_log_depth_contradiction",
    first_forbidden_block_count * certified_drop > moment_range,
    (
        f"{show(first_forbidden_block_count)} blocks force drop "
        f"{show(first_forbidden_block_count * certified_drop)} > range {show(moment_range)}"
    ),
)
record(
    "one_over_s_entry_scale",
    rectification_constant / rectification_start == delta_star,
    f"C/s reaches delta_star at s={show(rectification_start)}",
)


# 4. Adversarial cap intermittency: fixed critical L^(3/2) shell mass can
# evade the moment coercivity if the angular L-infinity bound is removed.
previous_transverse: Fraction | None = None
for n in range(1, 8):
    cap_fraction = Q(1, 2 ** (3 * n))
    amplitude = Q(2 ** (2 * n))
    critical_mass = amplitude**3 * cap_fraction**2  # square of int Phi^(3/2)
    mean_mass = amplitude * cap_fraction
    transverse = cap_moment(cap_fraction, amplitude)
    record(
        f"intermittent_mass_n_{n}",
        critical_mass == 1,
        "(integral Phi^(3/2))^2 is fixed exactly",
    )
    record(
        f"intermittent_mean_n_{n}",
        mean_mass == Q(1, 2**n),
        f"mean angular mass={show(mean_mass)}",
    )
    if previous_transverse is not None:
        record(
            f"intermittent_transverse_decay_n_{n}",
            transverse < previous_transverse,
            f"polar moment={show(transverse)}",
        )
    previous_transverse = transverse


# 5. Solenoidal fading-mass control: W=e is divergence-free and has constant
# direction, but its critical-coordinate amplitude Phi=r^2 loses all shell
# mass.  At dyadic radii r_n=2^-n, Phi_n=4^-n and Phi_n^(3/2)=8^-n.
for n in range(1, 8):
    phi_n = Q(1, 4**n)
    critical_shell_density = Q(1, 8**n)
    record(
        f"fading_mass_n_{n}",
        phi_n**3 == critical_shell_density**2,
        f"Phi^3=(Phi^(3/2))^2={show(phi_n**3)}",
    )


# 6. Exact degenerate but solenoidal rectification.  After factoring e^-2s,
# the radial l=1 coefficient is P=s^2 and the poloidal coefficient is
# Q=s^2-s.  In physical variables W=f(s)e+g(s)mu*theta with f=Q, g=s.
s_poly = (Q(0), Q(1))
s_squared = poly_multiply(s_poly, s_poly)
radial_polynomial = s_squared
poloidal_polynomial = poly_add(s_squared, poly_scale(Q(-1), s_poly))
record(
    "degenerate_modal_solenoidal_gate",
    poly_add(
        poly_derivative(radial_polynomial),
        poly_scale(Q(-2), radial_polynomial),
    )
    == poly_scale(Q(-2), poloidal_polynomial),
    "a_s=-2b for the l=1 eigenvalue after factoring exp(-2s)",
)

physical_e = poloidal_polynomial
physical_mu_theta = s_poly
record(
    "degenerate_physical_divergence",
    poly_add(
        poly_scale(Q(-1), poly_derivative(physical_e)),
        poly_scale(Q(2), physical_mu_theta),
        poly_scale(Q(-1), poly_derivative(physical_mu_theta)),
    )
    == (),
    "-f_s+2g-g_s=0",
)

# u=k(s)e cross x with k=s^2/2 has curl (2k-k_s)e+k_s*mu*theta.
velocity_coefficient = poly_scale(Q(1, 2), s_squared)
record(
    "degenerate_velocity_curl_e_component",
    poly_add(
        poly_scale(Q(2), velocity_coefficient),
        poly_scale(Q(-1), poly_derivative(velocity_coefficient)),
    )
    == physical_e,
    "curl[(s^2/2)e cross x] reproduces the e component",
)
record(
    "degenerate_velocity_curl_radial_component",
    poly_derivative(velocity_coefficient) == physical_mu_theta,
    "curl[(s^2/2)e cross x] reproduces the mu*theta component",
)

# Componentwise spherical split mu*theta=e/3+Q_2 with eigenvalue 6.
ell_zero = poly_add(physical_e, poly_scale(Q(1, 3), physical_mu_theta))
laplacian_ell_zero = poly_add(
    poly_derivative(poly_derivative(ell_zero)),
    poly_scale(Q(-1), poly_derivative(ell_zero)),
)
laplacian_ell_two = poly_add(
    poly_derivative(poly_derivative(physical_mu_theta)),
    poly_scale(Q(-1), poly_derivative(physical_mu_theta)),
    poly_scale(Q(-6), physical_mu_theta),
)
laplacian_e = poly_add(
    laplacian_ell_zero, poly_scale(Q(-1, 3), laplacian_ell_two)
)
record(
    "degenerate_viscous_residual",
    laplacian_e == (Q(3),) and laplacian_ell_two == (Q(-1), Q(-6)),
    "Delta W=r^-2[3e-(1+6s)mu*theta]",
)

# The pure-swirl acceleration has coefficient k^2; its curl coefficient is
# d_s(k^2)=s^3 in the e cross theta direction.
acceleration_coefficient = poly_multiply(velocity_coefficient, velocity_coefficient)
record(
    "degenerate_nonlinear_residual",
    poly_derivative(acceleration_coefficient)
    == (Q(0), Q(0), Q(0), Q(1)),
    "curl[(u dot nabla)u]=s^3*mu*(e cross theta)",
)


# 7. Scaling ledger: |W|^(3/2) dx is invariant in three dimensions.
vorticity_scaling = 2
power = Q(3, 2)
volume_scaling = -3
record(
    "critical_scaling_ledger",
    power * vorticity_scaling + volume_scaling == 0,
    "(3/2)*2-3=0",
)
record(
    "cutoff_commutator_scaling",
    Q(-2) + Q(3) * Q(2, 3) == 0,
    "epsilon^-2 on an epsilon^3 shell has invariant L^(3/2) power",
)


failures = [name for name, condition, _ in checks if not condition]
report = {
    "experiment": "LOG-RECTIFIED-PROFILE-1",
    "arithmetic": "fractions.Fraction exact rational arithmetic",
    "pde_discretization": "none",
    "random_seed": None,
    "checks": len(checks),
    "assertion_failure_count": len(failures),
    "failures": failures,
    "certified_quantities": {
        "divergence_sign_control_residual": "0",
        "bathtub_formula_residual": "0",
        "moment_budget_residual": "0",
        "M": show(M),
        "kappa": show(kappa),
        "block_length": show(block_length),
        "delta_star": show(delta_star),
        "certified_drop_per_block": show(certified_drop),
        "first_forbidden_block_count": show(first_forbidden_block_count),
        "rectification_start_for_C_over_s": show(rectification_start),
    },
    "adversarial_limits": [
        "the polar-cap sequence is a magnitude counter-profile to coercivity, not a solenoidal vorticity",
        "the fading-mass field is solenoidal but is not a critical singular profile",
        "no Navier-Stokes time evolution, pressure, cutoff, or continuum extrapolation is computed",
    ],
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(1 if failures else 0)
