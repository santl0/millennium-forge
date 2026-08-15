#!/usr/bin/env python3
"""Exact audit of Bochner bounds in abstract fast-rotation models.

All calculations use Fraction.  The models are finite-dimensional or
piecewise-constant-in-time identities; they are not Navier--Stokes solutions
and do not certify any PDE regularity or blow-up statement.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path


Vector = tuple[Q, ...]


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, left: object, right: object) -> None:
        self.assertions += 1
        assert left == right, (left, right)

    def true(self, statement: bool) -> None:
        self.assertions += 1
        assert statement


def add(left: Vector, right: Vector) -> Vector:
    assert len(left) == len(right)
    return tuple(left[index] + right[index] for index in range(len(left)))


def subtract(left: Vector, right: Vector) -> Vector:
    assert len(left) == len(right)
    return tuple(left[index] - right[index] for index in range(len(left)))


def scale(coefficient: Q, vector: Vector) -> Vector:
    return tuple(coefficient * value for value in vector)


def l1_norm(vector: Vector) -> Q:
    return sum((abs(value) for value in vector), Q(0))


def weighted_l1(weights: tuple[Q, ...], values: tuple[Vector, ...]) -> Q:
    assert len(weights) == len(values)
    return sum(
        (weights[index] * l1_norm(values[index]) for index in range(len(values))),
        Q(0),
    )


def audit_positive_bochner_estimate(audit: Audit) -> None:
    # Exact L1 test of
    # ||RZ|| <= inf|beta|^-1 (||d_s Z|| + ||r||).
    # The analytic Lp statement follows from the same pointwise lower bound
    # and Minkowski; no irrational p-th roots are introduced here.
    weights = tuple(Q(index + 1, 36) for index in range(8))
    audit.equal(sum(weights, Q(0)), Q(1))
    previous_rz_norm = None
    for scale_index in range(1, 9):
        n = 2**scale_index
        beta_values = tuple(Q(n + index % 3) for index in range(8))
        rz_values = tuple(
            (
                Q((index % 3) - 1, n),
                Q((index % 4) - 2, 2 * n),
                Q((index % 5) - 2, 3 * n),
            )
            for index in range(8)
        )
        residual_values = tuple(
            (Q((-1) ** index, 5), Q(index % 2, 7), Q(-1, 11))
            for index in range(8)
        )
        derivative_values = tuple(
            add(scale(beta_values[index], rz_values[index]), residual_values[index])
            for index in range(8)
        )
        beta_floor = min(abs(beta) for beta in beta_values)
        audit.equal(beta_floor, Q(n))

        for index in range(8):
            difference = subtract(derivative_values[index], residual_values[index])
            audit.equal(difference, scale(beta_values[index], rz_values[index]))
            audit.true(
                l1_norm(rz_values[index])
                <= Q(1, beta_floor)
                * (
                    l1_norm(derivative_values[index])
                    + l1_norm(residual_values[index])
                )
            )

        rz_norm = weighted_l1(weights, rz_values)
        derivative_norm = weighted_l1(weights, derivative_values)
        residual_norm = weighted_l1(weights, residual_values)
        estimate_rhs = Q(1, beta_floor) * (derivative_norm + residual_norm)
        audit.true(rz_norm <= estimate_rhs)
        audit.true(derivative_norm < Q(6))
        audit.true(residual_norm < Q(1))
        audit.true(estimate_rhs < Q(7, n))
        if previous_rz_norm is not None:
            audit.true(rz_norm < previous_rz_norm)
        previous_rz_norm = rz_norm


def audit_nonaxisymmetric_stroboscopy(audit: Audit) -> None:
    # Period-one unitary orbit with ||U||=||RU||=1 and RU != 0.
    # N^2 positive-speed cycles fill [0,1].  Z_N approaches U in every finite
    # Lp, while ||RZ_N||_L1=1 and ||d_s Z_N||_L1=N^2.
    previous_orbit_bounds: dict[int, Q] = {}
    previous_derivative_l1 = None
    for scale_index in range(1, 9):
        n = 2**scale_index
        denominator = n**2 + n + 1
        angular_window = Q(n + 1, denominator)
        slow_measure = Q(n**2 + n, denominator)
        fast_measure = Q(1, denominator)
        slow_beta = Q(n)
        fast_beta = Q(n**4)

        audit.equal(slow_measure + fast_measure, Q(1))
        audit.true(angular_window < Q(1, n))
        audit.true(fast_measure < Q(1, n**2))
        audit.equal(max(Q(1, slow_beta), Q(1, fast_beta)), Q(1, n))

        derivative_l1 = slow_measure * slow_beta + fast_measure * fast_beta
        rz_l1 = slow_measure + fast_measure
        audit.equal(derivative_l1, Q(n**2))
        audit.equal(rz_l1, Q(1))
        audit.equal(Q(1, n) * derivative_l1, Q(n))

        for exponent in range(1, 7):
            orbit_lp_power_bound = (
                slow_measure * angular_window**exponent
                + fast_measure * Q(2) ** exponent
            )
            derivative_lp_power = (
                slow_measure * slow_beta**exponent
                + fast_measure * fast_beta**exponent
            )
            audit.true(
                orbit_lp_power_bound
                < Q(1, n**exponent) + Q(2**exponent, n**2)
            )
            audit.true(derivative_lp_power >= derivative_l1**exponent)
            if exponent in previous_orbit_bounds:
                audit.true(orbit_lp_power_bound < previous_orbit_bounds[exponent])
            previous_orbit_bounds[exponent] = orbit_lp_power_bound

        if previous_derivative_l1 is not None:
            audit.true(derivative_l1 > previous_derivative_l1)
        previous_derivative_l1 = derivative_l1


def audit_large_term_compensation(audit: Audit) -> None:
    previous_uniform_derivative = None
    previous_normalized_derivative = None
    for scale_index in range(1, 11):
        n = Q(2**scale_index)
        beta = n

        # Family A: the unnormalized difference is exactly one, although both
        # terms diverge quadratically.  Thus a bound on d_s Z-r gives no bound
        # on either summand separately.
        uniform_rz = Q(1, n)
        uniform_derivative = n**2
        uniform_residual = n**2 - 1
        audit.equal(uniform_derivative - uniform_residual, Q(1))
        audit.equal(beta * uniform_rz, Q(1))

        # Family B: the normalized difference (d_s Z-r)/beta is exactly one.
        # This does not imply collapse when the difference itself grows like
        # beta, and again neither summand has a uniform Bochner bound.
        normalized_rz = Q(1)
        normalized_derivative = n**2
        normalized_residual = n**2 - n
        normalized_difference = normalized_derivative - normalized_residual
        audit.equal(normalized_difference, beta * normalized_rz)
        audit.equal(normalized_difference / beta, Q(1))

        audit.true(uniform_derivative > Q(1))
        audit.true(uniform_residual > Q(1))
        audit.true(normalized_derivative > Q(1))
        audit.true(normalized_residual >= Q(0))
        if previous_uniform_derivative is not None:
            audit.true(uniform_derivative > previous_uniform_derivative)
        if previous_normalized_derivative is not None:
            audit.true(normalized_derivative > previous_normalized_derivative)
        previous_uniform_derivative = uniform_derivative
        previous_normalized_derivative = normalized_derivative


Vector3 = tuple[Q, Q, Q]


def rotation_generator(vector: Vector3) -> Vector3:
    return -vector[1], vector[0], Q(0)


def audit_degenerate_stabilizer(audit: Audit) -> None:
    # Z(s)=(0,0,1+s) lies in the rotation stabilizer.  Its derivative and the
    # residual are both e3, so d_s Z-r=beta RZ=0 for every beta.
    derivative: Vector3 = (Q(0), Q(0), Q(1))
    residual: Vector3 = (Q(0), Q(0), Q(1))
    zero: Vector3 = (Q(0), Q(0), Q(0))
    sample_times = (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1))
    rz_values = tuple(
        rotation_generator((Q(0), Q(0), Q(1) + time))
        for time in sample_times
    )
    for rz in rz_values:
        audit.equal(rz, zero)
    audit.equal(subtract(derivative, residual), zero)

    for n in (2, 4, 16, 256, 65536):
        speeds = (Q(0), Q(n), Q(n**4), Q(-n))
        for beta in speeds:
            for rz in rz_values:
                audit.equal(scale(beta, rz), subtract(derivative, residual))
        audit.true(len(set(speeds)) == 4)


def main() -> None:
    audit = Audit()
    audit_positive_bochner_estimate(audit)
    audit_nonaxisymmetric_stroboscopy(audit)
    audit_large_term_compensation(audit)
    audit_degenerate_stabilizer(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("bochner_rotation_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("positive_L1=Bochner_estimate_verified_pointwise_and_on_weighted_grid")
    print("stroboscopic=Z_N_to_nonaxisymmetric_U_in_finite_Lp")
    print("stroboscopic_derivative=||d_s_Z_N||_L1=N^2_while_||RZ_N||_L1=1")
    print("compensation_A=d_s_Z=N^2_r=N^2-1_difference=1")
    print("compensation_B=(d_s_Z-r)/beta=1_without_collapse")
    print("stabilizer=RZ=0_makes_beta_nonidentifiable")
    print("seed=n/a; arithmetic=Fraction; no Navier-Stokes PDE claim")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
