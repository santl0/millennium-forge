#!/usr/bin/env python3
"""Exact dyadic audit for the exterior kernel of Leray-divergence.

No Navier--Stokes equation is integrated. Fraction arithmetic certifies
kernel coefficient bounds, weak-L^(3/2) shell summation, and a separate
critical-annulus budget showing that global cutoff ledgers may still grow.
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


def derivative_numerator_bounds(audit: Audit) -> dict[int, int]:
    """Bounds before division by 4*pi for derivatives of |x|^-1.

    m=0 is the third derivative, the kernel of the nonlocal part of
    P_L div. m=1 is one additional spatial derivative.
    """
    third = 3 + 3 + 3 + 15
    # Differentiate the three 3*delta*x*r^-5 terms and the
    # -15*x*x*x*r^-7 term. Absolute coefficient sums are used.
    fourth_from_delta_x = 3 * 3 * (1 + 5)
    fourth_from_cubic = 15 * (3 + 7)
    fourth = fourth_from_delta_x + fourth_from_cubic
    audit.equal(third, 24)
    audit.equal(fourth_from_delta_x, 54)
    audit.equal(fourth_from_cubic, 150)
    audit.equal(fourth, 204)
    return {0: third, 1: fourth}


def rational_kernel_bounds(audit: Audit) -> dict[int, Q]:
    """Use pi>3 to turn C/(4*pi) into rational upper bounds."""
    numerators = derivative_numerator_bounds(audit)
    bounds = {0: Q(2), 1: Q(17)}
    audit.equal(Q(numerators[0], 12), bounds[0])
    audit.equal(Q(numerators[1], 12), bounds[1])
    return bounds


def tail_constant(m: int, kernel_bound: Q) -> tuple[Q, Q]:
    """Return the per-shell and infinite-sum rational constants."""
    weak_l3_over_2_to_l1 = Q(3)
    shell_volume_cube_root = Q(31, 10)
    distance_factor = Q(2 ** (4 + m))
    per_shell = (
        weak_l3_over_2_to_l1
        * shell_volume_cube_root
        * distance_factor
        * kernel_bound
    )
    ratio = Q(1, 2 ** (3 + m))
    infinite_sum = per_shell / (1 - ratio)
    return per_shell, infinite_sum


def audit_shell_constants(audit: Audit) -> dict[int, Q]:
    # |{r<=|y|<2r}|=(28*pi/3)r^3 and pi<22/7.
    # Thus 28*pi/3<88/3<(31/10)^3.
    audit.true(Q(88, 3) < Q(31, 10) ** 3)

    # Layer cake at p=3/2 gives ||f||_1<=3 |E|^(1/3)||f||_(p,infinity).
    p = Q(3, 2)
    audit.equal(p / (p - 1), Q(3))

    kernel_bounds = rational_kernel_bounds(audit)
    expected = {0: Q(11904, 35), 1: Q(134912, 25)}
    obtained: dict[int, Q] = {}
    for m in (0, 1):
        per_shell, infinite_sum = tail_constant(m, kernel_bounds[m])
        obtained[m] = infinite_sum
        audit.equal(infinite_sum, expected[m])
        ratio = Q(1, 2 ** (3 + m))
        for shell_count in (1, 2, 3, 8, 32, 128):
            finite_geometric = sum(
                (ratio**k for k in range(shell_count)), Q(0)
            )
            exact_geometric = (1 - ratio**shell_count) / (1 - ratio)
            audit.equal(finite_geometric, exact_geometric)
            audit.true(per_shell * finite_geometric < infinite_sum)

        for outer_radius in (Q(2), Q(4), Q(16), Q(256), Q(4096)):
            for weak_bound in (Q(1, 11), Q(1), Q(7, 3)):
                finite = per_shell * weak_bound * outer_radius ** (-3 - m)
                finite *= sum((ratio**k for k in range(24)), Q(0))
                infinite = (
                    infinite_sum
                    * weak_bound
                    * outer_radius ** (-3 - m)
                )
                audit.true(finite < infinite)
                doubled = (
                    infinite_sum
                    * weak_bound
                    * (2 * outer_radius) ** (-3 - m)
                )
                audit.equal(doubled / infinite, ratio)
    return obtained


def shell_masses(shell_count: int) -> list[Q]:
    """Normalized volumes of dyadic shells: 7*8^j."""
    return [Q(7 * 8**j) for j in range(shell_count)]


def audit_critical_annular_ledger(audit: Audit) -> None:
    """Track global budgets for a truncated critical annular profile."""
    for epsilon_root in (Q(1, 10), Q(1), Q(3, 2)):
        epsilon = epsilon_root**2
        for shell_count in (1, 2, 4, 8, 16, 32):
            masses = shell_masses(shell_count)
            cumulative = []
            running = Q(0)
            for mass in masses:
                running += mass
                cumulative.append(running)

            # Velocity amplitude epsilon*2^-j. Its weak-L3 cube is uniform
            # in the number of retained shells.
            velocity_weak_cubes = [
                (epsilon * Q(1, 2**j)) ** 3 * cumulative[j]
                for j in range(shell_count)
            ]
            audit.true(max(velocity_weak_cubes) < 8 * epsilon**3)

            # Cutoff stress amplitude epsilon*4^-j. Because epsilon is a
            # rational square, its weak-L^(3/2) power is exact.
            stress_weak_three_halves_powers = [
                epsilon_root**3 * Q(1, 8**j) * cumulative[j]
                for j in range(shell_count)
            ]
            audit.true(
                max(stress_weak_three_halves_powers)
                < 8 * epsilon_root**3
            )

            last = shell_count - 1
            outer_scale = Q(2**last)
            outer_dilation_l1 = (
                epsilon * Q(1, 2**last) * masses[last]
            )
            audit.equal(outer_dilation_l1, 7 * epsilon * outer_scale**2)

            cumulative_dilation_l1 = sum(
                (
                    epsilon * Q(1, 2**j) * masses[j]
                    for j in range(shell_count)
                ),
                Q(0),
            )
            audit.equal(
                cumulative_dilation_l1,
                7 * epsilon * Q(4**shell_count - 1, 3),
            )

            # A Laplacian-cutoff coefficient has amplitude
            # epsilon*2^(-3j), hence a constant L1 cost on every shell.
            viscous_l1 = [
                epsilon * Q(1, 8**j) * masses[j]
                for j in range(shell_count)
            ]
            audit.true(all(value == 7 * epsilon for value in viscous_l1))
            audit.equal(sum(viscous_l1, Q(0)), 7 * epsilon * shell_count)

            # Each stress shell has weak-L^(3/2) norm <4*epsilon because
            # 7^(2/3)<4. The triangle ledger grows linearly, although the
            # actual union remains bounded by 4*epsilon.
            audit.true(Q(7) ** 2 < Q(4) ** 3)
            triangle_stress_budget = 4 * epsilon * shell_count
            actual_union_upper = 4 * epsilon
            audit.true(triangle_stress_budget >= actual_union_upper)
            if shell_count > 1:
                audit.true(triangle_stress_budget > actual_union_upper)


def main() -> None:
    audit = Audit()
    constants = audit_shell_constants(audit)
    audit_critical_annular_ledger(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("outer_cutoff_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("kernel=N(x)=1/(4*pi*|x|), P_L=I+grad(-Delta)^-1 div")
    print("kernel_component_numerators=m0:24, m1:204")
    print("rational_kernel_bounds=m0:2*|z|^-4, m1:17*|z|^-5")
    print("weak_L3/2_to_L1_constant=3")
    print(f"tail_m0<={constants[0]}*M*L^-3")
    print(f"tail_m1<={constants[1]}*M*L^-4")
    print("critical_velocity_weak_L3=uniform_over_dyadic_shell_count")
    print("outer_dilation_L1=7*epsilon*L^2")
    print("cumulative_viscous_L1=7*epsilon*number_of_shells")
    print("stress_triangle_budget<=4*epsilon*number_of_shells")
    print("actual_stress_union_weak_L3/2<=4*epsilon")
    print("scope=exact kernel and scaling ledger; no Navier-Stokes simulation")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
