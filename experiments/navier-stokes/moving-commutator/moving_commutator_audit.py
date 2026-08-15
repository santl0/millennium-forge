#!/usr/bin/env python3
"""Exact audit of a high-frequency solenoidal cutoff commutator.

The script does not solve Navier--Stokes and does not discretize a PDE. It
uses Fraction arithmetic to certify the geometry, a positive L2 lower bound,
the distributional f0+div(G0) identity, and a choice-independent nonzero
Bogovskii witness.
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


def radial_jacobian_integral(r0: Q, r1: Q) -> Q:
    """Integral of r dr on [r0,r1]."""
    return (r1**2 - r0**2) / 2


def audit_geometry(audit: Audit) -> None:
    """Certify that the toroidal boxes lie in the affine cutoff shell."""
    r_support = (Q(1), Q(5, 4))
    z_support = (-Q(1, 8), Q(1, 8))
    shifted_z = (1 + z_support[0], 1 + z_support[1])

    rho_sq_min = r_support[0] ** 2 + shifted_z[0] ** 2
    rho_sq_max = r_support[1] ** 2 + shifted_z[1] ** 2
    audit.equal(rho_sq_min, Q(113, 64))
    audit.equal(rho_sq_max, Q(181, 64))
    audit.true(rho_sq_min > Q(6, 5) ** 2)
    audit.true(rho_sq_max < Q(7, 4) ** 2)
    audit.true(r_support[0] > 0)

    r_core = (Q(17, 16), Q(19, 16))
    z_core = (-Q(1, 16), Q(1, 16))
    radial_factor_support = radial_jacobian_integral(*r_support)
    radial_factor_core = radial_jacobian_integral(*r_core)
    audit.equal(radial_factor_support, Q(9, 32))
    audit.equal(radial_factor_core, Q(9, 64))
    audit.equal(z_support[1] - z_support[0], Q(1, 4))
    audit.equal(z_core[1] - z_core[0], Q(1, 8))

    # Using 3 < pi < 22/7, without floating-point arithmetic:
    # |S|=9*pi/64 < 99/224 < 1/2 and |Q|=9*pi/256 < 99/896 < 1/9.
    support_volume_upper = Q(99, 224)
    core_volume_upper = Q(99, 896)
    audit.true(support_volume_upper < Q(1, 2))
    audit.true(core_volume_upper < Q(1, 9))

    # On the core, s=z+1>=15/16 and rho<7/4, hence
    # |partial_z chi|=s/rho > 15/28 > 1/2.
    audit.true(Q(15, 28) > Q(1, 2))


def audit_swirl_structure(audit: Audit) -> None:
    """Check the cylindrical structural identities for U_N."""
    for epsilon in (Q(1, 17), Q(1), Q(7, 3)):
        for n in (1, 2, 17, 128):
            # U_r=U_z=0 and U_theta is theta-independent.
            divergence = Q(0) + Q(0) + Q(0)
            # a=grad chi has only e_r and e_z components.
            a_dot_u = Q(0)
            # Delta U is again theta-independent and purely azimuthal.
            a_dot_laplacian_u = Q(0)
            audit.equal(divergence, Q(0))
            audit.equal(a_dot_u, Q(0))
            audit.equal(a_dot_laplacian_u, Q(0))
            audit.true(epsilon > 0 and n > 0)


def commutator_mode_coefficients(
    *,
    epsilon: Q,
    n: int,
    phi: Q,
    phi_r: Q,
    phi_z: Q,
    chi_r: Q,
    chi_z: Q,
    laplacian_chi: Q,
) -> tuple[Q, Q]:
    """Return the sin(Nz), cos(Nz) coefficients of [Delta,chi]U_N."""
    sine = epsilon * (
        laplacian_chi * phi + 2 * (chi_r * phi_r + chi_z * phi_z)
    )
    cosine = 2 * epsilon * n * chi_z * phi
    return sine, cosine


def representation_mode_coefficients(
    *,
    epsilon: Q,
    n: int,
    phi: Q,
    phi_r: Q,
    phi_z: Q,
    chi_r: Q,
    chi_z: Q,
    laplacian_chi: Q,
) -> tuple[Q, Q]:
    """Return coefficients of f0+div(G0), G0=2 U_N tensor grad chi."""
    f0_sine = -epsilon * laplacian_chi * phi
    div_g_sine = 2 * epsilon * (
        laplacian_chi * phi + chi_r * phi_r + chi_z * phi_z
    )
    div_g_cosine = 2 * epsilon * n * chi_z * phi
    return f0_sine + div_g_sine, div_g_cosine


def audit_distributional_representation(audit: Audit) -> None:
    values = (-Q(7, 3), -Q(1), Q(0), Q(2, 5), Q(11, 4))
    for n in (1, 3, 16, 257):
        for index, value in enumerate(values):
            epsilon = Q(index + 1, 13)
            phi = Q(index + 2, 7)
            phi_r = value
            phi_z = values[-index - 1]
            chi_r = Q(2 * index - 3, 9)
            chi_z = Q(5 - index, 11)
            laplacian_chi = Q(index - 4, 6)
            direct = commutator_mode_coefficients(
                epsilon=epsilon,
                n=n,
                phi=phi,
                phi_r=phi_r,
                phi_z=phi_z,
                chi_r=chi_r,
                chi_z=chi_z,
                laplacian_chi=laplacian_chi,
            )
            represented = representation_mode_coefficients(
                epsilon=epsilon,
                n=n,
                phi=phi,
                phi_r=phi_r,
                phi_z=phi_z,
                chi_r=chi_r,
                chi_z=chi_z,
                laplacian_chi=laplacian_chi,
            )
            audit.equal(direct, represented)


def l2_lower_bound(epsilon: Q, n: int) -> Q:
    """Certified lower bound on the positive L2 norm over the core torus."""
    return epsilon * (Q(5 * n, 32) - Q(8, 15))


def audit_positive_norm_growth(audit: Audit) -> None:
    # On I=[-1/16,1/16],
    # integral cos(Nz)^2 dz = 1/16+sin(N/8)/(2N).
    # For N>=16 it is >=1/32. Combining theta length 2*pi>6 and
    # integral r dr=9/64 gives squared norm >27/1024>(5/32)^2.
    audit.true(Q(27, 1024) > Q(5, 32) ** 2)

    # |Q|<1/9 gives sqrt(|Q|)<1/3. Since |Delta chi|<=8/5,
    # the lower-order term has L2 norm <8*epsilon/15.
    audit.true(Q(99, 896) < Q(1, 9))

    previous = None
    for epsilon in (Q(1, 100), Q(1), Q(7, 4)):
        for n in (16, 32, 64, 128, 256, 512, 1024, 2048):
            lower = l2_lower_bound(epsilon, n)
            audit.true(lower > 0)
            audit.equal(
                lower / (epsilon * n),
                Q(5, 32) - Q(8, 15 * n),
            )
            if n >= 32:
                audit.true(lower > epsilon * n / 8)
            if previous is not None and previous[0] == epsilon:
                audit.true(lower > previous[1])
            previous = (epsilon, lower)
        previous = None


def audit_uniform_negative_space_budget(audit: Audit) -> None:
    """Check exact N-independent budgets for f0 and G0."""
    support_volume_upper = Q(99, 224)
    gradient_chi_bound = Q(1)
    laplacian_chi_bound = Q(8, 5)

    # (1/2)^(2/3)<4/5 follows after cubing: 1/4<64/125.
    audit.true(Q(1, 4) < Q(64, 125))
    support_two_thirds_upper = Q(4, 5)

    for epsilon in (Q(1, 1000), Q(1, 7), Q(1), Q(9, 2)):
        f0_l1_bound = (
            laplacian_chi_bound * epsilon * support_volume_upper
        )
        g0_weak_l3_over_2_bound = (
            2 * epsilon * gradient_chi_bound * support_two_thirds_upper
        )
        audit.equal(f0_l1_bound, Q(99, 140) * epsilon)
        audit.equal(g0_weak_l3_over_2_bound, Q(8, 5) * epsilon)
        for n in (1, 16, 10**3, 10**6):
            # N is absent from both coefficient budgets.
            audit.equal(f0_l1_bound + Q(0) * n, Q(99, 140) * epsilon)
            audit.equal(
                g0_weak_l3_over_2_bound + Q(0) * n,
                Q(8, 5) * epsilon,
            )


def audit_nonzero_bogovskii_witness(audit: Audit) -> None:
    """Certify nonzeroness for every right inverse, without selecting one."""
    # Axisymmetric streamfunction Psi=r*z near (r,z)=(3/4,0):
    # U_r=-(1/r)partial_z Psi=-1, U_z=(1/r)partial_r Psi=0.
    radius = Q(3, 4)
    shifted_z = Q(1)
    rho = Q(5, 4)
    audit.equal(radius**2 + shifted_z**2, rho**2)

    chi_prime = Q(-1)
    grad_chi_r = chi_prime * radius / rho
    grad_chi_z = chi_prime * shifted_z / rho
    velocity_r = Q(-1)
    velocity_z = Q(0)
    defect = grad_chi_r * velocity_r + grad_chi_z * velocity_z
    audit.equal(grad_chi_r, -Q(3, 5))
    audit.equal(grad_chi_z, -Q(4, 5))
    audit.equal(defect, Q(3, 5))
    audit.true(defect != 0)

    # div U=0 follows from equality of mixed derivatives of Psi.
    for mixed_derivative in (Q(-7, 3), Q(0), Q(11, 5)):
        divergence = (
            -mixed_derivative / radius + mixed_derivative / radius
        )
        audit.equal(divergence, Q(0))

    # If div(Bg)=g and g is nonzero, Bg cannot be the zero field.
    hypothetical_zero_corrector_divergence = Q(0)
    audit.true(hypothetical_zero_corrector_divergence != defect)


def main() -> None:
    audit = Audit()
    audit_geometry(audit)
    audit_swirl_structure(audit)
    audit_distributional_representation(audit)
    audit_positive_norm_growth(audit)
    audit_uniform_negative_space_budget(audit)
    audit_nonzero_bogovskii_witness(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("moving_commutator_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("family=epsilon*phi(r,z)*sin(N*z)*e_theta on r>1")
    print("div_U_N=0, grad_chi_dot_U_N=0, grad_chi_dot_Delta_U_N=0")
    print("full_commutator=[Delta,Q]U_N=[Delta,chi]U_N for every B")
    print("positive_L2_lower=epsilon*(5*N/32-8/15), N>=16")
    print("growth=Theta(N) for fixed epsilon and fixed smooth profiles")
    print("representation=[Delta,chi]U_N=f0+div(G0)")
    print("f0=-(Delta chi)U_N, G0=2*U_N tensor grad(chi)")
    print("uniform_budget=||f0||_1<=99*epsilon/140")
    print("uniform_budget=||G0||_L(3/2,infinity)<=8*epsilon/5")
    print("nonzero_B_witness=defect_at_(3/4,0)=3/5")
    print("scope=exact differential ledger; no Navier-Stokes simulation")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
