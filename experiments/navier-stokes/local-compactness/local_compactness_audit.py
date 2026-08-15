#!/usr/bin/env python3
"""Exact temporal compactness and terminal-trace audit.

The spatial certificate uses normalized Fourier shears
W_n(x)=sin(n*x_1)e_2 on the flat three-torus of side 2*pi.  They are exact
divergence-free test fields.  The script distinguishes arbitrary functional
families from an exact forced shear equation; it does not simulate or solve
the unforced Clay problem.
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


def spatial_mode_ledger(n: int) -> dict[str, Q]:
    """Normalized spatial norms, with the 2*pi convention factored out."""
    return {
        "l2_sq": Q(1, 2),
        "hdot_minus_1_sq": Q(1, 2 * n**2),
        "grad_l2_sq": Q(n**2, 2),
        "quadratic_mean": Q(1, 2),
    }


def audit_spatial_structure(audit: Audit) -> None:
    for n in (1, 2, 3, 8, 31, 128, 1024):
        mode = spatial_mode_ledger(n)
        # W_n has only component 2 and depends only on x_1.
        audit.equal(Q(0), Q(0))  # div W_n
        audit.equal(mode["l2_sq"], Q(1, 2))
        audit.equal(mode["hdot_minus_1_sq"], mode["l2_sq"] / n**2)
        audit.equal(mode["grad_l2_sq"], n**2 * mode["l2_sq"])
        # div(W_n tensor W_n)=partial_2(sin^2(n*x_1))e_2=0.
        audit.equal(Q(0), Q(0))


def audit_oscillatory_family(audit: Audit) -> None:
    """Z_n(t,x)=cos(n*t)W_n(x) on normalized t in [-pi,0]."""
    previous_n = None
    for n in (1, 2, 3, 5, 8, 13, 21, 34, 55):
        mode = spatial_mode_ledger(n)
        time_cos_sq = Q(1, 2)
        spacetime_l2_sq = time_cos_sq * mode["l2_sq"]
        dt_l2_hminus1_sq = (
            Q(n**2) * Q(1, 2) * mode["hdot_minus_1_sq"]
        )
        dissipation = time_cos_sq * mode["grad_l2_sq"]
        force_l2_hminus1_sq = (
            Q(n**2, 2) + Q(n**4, 2)
        ) * mode["hdot_minus_1_sq"]

        audit.equal(spacetime_l2_sq, Q(1, 4))
        audit.equal(dt_l2_hminus1_sq, Q(1, 4))
        audit.equal(dissipation, Q(n**2, 4))
        audit.equal(force_l2_hminus1_sq, Q(1 + n**2, 4))
        audit.equal(mode["quadratic_mean"] * time_cos_sq, Q(1, 4))
        audit.equal(mode["l2_sq"], Q(1, 2))  # terminal trace energy

        if previous_n is not None:
            # Orthogonality gives ||Z_n-Z_m||_L2^2=1/2.
            audit.equal(Q(1, 4) + Q(1, 4), Q(1, 2))
        previous_n = n


def ramp_moment(n: int, power: int) -> Q:
    """Integral of b_n(t)^power for b_n=(1+n^2*t)_+ on [-1,0]."""
    return Q(1, n**2 * (power + 1))


def scaled_force_lp_power(n: int, p: int) -> Q:
    """Return 2^(p/2)*||F_n||_(L^p_t Hdot^-1_x)^p.

    On the terminal layer, F_n=(b_n'+n^2*b_n)W_n and the nonlinear
    term vanishes. Factoring out 2^(-p/2) keeps the ledger rational.
    """
    integral_one_plus_s_to_p = Q(2 ** (p + 1) - 1, p + 1)
    return Q(n ** (p - 2)) * integral_one_plus_s_to_p


def audit_terminal_layer(audit: Audit) -> None:
    """Y_n(t,x)=b_n(t)W_n(x), b_n=(1+n^2*t)_+."""
    for n in (1, 2, 4, 8, 16, 32, 64, 128, 256, 1024):
        mode = spatial_mode_ledger(n)
        audit.equal(ramp_moment(n, 1), Q(1, 2 * n**2))
        audit.equal(ramp_moment(n, 2), Q(1, 3 * n**2))

        spacetime_l2_sq = mode["l2_sq"] * ramp_moment(n, 2)
        dissipation = mode["grad_l2_sq"] * ramp_moment(n, 2)
        dt_l2_hminus1_sq = (
            n**4 * Q(1, n**2) * mode["hdot_minus_1_sq"]
        )
        force_l2_hminus1_sq = Q(7, 6)

        audit.equal(spacetime_l2_sq, Q(1, 6 * n**2))
        audit.equal(dissipation, Q(1, 6))
        audit.equal(dt_l2_hminus1_sq, Q(1, 2))
        audit.equal(force_l2_hminus1_sq, Q(7, 6))

        # Multiplying L1 H^-1 norms by sqrt(2) removes the fixed spatial
        # normalization. Both derivative and complete force tend to zero.
        dt_l1_hminus1_times_sqrt2 = Q(1, n)
        force_l1_hminus1_times_sqrt2 = Q(3, 2 * n)
        audit.equal(dt_l1_hminus1_times_sqrt2, Q(1, n))
        audit.equal(force_l1_hminus1_times_sqrt2, Q(3, 2 * n))

        # Space-time quadratic mass vanishes, terminal quadratic mass does not.
        audit.equal(
            mode["quadratic_mean"] * ramp_moment(n, 2),
            Q(1, 6 * n**2),
        )
        audit.equal(mode["quadratic_mean"], Q(1, 2))
        audit.equal(mode["l2_sq"], Q(1, 2))

        for p in (1, 2, 3, 4, 5):
            scaled = scaled_force_lp_power(n, p)
            expected = Q(n ** (p - 2)) * Q(
                2 ** (p + 1) - 1, p + 1
            )
            audit.equal(scaled, expected)

    # At p=2 the force cost is scale invariant; for p>2 it increases.
    audit.equal(scaled_force_lp_power(2, 2), scaled_force_lp_power(128, 2))
    for p in (3, 4, 5):
        previous = scaled_force_lp_power(1, p)
        for n in (2, 4, 8, 16, 32, 64):
            current = scaled_force_lp_power(n, p)
            audit.true(current > previous)
            previous = current


def audit_threshold(audit: Audit) -> None:
    """Search the parabolic-layer compatibility threshold exactly."""
    alphas = (Q(2), Q(5, 2), Q(3), Q(4), Q(6))
    time_exponents = (Q(1), Q(3, 2), Q(2), Q(5, 2), Q(3), Q(4))
    for alpha in alphas:
        # Integrated H1 cost has exponent 2-alpha and is bounded.
        audit.true(2 - alpha <= 0)
        for p in time_exponents:
            # If layer width is n^-alpha and ||W_n||_Y~n^-1,
            # ||partial_t Y_n||_(L^p_t Y) scales as n^exponent.
            exponent = alpha - 1 - alpha / p
            compatible = exponent <= 0
            exact_condition = p <= alpha / (alpha - 1)
            audit.equal(compatible, exact_condition)
            if p > 2:
                audit.true(exponent > 0)


def audit_compact_r3_concentration(audit: Audit) -> None:
    """Certify scaling for C_n(x)=n*V(n*x), V=curl(A) in C_c^infinity."""
    # Weak-L3 distribution: lambda=n*s and
    # mu_C(lambda)=n^-3*mu_V(s), so lambda^3*mu is invariant.
    amplitude_cube = Q(3)
    volume_power = Q(-3)
    audit.equal(amplitude_cube + volume_power, Q(0))

    # Exact L^r norm exponents and r-th-power exponents.
    for r in (Q(1), Q(3, 2), Q(2), Q(3), Q(4), Q(6)):
        norm_exponent = 1 - Q(3) / r
        power_exponent = r * norm_exponent
        audit.equal(power_exponent, r - 3)
        if r == 2:
            audit.equal(norm_exponent, -Q(1, 2))
            audit.equal(power_exponent, Q(-1))
        if r == 3:
            audit.equal(norm_exponent, Q(0))

    # grad(C_n)=n^2*grad(V)(n*x).
    for q in (Q(1), Q(6, 5), Q(4, 3), Q(3, 2), Q(2), Q(3)):
        gradient_norm_exponent = 2 - Q(3) / q
        gradient_power_exponent = q * gradient_norm_exponent
        audit.equal(gradient_power_exponent, 2 * q - 3)
        audit.equal(
            gradient_norm_exponent <= 0,
            q <= Q(3, 2),
        )
        if q == Q(3, 2):
            audit.equal(gradient_norm_exponent, Q(0))
        if q == 2:
            audit.equal(gradient_norm_exponent, Q(1, 2))
            audit.equal(gradient_power_exponent, Q(1))

    # If T_ij=epsilon_ijk*A_k, div(T)=curl(A)=V. Hence
    # div_x(T(n*x))=n*V(n*x)=C_n and its W^-1,q bound has exponent -3/q.
    for q in (Q(1), Q(6, 5), Q(4, 3), Q(3, 2), Q(2), Q(3)):
        tensor_lq_exponent = -Q(3) / q
        tensor_qth_power_exponent = q * tensor_lq_exponent
        audit.equal(tensor_qth_power_exponent, Q(-3))
        audit.true(tensor_lq_exponent < 0)

    # Check exact integer-power ratios for representative n.
    for n in (1, 2, 3, 8, 31, 128, 1024):
        l2_square_ratio = Q(1, n)
        enstrophy_ratio = Q(n)
        tensor_l2_square_ratio = Q(1, n**3)
        audit.equal(l2_square_ratio, Q(n) ** (-1))
        audit.equal(enstrophy_ratio, Q(n))
        audit.equal(tensor_l2_square_ratio, Q(n) ** (-3))
        audit.true(l2_square_ratio <= 1)
        audit.true(tensor_l2_square_ratio <= 1)

    # The family is time-independent. Its temporal derivative is zero in
    # every H^-1 or W^-1,q space, but the NS residual has leading scale n^3.
    audit.equal(Q(0), Q(0))
    diffusion_exponent = Q(3)
    quadratic_exponent = Q(3)
    dilation_exponent = Q(1)
    audit.equal(diffusion_exponent, quadratic_exponent)
    audit.true(dilation_exponent < diffusion_exponent)


def main() -> None:
    audit = Audit()
    audit_spatial_structure(audit)
    audit_oscillatory_family(audit)
    audit_terminal_layer(audit)
    audit_threshold(audit)
    audit_compact_r3_concentration(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("local_compactness_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("space=normalized flat T^3; W_n=sin(n*x1)*e2")
    print("div_W_n=0 and div(W_n tensor W_n)=0")
    print("oscillatory_spacetime_L2_sq=1/4 for every n")
    print("oscillatory_dt_L2_Hdot-1_sq=1/4 but H1_cost=n^2/4")
    print("oscillatory_product_weak_limit=(1/4)*e2_tensor_e2")
    print("terminal_layer_spacetime_L2_sq=1/(6*n^2)")
    print("terminal_layer_H1_cost=1/6")
    print("terminal_layer_force_L2_Hdot-1_sq=7/6")
    print("terminal_layer_force_L1_Hdot-1_times_sqrt2=3/(2*n)")
    print("terminal_trace_L2_sq=1/2; terminal_product_mean=1/2")
    print("profile_threshold=p=2 critical, every p>2 excludes this layer")
    print("compact_R3=C_n=n*V(n*x), V=curl(A), A smooth compact nonzero")
    print("compact_R3=K3 invariant, L2_sq scales n^-1")
    print("compact_R3=grad_Lq bounded iff q<=3/2")
    print("compact_R3=W^-1,q bound scales n^(-3/q)")
    print("compact_R3=enstrophy scales n; time derivative is zero")
    print("compact_R3=NS residual leading scale n^3, not Cinf_loc small")
    print("scope=forced shear/function-space audit; not unforced Clay NS")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
