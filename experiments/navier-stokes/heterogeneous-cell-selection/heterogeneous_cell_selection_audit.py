"""Exact audit for cycle 0034 heterogeneous-cell selection.

The script has two independent parts.

1. A dyadic measurable counterexample disproves same-cell selection from
   weak-Lorentz quasi-norms alone.
2. A finite registered-atom model verifies the exact algebra of the BV
   selection lemma.  Each registered cell satisfies

       B_j q_j = A_j v_j^(2/3),   q_j <= v_j,

   with v_j and q_j chosen as rational cubes, so no roots are evaluated.

No PDE is evolved and no continuum inequality is numerically certified.
"""

from __future__ import annotations

import json
from fractions import Fraction as F


def grouped_volumes(atoms: list[tuple[F, F]]) -> list[tuple[F, F]]:
    """Return amplitudes in descending order with equal levels grouped."""
    grouped: dict[F, F] = {}
    for amplitude, volume in atoms:
        assert amplitude > 0
        assert volume > 0
        grouped[amplitude] = grouped.get(amplitude, F(0)) + volume
    return sorted(grouped.items(), key=lambda item: item[0], reverse=True)


def weak_l3_cube(atoms: list[tuple[F, F]]) -> F:
    """Exact cube of sup_t t |{|f|>t}|^(1/3) for step atoms."""
    cumulative = F(0)
    maximum = F(0)
    for amplitude, volume in grouped_volumes(atoms):
        cumulative += volume
        maximum = max(maximum, amplitude**3 * cumulative)
    return maximum


def weak_l32_cube(atoms: list[tuple[F, F]]) -> F:
    """Exact cube of sup_t t |{|f|>t}|^(2/3) for step atoms."""
    cumulative = F(0)
    maximum = F(0)
    for amplitude, volume in grouped_volumes(atoms):
        cumulative += volume
        maximum = max(maximum, amplitude**3 * cumulative**2)
    return maximum


checks = 0
max_exact_residual = F(0)
abstract_rows = 0
registered_families = 0
registered_cells = 0


# Part I: exact dyadic counterexample.  Closed forms avoid materializing
# 8**n atoms at the larger rows.
for n in range(1, 5):
    component_count = 8**n
    cell_volume = F(1, 8**n)
    cell_ku_cube = cell_volume

    assert component_count * cell_volume == 1
    assert cell_ku_cube == F(1, 8**n)
    checks += 2

    # At curl level j: G_j=4^(n+j), q_j=8^(-(n+j)).
    for j in (0, min(n, component_count - 1), component_count - 1):
        gradient = F(4 ** (n + j))
        curl_volume = F(1, 8 ** (n + j))
        local_kw_cube = gradient**3 * curl_volume**2
        assert local_kw_cube == 1
        assert cell_ku_cube / local_kw_cube == F(1, 8**n)

        # The registered BV ratio would be
        # (G_j q_j)/(A_j v_j^(2/3))=2^(n-j).
        bv_ratio = gradient * curl_volume / F(1, 4**n)
        assert bv_ratio == F(2**n, 2**j)
        checks += 3

    # The global weak-L^(3/2) cube just below level k is the square of a
    # truncated geometric tail.  It lies in [1, 64/49].
    for k in (0, min(n, component_count - 1), component_count - 1):
        tail_factor = (
            1 - F(1, 8 ** (component_count - k))
        ) / (1 - F(1, 8))
        global_kw_cube_at_k = tail_factor**2
        assert F(1) <= global_kw_cube_at_k <= F(64, 49)
        checks += 1

    # A compulsory thick return at common amplitude 2^n accumulates across
    # all cells and has global Kw^3=8^n.
    base_gradient = F(2**n)
    global_base_kw_cube = base_gradient**3 * (
        component_count * cell_volume
    ) ** 2
    assert global_base_kw_cube == F(8**n)
    checks += 1
    abstract_rows += 1


# Materialize the two manageable rows and recompute both total distribution
# functions by sorting and cumulative volumes.
for n in (1, 2):
    component_count = 8**n
    cell_volume = F(1, 8**n)
    velocity_atoms = [(F(1), cell_volume) for _ in range(component_count)]
    curl_atoms = [
        (F(4 ** (n + j)), F(1, 8 ** (n + j)))
        for j in range(component_count)
    ]

    ku_cube = weak_l3_cube(velocity_atoms)
    kw_cube = weak_l32_cube(curl_atoms)
    closed_kw_cube = (
        (1 - F(1, 8**component_count)) / (1 - F(1, 8))
    ) ** 2
    residual = kw_cube - closed_kw_cube
    max_exact_residual = max(max_exact_residual, abs(residual))

    assert ku_cube == 1
    assert residual == 0
    assert F(1) <= kw_cube <= F(64, 49)
    checks += 3


def amplitude(pattern: int, index: int) -> F:
    """Deterministic heterogeneous amplitude families."""
    if pattern == 0:
        return F(1)
    if pattern == 1:
        return F(2**index)
    if pattern == 2:
        return F(1, 2**index)
    if pattern == 3:
        return F(2 ** (index // 2), 3 ** (index % 2))
    if pattern == 4:
        return F(index + 1, 2)
    return F(3, index + 2)


# Part II: exact registered-atom selection.  Put v_j=r_j^3, q_j=s_j^3 and
# B_j=A_j r_j^2/s_j^3.  Then B_j q_j=A_j v_j^(2/3) exactly.
for scale in range(1, 13):
    for cell_count in range(1, 17):
        for pattern in range(6):
            velocity_atoms: list[tuple[F, F]] = []
            curl_atoms: list[tuple[F, F]] = []
            local_ku_cubes: list[F] = []
            local_ratio_cubes: list[F] = []

            for index in range(cell_count):
                amp = amplitude(pattern, index)
                radius = F(1, 2 ** (scale + index % 4))
                return_divisor = 1 + (pattern + 2 * index) % 7
                return_radius = radius / return_divisor

                velocity_volume = radius**3
                curl_volume = return_radius**3
                gradient = amp * radius**2 / return_radius**3

                velocity_atoms.append((amp, velocity_volume))
                curl_atoms.append((gradient, curl_volume))

                local_ku_cube = amp**3 * velocity_volume
                local_kw_cube = gradient**3 * curl_volume**2
                local_ratio_cube = local_ku_cube / local_kw_cube

                assert curl_volume <= velocity_volume
                assert gradient * curl_volume == amp * radius**2
                assert local_ratio_cube == (return_radius / radius) ** 3
                checks += 3

                local_ku_cubes.append(local_ku_cube)
                local_ratio_cubes.append(local_ratio_cube)
                registered_cells += 1

            ku_cube = weak_l3_cube(velocity_atoms)
            kw_cube = weak_l32_cube(curl_atoms)
            epsilon_cube = max(local_ku_cubes)
            max_ratio_cube = max(local_ratio_cubes)

            # Exact cubed forms of
            #   epsilon >= Ku^2/(3 Kw),
            #   max_j Ku_j/Kw_j >= Ku^2/(3 Kw^2).
            assert 27 * epsilon_cube * kw_cube >= ku_cube**2
            assert 27 * max_ratio_cube * kw_cube**2 >= ku_cube**2
            checks += 2
            registered_families += 1


result = {
    "adversarial_limits": [
        "the dyadic counterexample does not impose W=curl U",
        "the registered atoms encode, but do not numerically prove, the BV/coarea closure cost",
        "overlapping curl supports and cancellation are excluded",
        "effective boxes must have volume comparable to their active cores",
        "no pressure, Biot-Savart tail, viscosity, or time evolution is computed",
    ],
    "arithmetic": "fractions.Fraction exact; all roots removed by cubing",
    "assertion_failure_count": 0,
    "checks": checks,
    "counterexample": {
        "abstract_rows": abstract_rows,
        "global_Ku_cube": "1",
        "global_Kw_cube_upper": "64/49",
        "local_ratio_cube": "1/8^n",
        "maximum_exact_residual": str(max_exact_residual),
    },
    "experiment": "HETEROGENEOUS-CELL-SELECTION-1",
    "pde_discretization": "none; finite exact distribution ledger",
    "question": "Do global weak-L3/weak-L3/2 gates select one cell, and which geometric register is indispensable?",
    "random_seed": None,
    "registered_model": {
        "families": registered_families,
        "cells": registered_cells,
        "identity": "B_j q_j=A_j v_j^(2/3)",
        "selection_inequalities": [
            "epsilon >= Ku^2/(3 Kw)",
            "max_j(Ku_j/Kw_j) >= Ku^2/(3 Kw^2)",
        ],
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
