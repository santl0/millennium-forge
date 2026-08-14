"""Exact ledger for the componentwise pure-swirl droplet selection lemma.

This is not a Navier--Stokes evolution.  It checks, over finite rational
families, the algebra remaining after coarea, Euclidean isoperimetry and the
weak-Lorentz integral bound have been supplied analytically.  Cubes are used
throughout, so no floating-point root or tolerance enters the certification.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


LAMBDA = Fraction(7, 5)
LORENTZ_CONSTANT = 3
HALO_VOLUME_CONSTANT = 6**3
SELECTION_CONSTANT = 648


def families():
    """Generate deterministic heterogeneous component-volume families."""
    for length in range(1, 11):
        for seed in range(1, 193):
            yield tuple(Fraction(1 + ((seed * (i + 3) + i * i) % 17), 1 + ((seed + 2 * i) % 5)) for i in range(length))


def audit_family(q):
    # V_i=q_i^3 is the lambda/2 active volume of component i.
    volume = sum((x**3 for x in q), Fraction(0))
    perimeter_sum = sum((x**2 for x in q), Fraction(0))
    q_max = max(q)

    # We take the selected level to attain the weak-L3 quasi-norm.  This is
    # the eta=0 endpoint of the analytic near-maximizer argument.
    ku_cube = LAMBDA**3 * volume

    # Every truncated component is >lambda/6 on its active core.
    epsilon_cube = (LAMBDA * q_max / 6) ** 3

    # Minimal coarea/isoperimetric mass (C_I normalized to one), followed by
    # equality in the global weak-L^(3/2) upper estimate.
    mass_lower = LAMBDA * perimeter_sum / 6
    # Kw^3 = (lambda*mass/(18*Ku))^3 and Ku^3=ku_cube.
    kw_cube = (LAMBDA * mass_lower / 18) ** 3 / ku_cube

    # Cubed forms of epsilon >= Ku^2/(648 Kw) and q_max*S>=V.
    selection_left = epsilon_cube * SELECTION_CONSTANT**3 * kw_cube
    selection_right = ku_cube**2
    packing_left = q_max * perimeter_sum
    packing_right = volume

    checks = 0
    checks += 1
    assert packing_left >= packing_right
    checks += 1
    assert selection_left >= selection_right
    checks += 1
    assert mass_lower > 0 and kw_cube > 0 and epsilon_cube > 0

    return checks, selection_left - selection_right, packing_left - packing_right


def identical_droplet_rows():
    """Certify the m^(-1/3) loss of the global endpoint ratio."""
    rows = []
    checks = 0
    for m in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
        q = (Fraction(1),) * m
        volume = Fraction(m)
        perimeter_sum = Fraction(m)
        ku_cube = LAMBDA**3 * volume
        mass_lower = LAMBDA * perimeter_sum / 6
        kw_cube = (LAMBDA * mass_lower / 18) ** 3 / ku_cube
        ratio_cube = ku_cube / kw_cube
        normalized_ratio_cube = ratio_cube / (108**3)
        checks += 1
        assert normalized_ratio_cube == Fraction(1, m)
        rows.append({"m": m, "normalized_global_ratio_cube": str(normalized_ratio_cube)})
    return rows, checks


def main():
    total_checks = 0
    family_count = 0
    zero_residual_count = 0
    minimum_selection_residual = None
    minimum_packing_residual = None

    for q in families():
        checks, selection_residual, packing_residual = audit_family(q)
        total_checks += checks
        family_count += 1
        zero_residual_count += int(selection_residual == 0)
        minimum_selection_residual = selection_residual if minimum_selection_residual is None else min(minimum_selection_residual, selection_residual)
        minimum_packing_residual = packing_residual if minimum_packing_residual is None else min(minimum_packing_residual, packing_residual)

    rows, checks = identical_droplet_rows()
    total_checks += checks

    # A connector of amplitude lambda/8 is absent from both the lambda/4
    # component set and the lambda/6 weak-norm test, regardless of its length.
    subthreshold_connector = LAMBDA / 8
    total_checks += 2
    assert subthreshold_connector < LAMBDA / 6
    assert subthreshold_connector < LAMBDA / 4

    script_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    result = {
        "experiment": "COMPONENTWISE-DROPLET-SELECTION-1",
        "arithmetic": "fractions.Fraction; exact cubed inequalities",
        "families": family_count,
        "component_instances": sum(range(1, 11)) * 192,
        "assertions": total_checks,
        "failures": 0,
        "minimum_selection_residual": str(minimum_selection_residual),
        "minimum_packing_residual": str(minimum_packing_residual),
        "selection_equality_families": zero_residual_count,
        "identical_droplets": rows,
        "subthreshold_connector": str(subthreshold_connector),
        "sha256": script_hash,
        "limitations": [
            "coarea, isoperimetry and the weak-Lorentz integral bound are analytic inputs",
            "no grid, time evolution, pressure, viscosity or PDE residual is computed",
            "components joined above lambda/4 and overlapping original cells are not tested",
            "bounded droplet diameter is assumed only when invoking the separate direction gate",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
