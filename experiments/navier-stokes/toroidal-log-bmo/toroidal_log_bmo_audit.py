"""Exact scale audit for the thin-torus log-BMO escape (cycle 0028).

The script certifies only rational scale identities and an analytic all-ball
envelope reduced in the cycle report.  It does not discretize Navier--Stokes,
compute the periodic Biot--Savart operator, or prove the geometric constants
hidden in that reduction.
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


previous_envelope: Fraction | None = None
last_values: dict[str, str] = {}

for n in range(4, 65):
    # Physical major radius, logarithmic-extension radius, and active core.
    radius = dyadic(n)
    corridor = dyadic(2 * n)
    core = dyadic(n * n)
    volume_scale = radius * core * core

    require(0 < core < corridor < radius < Fraction(1, 2), f"scale order n={n}")
    require(corridor == radius * radius, f"q=R^2 n={n}")

    # If A=(R h^2)^(-2/3), all identities below avoid fractional powers.
    amplitude_cubed = 1 / (volume_scale * volume_scale)
    weak_l32_cube = amplitude_cubed * volume_scale * volume_scale
    strong_l32_cube = amplitude_cubed * volume_scale * volume_scale
    l1_mass_cube = amplitude_cubed * volume_scale**3
    l65_norm_sixth = amplitude_cubed**2 * volume_scale**5
    enstrophy_cubed = amplitude_cubed**2 * volume_scale**3

    require(weak_l32_cube == 1, f"critical weak L32 cube n={n}")
    require(strong_l32_cube == 1, f"critical strong L32 cube n={n}")
    require(l1_mass_cube == volume_scale, f"L1 mass cube n={n}")
    require(l65_norm_sixth == volume_scale, f"L65 sixth power n={n}")
    require(enstrophy_cubed == 1 / volume_scale, f"enstrophy cube n={n}")

    # Logarithms are measured in units of log(2), which cancels in ratios.
    log_core = n * n
    log_corridor = 2 * n
    log_radius = n
    log_span = log_core - log_corridor
    require(log_span > 0, f"positive log span n={n}")

    # Regime envelope from the analytic four-scale ball decomposition:
    # rho<=h, h<=rho<=q, q<=rho<=R/2, and rho>=R/2.
    local_transition = Fraction(log_core, log_span)
    corridor_transition = Fraction(log_corridor, log_span)
    azimuthal_turn = log_corridor * corridor / radius
    core_leakage = log_corridor * (core / corridor) ** 2
    outer_sparse = Fraction(log_radius, log_span) * (corridor / radius) ** 2
    outer_core = log_radius * (core / radius) ** 2
    envelope = (
        local_transition
        + corridor_transition
        + azimuthal_turn
        + core_leakage
        + outer_sparse
        + outer_core
    )

    require(local_transition <= 2, f"local log budget n={n}")
    require(corridor_transition <= 1, f"corridor log budget n={n}")
    require(azimuthal_turn <= Fraction(1, 2), f"azimuth budget n={n}")
    require(envelope < 4, f"uniform all-ball envelope n={n}")
    if previous_envelope is not None:
        require(envelope < previous_envelope, f"decreasing envelope n={n}")
    previous_envelope = envelope

    # The Biot--Savart tube estimate predicts ||U||_3^3 <= C h/R.
    velocity_l3_cube_scale = core / radius
    require(velocity_l3_cube_scale <= dyadic(n * (n - 1)), f"L3 collapse n={n}")

    # For every fixed polynomial exponent p, the terminal active fraction is
    # eventually smaller than R^p.  The threshold is checked exactly.
    terminal_fraction = (core / corridor) ** 2
    for power in range(1, 25):
        if 2 * n - 4 >= power:
            require(
                terminal_fraction <= radius**power,
                f"superpolynomial terminal fraction n={n}, p={power}",
            )

    last_values = {
        "n": str(n),
        "R": f"2^-{n}",
        "q": f"2^-{2 * n}",
        "h": f"2^-{n * n}",
        "volume_scale": f"2^-{n + 2 * n * n}",
        "all_ball_envelope_upper": "4",
        "terminal_fraction": f"2^-{2 * n * n - 4 * n}",
        "velocity_L3_cube_scale": f"2^-{n * n - n}",
    }


result = {
    "experiment": "TOROIDAL-LOG-BMO-ESCAPE-1",
    "arithmetic": "fractions.Fraction exact dyadic scale arithmetic",
    "pde_discretization": "none",
    "random_seed": None,
    "checks": CHECKS,
    "assertion_failure_count": len(FAILURES),
    "failures": FAILURES,
    "certified_quantities": {
        "scales": "R_n=2^-n, q_n=2^-2n, h_n=2^-n^2 for 4<=n<=64",
        "critical_normalization": "A_n^3 (R_n h_n^2)^2 = 1",
        "strong_L32_normalization": "||W_n||_(3/2)^3 comparable to 1 in the smooth torus model",
        "L1_mass_cube": "(R_n h_n^2)",
        "L65_norm_sixth": "(R_n h_n^2)",
        "enstrophy_cubed": "1/(R_n h_n^2)",
        "dimensionless_log_bmo_envelope": "strictly below 4 before universal geometric constants",
        "terminal_fraction": "(h_n/q_n)^2 is eventually below R_n^p for each checked 1<=p<=24",
        "velocity_L3_cube_scale": "h_n/R_n",
    },
    "analytic_identities_not_discretized": [
        "div(f(r,z)e_theta)=0 for axisymmetric f",
        "the vector mean vanishes after theta integration",
        "on T^3, mean-zero divergence-free W has a smooth mean-zero periodic Biot--Savart velocity",
        "the four-regime ball estimate reduces localized log-BMO to the audited envelope up to universal constants",
    ],
    "adversarial_limits": [
        "the smooth bump and tubular-coordinate constants are analytic inputs, not interval-certified here",
        "the all-ball estimate is an upper envelope, not the exact BMO seminorm",
        "the periodic pressure and Navier--Stokes evolution are not computed",
        "the velocity L3 collapse uses a separate proved Biot--Savart tube lemma, not interval-certified by this script",
        "the family is static and does not produce a blow-up trajectory",
    ],
    "last_scale": last_values,
}

print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
