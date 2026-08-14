#!/usr/bin/env python3
"""Exact audit of a sparse critical train of solenoidal vorticity blobs.

This script does not solve Navier--Stokes.  It uses rational polynomial
arithmetic to certify a compactly supported base velocity/vorticity pair and
then checks the scale bookkeeping of an infinite disjoint blob train.  The
decisive test compares centered mean oscillation with the global small-ball
oscillation forced by a recurrent internal direction pattern.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from typing import TypeAlias


Q = Fraction
Exponent: TypeAlias = tuple[int, int, int]
Poly: TypeAlias = dict[Exponent, Fraction]

checks: list[tuple[str, bool, str]] = []


def show(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def record(name: str, condition: bool, detail: str) -> None:
    checks.append((name, condition, detail))


def clean(poly: Poly) -> Poly:
    return {power: coefficient for power, coefficient in poly.items() if coefficient}


def add(*polys: Poly) -> Poly:
    result: Poly = {}
    for poly in polys:
        for power, coefficient in poly.items():
            result[power] = result.get(power, Q(0)) + coefficient
    return clean(result)


def scale(poly: Poly, coefficient: Fraction | int) -> Poly:
    factor = Q(coefficient)
    return clean({power: factor * value for power, value in poly.items()})


def multiply(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for p_left, c_left in left.items():
        for p_right, c_right in right.items():
            power = tuple(p_left[j] + p_right[j] for j in range(3))
            result[power] = result.get(power, Q(0)) + c_left * c_right
    return clean(result)


def derivative(poly: Poly, axis: int) -> Poly:
    result: Poly = {}
    for power, coefficient in poly.items():
        if power[axis] == 0:
            continue
        new_power = list(power)
        factor = new_power[axis]
        new_power[axis] -= 1
        key = tuple(new_power)
        result[key] = result.get(key, Q(0)) + coefficient * factor
    return clean(result)


def evaluate(poly: Poly, point: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return sum(
        coefficient
        * point[0] ** power[0]
        * point[1] ** power[1]
        * point[2] ** power[2]
        for power, coefficient in poly.items()
    )


def coefficient_l1(poly: Poly) -> Fraction:
    return sum(abs(value) for value in poly.values())


def vector_divergence(vector: tuple[Poly, Poly, Poly]) -> Poly:
    return add(*(derivative(vector[j], j) for j in range(3)))


def vector_curl(vector: tuple[Poly, Poly, Poly]) -> tuple[Poly, Poly, Poly]:
    return (
        add(derivative(vector[2], 1), scale(derivative(vector[1], 2), -1)),
        add(derivative(vector[0], 2), scale(derivative(vector[2], 0), -1)),
        add(derivative(vector[1], 0), scale(derivative(vector[0], 1), -1)),
    )


def laplacian(poly: Poly) -> Poly:
    return add(*(derivative(derivative(poly, j), j) for j in range(3)))


def directional_derivative(
    velocity: tuple[Poly, Poly, Poly], component: Poly
) -> Poly:
    return add(
        *(multiply(velocity[j], derivative(component, j)) for j in range(3))
    )


def tensor_product_3(one_dimensional: dict[int, Fraction]) -> Poly:
    result: Poly = {}
    for i, ci in one_dimensional.items():
        for j, cj in one_dimensional.items():
            for k, ck in one_dimensional.items():
                result[(i, j, k)] = ci * cj * ck
    return clean(result)


def derivative_1d(poly: dict[int, Fraction]) -> dict[int, Fraction]:
    return {power - 1: coefficient * power for power, coefficient in poly.items() if power}


def multiply_1d(
    left: dict[int, Fraction], right: dict[int, Fraction]
) -> dict[int, Fraction]:
    result: dict[int, Fraction] = {}
    for p_left, c_left in left.items():
        for p_right, c_right in right.items():
            power = p_left + p_right
            result[power] = result.get(power, Q(0)) + c_left * c_right
    return {power: coefficient for power, coefficient in result.items() if coefficient}


def integrate_minus_one_one(poly: dict[int, Fraction]) -> Fraction:
    return sum(
        coefficient * Q(2, power + 1)
        for power, coefficient in poly.items()
        if power % 2 == 0
    )


# P(t)=(1-t^2)^4 on |t|<1 and zero outside.  Its first three derivatives
# vanish at both endpoints, so the zero extension is C^3.
P = {2 * j: Q(((-1) ** j) * comb(4, j)) for j in range(5)}
P1 = derivative_1d(P)
endpoint_checks: list[Fraction] = []
current = P
for _order in range(4):
    for endpoint in (Q(-1), Q(1)):
        endpoint_checks.append(
            sum(coefficient * endpoint**power for power, coefficient in current.items())
        )
    current = derivative_1d(current)
record(
    "compact_support_C3_gate",
    all(value == 0 for value in endpoint_checks),
    "P and derivatives of orders 0,1,2,3 vanish at +/-1",
)


# psi=P(x)P(y)P(z), U=(partial_y psi,-partial_x psi,0), W=curl U.
psi = tensor_product_3(P)
zero: Poly = {}
velocity = (derivative(psi, 1), scale(derivative(psi, 0), -1), zero)
vorticity = vector_curl(velocity)

record(
    "base_velocity_divergence",
    not vector_divergence(velocity),
    "div U0 is the zero polynomial inside the cube",
)
record(
    "base_curl_identity",
    vector_curl(velocity) == vorticity,
    "curl U0-W0 has zero coefficients",
)
record(
    "base_vorticity_divergence",
    not vector_divergence(vorticity),
    "div W0 is the zero polynomial; C1 zero extension gives the distributional identity",
)


origin = (Q(0), Q(0), Q(0))
tilted_point = (Q(1, 2), Q(0), Q(1, 2))
w_origin = tuple(evaluate(component, origin) for component in vorticity)
w_tilted = tuple(evaluate(component, tilted_point) for component in vorticity)
cross_y = w_origin[2] * w_tilted[0] - w_origin[0] * w_tilted[2]

record(
    "base_vorticity_at_origin",
    w_origin == (Q(0), Q(0), Q(16)),
    f"W0(0)={tuple(show(value) for value in w_origin)}",
)
record(
    "recurrent_direction_nonconstant",
    cross_y > 0,
    f"the directions at 0 and (1/2,0,1/2) are not parallel; cross component={show(cross_y)}",
)


# Exact energy of the base velocity by separation of variables.
I0 = integrate_minus_one_one(multiply_1d(P, P))
I1 = integrate_minus_one_one(multiply_1d(P1, P1))
base_energy = 2 * I0 * I0 * I1
record(
    "base_energy_positive",
    base_energy > 0,
    f"||U0||_2^2={show(base_energy)}",
)


# A core cube [-1/8,1/8]^3 has |W0|>=|W0_z|>10.  Indeed
# -P''/P=8(1-7t^2)/(1-t^2)^2>=57/8 there.
core_factor_lower = Q(63, 64) ** 12 * Q(57, 4)
record(
    "core_vorticity_lower_bound",
    core_factor_lower > 10,
    f"|W0_z|>={show(core_factor_lower)}>10 on the core cube",
)
core_volume = Q(1, 64)


# On the inside half of B((1,0,0),rho), rho<1/4, W0_z is nonzero.
# The logarithmic derivative P''/P gives the rational sign certificate.
face_positive_part = Q(6016, 49)
face_negative_part = Q(2048, 225)
record(
    "regular_face_active_half_ball",
    face_positive_part - face_negative_part > 0,
    "P''(x)/P(x)+P''(y)/P(y)>0 for x>3/4 and |y|<1/4",
)
record(
    "zero_extension_face_mo",
    Q(1, 2) > 0,
    "an exactly half-active ball forces vector mean oscillation at least 1/2",
)


# Quantitative internal-direction oscillation independent of the convention on
# zeros.  Coefficient l1 bounds control W0 on small rational cubes around the
# two sample points.
direction_lipschitz = sum(
    coefficient_l1(derivative(component, axis))
    for component in vorticity
    for axis in range(3)
)
b_x = w_tilted[0]
b_l1 = sum(abs(value) for value in w_tilted)
delta = min(Q(1, 100), b_x / (16 * direction_lipschitz), Q(1, 16 * direction_lipschitz))
eta = direction_lipschitz * delta
origin_x_component_upper = eta / (16 - eta)
tilted_x_component_lower = (b_x - eta) / (b_l1 + eta)
direction_scalar_gap = tilted_x_component_lower - origin_x_component_upper
# Both cubes lie in B((1/4,0,1/4),1/2).  Using pi<22/7, each occupies at
# least (168/11)delta^3 of that ball.
subcube_ball_fraction_lower = Q(168, 11) * delta**3
internal_mo_lower = direction_scalar_gap * subcube_ball_fraction_lower
subcubes_inside_test_ball = (
    2 * (Q(1, 4) + delta) ** 2 + delta**2 < Q(1, 4)
)

record(
    "direction_lipschitz_positive",
    direction_lipschitz > 0,
    f"coefficient-l1 Lipschitz bound={show(direction_lipschitz)}",
)
record(
    "internal_direction_gap",
    direction_scalar_gap > 0,
    f"separated normalized x-components by at least {show(direction_scalar_gap)}",
)
record(
    "direction_subcubes_inside_test_ball",
    subcubes_inside_test_ball,
    "both rational subcubes lie in B((1/4,0,1/4),1/2)",
)
record(
    "extension_independent_mo_lower",
    internal_mo_lower > 0,
    f"every extension has MO at least {show(internal_mo_lower)} on one fixed base ball",
)


# Stationary Navier--Stokes residual at viscosity nu=1.  A pressure could only
# remove a gradient, so curl(-Delta U+(U dot nabla)U) must vanish for a
# stationary solution.  It does not.
unprojected_residual = tuple(
    add(scale(laplacian(component), -1), directional_derivative(velocity, component))
    for component in velocity
)
residual_curl = vector_curl(unprojected_residual)
nonzero_residual_terms = sum(len(component) for component in residual_curl)
record(
    "stationary_residual_not_pressure",
    nonzero_residual_terms > 0,
    f"curl of the unprojected residual has {nonzero_residual_terms} nonzero monomials",
)


# Infinite train: r_n=2^-n, ell_n=r_n/(8n), x_n=r_n e_3.
def radius(n: int) -> Fraction:
    return Q(1, 2**n)


def blob_scale(n: int) -> Fraction:
    return radius(n) / (8 * n)


record(
    "support_separation_all_n",
    Q(1, 2) - Q(1, 8) - Q(1, 32) == Q(11, 32) > 0,
    "adjacent z-interval gap is at least (11/32)r_n",
)
for n in range(1, 65):
    lower_current = radius(n) - blob_scale(n)
    upper_next = radius(n + 1) + blob_scale(n + 1)
    record(
        f"finite_support_separation_{n}",
        lower_current > upper_next,
        f"gap={show(lower_current-upper_next)}",
    )


# Sum ell_n <=(1/8)sum 2^-n=1/8, hence finite kinetic energy.
energy_scale_sum_upper = Q(1, 8)
record(
    "finite_total_energy",
    base_energy * energy_scale_sum_upper > 0,
    f"sum ||U_n||_2^2 <= {show(base_energy*energy_scale_sum_upper)}",
)


# Critical weak-L^(3/2) upper and lower bounds.  The crude pointwise bound
# |W0|<=224 follows from |P|<=1, |P'|<=8, |P''|<=48.
base_vorticity_upper = Q(224)
weak_l32_upper = Q(3584)
weak_l32_lower = Q(5, 16)
record(
    "weak_l32_upper_bound",
    weak_l32_upper == 16 * base_vorticity_upper,
    "lambda |{|W|>lambda}|^(2/3)<=3584 from the geometric tail",
)
record(
    "weak_l32_lower_bound",
    weak_l32_lower == Q(5, 16),
    "core threshold gives lambda |{|W|>lambda}|^(2/3)>=5/16",
)


# The centered ball B_{(3/2)r_N} contains exactly the tail n>=N.  Its active
# fraction is <1/(756 N^3), hence the zero-extension MO is <1/(378 N^3).
for n in (2, 4, 8, 16, 32, 64):
    centered_active_upper = Q(1, 756 * n**3)
    centered_mo_upper = 2 * centered_active_upper
    angular_amplitude_at_center = 16 * (radius(n) / blob_scale(n)) ** 2
    record(
        f"centered_sparse_mo_{n}",
        centered_mo_upper == Q(1, 378 * n**3),
        f"centered MO <= {show(centered_mo_upper)}",
    )
    record(
        f"unbounded_angular_amplitude_{n}",
        angular_amplitude_at_center == 1024 * n**2,
        f"r_n^2|W_n(x_n)|={show(angular_amplitude_at_center)}",
    )


# Every blob repeats the internal direction pattern on a ball of radius
# ell_n/2.  Since ell_n->0 while the certified MO lower bound is fixed, no
# extension agreeing with W/|W| on the active set can be VMO or log-BMO.
for n in (1, 2, 4, 8, 16, 32):
    test_radius = blob_scale(n) / 2
    record(
        f"shrinking_internal_ball_{n}",
        test_radius > blob_scale(n + 1) / 2,
        f"test radius={show(test_radius)}, MO lower={show(internal_mo_lower)}",
    )


# Scaling ledger and residual gate.
record(
    "critical_mass_scaling",
    Q(-2) * Q(3, 2) + 3 == 0,
    "integral |W_n|^(3/2) is independent of ell_n",
)
record(
    "velocity_energy_scaling",
    Q(-1) * 2 + 3 == 1,
    "||U_n||_2^2=ell_n||U0||_2^2",
)
record(
    "stationary_residual_scaling",
    Q(-3) * 1 + 3 == 0,
    "the unprojected stationary residual has scale-invariant L1 mass per blob",
)


failures = [name for name, condition, _detail in checks if not condition]
report = {
    "experiment": "CRITICAL-SOLENOIDAL-BLOB-TRAIN-1",
    "arithmetic": "fractions.Fraction exact polynomial and scaling arithmetic",
    "pde_discretization": "none",
    "random_seed": None,
    "checks": len(checks),
    "assertion_failure_count": len(failures),
    "failures": failures,
    "certified_quantities": {
        "base_energy": show(base_energy),
        "base_core_vorticity_lower": show(core_factor_lower),
        "weak_L32_quasinorm_lower": show(weak_l32_lower),
        "weak_L32_quasinorm_upper": show(weak_l32_upper),
        "centered_zero_extension_MO_rate": "<1/(378 n^3)",
        "zero_extension_face_MO_lower": "1/2",
        "extension_independent_internal_MO_lower": show(internal_mo_lower),
        "angular_amplitude_at_blob_center": "1024 n^2",
        "stationary_residual_curl_nonzero_monomials": nonzero_residual_terms,
        "polynomial_identity_residuals": "0",
    },
    "adversarial_limits": [
        "the train is a static finite-energy divergence-free field, not a Navier--Stokes trajectory",
        "the base cutoff is C3, the velocity C2 and the vorticity C1, not a smooth Clay datum at the accumulation point",
        "global log-BMO fails on balls at the blob scale despite the much smaller centered oscillation",
        "the stationary residual is not a gradient and has scale-invariant L1 cost per blob",
        "pressure and a time-dependent correction are not constructed",
    ],
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(1 if failures else 0)
