#!/usr/bin/env python3
"""Exact rational audit of a canonical Hilbert phase decomposition.

The certificate checks finite-dimensional inner-product identities and two
countermodels.  It contains no Navier--Stokes PDE solution or continuum proof.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path


Vector = tuple[Q, ...]
Vector3 = tuple[Q, Q, Q]


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, left: object, right: object) -> None:
        self.assertions += 1
        assert left == right, (left, right)

    def true(self, statement: bool) -> None:
        self.assertions += 1
        assert statement


def dot(left: Vector, right: Vector) -> Q:
    assert len(left) == len(right)
    return sum((left[index] * right[index] for index in range(len(left))), Q(0))


def add(left: Vector, right: Vector) -> Vector:
    assert len(left) == len(right)
    return tuple(left[index] + right[index] for index in range(len(left)))


def subtract(left: Vector, right: Vector) -> Vector:
    assert len(left) == len(right)
    return tuple(left[index] - right[index] for index in range(len(left)))


def scale(coefficient: Q, vector: Vector) -> Vector:
    return tuple(coefficient * value for value in vector)


def norm_square(vector: Vector) -> Q:
    return dot(vector, vector)


def canonical_phase(derivative: Vector, tangent: Vector) -> tuple[Q, Vector]:
    gram = norm_square(tangent)
    if gram == 0:
        raise ZeroDivisionError("canonical phase is undefined on ker R")
    beta = dot(derivative, tangent) / gram
    residual = subtract(derivative, scale(beta, tangent))
    return beta, residual


def audit_decomposition(
    audit: Audit,
    derivative: Vector,
    tangent: Vector,
    competitors: tuple[Q, ...],
) -> tuple[Q, Vector]:
    beta, residual = canonical_phase(derivative, tangent)
    gram = norm_square(tangent)
    beta_tangent = scale(beta, tangent)

    audit.equal(beta, dot(derivative, tangent) / gram)
    audit.equal(dot(residual, tangent), Q(0))
    audit.equal(add(beta_tangent, residual), derivative)
    audit.equal(
        norm_square(derivative),
        norm_square(beta_tangent) + norm_square(residual),
    )
    audit.true(norm_square(beta_tangent) <= norm_square(derivative))

    for competitor in competitors:
        competitor_residual = subtract(derivative, scale(competitor, tangent))
        audit.equal(
            norm_square(competitor_residual),
            norm_square(residual) + (competitor - beta) ** 2 * gram,
        )
        audit.true(norm_square(residual) <= norm_square(competitor_residual))
    return beta, residual


def audit_rational_grids(audit: Audit) -> None:
    for dimension in range(2, 7):
        for denominator in range(2, 14):
            for offset in range(5):
                tangent = tuple(
                    Q((index + 1) * (offset + 2) - denominator, denominator + index + 1)
                    for index in range(dimension)
                )
                # The final coordinate prevents a zero Gram vector.
                tangent = tangent[:-1] + (tangent[-1] + Q(1, denominator),)
                derivative = tuple(
                    Q((index + 2) * (denominator - offset) - 3, denominator + 2 * index + 1)
                    for index in range(dimension)
                )
                audit.true(norm_square(tangent) > 0)
                beta, _ = canonical_phase(derivative, tangent)
                competitors = (
                    Q(0),
                    Q(1),
                    Q(-1),
                    beta + Q(1, denominator),
                    beta - Q(2, denominator + 1),
                )
                audit_decomposition(audit, derivative, tangent, competitors)


def audit_degenerate_gram(audit: Audit) -> None:
    transverse: Vector3 = (Q(0), Q(2, 3), Q(-3, 5))
    previous_gram = None
    previous_beta = None
    previous_perturbation = None
    for scale_index in range(1, 11):
        n = 2**scale_index
        epsilon = Q(1, n)
        tangent: Vector3 = (epsilon, Q(0), Q(0))
        tangential_derivative: Vector3 = (Q(1), Q(0), Q(0))
        derivative = add(tangential_derivative, transverse)
        beta, residual = audit_decomposition(
            audit,
            derivative,
            tangent,
            (Q(0), Q(n - 1), Q(n + 1)),
        )

        gram = norm_square(tangent)
        audit.equal(gram, Q(1, n**2))
        audit.equal(beta, Q(n))
        audit.equal(residual, transverse)
        audit.equal(scale(beta, tangent), tangential_derivative)

        # A tangential perturbation of norm epsilon changes beta by exactly 1.
        perturbation: Vector3 = (epsilon, Q(0), Q(0))
        perturbed_derivative = add(derivative, perturbation)
        perturbed_beta, perturbed_residual = canonical_phase(perturbed_derivative, tangent)
        audit.equal(norm_square(perturbation), Q(1, n**2))
        audit.equal(perturbed_beta - beta, Q(1))
        audit.equal(perturbed_residual, transverse)

        if previous_gram is not None:
            audit.true(gram < previous_gram)
        if previous_beta is not None:
            audit.true(beta > previous_beta)
        if previous_perturbation is not None:
            audit.true(norm_square(perturbation) < previous_perturbation)
        previous_gram = gram
        previous_beta = beta
        previous_perturbation = norm_square(perturbation)


def rotation_generator(vector: Vector3) -> Vector3:
    fixed, x_value, y_value = vector
    del fixed
    return Q(0), -y_value, x_value


def quarter_rotation(quarter_index: int, vector: Vector3) -> Vector3:
    fixed, x_value, y_value = vector
    phase = quarter_index % 4
    if phase == 0:
        return fixed, x_value, y_value
    if phase == 1:
        return fixed, -y_value, x_value
    if phase == 2:
        return fixed, -x_value, -y_value
    return fixed, y_value, -x_value


def haar_projection(vector: Vector3) -> Vector3:
    return vector[0], Q(0), Q(0)


def audit_so2_kernel_drift(audit: Audit) -> None:
    # H=ker(R) direct-sum the rotating plane.  The exact smooth model behind
    # the algebraic samples is Z_N(s)=s*e0+epsilon_N*Q_{N*s}e1 for the
    # standard radian-parametrized SO(2) action.  The Fraction certificate
    # samples rational heights and the four rational quarter-turn states
    # independently; it does not discretize the transcendental time orbit.
    previous_gram = None
    previous_beta = None
    for scale_index in range(1, 8):
        n = 2**scale_index
        epsilon = Q(1, n**2)
        expected_gram = epsilon**2
        expected_rotating_derivative_square = Q(1, n**2)

        for height_index in range(4 * n + 1):
            height = Q(height_index, 4 * n)
            for phase_index in range(4):
                rotating_profile: Vector3 = (Q(0), epsilon, Q(0))
                rotated = quarter_rotation(phase_index, rotating_profile)
                profile: Vector3 = (height, rotated[1], rotated[2])
                tangent = rotation_generator(profile)
                fixed_drift: Vector3 = (Q(1), Q(0), Q(0))
                derivative = add(fixed_drift, scale(Q(n), tangent))
                beta, residual = canonical_phase(derivative, tangent)

                audit.equal(norm_square(tangent), expected_gram)
                audit.equal(beta, Q(n))
                audit.equal(residual, fixed_drift)
                audit.equal(dot(residual, tangent), Q(0))
                audit.equal(haar_projection(residual), fixed_drift)
                audit.equal(haar_projection(derivative), fixed_drift)
                audit.equal(haar_projection(profile), (height, Q(0), Q(0)))
                audit.equal(
                    norm_square(scale(beta, tangent)),
                    expected_rotating_derivative_square,
                )

        start_profile: Vector3 = (Q(0), epsilon, Q(0))
        end_profile: Vector3 = (Q(1), epsilon, Q(0))
        audit.equal(
            subtract(haar_projection(end_profile), haar_projection(start_profile)),
            (Q(1), Q(0), Q(0)),
        )
        if previous_gram is not None:
            audit.true(expected_gram < previous_gram)
        if previous_beta is not None:
            audit.true(Q(n) > previous_beta)
        previous_gram = expected_gram
        previous_beta = Q(n)


def audit_zero_gram_gate(audit: Audit) -> None:
    derivative: Vector3 = (Q(1), Q(2), Q(3))
    tangent: Vector3 = (Q(0), Q(0), Q(0))
    try:
        canonical_phase(derivative, tangent)
    except ZeroDivisionError:
        audit.true(True)
    else:
        raise AssertionError("zero Gram must make the canonical phase undefined")


def main() -> None:
    audit = Audit()
    audit_rational_grids(audit)
    audit_degenerate_gram(audit)
    audit_so2_kernel_drift(audit)
    audit_zero_gram_gate(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("canonical_phase_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("projection=beta=(d_dot_g)/(g_dot_g)_and_r=d-beta*g")
    print("orthogonality=r_dot_g=0_and_Pythagoras_exact")
    print("contraction=||beta*g||<=||d||")
    print("degenerate_Gram=g=epsilon*e1_beta=1/epsilon_transverse_residual_fixed")
    print("SO2=beta_to_infinity_g_to_zero_but_Haar(r)=e0")
    print("zero_Gram=canonical_beta_undefined")
    print("seed=n/a; arithmetic=Fraction; no Navier-Stokes PDE claim")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
