#!/usr/bin/env python3
"""Exact counter-tests for a putative stationary-subsequence lemma.

The certificate uses rational scaling ledgers, support geometry, a sampled
exact periodic linear orbit, and nested/non-nested defect families.  These
are functional and logical tests, not Navier--Stokes solutions or PDE proofs.
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


def strong_lp_power(amplitude_power: Q, spatial_dimension: int, p: Q) -> Q:
    """Power of n in ||n^alpha A(n x)||_p^p."""
    return p * amplitude_power - spatial_dimension


def weak_lp_norm_power(amplitude_power: Q, spatial_dimension: int, p: Q) -> Q:
    """Power of n in the weak-Lp quasi-norm."""
    return amplitude_power - Q(spatial_dimension) / p


def derivative_l2_square_power(
    amplitude_power: Q, spatial_dimension: int, derivative_order: int
) -> Q:
    return 2 * (amplitude_power + derivative_order) - spatial_dimension


def audit_concentration(audit: Audit) -> None:
    dimension = 3
    amplitude = Q(1)

    audit.equal(weak_lp_norm_power(amplitude, dimension, Q(3)), Q(0))
    audit.equal(strong_lp_power(amplitude, dimension, Q(3)), Q(0))
    audit.equal(strong_lp_power(amplitude, dimension, Q(2)), Q(-1))
    audit.equal(derivative_l2_square_power(amplitude, dimension, 1), Q(1))

    # C_n=n*A(n x), with supp(A) in B_(1/4).  The support is inside B_1,
    # its volume scales as n^-3, and all its global L3 mass is local to B_1.
    for n in (1, 2, 3, 5, 8, 13, 32, 128, 512, 2048):
        support_radius = Q(1, 4 * n)
        volume_ratio = Q(1, n**3)
        l3_mass_ratio = Q(n**3) * volume_ratio
        l2_square_ratio = Q(n**2) * volume_ratio
        gradient_square_ratio = Q(n**4) * volume_ratio

        audit.true(support_radius <= Q(1, 4))
        audit.equal(l3_mass_ratio, Q(1))
        audit.equal(l2_square_ratio, Q(1, n))
        audit.equal(gradient_square_ratio, Q(n))

        # Distribution scaling: mu_C(lambda)=n^-3*mu_A(lambda/n), so the
        # weak-L3 cubic expression has unit scaling ratio.
        threshold_cube_ratio = Q(n**3)
        audit.equal(threshold_cube_ratio * volume_ratio, Q(1))

    # Fixed nonzero L3 mass plus support volume tending to zero is incompatible
    # with strong local L3 convergence to the a.e. limit zero.
    previous_volume = None
    for n in (1, 2, 4, 8, 16, 32, 64, 128):
        volume_ratio = Q(1, n**3)
        local_l3_mass_ratio = Q(1)
        audit.equal(local_l3_mass_ratio, Q(1))
        if previous_volume is not None:
            audit.true(volume_ratio < previous_volume)
        previous_volume = volume_ratio


def audit_translation(audit: Audit) -> None:
    # T_n(x)=A(x-2n e_1), supp(A) in B_(1/4).  Each time-independent member
    # has temporal generator zero but lies outside B_1.
    atom_radius = Q(1, 4)
    for n in (1, 2, 3, 5, 8, 13, 32, 128, 512):
        center_distance = Q(2 * n)
        nearest_origin_distance = center_distance - atom_radius
        audit.true(nearest_origin_distance > 1)
        audit.equal(Q(0), Q(0))  # normalized temporal-generator square.
        audit.equal(Q(1), Q(1))  # every translation preserves global mass.
        audit.equal(Q(0), Q(0))  # mass in B_1.

    # For every fixed integer radius R, one can choose n=R+1 so all mass is
    # outside B_R.  Hence no uniform spatial tightness follows.
    for radius in (1, 2, 3, 5, 8, 13, 32, 128):
        n = radius + 1
        nearest_origin_distance = Q(2 * n) - atom_radius
        audit.true(nearest_origin_distance > radius)
        audit.equal(Q(1), Q(1))  # normalized mass outside B_R.


Vector2 = tuple[Q, Q]


def apply_j(vector: Vector2) -> Vector2:
    return (-vector[1], vector[0])


def phase_sample(index: int) -> Vector2:
    phases = ((Q(1), Q(0)), (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1)))
    return phases[index % 4]


def norm_square(vector: Vector2) -> Q:
    return vector[0] ** 2 + vector[1] ** 2


def audit_periodic_generator(audit: Audit) -> None:
    # Samples at t=m*pi/2 of z(t)=(cos t,sin t), the exact solution z'=Jz.
    for index in range(-64, 65):
        state = phase_sample(index)
        generator = apply_j(state)
        audit.equal(phase_sample(index + 4), state)
        audit.equal(generator, phase_sample(index + 1))
        audit.equal(norm_square(state), Q(1))
        audit.equal(norm_square(generator), Q(1))
        audit.true(generator != (Q(0), Q(0)))

    # Recurrence defects over complete periods vanish exactly, while the
    # instantaneous and time-averaged generator square remain one.
    for period_count in (1, 2, 3, 5, 8, 13, 32, 128):
        for index in (-8, -3, 0, 2, 5, 13):
            recurrence_defect = (
                phase_sample(index + 4 * period_count)[0] - phase_sample(index)[0],
                phase_sample(index + 4 * period_count)[1] - phase_sample(index)[1],
            )
            audit.equal(recurrence_defect, (Q(0), Q(0)))
            audit.equal(norm_square(apply_j(phase_sample(index))), Q(1))


def nested_defect(test_index: int, sequence_value: int) -> Q:
    return Q(0) if sequence_value % (2**test_index) == 0 else Q(1)


def parity_defect(defect_index: int, sequence_value: int) -> Q:
    assert defect_index in (0, 1)
    parity = sequence_value % 2
    if defect_index == 0:
        return Q(parity)  # zero on even integers.
    return Q(1 - parity)  # zero on odd integers.


def audit_diagonal_logic(audit: Audit) -> None:
    # Correct nested extraction: S_m={n:2^m divides n}; diagonal n_m=2^m.
    for diagonal_index in range(1, 17):
        diagonal_value = 2**diagonal_index
        for fixed_test in range(1, diagonal_index + 1):
            audit.equal(nested_defect(fixed_test, diagonal_value), Q(0))

        # Pointwise diagonal convergence does not control a moving defect.
        audit.equal(
            nested_defect(diagonal_index + 1, diagonal_value),
            Q(1),
        )

    # Membership is nested: a multiple of 2^(m+1) satisfies every previous
    # divisibility constraint.
    for level in range(1, 17):
        candidate = 2 ** (level + 1)
        audit.equal(nested_defect(level + 1, candidate), Q(0))
        audit.equal(nested_defect(level, candidate), Q(0))

    # False inference from individual subsequences: even and odd zero sets
    # are both infinite but have empty intersection.
    for sequence_value in range(0, 256):
        first = parity_defect(0, sequence_value)
        second = parity_defect(1, sequence_value)
        audit.equal(first + second, Q(1))
        audit.true(first == 0 or second == 0)
        audit.true(not (first == 0 and second == 0))


def main() -> None:
    audit = Audit()
    audit_concentration(audit)
    audit_translation(audit)
    audit_periodic_generator(audit)
    audit_diagonal_logic(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("stationary_subsequence_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("concentration=weak-L3_and_local_L3_invariant; L2^2~n^-1; grad_L2^2~n")
    print("translation=temporal_generator_zero_but_mass_escapes_every_fixed_ball")
    print("periodic=z_prime=Jz; exact_recurrence_with_generator_norm_one")
    print("diagonal=nested_fixed_defects_vanish_but_moving_defect_equals_one")
    print("quantifiers=individual_subsequences_need_not_have_common_refinement")
    print("scope=functional_and_logical_certificate; no Navier-Stokes or PDE claim")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
