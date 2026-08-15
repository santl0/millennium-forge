#!/usr/bin/env python3
"""Exact dyadic audit for fast-rotation collapse and its failure modes.

The positive certificate is a discrete integration-by-parts estimate with
q_n=1/beta_n.  A positive-speed stroboscopic countermodel isolates unbounded
variation of q_n; separate countermodels cover sign changes, zero crossings,
distributional residuals with moving tests, and angular averages.  This is
finite-dimensional/discrete algebra, not a Navier--Stokes PDE certificate.
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


def total_variation(values: tuple[Q, ...]) -> Q:
    return sum((abs(values[index] - values[index - 1]) for index in range(1, len(values))), Q(0))


def sup_norm(values: tuple[Q, ...]) -> Q:
    return max(abs(value) for value in values)


def summation_by_parts_left(
    q_values: tuple[Q, ...],
    orbit_values: tuple[Q, ...],
    test_values: tuple[Q, ...],
) -> Q:
    assert len(orbit_values) == len(q_values) + 1
    assert len(test_values) == len(q_values)
    return sum(
        (
            q_values[index]
            * test_values[index]
            * (orbit_values[index + 1] - orbit_values[index])
            for index in range(len(q_values))
        ),
        Q(0),
    )


def summation_by_parts_right(
    q_values: tuple[Q, ...],
    orbit_values: tuple[Q, ...],
    test_values: tuple[Q, ...],
) -> Q:
    coefficients = tuple(q_values[index] * test_values[index] for index in range(len(q_values)))
    boundary = coefficients[-1] * orbit_values[-1] - coefficients[0] * orbit_values[0]
    interior = sum(
        (
            (coefficients[index - 1] - coefficients[index]) * orbit_values[index]
            for index in range(1, len(q_values))
        ),
        Q(0),
    )
    return boundary + interior


def integration_by_parts_bound(
    q_values: tuple[Q, ...],
    orbit_values: tuple[Q, ...],
    test_values: tuple[Q, ...],
) -> Q:
    orbit_bound = sup_norm(orbit_values)
    return orbit_bound * (
        2 * sup_norm(q_values) * sup_norm(test_values)
        + sup_norm(test_values) * total_variation(q_values)
        + sup_norm(q_values) * total_variation(test_values)
    )


def audit_positive_bv_estimate(audit: Audit) -> None:
    previous_q_sup = None
    previous_q_variation = None
    previous_bound = None
    for scale_index in range(2, 11):
        cell_count = 2**scale_index
        # Positive q_i=1/N+(-1)^i/N^3, hence beta_i=1/q_i is defined.
        q_values = tuple(
            Q(1, cell_count) + Q((-1) ** index, cell_count**3)
            for index in range(cell_count)
        )
        beta_values = tuple(1 / value for value in q_values)
        orbit_values = tuple(Q((index % 5) - 2, 2) for index in range(cell_count + 1))
        test_values = tuple(Q(index, cell_count) for index in range(cell_count))

        left = summation_by_parts_left(q_values, orbit_values, test_values)
        right = summation_by_parts_right(q_values, orbit_values, test_values)
        bound = integration_by_parts_bound(q_values, orbit_values, test_values)
        audit.equal(left, right)
        audit.true(abs(left) <= bound)

        q_sup = Q(cell_count**2 + 1, cell_count**3)
        q_variation = Q(2 * (cell_count - 1), cell_count**3)
        audit.equal(sup_norm(q_values), q_sup)
        audit.equal(total_variation(q_values), q_variation)
        audit.true(min(abs(value) for value in beta_values) > 0)

        if previous_q_sup is not None:
            audit.true(q_sup < previous_q_sup)
        if previous_q_variation is not None:
            audit.true(q_variation < previous_q_variation)
        if previous_bound is not None:
            audit.true(bound < previous_bound)
        previous_q_sup = q_sup
        previous_q_variation = q_variation
        previous_bound = bound


def audit_positive_stroboscopic_high_variation(audit: Audit) -> None:
    # Normalize the angular period to one.  Each of N^2 cycles consists of:
    #   * a slow window of angular width delta_N at speed N;
    #   * the remaining angle at speed N^4.
    # The choice delta_N=(N+1)/(N^2+N+1) makes every cycle last exactly N^-2.
    # Hence N^2 cycles fill [0,1], beta is everywhere positive, and the total
    # fast-time measure is exactly 1/(N^2+N+1).
    previous_q_sup = None
    previous_q_variation = None
    previous_fast_measure = None
    previous_lp_bounds: dict[int, Q] = {}
    for scale_index in range(1, 9):
        n = 2**scale_index
        cycle_count = n**2
        denominator = n**2 + n + 1
        angular_window = Q(n + 1, denominator)
        slow_duration = Q(n + 1, n * denominator)
        fast_duration = Q(1, n**2 * denominator)
        slow_beta = Q(n)
        fast_beta = Q(n**4)
        slow_q = 1 / slow_beta
        fast_q = 1 / fast_beta

        audit.equal(slow_duration + fast_duration, Q(1, n**2))
        audit.equal(slow_beta * slow_duration, angular_window)
        audit.equal(fast_beta * fast_duration, 1 - angular_window)
        audit.equal(Q(cycle_count) * (slow_duration + fast_duration), Q(1))
        audit.true(Q(0) < angular_window < Q(1, n))

        beta_values = tuple(
            beta
            for _ in range(cycle_count)
            for beta in (slow_beta, fast_beta)
        )
        q_values = tuple(1 / beta for beta in beta_values)
        q_sup = sup_norm(q_values)
        q_variation = total_variation(q_values)
        expected_variation = Q(2 * cycle_count - 1) * (slow_q - fast_q)
        fast_measure = Q(cycle_count) * fast_duration
        slow_measure = Q(cycle_count) * slow_duration

        audit.equal(min(beta_values), Q(n))
        audit.true(all(beta > 0 for beta in beta_values))
        audit.equal(q_sup, Q(1, n))
        audit.equal(q_variation, expected_variation)
        audit.equal(
            Q(2 * n) - q_variation,
            Q(1, n) + Q(2, n**2) - Q(1, n**4),
        )
        audit.true(Q(n) < q_variation < Q(2 * n))
        audit.equal(fast_measure, Q(1, denominator))
        audit.equal(slow_measure, Q(n**2 + n, denominator))
        audit.equal(slow_measure + fast_measure, Q(1))
        audit.true(fast_measure < Q(1, n**2))

        # Abstract unitary-orbit estimate with ||U||=||RU||=1.  On slow
        # passages the phase modulo the group lies in [0,delta_N]; the fast
        # passages have total measure fast_measure and orbit distance <=2.
        for exponent in range(1, 7):
            lp_power_bound = (
                slow_measure * angular_window**exponent
                + fast_measure * Q(2) ** exponent
            )
            crude_bound = Q(1, n**exponent) + Q(2**exponent, n**2)
            audit.true(lp_power_bound < crude_bound)
            if exponent in previous_lp_bounds:
                audit.true(lp_power_bound < previous_lp_bounds[exponent])
            previous_lp_bounds[exponent] = lp_power_bound

        # Uniform convergence fails for a nontrivial planar orbit: every fast
        # passage crosses the half-turn phase exactly.
        half_turn_offset = (Q(1, 2) - angular_window) / fast_beta
        audit.true(Q(0) < half_turn_offset < fast_duration)
        audit.equal(
            angular_window + fast_beta * half_turn_offset,
            Q(1, 2),
        )

        if previous_q_sup is not None:
            audit.true(q_sup < previous_q_sup)
        if previous_q_variation is not None:
            audit.true(q_variation > previous_q_variation)
        if previous_fast_measure is not None:
            audit.true(fast_measure < previous_fast_measure)
        previous_q_sup = q_sup
        previous_q_variation = q_variation
        previous_fast_measure = fast_measure


def audit_signed_triangular_stroboscopy(audit: Audit) -> None:
    # On N^2 cells of width N^-2, add a triangular jitter a_n of amplitude
    # N^-1 to the prescribed phase psi(t)=t.  Its slopes are +/-N, so
    # beta=1+a_n' equals N+1 or 1-N and never vanishes for N>=2.
    previous_phase_error = None
    previous_q_sup = None
    previous_q_variation = None
    for scale_index in range(1, 9):
        n = 2**scale_index
        cell_count = n**2
        beta_plus = Q(n + 1)
        beta_minus = Q(1 - n)
        q_plus = 1 / beta_plus
        q_minus = 1 / beta_minus
        beta_values = tuple(beta_plus if index % 2 == 0 else beta_minus for index in range(cell_count))
        q_values = tuple(1 / beta for beta in beta_values)

        phase_jitter_nodes = tuple(Q(0) if index % 2 == 0 else Q(1, n) for index in range(cell_count + 1))
        phase_error = sup_norm(phase_jitter_nodes)
        q_sup = sup_norm(q_values)
        q_variation = total_variation(q_values)

        audit.equal(phase_error, Q(1, n))
        audit.equal(q_sup, Q(1, n - 1))
        audit.equal(
            q_variation,
            Q(cell_count - 1) * (Q(1, n + 1) + Q(1, n - 1)),
        )
        audit.true(min(abs(beta) for beta in beta_values) == n - 1)

        # Every even stroboscopic node exactly matches the prescribed phase.
        for node in range(0, cell_count + 1, 2):
            prescribed_phase = Q(node, cell_count)
            perturbed_phase = prescribed_phase + phase_jitter_nodes[node]
            audit.equal(perturbed_phase, prescribed_phase)

        if previous_phase_error is not None:
            audit.true(phase_error < previous_phase_error)
        if previous_q_sup is not None:
            audit.true(q_sup < previous_q_sup)
        if previous_q_variation is not None:
            audit.true(q_variation > previous_q_variation)
        previous_phase_error = phase_error
        previous_q_sup = q_sup
        previous_q_variation = q_variation


def audit_beta_zero_crossing(audit: Audit) -> None:
    # beta(t)=2t-1 on the rational grid t_i=i/(2N).  It vanishes at i=N;
    # on the punctured grid the nearest reciprocal has magnitude N.
    previous_punctured_sup = None
    for n in (1, 2, 3, 5, 8, 13, 32, 128, 512):
        beta_values = tuple(Q(index - n, n) for index in range(2 * n + 1))
        audit.equal(beta_values[n], Q(0))
        audit.true(any(value < 0 for value in beta_values))
        audit.true(any(value > 0 for value in beta_values))

        punctured_reciprocals = tuple(1 / value for value in beta_values if value != 0)
        punctured_sup = sup_norm(punctured_reciprocals)
        audit.equal(punctured_sup, Q(n))
        if previous_punctured_sup is not None:
            audit.true(punctured_sup > previous_punctured_sup)
        previous_punctured_sup = punctured_sup


def rademacher(level: int, grid_level: int) -> tuple[Q, ...]:
    assert 1 <= level <= grid_level
    block_size = 2 ** (grid_level - level)
    return tuple(
        Q(1) if (index // block_size) % 2 == 0 else Q(-1)
        for index in range(2**grid_level)
    )


def lift_test(level: int, grid_level: int) -> tuple[Q, ...]:
    values = tuple(Q(((-1) ** index) * (index + 1), 2**level + 1) for index in range(2**level))
    repetitions = 2 ** (grid_level - level)
    return tuple(value for value in values for _ in range(repetitions))


def pairing(left: tuple[Q, ...], right: tuple[Q, ...]) -> Q:
    assert len(left) == len(right)
    return sum((left[index] * right[index] for index in range(len(left))), Q(0)) / len(left)


def audit_distributional_residual_mobile_test(audit: Audit) -> None:
    for oscillation_level in range(2, 13):
        residual = rademacher(oscillation_level, oscillation_level)
        for fixed_level in range(0, oscillation_level):
            fixed_test = lift_test(fixed_level, oscillation_level)
            audit.equal(pairing(residual, fixed_test), Q(0))

        moving_test = residual
        audit.equal(pairing(residual, moving_test), Q(1))
        audit.equal(sup_norm(residual), Q(1))


Vector3 = tuple[Q, Q, Q]


def quarter_rotation(index: int, vector: Vector3) -> Vector3:
    x, y, z = vector
    phase = index % 4
    if phase == 0:
        return x, y, z
    if phase == 1:
        return -y, x, z
    if phase == 2:
        return -x, -y, z
    return y, -x, z


def add3(left: Vector3, right: Vector3) -> Vector3:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def scale3(coefficient: Q, vector: Vector3) -> Vector3:
    return tuple(coefficient * value for value in vector)  # type: ignore[return-value]


def generator(vector: Vector3) -> Vector3:
    return -vector[1], vector[0], Q(0)


def norm_square3(vector: Vector3) -> Q:
    return sum((value**2 for value in vector), Q(0))


def audit_angular_average_not_profile_symmetry(audit: Audit) -> None:
    profile: Vector3 = (Q(1), Q(0), Q(1))
    orbit = tuple(quarter_rotation(index, profile) for index in range(4))
    orbit_sum: Vector3 = (Q(0), Q(0), Q(0))
    for orbit_point in orbit:
        orbit_sum = add3(orbit_sum, orbit_point)
    angular_average = scale3(Q(1, 4), orbit_sum)
    audit.equal(angular_average, (Q(0), Q(0), Q(1)))
    audit.equal(generator(angular_average), (Q(0), Q(0), Q(0)))
    audit.equal(norm_square3(generator(profile)), Q(1))
    audit.true(generator(profile) != (Q(0), Q(0), Q(0)))
    for phase in range(4):
        audit.equal(quarter_rotation(phase, angular_average), angular_average)


def main() -> None:
    audit = Audit()
    audit_positive_bv_estimate(audit)
    audit_positive_stroboscopic_high_variation(audit)
    audit_signed_triangular_stroboscopy(audit)
    audit_beta_zero_crossing(audit)
    audit_distributional_residual_mobile_test(audit)
    audit_angular_average_not_profile_symmetry(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("fast_rotation_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("positive=||q_n||_infinity_to_zero_and_Var(q_n)_to_zero_close_IBP")
    print("positive_stroboscopy=beta_in_{N,N^4}_and_||q_n||_infinity=1/N")
    print("positive_stroboscopy_Var(q_n)=(2N^2-1)*(1/N-1/N^4)~2N")
    print("positive_stroboscopy_fast_measure=1/(N^2+N+1)_and_strong_Lp")
    print("signed_stroboscopy=uniform_nonstationary_limit_but_sign_and_W11_gate_fail")
    print("zero_crossing=q_n=1/beta_n_is_undefined_and_punctured_sup_grows")
    print("distributional=fixed_tests_vanish_but_mobile_test_pairing_is_one")
    print("angular_average=is_axis_fixed_while_profile_generator_norm_is_one")
    print("seed=n/a; scope=exact_discrete_models; no Navier-Stokes PDE claim")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
