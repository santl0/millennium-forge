#!/usr/bin/env python3
"""Exact k=1 and k=2 audit of metric-dependent canonical SO(2) phases.

The calculation is finite-dimensional representation theory over Fraction.
It does not realize the modes as Navier--Stokes fields or solutions.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path


Mode = tuple[Q, Q]
State = tuple[Mode, Mode]
Weights = tuple[Q, Q]


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, left: object, right: object) -> None:
        self.assertions += 1
        assert left == right, (left, right)

    def true(self, statement: bool) -> None:
        self.assertions += 1
        assert statement


def mode_add(left: Mode, right: Mode) -> Mode:
    return left[0] + right[0], left[1] + right[1]


def mode_subtract(left: Mode, right: Mode) -> Mode:
    return left[0] - right[0], left[1] - right[1]


def mode_scale(coefficient: Q, mode: Mode) -> Mode:
    return coefficient * mode[0], coefficient * mode[1]


def mode_dot(left: Mode, right: Mode) -> Q:
    return left[0] * right[0] + left[1] * right[1]


def generator(mode: Mode) -> Mode:
    return -mode[1], mode[0]


def quarter_rotation(quarter_index: int, mode: Mode) -> Mode:
    phase = quarter_index % 4
    if phase == 0:
        return mode
    if phase == 1:
        return -mode[1], mode[0]
    if phase == 2:
        return -mode[0], -mode[1]
    return mode[1], -mode[0]


def state_add(left: State, right: State) -> State:
    return mode_add(left[0], right[0]), mode_add(left[1], right[1])


def state_subtract(left: State, right: State) -> State:
    return mode_subtract(left[0], right[0]), mode_subtract(left[1], right[1])


def state_scale(coefficient: Q, state: State) -> State:
    return mode_scale(coefficient, state[0]), mode_scale(coefficient, state[1])


def state_generator(state: State) -> State:
    # Distinct real SO(2) isotypes: angular frequencies k=1 and k=2.
    return generator(state[0]), mode_scale(Q(2), generator(state[1]))


def weighted_dot(left: State, right: State, weights: Weights) -> Q:
    return (
        weights[0] * mode_dot(left[0], right[0])
        + weights[1] * mode_dot(left[1], right[1])
    )


def weighted_norm_square(state: State, weights: Weights) -> Q:
    return weighted_dot(state, state, weights)


def canonical_decomposition(
    derivative: State,
    tangent: State,
    weights: Weights,
) -> tuple[Q, State]:
    if not all(weight > 0 for weight in weights):
        raise ValueError("metric weights must be strictly positive")
    gram = weighted_norm_square(tangent, weights)
    if gram == 0:
        raise ZeroDivisionError("zero canonical Gram")
    beta = weighted_dot(derivative, tangent, weights) / gram
    residual = state_subtract(derivative, state_scale(beta, tangent))
    return beta, residual


def audit_decomposition(
    audit: Audit,
    derivative: State,
    tangent: State,
    weights: Weights,
    expected_beta: Q,
) -> State:
    beta, residual = canonical_decomposition(derivative, tangent, weights)
    gram = weighted_norm_square(tangent, weights)
    beta_tangent = state_scale(beta, tangent)
    identity_error = state_subtract(
        derivative,
        state_add(beta_tangent, residual),
    )

    audit.true(weights[0] > 0 and weights[1] > 0)
    audit.true(gram > 0)
    audit.equal(beta, expected_beta)
    audit.equal(identity_error, ((Q(0), Q(0)), (Q(0), Q(0))))
    audit.equal(weighted_norm_square(identity_error, weights), Q(0))
    audit.equal(weighted_dot(residual, tangent, weights), Q(0))
    audit.equal(
        weighted_norm_square(derivative, weights),
        weighted_norm_square(beta_tangent, weights)
        + weighted_norm_square(residual, weights),
    )
    return residual


def audit_opposed_velocities(audit: Audit, records: list[tuple[object, ...]]) -> None:
    unit: Mode = (Q(1), Q(0))
    for scale_index in range(1, 11):
        n = 2**scale_index
        for phase_index in range(4):
            state: State = (
                quarter_rotation(phase_index, unit),
                mode_scale(
                    Q(1, 2),
                    quarter_rotation(2 * phase_index, unit),
                ),
            )
            tangent = state_generator(state)
            derivative: State = (
                mode_scale(Q(n), tangent[0]),
                mode_scale(Q(-n), tangent[1]),
            )

            equal_weights: Weights = (Q(1), Q(1))
            audit.equal(
                (
                    weighted_norm_square((tangent[0], (Q(0), Q(0))), equal_weights),
                    weighted_norm_square(((Q(0), Q(0)), tangent[1]), equal_weights),
                ),
                (Q(1), Q(1)),
            )
            equal_residual = audit_decomposition(
                audit,
                derivative,
                tangent,
                equal_weights,
                Q(0),
            )
            audit.equal(equal_residual, derivative)

            biased_weights: Weights = (Q(2), Q(1))
            audit.equal(
                (
                    weighted_norm_square((tangent[0], (Q(0), Q(0))), biased_weights),
                    weighted_norm_square(((Q(0), Q(0)), tangent[1]), biased_weights),
                ),
                (Q(2), Q(1)),
            )
            biased_residual = audit_decomposition(
                audit,
                derivative,
                tangent,
                biased_weights,
                Q(n, 3),
            )
            audit.equal(
                biased_residual,
                (
                    mode_scale(Q(2 * n, 3), tangent[0]),
                    mode_scale(Q(-4 * n, 3), tangent[1]),
                ),
            )
            records.append(("opposed", n, phase_index, Q(0), Q(n, 3)))


def audit_slow_mode_visibility(audit: Audit, records: list[tuple[object, ...]]) -> None:
    unit: Mode = (Q(1), Q(0))
    previous_fixed_share = None
    for scale_index in range(1, 11):
        n = 2**scale_index
        for phase_index in range(4):
            fast_mode = quarter_rotation(phase_index, unit)
            slow_mode = mode_scale(
                Q(1, 2 * n),
                quarter_rotation(2 * phase_index, unit),
            )
            state: State = (fast_mode, slow_mode)
            tangent = state_generator(state)
            derivative: State = (
                mode_scale(Q(n), tangent[0]),
                tangent[1],
            )

            fixed_weights: Weights = (Q(1), Q(1))
            fixed_beta = Q(n**3 + 1, n**2 + 1)
            audit_decomposition(
                audit,
                derivative,
                tangent,
                fixed_weights,
                fixed_beta,
            )
            fixed_slow_gram_share = Q(1, n**2 + 1)
            audit.equal(
                Q(1) - fixed_beta / n,
                Q(n - 1, n * (n**2 + 1)),
            )

            dependent_weights: Weights = (Q(1), Q(n**2))
            dependent_beta = Q(n + 1, 2)
            audit_decomposition(
                audit,
                derivative,
                tangent,
                dependent_weights,
                dependent_beta,
            )
            dependent_slow_gram_share = Q(1, 2)
            audit.equal(
                dependent_weights[1] * mode_dot(tangent[1], tangent[1]),
                Q(1),
            )
            audit.equal(dependent_slow_gram_share, Q(1, 2))

            # Deliberately non-uniform metric: the N^4 slow weight makes its
            # effective Gram N^2 and forces beta to a bounded limit one.
            dominant_slow_weights: Weights = (Q(1), Q(n**4))
            dominant_slow_beta = Q(n**2 + n, n**2 + 1)
            audit_decomposition(
                audit,
                derivative,
                tangent,
                dominant_slow_weights,
                dominant_slow_beta,
            )
            dominant_slow_gram_share = Q(n**2, n**2 + 1)
            audit.equal(
                dominant_slow_weights[1] * mode_dot(tangent[1], tangent[1]),
                Q(n**2),
            )
            audit.equal(
                dominant_slow_beta - 1,
                Q(n - 1, n**2 + 1),
            )
            audit.true(Q(1) < dominant_slow_beta < Q(2))

            records.append(
                (
                    "slow",
                    n,
                    phase_index,
                    fixed_beta,
                    dependent_beta,
                    fixed_slow_gram_share,
                    dependent_slow_gram_share,
                    dominant_slow_beta,
                    dominant_slow_gram_share,
                )
            )

        if previous_fixed_share is not None:
            audit.true(fixed_slow_gram_share < previous_fixed_share)
        previous_fixed_share = fixed_slow_gram_share


def main() -> None:
    audit = Audit()
    records: list[tuple[object, ...]] = []
    audit_opposed_velocities(audit, records)
    audit_slow_mode_visibility(audit, records)

    case_hash = sha256(repr(tuple(records)).encode("ascii")).hexdigest()
    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("modal_metric_robustness: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("opposed_equal_weights=beta_N=0")
    print("opposed_weights_2_to_1=beta_N=N/3")
    print("fixed_metric_slow_share=1/(N^2+1)_to_zero")
    print("N_dependent_metric_slow_share=1/2_and_beta_N=(N+1)/2")
    print("N4_metric=slow_share=N^2/(N^2+1)_and_beta_N=(N^2+N)/(N^2+1)_to_1")
    print("identity_residual=0; orthogonality_residual=0; arithmetic=Fraction")
    print(f"case_sha256={case_hash}")
    print("seed=n/a; scope=SO(2) isotypes k=1 and k=2; no PDE realization")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
