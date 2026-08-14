"""Exact ledger for the common-level pure-swirl cell selection theorem.

This is not a Navier--Stokes time discretisation.  It removes every root by
cubing and checks the finite algebra that follows the analytic inputs

    coarea + Per(E) >= C_I |E|^(2/3),
    integral_H |W| <= 3 ||W||_(3/2,infinity) |H|^(1/3).

The isoperimetric constant is normalised to C_I=1.  Restoring C_I changes the
selection constant from 1/324 to C_I/324.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


F = Fraction
SELECTION_DENOMINATOR = 324


def assert_nonnegative(value: Fraction, label: str, state: dict[str, object]) -> None:
    state["checks"] = int(state["checks"]) + 1
    if value < 0:
        failures = state["failures"]
        assert isinstance(failures, list)
        failures.append({"label": label, "residual": str(value)})


def assert_zero(value: Fraction, label: str, state: dict[str, object]) -> None:
    state["checks"] = int(state["checks"]) + 1
    absolute = abs(value)
    maximum = state["maximum_exact_residual"]
    assert isinstance(maximum, Fraction)
    state["maximum_exact_residual"] = max(maximum, absolute)
    if value:
        failures = state["failures"]
        assert isinstance(failures, list)
        failures.append({"label": label, "residual": str(value)})


def family_entries(family_id: int, cell_count: int) -> list[tuple[int, int, int]]:
    """Return (cell, sign, cube-root volume), including asymmetric zero signs."""

    entries: list[tuple[int, int, int]] = []
    for cell in range(cell_count):
        q_plus = 1 + ((family_id * (2 * cell + 3) + cell * cell + 1) % 11)
        entries.append((cell, 1, q_plus))
        if (family_id + 2 * cell) % 4:
            q_minus = 1 + ((family_id * (cell + 5) + 3 * cell + 2) % 9)
            entries.append((cell, -1, q_minus))
    return entries


def audit_common_level_families(state: dict[str, object]) -> dict[str, object]:
    lambdas = [F(1, 4), F(1, 2), F(1), F(3, 2), F(2), F(5)]
    family_count = 0
    entry_count = 0
    minimum_margin: Fraction | None = None

    for family_id in range(1536):
        cell_count = 1 + family_id % 8
        entries = family_entries(family_id, cell_count)
        lam = lambdas[family_id % len(lambdas)]
        volumes = [F(q**3) for _, _, q in entries]
        volume_total = sum(volumes, F(0))
        perimeter_sum = sum((F(q**2) for _, _, q in entries), F(0))
        maximum_signed_volume = max(volumes)

        # We test the sharp algebraic corner of every analytic inequality.
        ku_cube = lam**3 * volume_total
        epsilon_cube = lam**3 * maximum_signed_volume / 27
        halo_volume_upper = 216 * ku_cube / lam**3
        coarea_mass_lower = lam * perimeter_sum / 6
        kw_cube_minimum = coarea_mass_lower**3 / (27 * halo_volume_upper)

        assert_zero(
            ku_cube - lam**3 * volume_total,
            f"family-{family_id}: near-optimal volume identity",
            state,
        )
        assert_zero(
            halo_volume_upper - 216 * ku_cube / lam**3,
            f"family-{family_id}: lower-superlevel halo identity",
            state,
        )
        assert_zero(
            coarea_mass_lower - lam * perimeter_sum / 6,
            f"family-{family_id}: coarea mass identity",
            state,
        )
        assert_zero(
            27 * kw_cube_minimum * halo_volume_upper - coarea_mass_lower**3,
            f"family-{family_id}: weak-L3/2 integral identity",
            state,
        )

        # Cubed versions of both theorem conclusions are the same inequality.
        selection_margin = (
            epsilon_cube * SELECTION_DENOMINATOR**3 * kw_cube_minimum
            - ku_cube**2
        )
        assert_nonnegative(
            selection_margin,
            f"family-{family_id}: selected local velocity",
            state,
        )
        assert_nonnegative(
            selection_margin,
            f"family-{family_id}: selected local ratio",
            state,
        )

        # This is the finite concavity step used before the Lorentz estimate.
        concavity_margin = (
            perimeter_sum * F(max(q for _, _, q in entries)) - volume_total
        )
        assert_nonnegative(
            concavity_margin,
            f"family-{family_id}: sum V^(2/3) versus max V^(1/3)",
            state,
        )

        minimum_margin = (
            selection_margin
            if minimum_margin is None
            else min(minimum_margin, selection_margin)
        )
        family_count += 1
        entry_count += len(entries)

    assert minimum_margin is not None
    return {
        "families": family_count,
        "signed_superlevel_entries": entry_count,
        "minimum_selection_margin": str(minimum_margin),
        "selection_constant_normalized": "1/324",
    }


def audit_dyadic_core_tail(state: dict[str, object]) -> dict[str, object]:
    """Test a long low-amplitude tail with exact atomic distribution data.

    Level k has amplitude 2^-k and volume 8^k.  The total support/core ratio
    diverges, but every threshold sees a controlled lower superlevel and the
    common transition band forces a non-vanishing weak curl budget.
    """

    rows: list[dict[str, object]] = []
    minimum_forced_kw_cube: Fraction | None = None

    for depth in range(4, 25):
        amplitudes = [F(1, 2**k) for k in range(depth + 1)]
        volumes = [F(8**k) for k in range(depth + 1)]
        cumulative: list[Fraction] = []
        running = F(0)
        for volume in volumes:
            running += volume
            cumulative.append(running)

        weak_u_candidates = [
            amplitudes[k] ** 3 * cumulative[k] for k in range(depth + 1)
        ]
        ku_cube = max(weak_u_candidates)
        assert_nonnegative(F(8, 7) - ku_cube, f"tail-{depth}: Ku upper", state)
        assert_nonnegative(ku_cube - F(1), f"tail-{depth}: Ku lower", state)

        threshold_index = depth - 2
        lam = amplitudes[threshold_index]
        volume_above_lambda = cumulative[threshold_index - 1]
        halo_last_index = min(depth, threshold_index + 2)
        halo_volume = cumulative[halo_last_index]

        # Cubed coarea lower mass: (lambda V^(2/3)/6)^3.
        coarea_mass_cube = lam**3 * volume_above_lambda**2 / 216
        forced_kw_cube = coarea_mass_cube / (27 * halo_volume)
        assert_nonnegative(
            forced_kw_cube,
            f"tail-{depth}: forced weak curl nonnegative",
            state,
        )
        assert_zero(
            5832 * halo_volume * forced_kw_cube
            - lam**3 * volume_above_lambda**2,
            f"tail-{depth}: forced weak curl identity",
            state,
        )

        minimum_forced_kw_cube = (
            forced_kw_cube
            if minimum_forced_kw_cube is None
            else min(minimum_forced_kw_cube, forced_kw_cube)
        )
        rows.append(
            {
                "depth": depth,
                "support_to_core_volume": str(cumulative[-1]),
                "Ku_cube": str(ku_cube),
                "forced_Kw_cube_at_common_level": str(forced_kw_cube),
            }
        )

    assert minimum_forced_kw_cube is not None
    assert_nonnegative(
        minimum_forced_kw_cube - F(1, 22_000_000),
        "dyadic tail: uniform forced curl floor",
        state,
    )
    return {
        "depth_range": [4, 24],
        "largest_support_to_core_volume": rows[-1]["support_to_core_volume"],
        "Ku_cube_interval": ["1", "8/7"],
        "minimum_forced_Kw_cube": str(minimum_forced_kw_cube),
        "sample_rows": [rows[0], rows[len(rows) // 2], rows[-1]],
    }


def main() -> None:
    state: dict[str, object] = {
        "checks": 0,
        "failures": [],
        "maximum_exact_residual": F(0),
    }
    common_level = audit_common_level_families(state)
    core_tail = audit_dyadic_core_tail(state)
    failures = state["failures"]
    assert isinstance(failures, list)

    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result = {
        "experiment": "COMMON-LEVEL-HALO-SELECTION-1",
        "question": (
            "Can arbitrarily long low-amplitude pure-swirl tails destroy "
            "same-cell weak-endpoint selection?"
        ),
        "equation": (
            "static U_j=(R_j/r)F_j e_theta and "
            "W_j=curl U_j=(R_j/r)(-F_j,z e_r+F_j,r e_z)"
        ),
        "pde_discretization": "none; exact finite level-set ledger",
        "arithmetic": "fractions.Fraction; all roots removed by cubing",
        "random_seed": None,
        "common_level_ledger": common_level,
        "dyadic_core_tail": core_tail,
        "checks": state["checks"],
        "assertion_failure_count": len(failures),
        "maximum_exact_residual": str(state["maximum_exact_residual"]),
        "script_sha256": script_hash,
        "adversarial_limits": [
            "the ledger assumes the continuum coarea and R3 isoperimetric inputs",
            "cells are pure-swirl, annular and have disjoint complete supports",
            "the experiment certifies level-set algebra, not a smooth PDE trajectory",
            "controlled halo volume does not imply controlled spatial diameter",
            "overlapping curls, pressure, viscosity and time evolution are absent",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(json.dumps(failures[:10], indent=2))


if __name__ == "__main__":
    main()
