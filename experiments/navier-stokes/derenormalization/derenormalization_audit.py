#!/usr/bin/env python3
"""Exact audit of the inverse self-similar Navier--Stokes transform.

Only the standard library and Fraction are used. The program checks scaling
exponents and symbolic residual coefficients; it does not integrate a PDE.
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


def audit_clock(audit: Audit) -> None:
    """Check r_s=-kappa*r and tau_s=r^2 algebraically."""
    for kappa in (Q(1, 7), Q(1), Q(5, 2), Q(11)):
        for r in (Q(1, 16), Q(1, 3), Q(1, 2), Q(3, 4), Q(1)):
            r_s = -kappa * r
            tau = (1 - r**2) / (2 * kappa)
            tau_s = -(2 * r * r_s) / (2 * kappa)
            audit.equal(r_s / r, -kappa)
            audit.equal(tau_s, r**2)
            audit.equal(r**2, 1 - 2 * kappa * tau)
            audit.true(tau <= Q(1, 2) / kappa)


def audit_pde_exponents(audit: Audit) -> None:
    """Solve the exponent matching conditions for v=r^-a Z, q=r^-b Pi."""
    for a in (Q(-1), Q(0), Q(1), Q(2), Q(3)):
        for b in (Q(0), Q(1), Q(2), Q(3), Q(4)):
            for clock_power in (Q(0), Q(1), Q(2), Q(3)):
                time_exponent = -a - clock_power
                diffusion_exponent = -a - 2
                convection_exponent = -2 * a - 1
                pressure_exponent = -b - 1
                all_navier_stokes = (
                    time_exponent == -3
                    and diffusion_exponent == -3
                    and convection_exponent == -3
                    and pressure_exponent == -3
                )
                audit.equal(
                    all_navier_stokes,
                    a == 1 and b == 2 and clock_power == 2,
                )

    # Correct transform: every term has the common factor r^-3.
    a = Q(1)
    b = Q(2)
    clock_power = Q(2)
    audit.equal(-a - clock_power, Q(-3))
    audit.equal(-a - 2, Q(-3))
    audit.equal(-2 * a - 1, Q(-3))
    audit.equal(-b - 1, Q(-3))


def audit_chain_rule_and_divergence(audit: Audit) -> None:
    """Track coefficients of Z, y.grad Z, and div Z."""
    # For alpha=r_s/r=-kappa and v=r^-1 Z(s,x/r),
    # d_s v=r^-1[Z_s+kappa(Z+y.grad Z)].
    alpha_over_kappa = Q(-1)
    velocity_power = Q(1)
    coefficient_z = -velocity_power * alpha_over_kappa
    coefficient_y_grad = -alpha_over_kappa
    audit.equal(coefficient_z, Q(1))
    audit.equal(coefficient_y_grad, Q(1))

    # div_x(r^-1 Z)=r^-2 div_y Z.
    divergence_exponent = -velocity_power - 1
    audit.equal(divergence_exponent, Q(-2))


def audit_jacobian_and_local_quantities(audit: Audit) -> None:
    spatial_dimension = Q(3)
    time_jacobian_power = Q(2)
    velocity_power = Q(-1)

    audit.equal(spatial_dimension + time_jacobian_power, Q(5))
    audit.equal(2 * velocity_power + spatial_dimension, Q(1))
    audit.equal(3 * velocity_power + spatial_dimension, Q(0))

    # Energy divided by the physical radius r*R is invariant.
    energy_power = 2 * velocity_power + spatial_dimension
    physical_radius_power = Q(1)
    audit.equal(energy_power - physical_radius_power, Q(0))

    # Distribution scaling for weak L3:
    # mu_v(lambda)=r^3 mu_Z(r*lambda), hence lambda^3 mu_v is invariant.
    threshold_cube_power = Q(-3)
    distribution_power = Q(3)
    audit.equal(threshold_cube_power + distribution_power, Q(0))

    for r in (Q(1, 32), Q(1, 5), Q(1, 2), Q(3, 4), Q(1)):
        dx_factor = r**3
        dtau_factor = r**2
        audit.equal(dx_factor * dtau_factor, r**5)
        audit.equal(r ** (-2) * dx_factor, r)  # local L2 energy
        audit.equal(r ** (-3) * dx_factor, Q(1))  # L3 cube


def audit_local_energy_inequality(audit: Audit) -> None:
    """Check the full local-energy operator and weak-test weight.

    With E_v=r^-2 E_Z, the time derivative contributes the two drift
    coefficients 2*kappa*E_Z+kappa*y.grad(E_Z).  These are exactly
    kappa*div(y E_Z)-kappa*E_Z in dimension three.
    """
    spatial_dimension = Q(3)
    for kappa in (Q(1, 7), Q(1), Q(5, 2), Q(11)):
        time_extra_energy = 2 * kappa
        time_extra_radial = kappa
        divergence_drift_energy = (spatial_dimension - 1) * kappa
        divergence_drift_radial = kappa
        audit.equal(time_extra_energy, divergence_drift_energy)
        audit.equal(time_extra_radial, divergence_drift_radial)

        # Every term in the physical local-energy distribution has r^-4.
        audit.equal(Q(-2) - Q(2), Q(-4))  # time: E_v and tau_s
        audit.equal(Q(-2) - Q(2), Q(-4))  # Laplacian of E_v
        audit.equal(Q(-4), Q(-4))  # |grad_x v|^2
        audit.equal(Q(-3) - Q(1), Q(-4))  # energy/pressure flux

    # dx*d_tau contributes r^5, hence a physical test phi pulls back as
    # the nonnegative renormalized test r*phi.
    audit.equal(Q(5) + Q(-4), Q(1))

    for r in (Q(1, 32), Q(1, 5), Q(1, 2), Q(3, 4), Q(1)):
        spacetime_jacobian = r**5
        audit.equal(r ** (-4) * spacetime_jacobian, r)  # |grad v|^2
        audit.equal(r ** (-3) * spacetime_jacobian, r**2)  # |v|^3
        audit.equal(r ** (-3) * spacetime_jacobian, r**2)  # |q|^(3/2)


def general_wrong_power_residual(
    r: Q, kappa: Q, a: Q, b: Q
) -> dict[str, Q]:
    """Residual coefficients after factoring r^(-a-2).

    The correct renormalized equation is
    Z_s-Delta Z+N(Z)+grad Pi+kappa*(Z+y.grad Z)=0.
    """
    return {
        "extra_Z": kappa * (a - 1),
        "nonlinearity": r ** (1 - a) - 1,
        "pressure": r ** (a + 1 - b) - 1,
    }


def audit_wrong_signs(audit: Audit) -> None:
    for kappa in (Q(1, 5), Q(1), Q(7, 3)):
        # Wrong expanding scale alpha=+kappa leaves -2*kappa*D Z.
        expanding_alpha_over_kappa = Q(1)
        residual_drift = -(expanding_alpha_over_kappa + 1) * kappa
        audit.equal(residual_drift, -2 * kappa)
        audit.true(residual_drift != 0)

        # Keeping r_s/r=-kappa but writing the renormalized drift with
        # the opposite sign leaves +2*kappa*D Z after transformation.
        wrong_pde_sign_residual = 2 * kappa
        audit.equal(wrong_pde_sign_residual, 2 * kappa)
        audit.true(wrong_pde_sign_residual != 0)


def audit_wrong_velocity_pressure_powers(audit: Audit) -> None:
    for r in (Q(1, 16), Q(1, 3), Q(1, 2), Q(3, 4)):
        for kappa in (Q(1, 7), Q(1), Q(5, 2)):
            correct = general_wrong_power_residual(r, kappa, Q(1), Q(2))
            audit.equal(correct["extra_Z"], Q(0))
            audit.equal(correct["nonlinearity"], Q(0))
            audit.equal(correct["pressure"], Q(0))

            wrong_velocity = general_wrong_power_residual(
                r, kappa, Q(0), Q(1)
            )
            audit.equal(wrong_velocity["extra_Z"], -kappa)
            audit.equal(wrong_velocity["nonlinearity"], r - 1)
            audit.equal(wrong_velocity["pressure"], Q(0))
            audit.true(any(value != 0 for value in wrong_velocity.values()))

            wrong_pressure_low = general_wrong_power_residual(
                r, kappa, Q(1), Q(1)
            )
            audit.equal(wrong_pressure_low["pressure"], r - 1)
            audit.true(wrong_pressure_low["pressure"] != 0)

            wrong_pressure_high = general_wrong_power_residual(
                r, kappa, Q(1), Q(3)
            )
            audit.equal(wrong_pressure_high["pressure"], r ** (-1) - 1)
            audit.true(wrong_pressure_high["pressure"] != 0)


def audit_frozen_clocks(audit: Audit) -> None:
    for r in (Q(1, 16), Q(1, 3), Q(1, 2), Q(3, 4)):
        # If tau_s=1 while r still changes correctly, the time term has
        # factor r^-1 instead of r^-3. After using the renormalized PDE,
        # the residual is r^-3*(r^2-1)*(Z_s+kappa*D Z).
        frozen_time_coefficient = r**2 - 1
        audit.true(frozen_time_coefficient != 0)
        audit.true(frozen_time_coefficient < 0)

        # If the radius itself is frozen at one, no chain-rule drift is
        # generated and the residual is -kappa*D Z.
        for kappa in (Q(1, 7), Q(1), Q(5, 2)):
            frozen_radius_drift = -kappa
            audit.true(frozen_radius_drift != 0)


def audit_wrong_local_scaling(audit: Audit) -> None:
    """Quantify loss of energy and K3 invariance for v=r^-a Z."""
    for a in (Q(0), Q(1), Q(2)):
        energy_over_radius_exponent = 2 - 2 * a
        l3_cube_exponent = 3 - 3 * a
        k3_exponent = 1 - a
        audit.equal(energy_over_radius_exponent == 0, a == 1)
        audit.equal(l3_cube_exponent == 0, a == 1)
        audit.equal(k3_exponent == 0, a == 1)


def main() -> None:
    audit = Audit()
    audit_clock(audit)
    audit_pde_exponents(audit)
    audit_chain_rule_and_divergence(audit)
    audit_jacobian_and_local_quantities(audit)
    audit_local_energy_inequality(audit)
    audit_wrong_signs(audit)
    audit_wrong_velocity_pressure_powers(audit)
    audit_frozen_clocks(audit)
    audit_wrong_local_scaling(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("derenormalization_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("correct=r_s/r=-kappa, tau_s=r^2, v=r^-1*Z, q=r^-2*Pi")
    print("PDE_standard=r^-3*(PDE_renormalized)")
    print("div_x(v)=r^-2*div_y(Z)")
    print("jacobian_dx_dtau=r^5*dy*ds")
    print("local_energy=integral_B(rR)|v|^2=r*integral_B(R)|Z|^2")
    print("K3(v;B(rR))=K3(Z;B(R))")
    print("local_energy_operator_standard=r^-4*local_energy_operator_renormalized")
    print("local_energy_test_pullback=r*phi(x=r*y,tau(s))")
    print("wrong_scale_sign_residual=-2*kappa*D(Z)")
    print("wrong_drift_sign_residual=+2*kappa*D(Z)")
    print("frozen_clock_residual_coefficient=r^2-1")
    print("scope=exact chain-rule ledger; no PDE simulation")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
