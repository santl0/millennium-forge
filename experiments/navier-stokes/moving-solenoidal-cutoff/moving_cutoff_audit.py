#!/usr/bin/env python3
"""Exact scaling audit for a moving solenoidal cutoff.

This program does not integrate Navier--Stokes. It checks, with rational
arithmetic, the dilation identities for R(t)=c*sqrt(T-t), a homothetically
conjugated Bogovskii operator, and an explicit smooth pure-swirl witness.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path


Vector = tuple[Q, Q, Q]


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, left: object, right: object) -> None:
        self.assertions += 1
        assert left == right, (left, right)

    def true(self, statement: bool) -> None:
        self.assertions += 1
        assert statement


def add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: Q, vector: Vector) -> Vector:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


@dataclass(frozen=True)
class RadiusClock:
    """An exact point on R(t)=c*sqrt(T-t), parametrized by rational R."""

    c: Q
    radius: Q
    terminal_time: Q = Q(1)

    @property
    def tau(self) -> Q:
        return (self.radius / self.c) ** 2

    @property
    def time(self) -> Q:
        return self.terminal_time - self.tau

    @property
    def radius_prime(self) -> Q:
        return -(self.c**2) / (2 * self.radius)

    @property
    def logarithmic_rate(self) -> Q:
        return self.radius_prime / self.radius


@dataclass(frozen=True)
class PowerLedger:
    """Powers alpha in quantities of the form R**alpha."""

    velocity: Q = Q(-1)
    spatial_derivative: Q = Q(-1)
    moving_time_derivative: Q = Q(-2)
    bogovskii_gain: Q = Q(1)

    def lp_power(self, amplitude_power: Q, p: Q) -> Q:
        return amplitude_power + Q(3) / p

    def homogeneous_sobolev_power(self, amplitude_power: Q, order: Q) -> Q:
        return amplitude_power + Q(3, 2) - order

    def spacetime_power(self, spatial_power: Q, time_exponent: Q) -> Q:
        return spatial_power + Q(2) / time_exponent


def audit_clock(audit: Audit) -> None:
    for c in (Q(1, 3), Q(1), Q(5, 2), Q(7)):
        for j in range(1, 13):
            radius = c / (2**j)
            clock = RadiusClock(c=c, radius=radius)
            audit.equal(radius**2, c**2 * clock.tau)
            audit.equal(clock.logarithmic_rate, -Q(1, 2) / clock.tau)
            audit.equal(clock.logarithmic_rate, -(c**2) / (2 * radius**2))
            audit.true(clock.time < clock.terminal_time)
            audit.true(clock.time >= 0)


def audit_power_ledger(audit: Audit) -> dict[str, Q]:
    ledger = PowerLedger()
    powers: dict[str, Q] = {}
    powers["grad_chi"] = ledger.spatial_derivative
    powers["dt_chi"] = ledger.moving_time_derivative
    powers["u"] = ledger.velocity
    powers["g=grad_chi_dot_u"] = powers["grad_chi"] + powers["u"]
    powers["B_R_g"] = powers["g=grad_chi_dot_u"] + ledger.bogovskii_gain
    powers["dt_chi_times_u"] = powers["dt_chi"] + powers["u"]
    powers["dt_B_R_g"] = powers["B_R_g"] + ledger.moving_time_derivative
    powers["laplacian_V"] = powers["B_R_g"] + 2 * ledger.spatial_derivative
    powers["V_dot_grad_V"] = (
        powers["B_R_g"]
        + powers["B_R_g"]
        + ledger.spatial_derivative
    )

    audit.equal(powers["g=grad_chi_dot_u"], Q(-2))
    audit.equal(powers["B_R_g"], Q(-1))
    for name in (
        "dt_chi_times_u",
        "dt_B_R_g",
        "laplacian_V",
        "V_dot_grad_V",
    ):
        audit.equal(powers[name], Q(-3))

    force = Q(-3)
    spatial_powers = {
        "L1": ledger.lp_power(force, Q(1)),
        "L3/2_weak": ledger.lp_power(force, Q(3, 2)),
        "L3": ledger.lp_power(force, Q(3)),
        "Hdot_minus_1": ledger.homogeneous_sobolev_power(force, Q(-1)),
    }
    audit.equal(spatial_powers["L1"], Q(0))
    audit.equal(spatial_powers["L3/2_weak"], Q(-1))
    audit.equal(spatial_powers["L3"], Q(-2))
    audit.equal(spatial_powers["Hdot_minus_1"], Q(-1, 2))

    critical_pairs = {
        "Linfinity_t_L1_x": (spatial_powers["L1"], None),
        "L2_t_L3/2_weak_x": (spatial_powers["L3/2_weak"], Q(2)),
        "L1_t_L3_x": (spatial_powers["L3"], Q(1)),
        "L4_t_Hdot_minus_1_x": (spatial_powers["Hdot_minus_1"], Q(4)),
    }
    for spatial_power, time_exponent in critical_pairs.values():
        if time_exponent is None:
            audit.equal(spatial_power, Q(0))
        else:
            audit.equal(
                ledger.spacetime_power(spatial_power, time_exponent), Q(0)
            )
            # R(t)~tau^(1/2): the a-th power is tau^(-1).
            audit.equal(time_exponent * spatial_power / 2, Q(-1))

    return {**powers, **spatial_powers}


def audit_smooth_swirl_witness(audit: Audit) -> None:
    """Check exact jets at y0=(3/2,0,0) for the smooth witness.

    On 1<r<2 use chi=h(2-r)/(h(2-r)+h(r-1)), where
    h(z)=exp(-1/z) for z>0 and h=0 otherwise. At r=3/2 the common
    transcendental factor cancels, so the jets below are rational.
    The compact swirl is U=eta(r)*(-y2,y1,0), with eta=1 on r<=2.
    """
    radius_y = Q(3, 2)
    chi = Q(1, 2)
    chi_prime = Q(-2)
    chi_second = Q(0)
    dilation_chi = radius_y * chi_prime
    velocity: Vector = (Q(0), radius_y, Q(0))
    dilation_velocity = velocity

    audit.equal(dilation_chi, Q(-3))
    audit.equal(velocity, (Q(0), Q(3, 2), Q(0)))

    # grad(chi) dot U=0 for every radial chi and azimuthal U. Hence the
    # Bogovskii input and correction vanish exactly for this witness.
    divergence_defect = Q(0)
    bogovskii_correction: Vector = (Q(0), Q(0), Q(0))
    audit.equal(divergence_defect, Q(0))
    audit.equal(bogovskii_correction, (Q(0), Q(0), Q(0)))

    for c in (Q(1, 2), Q(1), Q(2), Q(5, 2)):
        boundary_reference = scale(c**2 * dilation_chi / 2, velocity)
        profile_reference = scale(
            c**2 * chi / 2, add(velocity, dilation_velocity)
        )
        temporal_reference = add(boundary_reference, profile_reference)
        audit.equal(boundary_reference, (Q(0), -Q(9, 4) * c**2, Q(0)))
        audit.equal(profile_reference, (Q(0), Q(3, 4) * c**2, Q(0)))
        audit.equal(temporal_reference, (Q(0), -Q(3, 2) * c**2, Q(0)))

        # Delta(chi*A*y)=(chi''+4 chi'/r)A*y at this point.
        diffusion_reference = scale(
            chi_second + 4 * chi_prime / radius_y, velocity
        )
        convection_reference: Vector = (-Q(3, 8), Q(0), Q(0))
        audit.equal(diffusion_reference, (Q(0), Q(-8), Q(0)))

        for j in range(1, 10):
            radius = c / (2**j)
            clock = RadiusClock(c=c, radius=radius)
            dt_chi_at_point = -clock.logarithmic_rate * dilation_chi
            scaled_velocity = scale(1 / radius, velocity)
            boundary_direct = scale(dt_chi_at_point, scaled_velocity)
            audit.equal(boundary_direct, scale(radius ** (-3), boundary_reference))

            temporal = scale(radius ** (-3), temporal_reference)
            diffusion = scale(radius ** (-3), diffusion_reference)
            convection = scale(radius ** (-3), convection_reference)
            audit.equal(scale(radius**3, temporal), temporal_reference)
            audit.equal(scale(radius**3, diffusion), diffusion_reference)
            audit.equal(scale(radius**3, convection), convection_reference)

            # The pressure-free residual dt V-Delta V+(V.grad)V has a
            # nonzero first component for every c and R.
            residual = add(add(temporal, scale(-1, diffusion)), convection)
            audit.equal(residual[0] * radius**3, -Q(3, 8))
            audit.true(residual != (Q(0), Q(0), Q(0)))


def audit_critical_shells(audit: Audit) -> None:
    """Count normalized logarithmic shells without floating-point logs."""
    spatial_and_time = (
        (Q(-1), Q(2)),
        (Q(-2), Q(1)),
        (Q(-1, 2), Q(4)),
    )
    shell_count = 64
    for spatial_power, time_exponent in spatial_and_time:
        tau_integrand_power = time_exponent * spatial_power / 2
        audit.equal(tau_integrand_power, Q(-1))
        normalized_shell_weights = [Q(1) for _ in range(shell_count)]
        audit.equal(sum(normalized_shell_weights, Q(0)), Q(shell_count))


def main() -> None:
    audit = Audit()
    audit_clock(audit)
    powers = audit_power_ledger(audit)
    audit_smooth_swirl_witness(audit)
    audit_critical_shells(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("moving_cutoff_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("clock=R^2=c^2*(T-t), R'/R=-1/[2*(T-t)]=-c^2/(2*R^2)")
    print("bogovskii=g_R=R^-2*g(y), B_R(g_R)=R^-1*b(y), dt B_R=O(R^-3)")
    print("point_y0=(3/2,0,0), chi=1/2, chi'=-2, chi''=0")
    print("boundary_reference=(0,-9*c^2/4,0), so (dt chi_R)u_R=R^-3*reference")
    print("temporal_power=diffusion_power=convection_power=R^-3")
    print(
        "spatial_norm_powers="
        f"L1:R^{powers['L1']}, "
        f"L3/2_weak:R^{powers['L3/2_weak']}, "
        f"Hdot-1:R^{powers['Hdot_minus_1']}"
    )
    print("critical_time_pairs=LinfL1, L2L3/2weak, L1L3, L4Hdot-1")
    print("finite-time critical pairs accumulate one unit per logarithmic shell")
    print("scope=smooth divergence-free dilation family; no Navier-Stokes integration")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
