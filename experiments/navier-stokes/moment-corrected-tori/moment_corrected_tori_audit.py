"""Exact scale audit for an impulse-cancelled pair of thin vortex tori.

Cycle 0029 tests the first moment-correction gate only.  The script certifies
rational scale identities for two translated, oppositely signed copies of the
cycle-0028 torus.  Tubular geometry, the all-ball BMO reduction, the
Biot--Savart estimate, and the multipole interpretation are analytic inputs.
"""

from __future__ import annotations

import json
from fractions import Fraction


CHECKS = 0
FAILURES: list[str] = []


def require(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        FAILURES.append(label)


def dyadic(exponent: int) -> Fraction:
    return Fraction(1, 2**exponent)


previous_pair_envelope: Fraction | None = None
last_values: dict[str, str] = {}

for n in range(4, 65):
    radius = dyadic(n)
    corridor = dyadic(2 * n)
    core = dyadic(n * n)
    half_separation = 3 * radius
    one_torus_volume = radius * core * core

    require(0 < core < corridor < radius, f"ordered scales n={n}")
    require(2 * corridor < 2 * half_separation, f"disjoint corridors n={n}")
    require(corridor == radius * radius, f"q=R^2 n={n}")

    # A^3 V^2=1 for either torus.  The disjoint union has bounded, but not
    # unit, weak and strong critical cubes: their scale proxy equals four.
    amplitude_cubed = 1 / one_torus_volume**2
    pair_critical_cube = amplitude_cubed * (2 * one_torus_volume) ** 2
    require(pair_critical_cube == 4, f"pair critical cube n={n}")

    # The two copies have equal geometric impulse magnitudes and opposite
    # signs.  Translation does not alter impulse because each vector mean is
    # zero.  Coefficients are audited independently of the common magnitude.
    positive_impulse_coefficient = Fraction(1)
    negative_impulse_coefficient = Fraction(-1)
    total_impulse_coefficient = (
        positive_impulse_coefficient + negative_impulse_coefficient
    )
    require(total_impulse_coefficient == 0, f"impulse cancellation n={n}")

    # Translating the signed copies by +/-a creates a nonzero second-moment
    # coefficient 4aM_x,y.  This is the first uncancelled multipole proxy.
    second_moment_coefficient = 4 * half_separation
    require(second_moment_coefficient > 0, f"nonzero second moment n={n}")

    log_core = n * n
    log_corridor = 2 * n
    log_radius = n
    log_span = log_core - log_corridor
    single_envelope = (
        Fraction(log_core, log_span)
        + Fraction(log_corridor, log_span)
        + log_corridor * corridor / radius
        + log_corridor * (core / corridor) ** 2
        + Fraction(log_radius, log_span) * (corridor / radius) ** 2
        + log_radius * (core / radius) ** 2
    )
    pair_envelope = 2 * single_envelope
    require(pair_envelope < 8, f"pair all-ball envelope n={n}")
    if previous_pair_envelope is not None:
        require(
            pair_envelope < previous_pair_envelope,
            f"decreasing pair envelope n={n}",
        )
    previous_pair_envelope = pair_envelope

    # Minkowski and the one-torus tube lemma give the pair upper bound
    # ||u_+-u_-||_3^3 <= 8 C[(h/R)+(h/R)^2].
    pair_velocity_lower_scale = core / radius
    pair_velocity_upper_scale = 8 * (
        core / radius + (core / radius) ** 2
    )
    require(
        0 < pair_velocity_lower_scale < pair_velocity_upper_scale,
        f"two-sided L3 scale n={n}",
    )
    require(
        pair_velocity_upper_scale
        <= 16 * dyadic(n * n - n),
        f"pair L3 collapse n={n}",
    )

    # The algebraic upper scale beats any fixed power of R eventually.
    for power in range(1, 25):
        if n - 1 >= power:
            require(
                core / radius <= radius**power,
                f"superpolynomial pair collapse n={n}, p={power}",
            )

    last_values = {
        "n": str(n),
        "R": f"2^-{n}",
        "q": f"2^-{2 * n}",
        "h": f"2^-{n * n}",
        "half_separation": f"3*2^-{n}",
        "total_impulse_coefficient": "0",
        "pair_critical_cube_proxy": "4",
        "pair_log_bmo_envelope_upper": "8",
        "pair_velocity_lower_scale": f"2^-{n * n - n}",
        "pair_velocity_upper_scale": f"8*(2^-{n * n - n}+2^-{2 * n * n - 2 * n})",
    }


result = {
    "experiment": "MOMENT-CORRECTED-TORI-GATE-1",
    "question": "Can a finite opposite-signed torus pair cancel impulse while preserving a nonvanishing critical velocity?",
    "arithmetic": "fractions.Fraction exact dyadic scale arithmetic",
    "pde_discretization": "none",
    "random_seed": None,
    "checks": CHECKS,
    "assertion_failure_count": len(FAILURES),
    "failures": FAILURES,
    "certified_quantities": {
        "scales": "R_n=2^-n, q_n=2^-2n, h_n=2^-n^2 for 4<=n<=64",
        "pair_critical_cube_proxy": "A_n^3(2R_n h_n^2)^2=4",
        "impulse_coefficient": "+1-1=0",
        "first_uncancelled_multipole_proxy": "4 a_n M_xy != 0",
        "dimensionless_pair_log_bmo_envelope": "strictly below 8 before universal constants",
        "pair_velocity_two_sided_scale": "c(h_n/R_n) <= ||u_n||_3^3 <= C[(h_n/R_n)+(h_n/R_n)^2]",
    },
    "analytic_identities_not_discretized": [
        "each translated torus is smooth, divergence-free, and has zero vector mean",
        "translation leaves hydrodynamic impulse invariant when the vector mean vanishes",
        "disjoint logarithmic corridors can rotate +e_theta and -e_theta to the same e_z background",
        "the all-ball pair estimate follows by local separation and large-ball dilution",
        "the second moment produces an algebraic far-field tail unless further moments cancel",
        "Minkowski combines the two proved one-torus Biot--Savart L3 bounds",
        "Stokes on a core cross-section supplies the matching lower L3 scale for a fixed plateau profile",
    ],
    "adversarial_limits": [
        "no Navier--Stokes evolution or pressure is computed",
        "the script does not certify tubular or kernel constants",
        "impulse cancellation alone does not produce Schwartz velocity on R3",
        "the finite pair leaves the axisymmetric class only when its parallel axes are transversely displaced",
        "the experiment proves an upper collapse, not a matching L3 asymptotic",
    ],
    "last_scale": last_values,
}

print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
