"""Exact audit of the adaptive diameter selection constants.

No Navier--Stokes evolution is simulated.  The continuum inputs are the
three-dimensional isoperimetric inequality, coarea, and the Lorentz integral
bound.  This script checks their algebraic composition with rational
arithmetic and probes an abstract merge-tree obstruction.  Cubes are used
throughout, so no floating-point root or tolerance enters the certificate.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


ETA = Q(1, 2)
SCALE_DENOMINATOR = 432
SLICE_CONSTANT = 12 * SCALE_DENOMINATOR**2
SELECTION_DENOMINATOR = 20_736
CELL_SELECTION_DENOMINATOR = 324
FAMILY_SELECTION_DENOMINATOR = (
    SELECTION_DENOMINATOR * CELL_SELECTION_DENOMINATOR**2
)


def algebraic_registry(roots: tuple[Q, ...], lam: Q, isoperimetric: Q):
    """Check a sharp rational ledger for heterogeneous core components.

    ``roots`` contains exact cube roots of the component core volumes.  We
    place the near-optimal weak-L3 choice on its boundary,
    K^3 = 8 lambda^3 V, and place the coarea/Lorentz comparison on its
    boundary.  The claimed scale and selected-component inequalities must
    then be exact identities after cubing.
    """
    assert roots and all(x > 0 for x in roots)
    assert lam > 0 and isoperimetric > 0

    lam3 = lam**3
    volumes = tuple(x**3 for x in roots)
    volume = sum(volumes, Q(0))
    k3 = 8 * lam3 * volume
    k6 = k3**2

    # The largest component velocity witness is
    # epsilon^3 = lambda^3 max(V_i)/12^3.
    epsilon3 = lam3 * max(volumes) / 12**3

    # Equality in C_I lambda^2 V/(144 epsilon) <= 18 H K/lambda.
    h3 = (
        isoperimetric**3
        * lam**9
        * volume**3
        / (2592**3 * epsilon3 * k3)
    )

    # Equality in lambda R >= K^2/(432 H), after cubing.
    r3 = k6 / (SCALE_DENOMINATOR**3 * h3 * lam3)

    checks = 0
    checks += 1
    assert k3 == 8 * lam3 * volume
    checks += 1
    assert (
        epsilon3 * SELECTION_DENOMINATOR**3 * h3
        == isoperimetric**3 * k6
    )
    checks += 1
    assert (
        lam3 * r3 * SCALE_DENOMINATOR**3 * h3
        == k6
    )

    # The rational diameter constant replaces 36/pi by 12 using pi>3.
    q_inverse_cube = h3 / k3
    diameter_bound = SLICE_CONSTANT * q_inverse_cube
    analytic_bound_with_pi_lower = (
        Q(36, 3) * SCALE_DENOMINATOR**2 * q_inverse_cube
    )
    checks += 1
    assert diameter_bound == analytic_bound_with_pi_lower

    # Heterogeneity inequality used by the endpoint pigeonhole step.
    sum_two_thirds = sum((x**2 for x in roots), Q(0))
    max_root = max(roots)
    checks += 1
    assert volume <= max_root * sum_two_thirds
    checks += 1
    assert sum_two_thirds >= volume / max_root

    return {
        "checks": checks,
        "components": len(roots),
        "diameter_bound": diameter_bound,
        "endpoint_margin_cube": (
            epsilon3
            * SELECTION_DENOMINATOR**3
            * h3
            / (isoperimetric**3 * k6)
        ),
        "scale_margin_cube": (
            lam3
            * r3
            * SCALE_DENOMINATOR**3
            * h3
            / k6
        ),
    }


def merge_tree_ledger(depth: int):
    """Exact abstract tree with unbounded low-persistence diameters.

    The upper part of a unit level interval has N leaves and total diameter
    one.  Its lower 1/N fraction contains ``depth`` binary-merge regimes;
    each has total diameter N and equal width.  The integral of the diameter
    sum stays below two although the root diameter tends to infinity.

    This is deliberately an abstract persistence ledger, not a certified
    smooth pure-swirl realization.
    """
    assert depth >= 1
    n_leaves = 2**depth
    leaf_width = Q(n_leaves - 1, n_leaves)
    merge_width = Q(1, n_leaves * depth)

    regimes = [
        {
            "generation": 0,
            "components": n_leaves,
            "diameter_sum": Q(1),
            "level_width": leaf_width,
        }
    ]
    for generation in range(1, depth + 1):
        components = 2 ** (depth - generation)
        regimes.append(
            {
                "generation": generation,
                "components": components,
                "diameter_sum": Q(n_leaves),
                "level_width": merge_width,
            }
        )

    total_width = sum((row["level_width"] for row in regimes), Q(0))
    integral = sum(
        (row["diameter_sum"] * row["level_width"] for row in regimes),
        Q(0),
    )
    root = regimes[-1]

    checks = 0
    checks += 1
    assert total_width == 1
    checks += 1
    assert integral == 2 - Q(1, n_leaves)
    checks += 1
    assert min(row["diameter_sum"] for row in regimes) <= integral
    checks += 1
    assert root["components"] == 1
    checks += 1
    assert root["diameter_sum"] == n_leaves
    checks += 1
    assert root["diameter_sum"] * root["level_width"] == Q(1, depth)

    return {
        "checks": checks,
        "depth": depth,
        "leaves": n_leaves,
        "diameter_integral": integral,
        "root_diameter": root["diameter_sum"],
        "root_persistence": root["level_width"],
    }


def main():
    checks = 0
    registries = 0
    maximum_components = 0
    minimum_endpoint_margin = None
    minimum_scale_margin = None

    # 2,016 heterogeneous component registries, all exact.
    for count in range(1, 33):
        for seed in range(1, 10):
            for skew in range(1, 8):
                roots = tuple(
                    Q(1 + ((seed * j + skew) % 11), 1 + ((j + skew) % 7))
                    for j in range(1, count + 1)
                )
                lam = Q(1 + seed % 5, 1 + skew % 4)
                c_i = Q(1 + skew % 3, 1 + seed % 3)
                row = algebraic_registry(roots, lam, c_i)
                checks += row["checks"]
                registries += 1
                maximum_components = max(maximum_components, row["components"])
                endpoint_margin = row["endpoint_margin_cube"]
                scale_margin = row["scale_margin_cube"]
                minimum_endpoint_margin = (
                    endpoint_margin
                    if minimum_endpoint_margin is None
                    else min(minimum_endpoint_margin, endpoint_margin)
                )
                minimum_scale_margin = (
                    scale_margin
                    if minimum_scale_margin is None
                    else min(minimum_scale_margin, scale_margin)
                )

    merge_rows = []
    for depth in range(1, 25):
        row = merge_tree_ledger(depth)
        checks += row["checks"]
        merge_rows.append(
            {
                key: str(value) if isinstance(value, Q) else value
                for key, value in row.items()
                if key != "checks"
            }
        )

    # Composition with the preceding heterogeneous-cell selector.
    checks += 3
    assert FAMILY_SELECTION_DENOMINATOR == 2_176_782_336
    assert SLICE_CONSTANT == 2_239_488
    assert ETA == Q(1, 2)

    script_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    result = {
        "experiment": "ADAPTIVE-DIAMETER-SELECTION-1",
        "arithmetic": "fractions.Fraction; no floating-point tolerance",
        "registries": registries,
        "maximum_components": maximum_components,
        "merge_tree_depths": len(merge_rows),
        "assertions": checks,
        "failures": 0,
        "constants": {
            "near_optimal_eta": str(ETA),
            "scale_denominator": SCALE_DENOMINATOR,
            "slice_constant_using_pi_gt_3": SLICE_CONSTANT,
            "one_cell_selection_denominator": SELECTION_DENOMINATOR,
            "family_selection_denominator": FAMILY_SELECTION_DENOMINATOR,
        },
        "minimum_endpoint_margin_cube": str(minimum_endpoint_margin),
        "minimum_scale_margin_cube": str(minimum_scale_margin),
        "deepest_merge_tree": merge_rows[-1],
        "sha256": script_hash,
        "residual": "0 (exact rational identities)",
        "limitations": [
            "coarea, isoperimetry and Lorentz bounds are analytic inputs",
            "the merge-tree suite is an abstract persistence ledger, not a smooth curl-compatible realization",
            "no pressure, viscosity, Leray projection, time evolution or PDE residual is computed",
            "the result concerns disjoint compact pure-swirl cells, not arbitrary three-dimensional velocity fields",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
