"""Exact ledger for a persistent pure-swirl bridge.

No Navier--Stokes evolution is simulated.  The script checks rational lower
and upper distribution bounds for a piecewise-linear annular bridge and the
algebraic constant in the perimeter--diameter persistence corollary.  We use
3 < pi < 22/7, so every reported certificate is rational and tolerance-free.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


PI_LOWER = Q(3)
PI_UPPER = Q(22, 7)
PERSISTENCE_CONSTANT = Q(3, 2)


def bridge_bounds(R: Q, D: Q, w: Q, cutoff: Q, eta: Q):
    """Return exact distribution bounds for a linear radial bridge.

    The plateau height is B=cutoff*(1+eta), its axial length is D, its
    half-support width is w, and its two radial ramps have total width w.
    Axial caps of total length 2w are included in the velocity support bound.
    """
    assert R > 0 and D > 0 and Q(0) < w <= R / 4
    assert cutoff > 0 and eta > 0
    B = cutoff * (1 + eta)

    # A plateau of radial width w and length D has volume at least
    # 2*pi*R*w*D > 6*R*w*D.  There |U| >= (8/9)B.
    plateau_volume_lower = 2 * PI_LOWER * R * w * D
    ku_lower_cube = (Q(8, 9) * B) ** 3 * plateau_volume_lower

    # Full support: radial width 2w and axial length D+2w.
    support_volume_upper = 4 * PI_UPPER * R * w * (D + 2 * w)
    ku_upper_cube = B**3 * support_volume_upper

    # On both radial ramps over the central length D,
    # |W_z| >= (2/3)*(2B/w)=4B/(3w), and their total volume is
    # 2*pi*R*w*D > 6*R*w*D.
    ramp_volume_lower = 2 * PI_LOWER * R * w * D
    kw_lower_cube = (Q(4, 3) * B / w) ** 3 * ramp_volume_lower**2

    # Only eta/(1+eta) of each ramp survives in (F-cutoff)_+.
    truncated_ramp_volume_lower = ramp_volume_lower * eta / (1 + eta)
    kw_truncated_lower_cube = (
        (Q(4, 3) * B / w) ** 3 * truncated_ramp_volume_lower**2
    )

    ratio_upper_cube = ku_upper_cube / kw_lower_cube
    ratio_formula = Q(33, 224) * w**2 * (D + 2 * w) / (R * D**2)

    # The analytic lemma gives A^2 R D <= 9/(2*pi) Ku Kw.  The rational
    # certificate uses pi>3, hence A^2 R D <= (3/2) Ku Kw, equivalently
    # Ku*Kw >= (2/3) A^2 R D.  The explicit plateau/ramp witnesses are
    # stronger; cubes avoid irrational roots.
    persistence_required_product_cube = (
        Q(2, 3) * cutoff**2 * R * D
    ) ** 3
    witnessed_product_cube = ku_lower_cube * kw_lower_cube

    full_cost_formula = (
        Q(256, 3) * B**3 * R**2 * D**2 / w
    )
    truncated_cost_formula = (
        Q(256, 3)
        * cutoff**3
        * R**2
        * D**2
        / w
        * eta**2
        * (1 + eta)
    )

    checks = 0
    checks += 1
    assert kw_lower_cube == full_cost_formula
    checks += 1
    assert kw_truncated_lower_cube == truncated_cost_formula
    checks += 1
    assert ratio_upper_cube == ratio_formula
    checks += 1
    assert witnessed_product_cube >= persistence_required_product_cube
    checks += 1
    assert ku_lower_cube <= ku_upper_cube

    return {
        "checks": checks,
        "ratio_upper_cube": ratio_upper_cube,
        "full_cost_cube": kw_lower_cube / (cutoff * R) ** 3,
        "truncated_cost_cube": kw_truncated_lower_cube / (cutoff * R) ** 3,
        "persistence_margin_cube": (
            witnessed_product_cube / persistence_required_product_cube
        ),
    }


def main():
    checks = 0
    families = 0
    minimum_persistence_margin = None
    maximum_ratio_upper_cube = Q(0)

    # Heterogeneous exact registry.
    for n in range(1, 17):
        L = Q(2**n)
        for j in range(1, 9):
            delta = Q(1, 2**j)
            for k in range(1, 9):
                eta = Q(1, 2**k)
                R = Q(1 + (n % 3), 1 + (j % 3))
                D = L * R
                w = delta * R / 4
                cutoff = Q(1 + (k % 5), 1 + (n % 4))
                row = bridge_bounds(R, D, w, cutoff, eta)
                checks += row["checks"]
                families += 1
                maximum_ratio_upper_cube = max(
                    maximum_ratio_upper_cube, row["ratio_upper_cube"]
                )
                margin = row["persistence_margin_cube"]
                minimum_persistence_margin = (
                    margin
                    if minimum_persistence_margin is None
                    else min(minimum_persistence_margin, margin)
                )

    # Decisive vanishing-excess family: delta=1/L, eta=L^(-3/2), with
    # L=m^2.  The truncated curl stays O(1), but the original curl cost cube
    # grows exactly like L^3 up to the harmless factor (1+eta)^3.
    vanishing_excess = []
    for m in (2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64):
        L = Q(m * m)
        delta = 1 / L
        eta = Q(1, m**3)
        row = bridge_bounds(Q(1), L, delta, Q(1), eta)
        checks += row["checks"]
        families += 1
        checks += 2
        assert row["truncated_cost_cube"] == Q(256, 3) * (1 + eta)
        assert row["full_cost_cube"] == Q(256, 3) * (1 + eta) ** 3 * L**3
        vanishing_excess.append(
            {
                "L": str(L),
                "delta": str(delta),
                "eta": str(eta),
                "truncated_cost_cube": str(row["truncated_cost_cube"]),
                "full_cost_cube_over_L3": str(row["full_cost_cube"] / L**3),
            }
        )

    script_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    result = {
        "experiment": "PERSISTENT-BRIDGE-DIAMETER-1",
        "arithmetic": "fractions.Fraction; 3 < pi < 22/7",
        "families": families,
        "assertions": checks,
        "failures": 0,
        "persistence_constant": str(PERSISTENCE_CONSTANT),
        "minimum_persistence_margin_cube": str(minimum_persistence_margin),
        "maximum_ratio_upper_cube": str(maximum_ratio_upper_cube),
        "vanishing_excess": vanishing_excess,
        "sha256": script_hash,
        "limitations": [
            "the continuum perimeter-diameter and coarea steps are analytic inputs",
            "the explicit bridge is piecewise linear; smooth approximation is not interval-certified",
            "no pressure, viscosity, time evolution or PDE residual is computed",
            "the conditional diameter corollary still requires cutoff*R comparable to Ku",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
