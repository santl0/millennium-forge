#!/usr/bin/env python3
"""Exact dyadic audit for bounded weak-* modulation times strong factors.

Piecewise-constant functions on rational dyadic grids are integrated exactly
with Fraction.  Countermodels isolate weak-times-weak correlation, unbounded
modulation, generator degeneration, incompatible subsequences, and moving
tests.  No object is asserted to solve Navier--Stokes.
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


GridFunction = tuple[Q, ...]
Vector2 = tuple[Q, Q]


def average(values: GridFunction) -> Q:
    return sum(values, Q(0)) / len(values)


def pairing(left: GridFunction, right: GridFunction) -> Q:
    assert len(left) == len(right)
    return average(tuple(left[index] * right[index] for index in range(len(left))))


def l1_norm(values: GridFunction) -> Q:
    return average(tuple(abs(value) for value in values))


def linfinity_norm(values: GridFunction) -> Q:
    return max(abs(value) for value in values)


def add(left: GridFunction, right: GridFunction) -> GridFunction:
    assert len(left) == len(right)
    return tuple(left[index] + right[index] for index in range(len(left)))


def subtract(left: GridFunction, right: GridFunction) -> GridFunction:
    assert len(left) == len(right)
    return tuple(left[index] - right[index] for index in range(len(left)))


def scale(coefficient: Q, values: GridFunction) -> GridFunction:
    return tuple(coefficient * value for value in values)


def rademacher(level: int, grid_level: int) -> GridFunction:
    """r_level=(-1)^floor(2^level x), sampled exactly on a finer grid."""
    assert 1 <= level <= grid_level
    cell_count = 2**grid_level
    block_size = 2 ** (grid_level - level)
    return tuple(Q(1) if (index // block_size) % 2 == 0 else Q(-1) for index in range(cell_count))


def lift_coarse(values: tuple[Q, ...], coarse_level: int, grid_level: int) -> GridFunction:
    assert len(values) == 2**coarse_level
    assert coarse_level <= grid_level
    repetitions = 2 ** (grid_level - coarse_level)
    return tuple(value for value in values for _ in range(repetitions))


def deterministic_test(coarse_level: int, grid_level: int) -> GridFunction:
    denominator = 2**coarse_level + 1
    values = tuple(
        Q(((-1) ** index) * (index + 1), denominator)
        for index in range(2**coarse_level)
    )
    return lift_coarse(values, coarse_level, grid_level)


def audit_weak_star_against_fixed_tests(audit: Audit) -> None:
    for oscillation_level in range(2, 13):
        beta = rademacher(oscillation_level, oscillation_level)
        audit.equal(linfinity_norm(beta), Q(1))
        audit.equal(average(beta), Q(0))
        for test_level in range(0, oscillation_level):
            test = deterministic_test(test_level, oscillation_level)
            audit.equal(pairing(beta, test), Q(0))


def audit_bounded_weak_star_times_strong(audit: Audit) -> None:
    # Fixed h, constant on four dyadic cells.
    base_values = (Q(2, 3), Q(-5, 7), Q(11, 13), Q(-17, 19))
    previous_error = None
    for oscillation_level in range(3, 13):
        beta = rademacher(oscillation_level, oscillation_level)
        h = lift_coarse(base_values, 2, oscillation_level)
        epsilon = Q(1, oscillation_level)
        h_n = add(h, scale(epsilon, beta))
        difference = subtract(h_n, h)

        audit.equal(linfinity_norm(beta), Q(1))
        audit.equal(l1_norm(difference), epsilon)
        audit.equal(pairing(beta, h), Q(0))
        audit.equal(pairing(beta, difference), epsilon)
        audit.equal(pairing(beta, h_n), epsilon)

        # Exact decomposition with beta_limit=0.
        product_error = pairing(beta, h_n)
        fixed_test_term = pairing(beta, h)
        strong_error_term = pairing(beta, difference)
        audit.equal(product_error, fixed_test_term + strong_error_term)
        audit.true(abs(strong_error_term) <= linfinity_norm(beta) * l1_norm(difference))

        if previous_error is not None:
            audit.true(product_error < previous_error)
        previous_error = product_error

    # Exact discrete L-infinity/L1 inequality on varied rational patterns.
    for grid_level in range(1, 9):
        length = 2**grid_level
        bounded = tuple(Q((index % 7) - 3, 5) for index in range(length))
        perturbation = tuple(Q(((-1) ** index) * (index % 5), length + 3) for index in range(length))
        audit.true(abs(pairing(bounded, perturbation)) <= linfinity_norm(bounded) * l1_norm(perturbation))


def audit_weak_times_weak_failure(audit: Audit) -> None:
    # beta_n=h_n=r_n.  Both vanish against every fixed coarser dyadic test,
    # but their correlated product is identically one.
    for oscillation_level in range(2, 13):
        beta = rademacher(oscillation_level, oscillation_level)
        h_n = beta
        for test_level in range(0, oscillation_level):
            test = deterministic_test(test_level, oscillation_level)
            audit.equal(pairing(beta, test), Q(0))
            audit.equal(pairing(h_n, test), Q(0))
        audit.equal(l1_norm(h_n), Q(1))
        audit.equal(pairing(beta, h_n), Q(1))


def audit_unbounded_modulation_and_degenerate_generator(audit: Audit) -> None:
    previous_strong_norm = None
    for n in (1, 2, 3, 5, 8, 13, 32, 128, 512, 2048):
        # Scalar grid countermodel: beta_n=n, h_n=1/n strongly tends to zero,
        # while beta_n*h_n=1.  The missing hypothesis is uniform L-infinity.
        beta = (Q(n),) * 8
        h_n = (Q(1, n),) * 8
        audit.equal(linfinity_norm(beta), Q(n))
        audit.equal(l1_norm(h_n), Q(1, n))
        audit.equal(pairing(beta, h_n), Q(1))
        if previous_strong_norm is not None:
            audit.true(l1_norm(h_n) < previous_strong_norm)
        previous_strong_norm = l1_norm(h_n)

        # Generator form: U_n=(1/n,0), R U_n=(0,1/n), beta_n=n.
        generator: Vector2 = (Q(0), Q(1, n))
        modulated_generator: Vector2 = (
            Q(n) * generator[0],
            Q(n) * generator[1],
        )
        audit.equal(generator, (Q(0), Q(1, n)))
        audit.equal(modulated_generator, (Q(0), Q(1)))


def audit_no_common_subsequence(audit: Audit) -> None:
    # x_n alternates e_1/e_2.  Test e_1 vanishes on the odd-index branch and
    # test e_2 on the even-index branch, but no index annihilates both.
    e_one: Vector2 = (Q(1), Q(0))
    e_two: Vector2 = (Q(0), Q(1))

    def dot2(left: Vector2, right: Vector2) -> Q:
        return left[0] * right[0] + left[1] * right[1]

    for index in range(256):
        value = e_one if index % 2 == 0 else e_two
        first_defect = dot2(value, e_one)
        second_defect = dot2(value, e_two)
        audit.equal(first_defect + second_defect, Q(1))
        audit.true(first_defect == 0 or second_defect == 0)
        audit.true(not (first_defect == 0 and second_defect == 0))


def audit_fixed_test_not_moving_test(audit: Audit) -> None:
    for oscillation_level in range(2, 13):
        beta = rademacher(oscillation_level, oscillation_level)
        for test_level in range(0, oscillation_level):
            fixed_test = deterministic_test(test_level, oscillation_level)
            audit.equal(pairing(beta, fixed_test), Q(0))

        moving_test = beta
        audit.equal(pairing(beta, moving_test), Q(1))
        audit.equal(l1_norm(moving_test), Q(1))


def main() -> None:
    audit = Audit()
    audit_weak_star_against_fixed_tests(audit)
    audit_bounded_weak_star_times_strong(audit)
    audit_weak_times_weak_failure(audit)
    audit_unbounded_modulation_and_degenerate_generator(audit)
    audit_no_common_subsequence(audit)
    audit_fixed_test_not_moving_test(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("bounded_modulation_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("positive=beta_n_weak-star_bounded_times_h_n_strong_L1_converges")
    print("sharp_example=product_error=||h_n-h||_L1=1/n")
    print("weak_weak=rademacher_correlation_has_product_integral_one")
    print("unbounded=beta_n=n_and_h_n=1/n_have_product_one")
    print("degenerate=beta_n*R*U_n_stays_unit_while_R*U_n_to_zero")
    print("subsequence=individual_test_subsequences_need_not_be_common")
    print("tests=weak-star_is_fixed-test_not_sequence-dependent-test")
    print("scope=exact_dyadic_algebra; no Navier-Stokes PDE claim")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
