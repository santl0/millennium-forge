#!/usr/bin/env python3
"""Exact SO(2) relative-rotation and hypothesis-boundary audit.

The script uses rational rotations, autonomous equivariant toy operators,
and exact residual countermodels.  It certifies abstract algebra only; none
of the finite-dimensional operators is the Navier--Stokes operator.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, left: object, right: object) -> None:
        self.assertions += 1
        assert left == right, (left, right)

    def true(self, statement: bool) -> None:
        self.assertions += 1
        assert statement


Vector = tuple[Q, Q, Q]
Matrix = tuple[tuple[Q, Q, Q], tuple[Q, Q, Q], tuple[Q, Q, Q]]


IDENTITY: Matrix = (
    (Q(1), Q(0), Q(0)),
    (Q(0), Q(1), Q(0)),
    (Q(0), Q(0), Q(1)),
)

GENERATOR: Matrix = (
    (Q(0), Q(-1), Q(0)),
    (Q(1), Q(0), Q(0)),
    (Q(0), Q(0), Q(0)),
)


def dot(left: Vector, right: Vector) -> Q:
    return sum((left[index] * right[index] for index in range(3)), Q(0))


def add(left: Vector, right: Vector) -> Vector:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def scale(coefficient: Q, vector: Vector) -> Vector:
    return tuple(coefficient * component for component in vector)  # type: ignore[return-value]


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((matrix[row][column] * vector[column] for column in range(3)), Q(0))
        for row in range(3)
    )  # type: ignore[return-value]


def matrix_product(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (left[row][middle] * right[middle][column] for middle in range(3)),
                Q(0),
            )
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[column][row] for column in range(3)) for row in range(3)
    )  # type: ignore[return-value]


def determinant(matrix: Matrix) -> Q:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def rational_rotation(parameter: Q) -> Matrix:
    denominator = 1 + parameter**2
    cosine = (1 - parameter**2) / denominator
    sine = 2 * parameter / denominator
    return (
        (cosine, -sine, Q(0)),
        (sine, cosine, Q(0)),
        (Q(0), Q(0), Q(1)),
    )


def rotation_from_pair(cosine: Q, sine: Q) -> Matrix:
    assert cosine**2 + sine**2 == 1
    return (
        (cosine, -sine, Q(0)),
        (sine, cosine, Q(0)),
        (Q(0), Q(0), Q(1)),
    )


def rotation_pair(matrix: Matrix) -> tuple[Q, Q]:
    return matrix[0][0], matrix[1][0]


def linear_angular_operator(angular_speed: Q, vector: Vector) -> Vector:
    return scale(-angular_speed, matrix_vector(GENERATOR, vector))


def polynomial_angular_operator(vector: Vector) -> Vector:
    return scale(-dot(vector, vector), matrix_vector(GENERATOR, vector))


def singular_angular_operator(vector: Vector) -> Vector:
    rotating_part = matrix_vector(GENERATOR, vector)
    rotating_norm_square = dot(rotating_part, rotating_part)
    assert rotating_norm_square > 0
    # The audit calls this operator only on vectors (1/n,0,0), for which the
    # norm is the rational 1/n.  Recover it exactly from the first coordinate.
    rotating_norm = abs(vector[0])
    assert rotating_norm**2 == rotating_norm_square
    return scale(Q(-1) / rotating_norm, rotating_part)


def reduction_residual(beta: Q, profile: Vector, operator_at_profile: Vector) -> Vector:
    return add(scale(beta, matrix_vector(GENERATOR, profile)), operator_at_profile)


def audit_so2_action(audit: Audit) -> None:
    parameters = (
        Q(-13, 5),
        Q(-3, 2),
        Q(-1),
        Q(-2, 3),
        Q(-1, 8),
        Q(0),
        Q(1, 8),
        Q(2, 3),
        Q(1),
        Q(3, 2),
        Q(13, 5),
    )
    vectors = (
        (Q(1), Q(0), Q(0)),
        (Q(0), Q(1), Q(0)),
        (Q(0), Q(0), Q(1)),
        (Q(2, 3), Q(-5, 7), Q(11, 13)),
    )

    rotations = [rational_rotation(parameter) for parameter in parameters]
    for rotation in rotations:
        audit.equal(matrix_product(transpose(rotation), rotation), IDENTITY)
        audit.equal(determinant(rotation), Q(1))
        audit.equal(matrix_product(rotation, GENERATOR), matrix_product(GENERATOR, rotation))
        for vector in vectors:
            audit.equal(dot(matrix_vector(rotation, vector), matrix_vector(rotation, vector)), dot(vector, vector))

    for left in rotations:
        for right in rotations:
            composition = matrix_product(left, right)
            cosine, sine = rotation_pair(composition)
            audit.equal(cosine**2 + sine**2, Q(1))
            audit.equal(composition, rotation_from_pair(cosine, sine))
            audit.equal(matrix_product(composition, GENERATOR), matrix_product(GENERATOR, composition))


def audit_equivariance_and_reduction(audit: Audit) -> None:
    rotations = [rational_rotation(Q(value, 7)) for value in range(-6, 7)]
    profiles = (
        (Q(1), Q(0), Q(0)),
        (Q(2, 3), Q(-5, 7), Q(0)),
        (Q(3), Q(4), Q(5)),
    )
    angular_speeds = (Q(-5), Q(-2, 3), Q(0), Q(3, 5), Q(7))

    for rotation in rotations:
        for profile in profiles:
            for omega in angular_speeds:
                left = linear_angular_operator(omega, matrix_vector(rotation, profile))
                right = matrix_vector(rotation, linear_angular_operator(omega, profile))
                audit.equal(left, right)

            polynomial_left = polynomial_angular_operator(matrix_vector(rotation, profile))
            polynomial_right = matrix_vector(rotation, polynomial_angular_operator(profile))
            audit.equal(polynomial_left, polynomial_right)

    # Exact relative equilibrium: F(U)=-omega*R U and beta=omega.
    for profile in profiles:
        for omega in angular_speeds:
            operator_value = linear_angular_operator(omega, profile)
            audit.equal(reduction_residual(omega, profile, operator_value), (Q(0), Q(0), Q(0)))

            rotated_generator = matrix_vector(GENERATOR, profile)
            if dot(rotated_generator, rotated_generator) > 0:
                for beta in angular_speeds:
                    residual = reduction_residual(beta, profile, operator_value)
                    if beta == omega:
                        audit.equal(residual, (Q(0), Q(0), Q(0)))
                    else:
                        audit.true(dot(residual, residual) > 0)

    # Fixed-axis profile: R U=0.  The reduction requires F(U)=0 but places no
    # restriction on beta; the SO(2) orbit itself is stationary.
    fixed_profile = (Q(0), Q(0), Q(7, 5))
    audit.equal(matrix_vector(GENERATOR, fixed_profile), (Q(0), Q(0), Q(0)))
    for beta in angular_speeds:
        audit.equal(reduction_residual(beta, fixed_profile, (Q(0), Q(0), Q(0))), (Q(0), Q(0), Q(0)))
        for rotation in rotations:
            audit.equal(matrix_vector(rotation, fixed_profile), fixed_profile)


def audit_dichotomy(audit: Audit) -> None:
    profiles = (
        (Q(1), Q(0), Q(0)),
        (Q(2, 3), Q(-5, 7), Q(0)),
        (Q(3), Q(4), Q(5)),
    )
    beta_pairs = (
        (Q(-5), Q(7)),
        (Q(-2, 3), Q(3, 5)),
        (Q(0), Q(1)),
        (Q(13, 17), Q(13, 17)),
    )
    for profile in profiles:
        generator_profile = matrix_vector(GENERATOR, profile)
        for beta_one, beta_two in beta_pairs:
            difference = scale(beta_one - beta_two, generator_profile)
            audit.equal(
                difference,
                add(
                    reduction_residual(beta_one, profile, (Q(0), Q(0), Q(0))),
                    scale(
                        Q(-1),
                        reduction_residual(beta_two, profile, (Q(0), Q(0), Q(0))),
                    ),
                ),
            )
            if beta_one != beta_two:
                audit.true(dot(difference, difference) > 0)
            else:
                audit.equal(difference, (Q(0), Q(0), Q(0)))


def audit_nonautonomous_countermodel(audit: Audit) -> None:
    profile = (Q(2, 3), Q(-5, 7), Q(0))
    beta_samples = (Q(-8), Q(-3, 2), Q(0), Q(2, 3), Q(5), Q(21))
    previous_beta = None
    for beta in beta_samples:
        # F_s(x)=-beta(s) R x is equivariant for each s but not autonomous.
        time_dependent_operator_value = linear_angular_operator(beta, profile)
        audit.equal(
            reduction_residual(beta, profile, time_dependent_operator_value),
            (Q(0), Q(0), Q(0)),
        )
        if previous_beta is not None:
            audit.true(beta != previous_beta)
        previous_beta = beta


def audit_residual_countermodels(audit: Audit) -> None:
    unit_profile = (Q(1), Q(0), Q(0))
    beta_center = Q(7, 5)
    operator_value = linear_angular_operator(beta_center, unit_profile)

    # With ||R U||=1, residual epsilon permits beta oscillation of width
    # exactly 2 epsilon; it does not give exact constancy.
    for epsilon in (Q(1, 2), Q(1, 5), Q(1, 13), Q(1, 32), Q(1, 128), Q(1, 1024)):
        beta_plus = beta_center + epsilon
        beta_minus = beta_center - epsilon
        residual_plus = reduction_residual(beta_plus, unit_profile, operator_value)
        residual_minus = reduction_residual(beta_minus, unit_profile, operator_value)
        audit.equal(dot(residual_plus, residual_plus), epsilon**2)
        audit.equal(dot(residual_minus, residual_minus), epsilon**2)
        audit.equal(beta_plus - beta_minus, 2 * epsilon)

    # If ||R U_epsilon||=epsilon degenerates, two beta values separated by
    # two have residual epsilon.  No uniform approximate dichotomy survives.
    for epsilon in (Q(1, 2), Q(1, 5), Q(1, 13), Q(1, 32), Q(1, 128), Q(1, 1024)):
        profile = (epsilon, Q(0), Q(0))
        residual_plus = reduction_residual(Q(1), profile, (Q(0), Q(0), Q(0)))
        residual_minus = reduction_residual(Q(-1), profile, (Q(0), Q(0), Q(0)))
        audit.equal(dot(residual_plus, residual_plus), epsilon**2)
        audit.equal(dot(residual_minus, residual_minus), epsilon**2)
        audit.equal(Q(1) - Q(-1), Q(2))


def audit_unbounded_beta_and_degenerate_generator(audit: Audit) -> None:
    # Smooth autonomous equivariant polynomial F(U)=-||U||^2 R U.
    # Unbounded profiles U_n=n e_1 give exact beta_n=n^2 and no uniform beta.
    previous_beta = None
    for n in (1, 2, 3, 5, 8, 13, 32, 128):
        profile = (Q(n), Q(0), Q(0))
        beta = Q(n**2)
        operator_value = polynomial_angular_operator(profile)
        audit.equal(reduction_residual(beta, profile, operator_value), (Q(0), Q(0), Q(0)))
        if previous_beta is not None:
            audit.true(beta > previous_beta)
        previous_beta = beta

    # Bounded profiles approaching the fixed set with the autonomous but
    # singular equivariant F(U)=-R U/||R U||.  Here beta_n=n, ||R U_n||=1/n,
    # yet beta_n R U_n=e_2 has unit size.
    previous_generator_square = None
    for n in (1, 2, 3, 5, 8, 13, 32, 128, 512, 2048):
        profile = (Q(1, n), Q(0), Q(0))
        beta = Q(n)
        generator_profile = matrix_vector(GENERATOR, profile)
        operator_value = singular_angular_operator(profile)
        audit.equal(reduction_residual(beta, profile, operator_value), (Q(0), Q(0), Q(0)))
        audit.equal(dot(generator_profile, generator_profile), Q(1, n**2))
        audit.equal(dot(scale(beta, generator_profile), scale(beta, generator_profile)), Q(1))
        if previous_generator_square is not None:
            audit.true(dot(generator_profile, generator_profile) < previous_generator_square)
        previous_generator_square = dot(generator_profile, generator_profile)


def main() -> None:
    audit = Audit()
    audit_so2_action(audit)
    audit_equivariance_and_reduction(audit)
    audit_dichotomy(audit)
    audit_nonautonomous_countermodel(audit)
    audit_residual_countermodels(audit)
    audit_unbounded_beta_and_degenerate_generator(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("relative_rotation_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("action=exact_rational_SO2_on_Q3_with_generator_R")
    print("reduction=beta(s)*R*U+F(U)=0_for_autonomous_equivariant_F")
    print("dichotomy=beta_constant_or_RU_zero_and_orbit_stationary")
    print("nonautonomous=time-dependent_equivariant_F_tracks_arbitrary_beta")
    print("residual=epsilon_gives_only_quantitative_beta_control_if_||RU||>=c")
    print("degeneracy=beta_unbounded_times_RU_vanishing_can_stay_order_one")
    print("scope=abstract_finite-dimensional_models; no Navier-Stokes claim")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
