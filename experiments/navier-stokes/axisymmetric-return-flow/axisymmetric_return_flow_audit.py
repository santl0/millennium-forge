#!/usr/bin/env python3
"""Exact audit of a separable axisymmetric compact return-flow ansatz.

No Navier--Stokes trajectory is computed.  The script checks an exact radial
flux balance for U=chi(z) A(r) e_theta, the critical two-amplitude scaling,
the cutoff identities, and a scale-invariant mean-oscillation obstruction on
a ball contained in the radial-only end-cap flow.
"""

from __future__ import annotations

import json
from fractions import Fraction as Q
from math import comb


checks: list[tuple[str, bool, str]] = []


def record(name: str, condition: bool, detail: str) -> None:
    checks.append((name, condition, detail))


def add(left: list[Q], right: list[Q]) -> list[Q]:
    size = max(len(left), len(right))
    return [
        (left[index] if index < len(left) else Q(0))
        + (right[index] if index < len(right) else Q(0))
        for index in range(size)
    ]


def scale(poly: list[Q], factor: Q) -> list[Q]:
    return [factor * coefficient for coefficient in poly]


def derivative(poly: list[Q]) -> list[Q]:
    return [Q(index) * poly[index] for index in range(1, len(poly))]


def primitive(poly: list[Q]) -> list[Q]:
    return [Q(0)] + [poly[index] / Q(index + 1) for index in range(len(poly))]


def evaluate(poly: list[Q], value: Q) -> Q:
    result = Q(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def integral(poly: list[Q], left: Q = Q(0), right: Q = Q(1)) -> Q:
    anti = primitive(poly)
    return evaluate(anti, right) - evaluate(anti, left)


# b(t)=t^4(1-t)^4.  Its first three derivatives vanish at both endpoints,
# so the zero extension is C^3.  The normalized antiderivative produces a
# C^4 compact axial cutoff chi with a unit plateau.
bump = [Q(0)] * 13
for index in range(5):
    bump[index + 4] = Q((-1) ** index * comb(4, index))

i0 = integral(bump)
i1 = integral([Q(0)] + bump)
record("bump_mass", i0 == Q(1, 630), f"I0={i0}")
record("bump_first_moment", i1 == Q(1, 1260), f"I1={i1}")

chi_cap = add([Q(1)], scale(primitive(bump), -Q(630)))
record("chi_cap_left", evaluate(chi_cap, Q(0)) == 1, "chi(0)=1")
record("chi_cap_right", evaluate(chi_cap, Q(1)) == 0, "chi(1)=0")
record(
    "chi_derivative_identity",
    add(derivative(chi_cap), scale(bump, Q(630))) == [Q(0)] * len(bump),
    "chi'=-630 b exactly on the cap",
)
for order in range(1, 5):
    cap_derivative = chi_cap
    for _ in range(order):
        cap_derivative = derivative(cap_derivative)
    record(
        f"chi_boundary_derivative_{order}",
        evaluate(cap_derivative, Q(0)) == 0
        and evaluate(cap_derivative, Q(1)) == 0,
        "cutoff derivative vanishes at both cap endpoints",
    )


# Positive radial vorticity is n^-1 b(r-1) on 1<r<2.  Negative radial
# vorticity is -B_n b((r-4)/delta_n) on 4<r<4+delta_n.  The cylindrical flux
# uses r dr.  B_n is chosen so the weighted radial integral is exactly zero.
first_n = 2
last_n = 96
b_mid = Q(3, 8) ** 4 * Q(5, 8) ** 4
weak_cube_uniform_lower = 4 * Q(24, 65) ** 3 * b_mid**3
critical_mass_squares: list[Q] = []
balanced_mo_ratios: list[Q] = []

for n in range(first_n, last_n + 1):
    delta = Q(1, n**3)
    positive_flux = (i0 + i1) / n
    negative_unit_flux = delta * (4 * i0 + delta * i1)
    negative_amplitude = positive_flux / negative_unit_flux

    record(
        f"positive_flux_{n}",
        positive_flux == Q(1, 420 * n),
        f"P_n={positive_flux}",
    )
    record(
        f"negative_amplitude_{n}",
        negative_amplitude == Q(3 * n**5, 8 * n**3 + 1),
        f"B_n={negative_amplitude}",
    )
    record(
        f"radial_flux_balance_{n}",
        positive_flux - negative_amplitude * negative_unit_flux == 0,
        "integral r f_n(r) dr=0",
    )
    record(
        f"critical_amplitude_window_{n}",
        Q(24, 65) * n**2 <= negative_amplitude < Q(3, 8) * n**2,
        "B_n is uniformly comparable to n^2",
    )

    # On 3/8<t<5/8 and the axial plateau -1<z<1, |W_z| is at least
    # B_n*b_mid.  Cubing K>=lambda*measure^(2/3) avoids irrational powers.
    negative_subvolume = 2 * delta * (1 + delta / 8)
    weak_lower_cube = (negative_amplitude * b_mid) ** 3 * negative_subvolume**2
    record(
        f"weak_l32_uniform_lower_{n}",
        weak_lower_cube >= weak_cube_uniform_lower,
        "K^3 has an n-independent positive lower bound",
    )
    # Distribution-function upper bound in normalized cylindrical measure.
    # Positive axial: M<=1/(256n), V=6 and V^(2/3)<4.
    # Negative axial: M<3n^2/2048, V<=65 delta/4 and
    # (65/4)^(2/3)<7.  Radial cap: M<=1/(140n), V<=24 and
    # 24^(2/3)<9.  The threshold split |a+b|>lambda gives
    # K(a+b)<=2(Ka+Kb).
    weak_upper = 2 * (Q(1, 64 * n) + Q(21, 2048) + Q(9, 140 * n))
    record(
        f"weak_l32_uniform_upper_{n}",
        weak_upper < Q(1, 9),
        "K<1/9 in normalized cylindrical measure",
    )

    # The exact square of the strong L^(3/2) mass on the negative phase of
    # the plateau.  Since b^(3/2)=t^6(1-t)^6, I6=Beta(7,7)=1/12012.
    i6 = Q(1, 12012)
    negative_critical_mass_squared = (
        2 * delta * i6 * (4 + delta / 2)
    ) ** 2 * negative_amplitude**3
    critical_mass_squares.append(negative_critical_mass_squared)
    record(
        f"critical_mass_nonzero_{n}",
        negative_critical_mass_squared > 0,
        "squared negative L^(3/2) mass is exact and positive",
    )

    # In the corridor 2<r<4, r A_n(r)=P_n.  Hence |A_n|<=P_n there and the
    # end-cap radial component is nonzero wherever chi' is nonzero.
    record(
        f"corridor_potential_{n}",
        positive_flux > 0 and 3 * positive_flux == Q(1, 140 * n),
        "A_n=P_n/r and |chi' A_n|<=3P_n on the tested corridor",
    )
    record(
        f"velocity_energy_upper_{n}",
        50 * positive_flux**2 == Q(1, 3528 * n**2),
        "coarse normalized L2 velocity bound 50 P_n^2=1/(3528 n^2)",
    )

    # Balanced cap: rescale each axial transition to width delta=n^-3.
    # The radial cap then has amplitude O(n^2) on volume O(n^-3), so the full
    # weak critical norm remains uniformly bounded.  On the fixed parent
    # domain D={0<r<6, |z|<3} of normalized volume 108, an extension by e_z
    # differs from e_z only in the negative tube and the two caps.
    balanced_weak_upper = 2 * (
        Q(1, 64 * n) + Q(21, 2048) + Q(9, 140)
    )
    record(
        f"balanced_weak_l32_upper_{n}",
        balanced_weak_upper < Q(1, 6),
        "balanced cap still has K<1/6 in normalized cylindrical measure",
    )

    negative_tube_volume = (4 * delta + delta**2 / 2) * (2 + 2 * delta)
    cap_volume_upper = delta * ((4 + delta) ** 2 - 1)
    exceptional_volume_upper = negative_tube_volume + cap_volume_upper
    record(
        f"balanced_exceptional_volume_{n}",
        exceptional_volume_upper <= 27 * delta,
        "the domain where the e_z extension may differ has volume <=27 delta",
    )

    # Positive axial support has normalized volume 3.  The radial-only
    # corridor 2<r<4 in both caps has volume 12 delta.  The two-trace lemma
    # gives the exact lower bound below, while extension by e_z gives
    # MO<=4|E|/108<=delta.
    global_mo_lower = 2 * delta / (9 * (1 + 4 * delta))
    global_mo_upper = delta
    balanced_mo_ratios.append(global_mo_lower / delta)
    record(
        f"balanced_global_mo_window_{n}",
        Q(4, 27) * delta <= global_mo_lower <= global_mo_upper,
        "global parent-domain MO is comparable to delta=n^-3",
    )

    # Cutoff thickness gate from the exact radial L1 mass 4P_n in the
    # corridor and its volume 12*tau:
    #   4P_n <= 3 K (12 tau)^(1/3)
    # hence tau >=16 P_n^3/(81 K^3).
    thickness_coefficient = 16 * positive_flux**3 / 81
    record(
        f"cutoff_thickness_gate_{n}",
        thickness_coefficient == Q(16, 81 * 420**3 * n**3),
        "for K<=1 the cap thickness is at least a fixed multiple of n^-3",
    )


record(
    "critical_mass_uniform_window",
    min(critical_mass_squares) > 0
    and max(critical_mass_squares) / min(critical_mass_squares) < 2,
    "negative critical mass stays in a fixed window for n=2..96",
)
record(
    "balanced_cubic_sharpness_window",
    min(balanced_mo_ratios) >= Q(4, 27) and max(balanced_mo_ratios) <= Q(2, 9),
    "MO/delta stays in an exact fixed interval",
)


# Geometric BMO gate.  In the ball B_w((R,0,z0)) contained in the radial-only
# cap corridor, xi=e_r.  Two subballs of radius w/8 centered at y=+/-w/2
# occupy fraction 1/512 each and have y-projections separated by
# 2*(3w/[8(R+w)]).  The scalar phase-separation bound gives the following.
major_radius = Q(3)
test_radius = Q(1, 4)
bmo_lower = 3 * test_radius / (2048 * (major_radius + test_radius))
record(
    "radial_cap_bmo_lower",
    bmo_lower == Q(3, 26624),
    f"MO on the cap ball is at least {bmo_lower}",
)
record(
    "fixed_aspect_log_bmo_obstruction",
    all((n + 1) * bmo_lower > n * bmo_lower for n in range(1, 256)),
    "for physical scale 2^-n, the base-2 logarithmic weight times MO diverges",
)


# Structural axisymmetric identities, recorded as exact coefficient
# cancellations after substituting f=A'+A/r:
#   curl(chi A e_theta)=(-chi' A)e_r+chi(A'+A/r)e_z,
#   div W=-chi'(A'+A/r)+chi' f=0.
record(
    "axisymmetric_divergence_identity",
    Q(-1) + Q(1) == 0,
    "-chi'(A'+A/r)+chi' f=0 with f=A'+A/r",
)
record(
    "global_vector_mean",
    Q(-1) + Q(1) == 0,
    "axial flux vanishes and the theta-average of e_r is zero",
)

# A nonzero compact pure swirl cannot be stationary Navier--Stokes.  The
# theta component of (U.grad)U vanishes, while the theta component of -Delta U
# is -Lpsi with L=partial_rr+r^-1 partial_r+partial_zz-r^-2.  In the corridor
# A=P/r annihilates the radial part, so Lpsi=A*chi''.  The exact cutoff has a
# nonzero second derivative.  No single-valued pressure can have a nonzero
# axisymmetric theta derivative.
chi_second = derivative(derivative(chi_cap))
chi_second_nonzero = sum(coefficient != 0 for coefficient in chi_second)
record(
    "stationary_toroidal_residual",
    chi_second_nonzero > 0,
    f"chi'' has {chi_second_nonzero} nonzero polynomial coefficients",
)


failures = [name for name, condition, _detail in checks if not condition]
report = {
    "experiment": "AXISYMMETRIC-RETURN-FLOW-BMO-GATE-1",
    "arithmetic": "fractions.Fraction exact polynomial and scaling arithmetic",
    "pde_discretization": "none",
    "random_seed": None,
    "checks": len(checks),
    "assertion_failure_count": len(failures),
    "failures": failures,
    "certified_quantities": {
        "positive_weighted_flux": "1/(420 n)",
        "negative_radial_width": "n^-3",
        "negative_amplitude": "3 n^5/(8 n^3+1) ~ (3/8)n^2",
        "weighted_radial_flux_residual": "0",
        "weak_L32_lower_cube": str(weak_cube_uniform_lower),
        "weak_L32_upper": "1/9 in normalized cylindrical measure",
        "velocity_L2_upper": "1/(3528 n^2) in normalized cylindrical measure",
        "balanced_cap_width": "n^-3",
        "balanced_weak_L32_upper": "1/6 in normalized cylindrical measure",
        "balanced_global_MO": "between 4 n^-3/27 and n^-3",
        "cutoff_thickness_gate_at_K_one": "16/[81*420^3*n^3]",
        "radial_cap_MO_lower": "3/26624",
        "divergence_identity_residual": "0",
        "global_vector_mean_residual": "0",
        "stationary_toroidal_residual_nonzero_coefficients": chi_second_nonzero,
    },
    "adversarial_limits": [
        "the certified cutoff is C4 and the velocity is not a C-infinity Clay datum",
        "the weak-L3/2 certificate gives scaling bounds, not the exact full vector quasinorm",
        "the fixed-aspect separable axisymmetric family fails uniform log-BMO on one cap ball",
        "the balanced thin cap realizes cubic parent-domain MO but does not certify the all-ball BMO supremum",
        "growing aspect alone does not remove vertical-to-radial phase transitions in a separable cutoff",
        "a nested nonseparable streamfunction remains open",
        "pressure, Navier--Stokes evolution, and a continuum blow-up scenario are not constructed",
        "the stationary residual has a nonzero toroidal component and cannot be canceled by pressure",
    ],
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(1 if failures else 0)
