"""Exact cancellation-gauge ledger for two overlapping labelled cells.

The finite atom model is a falsifier for component-selection arguments based
only on global weak Lorentz endpoints and overlap multiplicity.  It is not a
discretization of Navier--Stokes and does not certify the smooth trigonometric
realization described in the cycle report.  All checks use Fraction.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def weak_cube(atoms: list[tuple[Q, Q]], exponent: Q) -> Q:
    """Return the cube of the weak-L^p quasi-norm of a step function.

    ``atoms`` are (absolute amplitude, volume).  For p=3 the cube is
    sup a^3 mu(a); for p=3/2 it is sup a^3 mu(a)^2.
    """
    ordered = sorted(atoms, key=lambda row: row[0], reverse=True)
    cumulative = Q(0)
    best = Q(0)
    for amplitude, volume in ordered:
        assert amplitude >= 0 and volume > 0
        cumulative += volume
        if exponent == 3:
            candidate = amplitude**3 * cumulative
        elif exponent == Q(3, 2):
            candidate = amplitude**3 * cumulative**2
        else:
            raise ValueError(exponent)
        best = max(best, candidate)
    return best


def cancellation_model(frequency: int, rho: Q = Q(1)) -> dict[str, Q | int]:
    """Evaluate the four-atom cancellation model at one frequency.

    Atoms are indexed by independent signs (p,z).  The total velocity and
    curl are V=B=1.  Add the cancelling pair P=p and Z=M z through
    (U1,W1)=(V+P,B+Z), (U2,W2)=(-P,-Z).  The two labelled cells overlap on
    every atom, yet their sum is exactly the fixed total field.
    """
    assert frequency >= 8 and rho > 0
    volume = Q(1, 4) / rho**3
    velocity_scale = rho
    curl_scale = rho**2

    global_u: list[tuple[Q, Q]] = []
    global_w: list[tuple[Q, Q]] = []
    cell1_u: list[tuple[Q, Q]] = []
    cell1_w: list[tuple[Q, Q]] = []
    cell2_u: list[tuple[Q, Q]] = []
    cell2_w: list[tuple[Q, Q]] = []

    checks = 0
    for p_sign in (-1, 1):
        for z_sign in (-1, 1):
            v = Q(1) * velocity_scale
            b = Q(1) * curl_scale
            p = Q(p_sign) * velocity_scale
            z = Q(frequency * z_sign) * curl_scale
            u1, u2 = v + p, -p
            w1, w2 = b + z, -z

            checks += 2
            assert u1 + u2 == v
            assert w1 + w2 == b

            global_u.append((abs(v), volume))
            global_w.append((abs(b), volume))
            cell1_u.append((abs(u1), volume))
            cell1_w.append((abs(w1), volume))
            cell2_u.append((abs(u2), volume))
            cell2_w.append((abs(w2), volume))

    ku_global3 = weak_cube(global_u, Q(3))
    kw_global3 = weak_cube(global_w, Q(3, 2))
    ku1_3 = weak_cube(cell1_u, Q(3))
    kw1_3 = weak_cube(cell1_w, Q(3, 2))
    ku2_3 = weak_cube(cell2_u, Q(3))
    kw2_3 = weak_cube(cell2_w, Q(3, 2))

    checks += 8
    assert ku_global3 == 1
    assert kw_global3 == 1
    assert ku1_3 == 4
    assert kw1_3 == Q((frequency - 1) ** 3)
    assert ku2_3 == 1
    assert kw2_3 == Q(frequency**3)
    assert ku1_3 / kw1_3 == Q(4, (frequency - 1) ** 3)
    assert ku2_3 / kw2_3 == Q(1, frequency**3)

    return {
        "checks": checks,
        "frequency": frequency,
        "global_ratio_cube": ku_global3 / kw_global3,
        "cell1_ratio_cube": ku1_3 / kw1_3,
        "cell2_ratio_cube": ku2_3 / kw2_3,
    }


def main() -> None:
    checks = 0
    models = 0
    maximum_local_ratio_cube = Q(0)
    minimum_local_ratio_cube = None

    # Consecutive frequencies expose threshold changes; several critical
    # rescalings independently check invariance of both endpoint cubes.
    scalings = (Q(1, 8), Q(1, 3), Q(1), Q(5, 2), Q(16))
    for frequency in range(8, 4097):
        reference = None
        for rho in scalings:
            row = cancellation_model(frequency, rho)
            checks += int(row["checks"])
            models += 1
            pair_max = max(row["cell1_ratio_cube"], row["cell2_ratio_cube"])
            maximum_local_ratio_cube = max(maximum_local_ratio_cube, pair_max)
            minimum_local_ratio_cube = (
                pair_max
                if minimum_local_ratio_cube is None
                else min(minimum_local_ratio_cube, pair_max)
            )
            signature = (
                row["global_ratio_cube"],
                row["cell1_ratio_cube"],
                row["cell2_ratio_cube"],
            )
            if reference is None:
                reference = signature
            else:
                checks += 1
                assert signature == reference

    # Dyadic asymptotic family: no positive function of the fixed global
    # ratio can lower-bound either labelled-cell ratio.
    dyadic = []
    previous = None
    for power in range(3, 41):
        frequency = 2**power
        row = cancellation_model(frequency)
        checks += int(row["checks"])
        local_max = max(row["cell1_ratio_cube"], row["cell2_ratio_cube"])
        if previous is not None:
            checks += 1
            assert local_max < previous
        previous = local_max
        dyadic.append(
            {
                "frequency": frequency,
                "global_ratio_cube": str(row["global_ratio_cube"]),
                "maximum_labelled_ratio_cube": str(local_max),
            }
        )

    script_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    result = {
        "experiment": "OVERLAPPING-CURL-CANCELLATION-1",
        "arithmetic": "fractions.Fraction; no floating-point tolerance",
        "models": models,
        "frequencies": "8..4096 plus dyadic 2^3..2^40",
        "critical_scalings": [str(value) for value in scalings],
        "assertions": checks,
        "failures": 0,
        "overlap_multiplicity": 2,
        "global_ratio_cube": "1",
        "maximum_local_ratio_cube_over_registry": str(maximum_local_ratio_cube),
        "minimum_local_ratio_cube_over_registry": str(minimum_local_ratio_cube),
        "last_dyadic": dyadic[-1],
        "residual": "0 (pointwise sums and exact distribution suprema)",
        "sha256": script_hash,
        "limitations": [
            "the four-atom ledger is not a spatial curl realization",
            "the smooth sin(nz) realization and its level-set measure are analytic inputs",
            "the construction refutes selection among labelled summands, not selection from the total field",
            "no pressure, Leray projection, viscosity, time evolution or PDE residual is computed",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
