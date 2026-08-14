"""Exact critical-scale audit for a compact separable swirl (cycle 0031).

The script validates rational proxy identities behind the anisotropic Lorentz
budget.  It does not discretize Navier--Stokes or certify smooth-profile,
all-ball BMO, or time-evolution estimates.
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


def critical_cubes(
    radius: Fraction,
    radial_width: Fraction,
    axial_width: Fraction,
    amplitude_cubed: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    """Return velocity, axial-curl, and radial-curl weak-norm cube proxies."""

    velocity = amplitude_cubed * radius * radial_width * axial_width
    axial_curl = (
        amplitude_cubed * radius**2 * axial_width**2 / radial_width
    )
    radial_curl = (
        amplitude_cubed * radius**2 * radial_width**2 / axial_width
    )
    return velocity, axial_curl, radial_curl


# General anisotropic ledger on an exact rational grid.  Write a=R/i and
# b=R/j.  Then K_z^3/K_u^3=i^2/j and K_r^3/K_u^3=j^2/i.
for scale_power in range(1, 9):
    radius = Fraction(1, 2**scale_power)
    for radial_aspect in range(1, 25):
        radial_width = radius / radial_aspect
        for axial_aspect in range(1, 25):
            axial_width = radius / axial_aspect
            amplitude_cubed = Fraction(
                1, radius * radial_width * axial_width
            )
            velocity, axial_curl, radial_curl = critical_cubes(
                radius,
                radial_width,
                axial_width,
                amplitude_cubed,
            )

            expected_axial = Fraction(radial_aspect**2, axial_aspect)
            expected_radial = Fraction(axial_aspect**2, radial_aspect)
            require(velocity == 1, "velocity normalization")
            require(axial_curl == expected_axial, "axial derivative budget")
            require(radial_curl == expected_radial, "radial derivative budget")
            require(
                axial_curl * radial_curl
                == Fraction(radial_aspect * axial_aspect, 1),
                "product aspect identity",
            )
            require(
                max(axial_curl, radial_curl) ** 2
                >= axial_curl * radial_curl,
                "max dominates geometric mean",
            )

            # If both derivative budgets are at most H, both aspect ratios are
            # at most H.  This is the exact discrete form of a/R,b/R>=1/H.
            derivative_budget = max(axial_curl, radial_curl)
            require(
                max(radial_aspect, axial_aspect) <= derivative_budget,
                "two-component non-thinning implication",
            )
            minimum_width_ratio = min(radial_width, axial_width) / radius
            require(
                velocity / derivative_budget <= minimum_width_ratio,
                "velocity-to-vorticity aspect collapse",
            )

            # Navier--Stokes isotropic scaling leaves all three critical cubes
            # invariant: lengths multiply by s and velocity by 1/s.
            dilation = Fraction(1, 2 ** (scale_power + 1))
            scaled = critical_cubes(
                dilation * radius,
                dilation * radial_width,
                dilation * axial_width,
                amplitude_cubed / dilation**3,
            )
            require(
                scaled == (velocity, axial_curl, radial_curl),
                "critical scaling invariance",
            )


# Decisive dyadic family: increasing aspect makes the known directional-MO
# lower proxy vanish, but one must lose either vorticity or velocity endpoint.
previous_weighted_bmo: Fraction | None = None
last_values: dict[str, str] = {}
for n in range(2, 41):
    radius = Fraction(1, 2**n)
    aspect = 2**n
    radial_width = radius / aspect
    axial_width = radius / aspect

    velocity_normalized_amplitude_cubed = Fraction(
        1, radius * radial_width * axial_width
    )
    velocity, axial_curl, radial_curl = critical_cubes(
        radius,
        radial_width,
        axial_width,
        velocity_normalized_amplitude_cubed,
    )
    require(velocity == 1, f"dyadic velocity gate n={n}")
    require(axial_curl == aspect, f"dyadic axial loss n={n}")
    require(radial_curl == aspect, f"dyadic radial loss n={n}")

    # Divide V^3 by the aspect to normalize both vorticity cube proxies.
    vorticity_normalized_amplitude_cubed = (
        velocity_normalized_amplitude_cubed / aspect
    )
    collapsed_velocity, normalized_axial, normalized_radial = critical_cubes(
        radius,
        radial_width,
        axial_width,
        vorticity_normalized_amplitude_cubed,
    )
    require(collapsed_velocity == Fraction(1, aspect), f"velocity loss n={n}")
    require(normalized_axial == 1, f"normalized axial curl n={n}")
    require(normalized_radial == 1, f"normalized radial curl n={n}")

    # The active cap ball has radius proportional to a=b=2^-2n.  Its known
    # directional-MO lower proxy is a/R=2^-n and its base-two log weight is 2n.
    bmo_lower_proxy = radial_width / radius
    weighted_bmo_lower_proxy = 2 * n * bmo_lower_proxy
    require(bmo_lower_proxy == Fraction(1, aspect), f"BMO aspect n={n}")
    require(
        weighted_bmo_lower_proxy == Fraction(2 * n, 2**n),
        f"weighted BMO proxy n={n}",
    )
    if previous_weighted_bmo is not None:
        require(
            weighted_bmo_lower_proxy < previous_weighted_bmo,
            f"decreasing weighted BMO proxy n={n}",
        )
    previous_weighted_bmo = weighted_bmo_lower_proxy

    last_values = {
        "n": str(n),
        "major_radius": f"2^-{n}",
        "radial_width": f"2^-{2 * n}",
        "axial_width": f"2^-{2 * n}",
        "aspect": f"2^{n}",
        "velocity_normalized_cube": "1",
        "vorticity_cube_under_velocity_normalization": f"2^{n}",
        "velocity_cube_under_vorticity_normalization": f"2^-{n}",
        "weighted_directional_mo_lower_proxy": f"{2 * n}/2^{n}",
    }


result = {
    "experiment": "COMPACT-SWIRL-ASPECT-GATE-1",
    "question": (
        "Can growing toroidal aspect flatten the active vorticity direction "
        "while preserving weak-L3 velocity and weak-L3/2 vorticity gates?"
    ),
    "arithmetic": "fractions.Fraction exact rational bookkeeping",
    "pde_discretization": "none",
    "random_seed": None,
    "checks": CHECKS,
    "assertion_failure_count": len(FAILURES),
    "failures": FAILURES,
    "certified_quantities": {
        "velocity_cube_proxy": "V^3 R a b",
        "axial_curl_cube_proxy": "V^3 R^2 b^2/a",
        "radial_curl_cube_proxy": "V^3 R^2 a^2/b",
        "cube_ratio_product": "R^2/(ab)",
        "endpoint_collapse": (
            "K_U^3 <= max(K_z^3,K_r^3) min(a,b)/R at proxy level"
        ),
        "dyadic_family": "R_n=2^-n and a_n=b_n=2^-2n",
        "endpoint_dichotomy": (
            "K_U^3=1 forces both curl proxies to 2^n; "
            "curl proxies=1 force K_U^3=2^-n"
        ),
        "directional_lower_proxy": "2n/2^n after logarithmic weighting",
    },
    "analytic_identities_not_discretized": [
        "the fixed smooth profiles have transition subsets of uniformly positive relative measure",
        "the R/r factor exactly cancels cylindrical curvature in the axial curl component",
        "weak Lorentz lower bounds follow from the transition-set amplitudes and volumes",
        "a cap ball of radius comparable to min(a,b) carries the pure radial direction e_r",
        "the all-ball log-BMO obstruction follows from the cap-ball mean-oscillation lemma",
    ],
    "adversarial_limits": [
        "only one fixed separable compact swirl profile is covered",
        "profile constants are not interval-certified",
        "nonseparable layers may mask or redistribute derivative transitions",
        "no pressure or Navier--Stokes evolution is computed",
        "no continuum PDE claim is certified by the finite audit",
    ],
    "last_scale": last_values,
}

print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
