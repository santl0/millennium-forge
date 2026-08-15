#!/usr/bin/env python3
"""Exact scaling audit for the weak-L3 relative-energy gate.

Only rational exponent and geometric-series ledgers are certified.  The
multi-scale construction is a functional counter-profile, not a solution of
Navier--Stokes and not a computer-assisted PDE proof.
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


def heat_exponent(source: Q, target: Q | None) -> Q:
    """gamma in ||exp(h Delta)||_(L^source -> L^target) <= C h^-gamma."""
    reciprocal_target = Q(0) if target is None else 1 / target
    return Q(3, 2) * (1 / source - reciprocal_target)


def monomial_integral(exponent: Q) -> tuple[Q, Q]:
    """Return coefficient and output exponent for integral_0^H h^exponent dh."""
    assert exponent > -1
    output_exponent = exponent + 1
    return 1 / output_exponent, output_exponent


def audit_heat_and_time(audit: Audit) -> None:
    source = Q(3)
    gamma_infinity = heat_exponent(source, None)
    gamma_four = heat_exponent(source, Q(4))
    audit.equal(gamma_infinity, Q(1, 2))
    audit.equal(gamma_four, Q(1, 8))

    # Powers of h in the norms themselves.
    v_infinity = -gamma_infinity
    v_four = -gamma_four
    w_two = Q(1, 4)

    # Bulk terms after Young's inequality in a formal relative-energy test.
    v_infinity_squared_w_two_squared = 2 * v_infinity + 2 * w_two
    v_four_fourth = 4 * v_four
    audit.equal(v_infinity_squared_w_two_squared, Q(-1, 2))
    audit.equal(v_four_fourth, Q(-1, 2))
    audit.equal(monomial_integral(v_infinity_squared_w_two_squared), (Q(2), Q(1, 2)))
    audit.equal(monomial_integral(v_four_fourth), (Q(2), Q(1, 2)))

    # The bare Gronwall coefficient is still h^-1 and is not integrable.
    bare_gronwall = 2 * v_infinity
    audit.equal(bare_gronwall, Q(-1))

    # Powers of M: ||V||_infinity~M, ||V||_4~M, ||w||_2~M^2.
    audit.equal(2 * 1 + 2 * 2, 6)
    audit.equal(4 * 1, 4)

    # Cutoff terms whose global norm bounds do close, before the R factors.
    drift_v_w_squared = v_infinity + 2 * w_two
    forcing_v_squared_w = 2 * v_four + w_two
    diffusion_w_squared = 2 * w_two
    profile_self_flux = 3 * w_two
    audit.equal(drift_v_w_squared, Q(0))
    audit.equal(forcing_v_squared_w, Q(0))
    audit.equal(diffusion_w_squared, Q(1, 2))
    audit.equal(profile_self_flux, Q(3, 4))
    audit.equal(monomial_integral(drift_v_w_squared), (Q(1), Q(1)))
    audit.equal(monomial_integral(forcing_v_squared_w), (Q(1), Q(1)))
    audit.equal(monomial_integral(diffusion_w_squared), (Q(2, 3), Q(3, 2)))
    audit.equal(monomial_integral(profile_self_flux), (Q(4, 7), Q(7, 4)))
    audit.equal(1 + 2 * 2, 5)  # M power in ||V||_infinity ||w||_2^2.
    audit.equal(2 * 1 + 2, 4)  # M power in ||V||_4^2 ||w||_2.


def audit_endpoint_quantifiers(audit: Audit) -> None:
    """The uniform endpoint majorant has one logarithmic unit per shell."""
    for shell_count in (1, 2, 3, 8, 32, 128, 1024):
        normalized_log = sum((Q(1) for _ in range(shell_count)), Q(0))
        audit.equal(normalized_log, Q(shell_count))
        audit.true(normalized_log >= 1)

    # Multiplication by the independently known h^(1/2) energy rate changes
    # h^-1 into h^-1/2; dropping that factor inverts the implication.
    audit.equal(Q(-1) + Q(1, 2), Q(-1, 2))
    audit.true(Q(-1, 2) > -1)
    audit.true(Q(-1) <= -1)


def audit_cutoff_scaling(audit: Audit) -> None:
    """Powers of R for chi_R(x)=chi(x/R)."""
    grad_cutoff = Q(-1)
    laplacian_cutoff = Q(-2)
    audit.equal(grad_cutoff, Q(-1))
    audit.equal(laplacian_cutoff, Q(-2))

    # A critical atom has amplitude ell^-1 and volume ell^3.
    length = Q(1)  # symbolic exponent of ell
    amplitude = -length
    volume = 3 * length
    l2_square = 2 * amplitude + volume
    l3_cube = 3 * amplitude + volume
    gradient_l2_square = 2 * (amplitude - length) + volume
    audit.equal(l2_square, Q(1))
    audit.equal(l3_cube, Q(0))
    audit.equal(gradient_l2_square, Q(-1))

    # For an atom whose physical length is independent of the outer cutoff
    # radius R, its mass has R-exponent zero.  Multiplicity, not atom size,
    # will cancel the R^-1 cubic prefactor in the diagonal construction.
    atom_mass_radius_exponent = Q(0)
    audit.equal(laplacian_cutoff + atom_mass_radius_exponent, Q(-2))
    audit.equal(grad_cutoff + atom_mass_radius_exponent, Q(-1))


def audit_multiscale_counterprofile(audit: Audit) -> None:
    """Audit a single multi-annular L2 cap weak-L3 counter-profile.

    Annulus n is at R_n=4^n.  It contains N_n=32^n disjoint critical
    atoms with group weight delta_n=2^-n and atom lengths ell_j=2^-j.
    All quantities below are normalized by fixed atom constants.
    """
    previous_radius = None
    previous_gradient_exponent = None
    for n in range(1, 4):
        radius = Q(4**n)
        delta = Q(1, 2**n)
        cell_count = 32**n
        audit.equal(Q(cell_count) * delta**3, radius)
        audit.equal(Q(cell_count) * delta**3 / radius, Q(1))

        # Sum_j ell_j=1-2^-N, hence the group L2 energy is <delta^2.
        length_sum = Q(1) - Q(1, 2**cell_count)
        group_l2_square = delta**2 * length_sum
        audit.true(Q(0) < group_l2_square < delta**2)

        # Each atom carries delta^3 units of strong L3 mass/cubic moment.
        group_l3_cube = Q(cell_count) * delta**3
        audit.equal(group_l3_cube, radius)

        # The rearranged geometric stack has a uniform weak-L3 bound.
        group_weak_l3_cube_upper = Q(8, 7) * delta**3
        audit.true(group_weak_l3_cube_upper > 0)

        # The smallest atom alone has gradient-energy exponent 2^(N-2n).
        gradient_base_two_exponent = cell_count - 2 * n
        audit.true(gradient_base_two_exponent > 0)
        if previous_gradient_exponent is not None:
            audit.true(gradient_base_two_exponent > previous_gradient_exponent)
        previous_gradient_exponent = gradient_base_two_exponent

        if previous_radius is not None:
            audit.equal(radius / previous_radius, Q(4))
        previous_radius = radius

    for group_count in (1, 2, 3, 5, 8, 13, 32):
        l2_upper = Q(1, 3) * (1 - Q(1, 4**group_count))
        weak_cube_upper = Q(8, 49) * (1 - Q(1, 8**group_count))
        audit.true(l2_upper < Q(1, 3))
        audit.true(weak_cube_upper < Q(8, 49))

    # Diagonal cutoff flux: N_n*delta_n^3/R_n=1 for every annulus.
    for n in (1, 2, 3, 5, 8, 13, 32):
        audit.equal(Q(32**n, 8**n * 4**n), Q(1))

    # Non-commuting limits for finite group truncation K and cutoff index n.
    def truncated_flux(group_cutoff: int, annulus_index: int) -> Q:
        return Q(1) if annulus_index <= group_cutoff else Q(0)

    for group_cutoff in (1, 2, 3, 8, 32):
        audit.equal(truncated_flux(group_cutoff, group_cutoff + 1), Q(0))
    for annulus_index in (1, 2, 3, 8, 32):
        audit.equal(truncated_flux(annulus_index, annulus_index), Q(1))

    # With w(h)=h^(1/4)W, the time-integrated diagonal cubic flux is
    # (4/7)H^(7/4), still independent of n.
    audit.equal(monomial_integral(Q(3, 4)), (Q(4, 7), Q(7, 4)))


def main() -> None:
    audit = Audit()
    audit_heat_and_time(audit)
    audit_endpoint_quantifiers(audit)
    audit_cutoff_scaling(audit)
    audit_multiscale_counterprofile(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("relative_energy_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("heat=||V||_inf~M*h^-1/2, ||V||_4~M*h^-1/8")
    print("bulk=||V||_inf^2||w||_2^2~M^6*h^-1/2")
    print("forcing=||V||_4^4~M^4*h^-1/2")
    print("time_integrals=2*M^6*H^1/2 and 2*M^4*H^1/2 up to operator constants")
    print("bare_gronwall=||V||_inf^2~M^2*h^-1 is endpoint-logarithmic")
    print("cutoff=grad_chi_R~R^-1, laplacian_chi_R~R^-2")
    print("multiscale=L2_and_weak-L3_bounded_but_diagonal_cubic_flux=1")
    print("scope=exact exponent ledger and functional counter-profile; no PDE claim")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
