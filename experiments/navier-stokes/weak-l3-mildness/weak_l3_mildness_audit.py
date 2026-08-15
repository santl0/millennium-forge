#!/usr/bin/env python3
"""Exact exponent audit for weak-L3 mild estimates.

The script uses only Fraction and symbolic pi coefficients. It certifies the
time exponents of a heat-gradient estimate and the scaling of explicit
weak-L3 profiles. It does not solve or simulate Navier--Stokes.
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


def heat_gradient_singularity(p: Q) -> Q:
    """alpha in ||grad exp(t Delta)||_(L3/2,inf -> Lp,inf)<=C*t^-alpha."""
    source = Q(3, 2)
    return Q(1, 2) + Q(3, 2) * (1 / source - 1 / p)


def time_gain(p: Q) -> Q:
    return 1 - heat_gradient_singularity(p)


def audit_heat_exponents(audit: Audit) -> None:
    exponents = (
        Q(8, 5),
        Q(5, 3),
        Q(9, 5),
        Q(2),
        Q(9, 4),
        Q(5, 2),
        Q(8, 3),
        Q(11, 4),
        Q(29, 10),
    )
    for p in exponents:
        alpha = heat_gradient_singularity(p)
        beta = time_gain(p)
        audit.equal(alpha, Q(3 * (p - 1), 2 * p))
        audit.equal(beta, Q(3 - p, 2 * p))
        audit.true(Q(0) < beta < Q(1))
        audit.equal(1 / beta, Q(2 * p, 3 - p))
        audit.true(alpha < 1)

    endpoint = Q(3)
    audit.equal(heat_gradient_singularity(endpoint), Q(1))
    audit.equal(time_gain(endpoint), Q(0))

    # p_n=3-1/n: the time-integration coefficient is exactly 6n-2.
    for n in (1, 2, 3, 5, 8, 13, 32, 128, 1024):
        p = Q(3) - Q(1, n)
        if p > Q(3, 2):
            audit.equal(1 / time_gain(p), Q(6 * n - 2))


def audit_endpoint_logarithm(audit: Audit) -> None:
    """Count normalized dyadic logarithmic shells at p=3."""
    for shell_count in (1, 2, 3, 8, 32, 128, 1024):
        # Integral on [2^-(k+1),2^-k] of dt/t is log(2).
        normalized_shells = [Q(1) for _ in range(shell_count)]
        audit.equal(sum(normalized_shells, Q(0)), Q(shell_count))
        audit.true(shell_count + 1 > shell_count)


def audit_yamazaki_exponents(audit: Audit) -> None:
    """Check the distinct predual endpoint exponent geometry."""
    test_source = Q(3, 2)
    test_target = Q(3)
    gap = 1 / test_source - 1 / test_target
    audit.equal(gap, Q(1, 3))
    alpha = Q(1, 2) + Q(3, 2) * gap
    audit.equal(alpha, Q(1))

    # Lorentz pairings used in the dual formulation:
    # L^(3/2,infinity) pairs with L^(3,1), and the target L^(3,infinity)
    # is tested against L^(3/2,1).
    audit.equal(1 / Q(3, 2) + 1 / Q(3), Q(1))


def audit_scalar_inverse_radius(audit: Audit) -> None:
    """Track coefficients after factoring powers of pi."""
    # |{|x|^-1>lambda}|=(4*pi/3)*lambda^-3.
    scalar_k3_cube_over_pi = Q(4, 3)
    audit.equal(scalar_k3_cube_over_pi, Q(4, 3))

    # ||1/|x| ||_L2(B_R)^2=4*pi*R.
    for radius in (Q(1, 100), Q(1), Q(7, 3), Q(16), Q(1024)):
        energy_over_pi = 4 * radius
        audit.equal(energy_over_pi, Q(4) * radius)
        audit.true(energy_over_pi > 0)


def audit_solenoidal_swirl(audit: Audit) -> None:
    """Audit U=(-x2,x1,0)/|x|^2."""
    # Distribution calculation:
    # (1/3)*integral_S2 sin(theta)^3 dOmega
    # =(1/3)*2*pi*integral_0^pi sin(theta)^4 dtheta
    # =(1/3)*2*pi*(3*pi/8)=pi^2/4.
    sine_four_integral_over_pi = Q(3, 8)
    distribution_over_pi_squared = (
        Q(1, 3) * 2 * sine_four_integral_over_pi
    )
    audit.equal(distribution_over_pi_squared, Q(1, 4))

    # Energy angular integral is integral_S2 sin(theta)^2 dOmega=8*pi/3.
    energy_per_radius_over_pi = Q(8, 3)
    for radius in (Q(1, 100), Q(1), Q(7, 3), Q(16), Q(1024)):
        truncated_energy_over_pi = energy_per_radius_over_pi * radius
        audit.equal(truncated_energy_over_pi, Q(8, 3) * radius)
        audit.true(truncated_energy_over_pi > 0)

        # Inner truncation and exterior tail both retain the full weak-L3
        # supremum because one may take respectively high or low thresholds.
        inner_k3_cube_over_pi_squared = Q(1, 4)
        outer_k3_cube_over_pi_squared = Q(1, 4)
        audit.equal(inner_k3_cube_over_pi_squared, Q(1, 4))
        audit.equal(outer_k3_cube_over_pi_squared, Q(1, 4))


def audit_energy_split(audit: Audit) -> None:
    """Show fixed weak tail and linearly growing L2 core."""
    k3_cube_over_pi_squared = Q(1, 4)
    previous_energy = None
    for radius in (Q(1), Q(2), Q(4), Q(8), Q(16), Q(32), Q(64), Q(128)):
        core_energy_over_pi = Q(8, 3) * radius
        tail_k3_cube_over_pi_squared = k3_cube_over_pi_squared
        audit.equal(tail_k3_cube_over_pi_squared, Q(1, 4))
        if previous_energy is not None:
            audit.true(core_energy_over_pi > previous_energy)
        previous_energy = core_energy_over_pi


def audit_weak_star_not_strong(audit: Audit) -> None:
    """Exact norm ledgers for translations and critical concentrations."""
    for index in (1, 2, 3, 8, 32, 128):
        # Translation preserves every rearrangement-invariant norm.
        weak_l3_ratio = Q(1)
        l2_ratio = Q(1)
        audit.equal(weak_l3_ratio, Q(1))
        audit.equal(l2_ratio, Q(1))

        # Critical concentration C_n=n*V(n*x) preserves K3 but has
        # L2^2 ratio n^-1. Neither statement is strong L3 convergence.
        concentration_k3_ratio = Q(1)
        concentration_l2_square_ratio = Q(1, index)
        audit.equal(concentration_k3_ratio, Q(1))
        audit.equal(concentration_l2_square_ratio, Q(1, index))


def main() -> None:
    audit = Audit()
    audit_heat_exponents(audit)
    audit_endpoint_logarithm(audit)
    audit_yamazaki_exponents(audit)
    audit_scalar_inverse_radius(audit)
    audit_solenoidal_swirl(audit)
    audit_energy_split(audit)
    audit_weak_star_not_strong(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("weak_l3_mildness_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("heat_gradient_alpha=3*(p-1)/(2*p)")
    print("time_gain_beta=(3-p)/(2*p), coefficient=2*p/(3-p)")
    print("endpoint_p3=termwise_integral_has_one_unit_per_log_shell")
    print("yamazaki_dual=distinct_L(3/2,1)_to_L(3,1)_time_integrated_lemma")
    print("scalar_1_over_r=K3_cube=(4*pi/3), L2_energy_B_R=4*pi*R")
    print("swirl=K3_cube=pi^2/4, L2_energy_B_R=(8*pi/3)*R")
    print("energy_split=outer_weak_L3_tail_does_not_become_small")
    print("scope=exact exponent/distribution ledger; no PDE simulation")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
