"""Exact scale audit for the bounded-cross-section direction gate.

The experiment checks the algebra behind cycle 0033.  It does not discretize
Navier--Stokes, compute a BMO supremum, or certify the continuum coarea and
Lorentz lemmas.  All declared finite quantities use Fraction arithmetic.
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


def weak_cubes_unit_cells(amplitudes: list[Fraction]) -> tuple[Fraction, Fraction]:
    """Return weak-L3 and weak-L3/2 norm cubes for unit-volume cells."""

    ordered = sorted((abs(value) for value in amplitudes), reverse=True)
    velocity_cube = max(
        value**3 * rank for rank, value in enumerate(ordered, start=1)
    )
    vorticity_cube = max(
        value**3 * rank**2 for rank, value in enumerate(ordered, start=1)
    )
    return velocity_cube, vorticity_cube


# 1. Exact cube-level identity in the analytic proof.  Plane weak cubes are
# K_f^3 and K_g^3.  Cylindrical lifting gives K_u^3=R K_f^3 and
# K_w^3=R^2 K_g^3.  The cone-compensation output is proportional to
# K_f^6/(K_g^3 K_w^3)=(K_u^3/K_w^3)^2.
for n in range(1, 33):
    major_radius = Fraction(1, 2**n)
    for f_cube in (Fraction(1, 8), Fraction(1), Fraction(27, 8), Fraction(8)):
        for g_cube in (Fraction(1, 16), Fraction(1), Fraction(16)):
            velocity_cube = major_radius * f_cube
            vorticity_cube = major_radius**2 * g_cube
            direction_proxy = f_cube**2 / (g_cube * vorticity_cube)
            endpoint_proxy = (velocity_cube / vorticity_cube) ** 2
            require(
                direction_proxy == endpoint_proxy,
                f"cylindrical direction identity n={n}",
            )


# 2. Plateau shell.  L=R/8 and transition thickness delta.  Up to fixed
# profile constants, K_u^3=V^3 R L^2 and K_w^3=V^3 R^2 L^2/delta.
# The active directional fraction delta/L is reciprocal to the endpoint cost.
plateau_records: list[dict[str, str | int]] = []
for n in range(2, 25):
    major_radius = Fraction(1, 2**n)
    outer_radius = major_radius / 8
    for depth in range(3, 15):
        transition = major_radius / 2**depth
        require(transition <= outer_radius, "transition inside plateau shell")
        amplitude_cube = Fraction(1)
        velocity_cube = amplitude_cube * major_radius * outer_radius**2
        vorticity_cube = (
            amplitude_cube
            * major_radius**2
            * outer_radius**2
            / transition
        )
        endpoint_cost = vorticity_cube / velocity_cube
        active_fraction = transition / outer_radius
        require(
            endpoint_cost == major_radius / transition,
            "plateau endpoint cost R/delta",
        )
        require(
            active_fraction * endpoint_cost == major_radius / outer_radius,
            "plateau direction-endpoint reciprocity",
        )

        # Normalize the vorticity cube to one.  The remaining velocity cube is
        # exactly delta/R and vanishes if the directional shell is made thin.
        normalized_amplitude_cube = (
            transition
            / (major_radius**2 * outer_radius**2)
        )
        normalized_velocity_cube = (
            normalized_amplitude_cube * major_radius * outer_radius**2
        )
        require(
            normalized_velocity_cube == transition / major_radius,
            "plateau normalized velocity collapse",
        )
        plateau_records.append(
            {
                "n": n,
                "depth": depth,
                "endpoint_cost": str(endpoint_cost),
                "active_fraction": str(active_fraction),
                "normalized_velocity_cube": str(normalized_velocity_cube),
            }
        )


# 3. Rare antipodal return.  A unit main direction on volume 1-epsilon is
# balanced by amplitude (1-epsilon)/epsilon on volume epsilon.  The mean is
# exactly zero, but the weak-L3/2 cube grows like epsilon^-1 while the smallest
# two-phase mean oscillation is 4 epsilon(1-epsilon).
rare_return_records: list[dict[str, str | int]] = []
for depth in range(2, 31):
    epsilon = Fraction(1, 2**depth)
    main_volume = 1 - epsilon
    return_amplitude = main_volume / epsilon
    signed_mean = main_volume - return_amplitude * epsilon
    weak_vorticity_cube = max(
        Fraction(1), return_amplitude**3 * epsilon**2
    )
    direction_mo = 4 * epsilon * main_volume
    require(signed_mean == 0, "rare return exact mean cancellation")
    require(
        weak_vorticity_cube == main_volume**3 / epsilon,
        "rare return weak endpoint cost",
    )
    require(direction_mo > 0, "rare return positive direction oscillation")
    require(
        direction_mo * weak_vorticity_cube
        == 4 * main_volume**4,
        "rare return cone-cost reciprocity",
    )
    rare_return_records.append(
        {
            "depth": depth,
            "epsilon": str(epsilon),
            "weak_vorticity_cube": str(weak_vorticity_cube),
            "direction_mo": str(direction_mo),
        }
    )


# 4. Axially separated cells.  Equal amplitudes make the endpoint ratio grow
# like the number of cells.  Dyadically decreasing amplitudes keep both weak
# endpoints dominated by the first cell, so separation alone does not erase a
# locally dominant component.
separated_records: list[dict[str, str | int]] = []
for count in range(1, 257):
    equal_velocity, equal_vorticity = weak_cubes_unit_cells(
        [Fraction(1)] * count
    )
    require(equal_velocity == count, "equal-cell weak-L3 cube")
    require(equal_vorticity == count**2, "equal-cell weak-L3/2 cube")
    require(
        equal_vorticity / equal_velocity == count,
        "equal-cell endpoint ratio",
    )

    dyadic = [Fraction(1, 2**index) for index in range(count)]
    dyadic_velocity, dyadic_vorticity = weak_cubes_unit_cells(dyadic)
    require(dyadic_velocity == 1, "dyadic cells velocity dominated by first")
    require(
        dyadic_vorticity == 1,
        "dyadic cells vorticity dominated by first",
    )
    separated_records.append(
        {
            "count": count,
            "equal_endpoint_ratio_cube": str(
                equal_vorticity / equal_velocity
            ),
            "dyadic_velocity_cube": str(dyadic_velocity),
            "dyadic_vorticity_cube": str(dyadic_vorticity),
        }
    )


result = {
    "experiment": "BOUNDED-CROSS-SECTION-DIRECTION-GATE-1",
    "question": (
        "Can thick plateaus, rare antipodal returns, or axial separation "
        "make the direction BMO small without paying a critical endpoint cost?"
    ),
    "pde_discretization": "none; static exact scale ledger",
    "random_seed": None,
    "arithmetic": "fractions.Fraction exact; all roots avoided by cubing",
    "checks": CHECKS,
    "assertion_failure_count": len(FAILURES),
    "failures": FAILURES,
    "certified_finite_quantities": {
        "cylindrical_identity": (
            "K_f^6/(K_g^3 K_w^3)=(K_u^3/K_w^3)^2"
        ),
        "plateau_shell": (
            "endpoint_cost=R/delta and active_fraction=delta/L"
        ),
        "rare_return": (
            "K_w^3=(1-epsilon)^3/epsilon and "
            "MO=4 epsilon(1-epsilon)"
        ),
        "separated_equal_cells": "K_w^3/K_u^3=N",
        "separated_dyadic_cells": (
            "both weak cubes are dominated exactly by the first cell"
        ),
    },
    "enumeration": {
        "cylindrical_scales": "1<=n<=32, 12 norm pairs per scale",
        "plateau_shells": len(plateau_records),
        "rare_returns": len(rare_return_records),
        "separated_cell_counts": len(separated_records),
    },
    "adversarial_limits": [
        "fixed profile constants and the continuum cone cover are not certified",
        "no BMO supremum over balls is numerically evaluated",
        "the plateau and cell ledgers are proxies, not smooth PDE solutions",
        "heterogeneous cells without a dominant component remain open",
        "no pressure, viscosity, stretching, or time evolution is computed",
    ],
}

print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
