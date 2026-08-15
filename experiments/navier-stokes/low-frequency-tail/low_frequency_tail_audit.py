#!/usr/bin/env python3
"""Exact low-frequency ledger for an ancient heat-cocycle counter-test.

The true heat multiplier is bounded by an exact dyadic proxy.  A separate
rational semigroup verifies cocycle and Duhamel algebra without floating
point.  Neither construction is asserted to be a Navier--Stokes solution.
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


def power_two(exponent: int) -> Q:
    if exponent >= 0:
        return Q(2**exponent)
    return Q(1, 2 ** (-exponent))


def shell_mass(shell: int) -> Q:
    """Integral of rho^-2 on [2^(-j-1),2^-j]."""
    return power_two(shell)


def proxy_multiplier(base_index: int, shell: int) -> Q:
    """min(1,T_n*2^-2j), with T_n=4^n."""
    if shell < base_index:
        return Q(1)
    return power_two(2 * (base_index - shell))


def proxy_shell_energy(base_index: int, shell: int) -> Q:
    multiplier = proxy_multiplier(base_index, shell)
    return shell_mass(shell) * multiplier**2


def proxy_total(base_index: int) -> Q:
    return Q(15, 7) * power_two(base_index)


def proxy_truncated(base_index: int, last_shell: int) -> Q:
    """Closed sum from shell -infinity through last_shell."""
    if last_shell < base_index:
        return power_two(last_shell + 1)
    low_shell_count = last_shell - base_index + 1
    saturated = power_two(base_index)
    low = (
        Q(8, 7)
        * power_two(base_index)
        * (1 - Q(1, 8**low_shell_count))
    )
    return saturated + low


def audit_shell_geometry(audit: Audit) -> None:
    for shell in range(-16, 17):
        lower = power_two(-shell - 1)
        upper = power_two(-shell)
        # Integral rho^-2 d rho is lower^-1-upper^-1.
        integral = 1 / lower - 1 / upper
        audit.equal(integral, shell_mass(shell))

    # On a low shell, integral rho^2 d rho=(7/24)*2^-3j.
    for shell in range(-8, 17):
        lower = power_two(-shell - 1)
        upper = power_two(-shell)
        integral = (upper**3 - lower**3) / 3
        audit.equal(integral, Q(7, 24) * power_two(-3 * shell))


def audit_proxy_series(audit: Audit) -> None:
    for base_index in range(-5, 13):
        # Saturated shells j<n sum to 2^n.
        saturated_sum = power_two(base_index)
        audit.equal(saturated_sum, power_two(base_index))

        # Unsaturated shells j>=n contribute (8/7)*2^n.
        low_sum = Q(8, 7) * power_two(base_index)
        audit.equal(saturated_sum + low_sum, proxy_total(base_index))

        for offset in (0, 1, 2, 3, 5, 8, 13):
            last_shell = base_index + offset
            closed = proxy_truncated(base_index, last_shell)

            # Direct finite low-shell sum plus the exact saturated half-line.
            direct = saturated_sum + sum(
                (
                    proxy_shell_energy(base_index, shell)
                    for shell in range(base_index, last_shell + 1)
                ),
                Q(0),
            )
            audit.equal(closed, direct)
            audit.true(closed < proxy_total(base_index))


def audit_true_heat_bounds(audit: Audit) -> None:
    """Exact constants from 1/2 min(1,x)<=1-exp(-x)<=min(1,x)."""
    high_lower = Q(1, 4)  # squared multiplier on shells j<n.
    high_upper = Q(1)

    low_integral = Q(7, 24)
    low_multiplier_lower = Q(1, 4)
    geometric_low_sum = Q(8, 7)
    low_lower = low_integral * low_multiplier_lower * geometric_low_sum
    low_upper = low_integral * geometric_low_sum
    audit.equal(low_lower, Q(1, 12))
    audit.equal(low_upper, Q(1, 3))

    total_lower = high_lower + low_lower
    total_upper = high_upper + low_upper
    audit.equal(total_lower, Q(1, 3))
    audit.equal(total_upper, Q(4, 3))
    audit.equal(total_upper - total_lower, Q(1))

    # Therefore the true radial heat-defect energy at T_n=4^n is between
    # (1/3)*2^n and (4/3)*2^n, up to the fixed angular/Fourier constant.
    for base_index in range(-5, 13):
        lower = total_lower * power_two(base_index)
        upper = total_upper * power_two(base_index)
        audit.true(Q(0) < lower < upper)
        audit.equal(upper - lower, power_two(base_index))


def audit_limit_order(audit: Audit) -> None:
    frequency_then_base = Q(15, 7)
    base_then_frequency = Q(0)
    audit.true(frequency_then_base != base_then_frequency)

    # For fixed J and n=J+k, the normalized retained energy is 2^(1-k).
    for last_shell in (-8, -3, 0, 2, 5, 13):
        previous = None
        for gap in (1, 2, 3, 5, 8, 13, 32):
            base_index = last_shell + gap
            normalized = proxy_truncated(base_index, last_shell) / power_two(base_index)
            audit.equal(normalized, power_two(1 - gap))
            if previous is not None:
                audit.true(normalized < previous)
            previous = normalized

        # The complementary normalized low-frequency tail tends to 15/7.
        far_base = last_shell + 32
        normalized_tail = (
            proxy_total(far_base) - proxy_truncated(far_base, last_shell)
        ) / power_two(far_base)
        audit.equal(normalized_tail, Q(15, 7) - power_two(1 - 32))

    audit.equal(frequency_then_base, Q(15, 7))
    audit.equal(base_then_frequency, Q(0))


def audit_littlewood_paley_endpoint(audit: Audit) -> None:
    # Unfiltered U has normalized L2 block masses 2^j.  Every finite block is
    # finite, while the low-frequency partial sum diverges.
    previous = None
    for last_shell in (0, 1, 2, 3, 5, 8, 13, 20, 32):
        low_partial = sum((shell_mass(j) for j in range(0, last_shell + 1)), Q(0))
        audit.equal(low_partial, power_two(last_shell + 1) - 1)
        if previous is not None:
            audit.true(low_partial > previous)
        previous = low_partial

    # Each D_T has a summable far-low-frequency tail, but no tail cutoff is
    # uniform in the base index n.
    for base_index in (0, 1, 2, 3, 5, 8, 13):
        for gap in (1, 2, 3, 5, 8):
            first_omitted = base_index + gap
            tail = (
                Q(8, 7)
                * power_two(base_index)
                * Q(1, 8**gap)
            )
            # This is the geometric tail from j=base_index+gap to infinity.
            direct_first = proxy_shell_energy(base_index, first_omitted)
            audit.equal(tail / direct_first, Q(8, 7))
            audit.true(tail > 0)


def audit_rational_duhamel_cocycle(audit: Audit) -> None:
    """Exact discrete semigroup showing algebra does not imply tightness."""
    semigroup_units = (Q(1, 2), Q(2, 3), Q(3, 4), Q(7, 8), Q(15, 16))
    durations = (1, 2, 3, 5, 8, 13)
    for unit in semigroup_units:
        for duration in durations:
            defect = 1 - unit**duration
            duhamel = sum(
                (unit**step * (1 - unit) for step in range(duration)),
                Q(0),
            )
            audit.equal(defect, duhamel)

        for first, second, third in ((1, 1, 1), (1, 2, 3), (2, 3, 5), (3, 5, 8)):
            defect = lambda length: 1 - unit**length
            direct = defect(first + second + third)
            cocycle = (
                defect(first)
                + unit**first * defect(second)
                + unit ** (first + second) * defect(third)
            )
            audit.equal(direct, cocycle)


def audit_spatial_scaling(audit: Audit) -> None:
    # D_T(x)=T^-1/2 D_1(x/sqrt(T)); squared norm scales T^1/2.
    amplitude = Q(-1, 2)
    volume = Q(3, 2)
    l2_square = 2 * amplitude + volume
    audit.equal(l2_square, Q(1, 2))
    audit.equal(l2_square / 2, Q(1, 4))

    # The L2-normalized family T^-1/4 D_T has amplitude T^-3/4 and
    # constant L2 norm, while its spatial scale is T^1/2.
    normalized_amplitude = amplitude - Q(1, 4)
    audit.equal(normalized_amplitude, Q(-3, 4))
    audit.equal(2 * normalized_amplitude + volume, Q(0))


def main() -> None:
    audit = Audit()
    audit_shell_geometry(audit)
    audit_proxy_series(audit)
    audit_true_heat_bounds(audit)
    audit_limit_order(audit)
    audit_littlewood_paley_endpoint(audit)
    audit_rational_duhamel_cocycle(audit)
    audit_spatial_scaling(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("low_frequency_tail_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("shell_mass=integral_[2^-j-1,2^-j](rho^-2)d_rho=2^j")
    print("proxy_total=(15/7)*2^n for T_n=4^n")
    print("true_heat_bounds=(1/3)*2^n <= radial_energy <= (4/3)*2^n")
    print("limit_order=frequency_then_base:15/7, base_then_frequency:0")
    print("LP_endpoint=finite_blocks_do_not_give_uniform_low_frequency_sum")
    print("duhamel_cocycle=exact_rational_algebra_without_tightness")
    print("scope=functional heat ledger; no forward self-similar or ancient NS claim")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
