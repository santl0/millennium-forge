#!/usr/bin/env python3
"""Exact audit of the finite-measure weak-L3 to L2 inclusion.

Only the Python standard library is used.  Every mathematical comparison is
performed with fractions.Fraction; decimal output is diagnostic only.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path


@dataclass(frozen=True)
class StepProfile:
    """A finite atomic representation of a decreasing rearrangement."""

    q: Q
    amplitudes: tuple[Q, ...]
    masses: tuple[Q, ...]


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, left: object, right: object) -> None:
        self.assertions += 1
        assert left == right, (left, right)

    def true(self, statement: bool) -> None:
        self.assertions += 1
        assert statement


def staircase(m: int, n: int) -> StepProfile:
    """Return the unit-volume q-staircase from the audit specification."""
    if m < 1 or n < 1:
        raise ValueError("m and n must be positive")
    q = Q(m + 1, m)
    amplitudes = tuple(q**k for k in range(n + 1))
    masses = tuple(
        q ** (-3 * k) - q ** (-3 * (k + 1)) for k in range(n)
    ) + (q ** (-3 * n),)
    return StepProfile(q=q, amplitudes=amplitudes, masses=masses)


def cumulative_from(profile: StepProfile, k: int) -> Q:
    """Mass on levels with amplitude at least q**k."""
    return sum(profile.masses[k:], Q(0))


def strict_distribution_at_level(profile: StepProfile, k: int) -> Q:
    """Mass on levels with amplitude strictly greater than q**k."""
    return sum(profile.masses[k + 1 :], Q(0))


def weak_l3_cube(profile: StepProfile) -> Q:
    """Compute sup_lambda lambda**3 mu(|f|>lambda) via left limits."""
    return max(
        amplitude**3 * cumulative_from(profile, k)
        for k, amplitude in enumerate(profile.amplitudes)
    )


def l2_square(profile: StepProfile) -> Q:
    return sum(
        (amplitude**2) * mass
        for amplitude, mass in zip(profile.amplitudes, profile.masses)
    )


def l2_formula(m: int, n: int) -> Q:
    r = Q(m, m + 1)
    return (1 + r + r**2) * (1 - r**n) + r**n


def gap_formula(m: int, n: int) -> Q:
    r = Q(m, m + 1)
    return (2 - r - r**2) + (r + r**2) * r**n


def scaled_quantities(
    profile: StepProfile, *, scale_root: Q, radius: Q, weak_bound: Q
) -> tuple[Q, Q, Q]:
    """Return volume, weak-L3 cube and L2 square after exact scaling.

    beta = scale_root**3 and V = beta*radius**3.  Amplitudes are multiplied
    by weak_bound/(scale_root*radius), masses by V.
    """
    volume = (scale_root * radius) ** 3
    amplitude_factor = weak_bound / (scale_root * radius)
    scaled_masses = tuple(volume * mass for mass in profile.masses)
    scaled_amplitudes = tuple(
        amplitude_factor * amplitude for amplitude in profile.amplitudes
    )
    weak_cube = max(
        scaled_amplitudes[k] ** 3 * sum(scaled_masses[k:], Q(0))
        for k in range(len(scaled_amplitudes))
    )
    l2_sq = sum(
        amplitude**2 * mass
        for amplitude, mass in zip(scaled_amplitudes, scaled_masses)
    )
    return volume, weak_cube, l2_sq


def profile_audit(audit: Audit) -> None:
    for m in (1, 2, 3, 5, 8, 13, 21, 34):
        for n in (1, 2, 3, 5, 8, 13):
            profile = staircase(m, n)
            q = profile.q
            audit.equal(sum(profile.masses, Q(0)), Q(1))
            audit.equal(weak_l3_cube(profile), Q(1))
            audit.equal(l2_square(profile), l2_formula(m, n))
            audit.equal(Q(3) - l2_square(profile), gap_formula(m, n))
            audit.true(l2_square(profile) < 3)
            for k in range(n + 1):
                audit.equal(cumulative_from(profile, k), q ** (-3 * k))
                expected_strict = q ** (-3 * (k + 1)) if k < n else Q(0)
                audit.equal(strict_distribution_at_level(profile, k), expected_strict)


def scaling_audit(audit: Audit) -> None:
    profile = staircase(7, 11)
    unit_l2 = l2_square(profile)
    for scale_root in (Q(1, 5), Q(1, 2), Q(1), Q(3, 2), Q(7, 3)):
        beta = scale_root**3
        for radius in (Q(1, 1024), Q(3, 7), Q(1), Q(11), Q(1024)):
            for weak_bound in (Q(1, 9), Q(1), Q(7, 4)):
                volume, weak_cube, scaled_l2 = scaled_quantities(
                    profile,
                    scale_root=scale_root,
                    radius=radius,
                    weak_bound=weak_bound,
                )
                audit.equal(volume, beta * radius**3)
                audit.equal(weak_cube, weak_bound**3)
                audit.equal(scaled_l2, weak_bound**2 * scale_root * radius * unit_l2)
                audit.true(scaled_l2 <= 3 * weak_bound**2 * scale_root * radius)
                audit.equal(
                    3 * weak_bound**2 * scale_root * radius - scaled_l2,
                    weak_bound**2
                    * scale_root
                    * radius
                    * gap_formula(7, 11),
                )


def absolute_concentration_audit(audit: Audit) -> None:
    """Separate absolute core bounds from relative weak-L3 capture."""
    for gamma in (Q(1, 100), Q(1, 3), Q(2)):
        for multiplier in (Q(1), Q(3, 2), Q(10)):
            global_weak_bound = multiplier * gamma
            local_weak_bound = gamma
            audit.true(local_weak_bound <= global_weak_bound)
            audit.true(
                local_weak_bound / global_weak_bound
                >= gamma / global_weak_bound
            )

        # The same algebra after squaring the local L2 Morrey coefficient.
        for radius in (Q(1, 128), Q(1), Q(37)):
            for multiplier in (Q(1), Q(3, 2), Q(10)):
                global_bound = multiplier * gamma
                core = gamma * radius
                total = global_bound * radius
                audit.true(core <= total)
                audit.true(core / total >= gamma / global_bound)

        fraction_cubes = []
        for j in range(1, 13):
            remote_weak_bound = Q(2**j)
            local_weak_bound = gamma
            # Exact realization: disjoint constant-amplitude packets of
            # volumes gamma^3 and T^3.  The capture fraction cubed is
            # gamma^3/(gamma^3+T^3), so no radical is evaluated.
            fraction_cube = local_weak_bound**3 / (
                local_weak_bound**3 + remote_weak_bound**3
            )
            fraction_cubes.append(fraction_cube)
            audit.true(
                fraction_cube
                <= (local_weak_bound / remote_weak_bound) ** 3
            )
        audit.true(
            all(b < a for a, b in zip(fraction_cubes, fraction_cubes[1:]))
        )
        audit.true(fraction_cubes[-1] < Q(1, 10**9))


def main() -> None:
    audit = Audit()
    profile_audit(audit)
    scaling_audit(audit)
    absolute_concentration_audit(audit)

    exact_sample = staircase(8, 64)
    sample_l2 = l2_square(exact_sample)
    sample_gap = Q(3) - sample_l2
    approach = []
    for m in (2, 4, 8, 16, 32, 64, 128):
        n = 16 * m
        value = l2_formula(m, n)
        gap = gap_formula(m, n)
        audit.equal(Q(3) - value, gap)
        approach.append((m, n, value, gap))
    audit.true(all(b[2] > a[2] for a, b in zip(approach, approach[1:])))
    audit.true(approach[-1][3] < Q(3, 100))

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("type_i_capture_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("identity=L2^2=(1+q^-1+q^-2)(1-q^-N)+q^-N")
    print("bound=L2^2<3 and sup_{m,N} L2^2=3")
    print(f"sample_m=8 sample_N=64 L2^2={sample_l2}")
    print(f"sample_exact_gap={sample_gap}")
    for m, n, value, gap in approach:
        print(
            f"approach m={m:3d} N={n:4d} "
            f"L2^2={float(value):.12f} gap={float(gap):.12f}"
        )
    print("scaling=V=beta*R^3 with beta=s^3; error=K^2*s*R*(3-L2^2)")
    print("adverse=disjoint exact packets force core/global to zero without M")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
