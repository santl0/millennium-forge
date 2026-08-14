"""Exact scale audit for a densely packed many-torus family (cycle 0030).

The script checks the dyadic bookkeeping behind the porous-tube Biot--Savart
lemma.  It does not discretize Navier--Stokes or certify the analytic kernel,
HLS, tubular-coordinate, or all-ball BMO estimates used by that lemma.
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


previous_porous_bound: Fraction | None = None
last_values: dict[str, str] = {}

for n in range(2, 41):
    # Parent scale, disjoint logarithmic corridor, and active tube radius.
    parent = dyadic(3 * n)
    corridor = dyadic(9 * n)
    core = dyadic(12 * n)

    # Coaxial circles are placed on a meridional square grid.  Spacing 8q and
    # M=2^(6n-6) use only one eighth of the parent span in each grid direction.
    grid_side = 2 ** (6 * n - 6)
    count = grid_side * grid_side
    grid_span = grid_side * 8 * corridor
    length_proxy = count * parent

    require(0 < core < corridor < parent, f"ordered scales n={n}")
    require(grid_span == parent / 8, f"grid span n={n}")
    require(count == 2 ** (12 * n - 12), f"torus count n={n}")

    parent_volume = parent**3
    corridor_volume_proxy = length_proxy * corridor**2
    active_volume_proxy = length_proxy * core**2
    packing_fraction = corridor_volume_proxy / parent_volume
    active_fraction = active_volume_proxy / parent_volume

    require(packing_fraction == dyadic(12), f"corridor packing n={n}")
    require(
        active_fraction == dyadic(6 * n + 12),
        f"active fraction n={n}",
    )
    require(
        active_fraction
        == packing_fraction * (core / corridor) ** 2,
        f"porous fraction identity n={n}",
    )

    # A^3 S^2=1 fixes the global weak-L^(3/2) scale for equal amplitudes.
    amplitude_cubed = 1 / active_volume_proxy**2
    weak_l32_cube = amplitude_cubed * active_volume_proxy**2
    strong_l32_cube = amplitude_cubed * active_volume_proxy**2
    require(weak_l32_cube == 1, f"weak L32 normalization n={n}")
    require(strong_l32_cube == 1, f"strong L32 normalization n={n}")

    # The logarithmic corridor has exactly the physical log-depth required at
    # the parent scale.  Logs are measured in units of log(2).
    physical_log = 3 * n
    corridor_depth = 12 * n - 9 * n
    require(corridor_depth == physical_log, f"log depth n={n}")
    local_bmo_proxy = Fraction(12 * n, corridor_depth)
    parent_bmo_proxy = physical_log * packing_fraction / corridor_depth
    bmo_envelope = local_bmo_proxy + parent_bmo_proxy
    require(local_bmo_proxy == 4, f"local BMO proxy n={n}")
    require(parent_bmo_proxy == packing_fraction, f"parent BMO proxy n={n}")
    require(bmo_envelope < 5, f"uniform BMO envelope n={n}")

    # A componentwise triangle estimate would permit growth: its cube proxy is
    # N h/R.  The porous-tube lemma instead gives the two collapsing terms
    # h/L_tot and (h/q)^(4/3).  The exponents were chosen to stay dyadic.
    naive_triangle_cube = count * core / parent
    local_velocity_cube = core / length_proxy
    far_velocity_cube = dyadic(4 * n)
    porous_velocity_cube = local_velocity_cube + far_velocity_cube

    require(
        naive_triangle_cube == Fraction(2 ** max(3 * n - 12, 0), 2 ** max(12 - 3 * n, 0)),
        f"naive triangle scale n={n}",
    )
    require(
        local_velocity_cube == dyadic(21 * n - 12),
        f"local velocity scale n={n}",
    )
    require(
        far_velocity_cube**3 == (core / corridor) ** 4,
        f"far porosity exponent n={n}",
    )
    require(
        active_volume_proxy < far_velocity_cube,
        f"periodic smooth remainder n={n}",
    )
    require(porous_velocity_cube < 1, f"porous collapse bound n={n}")
    if previous_porous_bound is not None:
        require(
            porous_velocity_cube < previous_porous_bound,
            f"decreasing porous bound n={n}",
        )
    previous_porous_bound = porous_velocity_cube

    if n >= 5:
        require(naive_triangle_cube > 1, f"triangle false positive n={n}")

    # The active occupation is exactly the corridor packing fraction times
    # ell^2; no superpolynomial claim is made for this decisive family.
    require(
        active_fraction == packing_fraction * parent**2,
        f"active parent-square law n={n}",
    )

    last_values = {
        "n": str(n),
        "parent_scale": f"2^-{3 * n}",
        "corridor_radius": f"2^-{9 * n}",
        "core_radius": f"2^-{12 * n}",
        "grid_side": f"2^{6 * n - 6}",
        "torus_count": f"2^{12 * n - 12}",
        "packing_fraction": "2^-12",
        "active_fraction": f"2^-{6 * n + 12}",
        "naive_triangle_cube": f"2^{3 * n - 12}",
        "local_velocity_cube": f"2^-{21 * n - 12}",
        "far_velocity_cube": f"2^-{4 * n}",
        "periodic_smooth_remainder_cube": f"2^-{15 * n + 12}",
    }


result = {
    "experiment": "MANY-TORUS-POROSITY-GATE-1",
    "question": "Can growing cardinality overcome thin-tube L3 collapse under disjoint log-BMO corridors and uniform local packing?",
    "arithmetic": "fractions.Fraction exact dyadic bookkeeping",
    "pde_discretization": "none",
    "random_seed": None,
    "checks": CHECKS,
    "assertion_failure_count": len(FAILURES),
    "failures": FAILURES,
    "certified_quantities": {
        "scales": "ell_n=2^-3n, q_n=2^-9n, h_n=2^-12n for 2<=n<=40",
        "growing_cardinality": "N_n=2^(12n-12)",
        "corridor_packing_fraction": "N_n ell_n q_n^2/ell_n^3=2^-12",
        "active_fraction": "N_n ell_n h_n^2/ell_n^3=2^(-6n-12)",
        "critical_normalization": "A_n^3 S_n^2=1",
        "log_depth": "log_2(q_n/h_n)=|log_2 ell_n|=3n",
        "naive_triangle_cube": "N_n h_n/ell_n=2^(3n-12), which diverges",
        "porous_local_cube": "h_n/L_n=2^(-21n+12)",
        "porous_far_cube": "(h_n/q_n)^(4/3)=2^-4n",
        "periodic_smooth_remainder_cube": "S_n=2^(-15n-12) in a unit cell",
    },
    "analytic_identities_not_discretized": [
        "coaxial circular q-tubes on the meridional grid are pairwise disjoint and have uniformly controlled reach",
        "local q-truncated Biot--Savart fields have L3 cube bounded by C A^3 L h^5",
        "disjoint q-tubes imply the Morrey packing bound mu(B_r)<=C A(h/q)^2 r^3 for r>=q",
        "Hedberg plus HLS and L2--L-infinity interpolation bound the far L3 cube by C K^3(h/q)^(4/3)",
        "the logarithmic direction extensions satisfy the all-ball envelope up to universal constants",
    ],
    "adversarial_limits": [
        "the porosity lemma assumes a common core radius, corridor radius, and amplitude",
        "heterogeneous multiscale tubes and overlapping corridors are not covered",
        "the exact geometric constants and smooth bump factors are not interval-certified",
        "the coaxial same-sign realization is axisymmetric without swirl and globally regular",
        "no pressure or Navier--Stokes evolution is computed",
    ],
    "last_scale": last_values,
}

print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
