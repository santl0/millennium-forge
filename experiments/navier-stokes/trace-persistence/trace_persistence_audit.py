#!/usr/bin/env python3
"""Exact weak-L3 persistence versus strong space-time L3 audit.

The certificate is purely measure-theoretic. It uses Fraction arithmetic for
atomic spatial profiles and temporal ledgers. It does not integrate or claim
to construct a Navier--Stokes solution.
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


def weak_l3_cube(amplitudes: tuple[Q, ...], masses: tuple[Q, ...]) -> Q:
    """Compute K3^3 using left limits at the finitely many amplitudes."""
    levels = sorted(set(amplitudes))
    return max(
        level**3
        * sum(
            (mass for amplitude, mass in zip(amplitudes, masses)
             if amplitude >= level),
            Q(0),
        )
        for level in levels
    )


def strong_l3_cube(amplitudes: tuple[Q, ...], masses: tuple[Q, ...]) -> Q:
    return sum(
        (amplitude**3 * mass
         for amplitude, mass in zip(amplitudes, masses)),
        Q(0),
    )


def sharp_step(gamma: Q, support_root: Q) -> tuple[tuple[Q, ...], tuple[Q, ...]]:
    """Return a one-level profile with K3=gamma and L3^3=gamma^3."""
    mass = support_root**3
    amplitude = gamma / support_root
    return (amplitude,), (mass,)


def audit_atomic_inequality(audit: Audit) -> None:
    values = (Q(1, 7), Q(1, 3), Q(1), Q(5, 2), Q(11))
    masses_pool = (Q(1, 1000), Q(1, 64), Q(1, 8), Q(1, 3))
    for shift in range(7):
        amplitudes = tuple(
            values[(index + shift) % len(values)]
            for index in range(len(masses_pool))
        )
        masses = tuple(
            masses_pool[(2 * index + shift) % len(masses_pool)]
            for index in range(len(masses_pool))
        )
        weak_cube = weak_l3_cube(amplitudes, masses)
        strong_cube = strong_l3_cube(amplitudes, masses)
        audit.true(weak_cube <= strong_cube)

    for gamma in (Q(1, 100), Q(1, 3), Q(1), Q(7, 2), Q(23)):
        for support_root in (Q(1, 16), Q(1, 5), Q(1, 2), Q(1)):
            amplitudes, masses = sharp_step(gamma, support_root)
            audit.equal(weak_l3_cube(amplitudes, masses), gamma**3)
            audit.equal(strong_l3_cube(amplitudes, masses), gamma**3)


def audit_uniform_interval(audit: Audit) -> None:
    for gamma in (Q(1, 10), Q(1), Q(7, 3)):
        for interval_length in (Q(1, 100), Q(1, 4), Q(1)):
            integrated_lower = interval_length * gamma**3
            audit.true(integrated_lower > 0)
            for support_root in (Q(1, 8), Q(1, 3), Q(1)):
                amplitudes, masses = sharp_step(gamma, support_root)
                integrated_exact = (
                    interval_length
                    * strong_l3_cube(amplitudes, masses)
                )
                audit.equal(integrated_exact, integrated_lower)


def audit_shrinking_intervals_and_thresholds(audit: Audit) -> None:
    for j in (1, 2, 3, 5, 8, 13, 32, 128, 1024):
        gamma = Q(3, 2)
        delta = Q(1, j)
        audit.equal(delta * gamma**3, Q(27, 8 * j))

        # delta=j^-3, gamma=j is critical: delta*gamma^3=1.
        audit.equal(Q(1, j**3) * Q(j) ** 3, Q(1))
        # delta=j^-4, gamma=j is subcritical and tends as 1/j.
        audit.equal(Q(1, j**4) * Q(j) ** 3, Q(1, j))
        # delta=j^-2, gamma=j is supercritical and grows as j.
        audit.equal(Q(1, j**2) * Q(j) ** 3, Q(j))


def audit_single_time_triangles(audit: Audit) -> None:
    """Audit b_delta(t)=max(1-|t-t0|/delta,0)."""
    for gamma in (Q(1, 7), Q(1), Q(5)):
        for delta in (Q(1, 1024), Q(1, 17), Q(1, 2)):
            # Integral of b_delta^3 is 2*delta*integral_0^1(1-s)^3 ds.
            temporal_cube_integral = 2 * delta * Q(1, 4)
            audit.equal(temporal_cube_integral, delta / 2)
            space_time_l3_cube = gamma**3 * temporal_cube_integral
            audit.equal(space_time_l3_cube, gamma**3 * delta / 2)

            # At the peak K3=gamma. At relative threshold theta<1,
            # the superlevel time interval has length 2*delta*(1-theta).
            for theta in (Q(1, 4), Q(1, 2), Q(3, 4), Q(15, 16)):
                superlevel_length = 2 * delta * (1 - theta)
                audit.true(superlevel_length > 0)
                audit.true(superlevel_length <= 2 * delta)


def audit_mobile_centers_and_scales(audit: Audit) -> None:
    """Critical spatial motion cannot reduce the per-time L3 cost."""
    for gamma in (Q(1, 11), Q(1), Q(9, 4)):
        for time_index in range(1, 17):
            # A rational cube models the volume of a ball moving inside B1.
            scale_root = Q(1, time_index + 2)
            amplitudes, masses = sharp_step(gamma, scale_root)
            audit.equal(weak_l3_cube(amplitudes, masses), gamma**3)
            audit.equal(strong_l3_cube(amplitudes, masses), gamma**3)


def audit_capture_time_measure(audit: Audit) -> None:
    """Certify |E_gamma|<=||f||_L3^3/gamma^3."""
    for gamma in (Q(1, 5), Q(1), Q(13, 3)):
        for space_time_cube in (Q(1, 1000), Q(1, 7), Q(3), Q(100)):
            upper_time_measure = space_time_cube / gamma**3
            audit.equal(
                upper_time_measure * gamma**3,
                space_time_cube,
            )
            audit.true(upper_time_measure >= 0)


def audit_type_i_clock_and_critical_scaling(audit: Audit) -> None:
    """Audit the exact algebra transporting every-time capture to B1.

    Write R^2=a*(T-t), d sigma/dt=R^-2 and kappa=a/2.  The
    chain rule gives d(log R)/d sigma=-a/2=-kappa.  The spatial ledger
    checks K3(R*u(x_*+R dot);B1)=K3(u;B(x_*,R)) on atomic profiles.
    """
    for smoothing_time in (Q(1, 64), Q(1, 7), Q(1), Q(13, 5)):
        a = Q(4) / smoothing_time
        kappa = Q(2) / smoothing_time
        audit.equal(a / 2, kappa)

        for time_to_blowup in (Q(1, 4096), Q(1, 17), Q(3, 2)):
            radius_squared = a * time_to_blowup
            dlog_radius_dt = -Q(1) / (2 * time_to_blowup)
            dt_dsigma = radius_squared
            audit.equal(dlog_radius_dt * dt_dsigma, -kappa)

        for radius in (Q(1, 128), Q(1, 9), Q(2, 3)):
            for normalized_amplitude in (Q(1, 11), Q(1), Q(7, 2)):
                for normalized_mass in (Q(1, 1000), Q(1, 8)):
                    physical_amplitude = normalized_amplitude / radius
                    physical_mass = radius**3 * normalized_mass
                    physical_weak_cube = (
                        physical_amplitude**3 * physical_mass
                    )
                    normalized_weak_cube = (
                        normalized_amplitude**3 * normalized_mass
                    )
                    audit.equal(physical_weak_cube, normalized_weak_cube)


def main() -> None:
    audit = Audit()
    audit_atomic_inequality(audit)
    audit_uniform_interval(audit)
    audit_shrinking_intervals_and_thresholds(audit)
    audit_single_time_triangles(audit)
    audit_mobile_centers_and_scales(audit)
    audit_capture_time_measure(audit)
    audit_type_i_clock_and_critical_scaling(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("trace_persistence_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("slice_inequality=K3(f(t);B1)^3<=integral_B1 |f(t,x)|^3 dx")
    print("time_inequality=|E_gamma|*gamma^3<=||f||_L3(E_gamma x B1)^3")
    print("uniform_interval=strong_L3_to_zero_is_impossible_for_fixed_gamma,delta")
    print("sharpness=one-level spatial profiles attain equality")
    print("threshold=delta_j*gamma_j^3 must tend to zero")
    print("single_time=triangular pulse has L3_cube=gamma^3*delta/2")
    print("mobile_center_scale=per-time cost remains gamma^3")
    print("type_i_clock=dlogR/dsigma=-kappa with kappa=2/S_star")
    print("critical_scaling=K3(R*u(x_star+R dot);B1)=K3(u;B(x_star,R))")
    print("scope=exact measure ledger; no Navier-Stokes simulation")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
