"""Exact finite-element scale audit for two-layer compact pure swirls.

Cycle 0032 tests whether cancellations between two nonseparable meridional
layers can defeat the support-area Lorentz collapse.  The finite-element
fields are exact continuous P1 functions on rational triangulations.  This is
not a Navier--Stokes time discretization and does not certify the continuum
Sobolev--Lorentz theorem used in the accompanying analytic lemma.
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


def hat(x: Fraction, center: Fraction, width: Fraction) -> Fraction:
    value = 1 - abs(x - center) / width
    return max(Fraction(0), value)


def layer(
    x: Fraction,
    y: Fraction,
    center_x: Fraction,
    center_y: Fraction,
    width_x: Fraction,
    width_y: Fraction,
) -> Fraction:
    return hat(x, center_x, width_x) * hat(y, center_y, width_y)


def triangle_gradient(
    vertices: tuple[
        tuple[Fraction, Fraction, Fraction],
        tuple[Fraction, Fraction, Fraction],
        tuple[Fraction, Fraction, Fraction],
    ],
) -> tuple[Fraction, Fraction, Fraction]:
    (x1, y1, f1), (x2, y2, f2), (x3, y3, f3) = vertices
    det = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    require(det != 0, "nondegenerate triangle")
    gx = ((f2 - f1) * (y3 - y1) - (f3 - f1) * (y2 - y1)) / det
    gy = ((x2 - x1) * (f3 - f1) - (x3 - x1) * (f2 - f1)) / det
    return gx, gy, abs(det) / 2


def weak_gradient_cube_squared(
    gradient_cells: list[tuple[Fraction, Fraction]],
) -> Fraction:
    """Return [sup_lambda lambda^3 |{|grad F|>lambda}|^2]^2 exactly."""

    by_magnitude: dict[Fraction, Fraction] = {}
    for magnitude_squared, area in gradient_cells:
        if magnitude_squared > 0:
            by_magnitude[magnitude_squared] = (
                by_magnitude.get(magnitude_squared, Fraction(0)) + area
            )

    cumulative_area = Fraction(0)
    best = Fraction(0)
    for magnitude_squared in sorted(by_magnitude, reverse=True):
        cumulative_area += by_magnitude[magnitude_squared]
        # (|grad F|^3 area^2)^2 = |grad F|^6 area^4.
        candidate = magnitude_squared**3 * cumulative_area**4
        best = max(best, candidate)
    return best


def p1_shape_audit(
    mesh: int,
    coefficient: Fraction,
    center_2: tuple[Fraction, Fraction],
    width_2: tuple[Fraction, Fraction],
) -> dict[str, Fraction]:
    coordinates = [Fraction(-2) + Fraction(4 * i, mesh) for i in range(mesh + 1)]
    values: dict[tuple[int, int], Fraction] = {}
    for i, x in enumerate(coordinates):
        for j, y in enumerate(coordinates):
            first = layer(x, y, Fraction(0), Fraction(0), Fraction(1), Fraction(1))
            second = layer(x, y, center_2[0], center_2[1], width_2[0], width_2[1])
            values[(i, j)] = first + coefficient * second

    maximum = max(abs(value) for value in values.values())
    support_area = Fraction(0)
    gradient_cells: list[tuple[Fraction, Fraction]] = []
    for i in range(mesh):
        for j in range(mesh):
            x0, x1 = coordinates[i], coordinates[i + 1]
            y0, y1 = coordinates[j], coordinates[j + 1]
            triangles = (
                ((i, j), (i + 1, j), (i, j + 1)),
                ((i + 1, j + 1), (i, j + 1), (i + 1, j)),
            )
            for indices in triangles:
                vertices = tuple(
                    (
                        coordinates[ii],
                        coordinates[jj],
                        values[(ii, jj)],
                    )
                    for ii, jj in indices
                )
                gx, gy, area = triangle_gradient(vertices)  # type: ignore[arg-type]
                vertex_values = [values[index] for index in indices]
                if any(value != 0 for value in vertex_values):
                    support_area += area
                gradient_cells.append((gx * gx + gy * gy, area))

            require((x1 - x0) * (y1 - y0) > 0, "positive mesh cell")

    gradient_weak_squared = weak_gradient_cube_squared(gradient_cells)
    require(maximum > 0, "nonzero two-layer field")
    require(gradient_weak_squared > 0, "nonzero compact gradient")

    # The velocity weak-L3 cube is at most ||F||_infinity^3 times support
    # area (and the ring factor R).  The following dimensionless quotient is
    # the square of that upper cube divided by the exact weak-gradient cube.
    shape_ratio_squared = (
        maximum**6 * support_area**2 / gradient_weak_squared
    )
    return {
        "maximum": maximum,
        "support_area": support_area,
        "gradient_weak_cube_squared": gradient_weak_squared,
        "shape_ratio_squared": shape_ratio_squared,
    }


meshes = (8, 12, 16, 20)
coefficients = (
    Fraction(-2),
    Fraction(-1),
    Fraction(-1, 2),
    Fraction(1, 2),
    Fraction(1),
    Fraction(2),
)
centers = (
    (Fraction(1, 2), Fraction(1, 2)),
    (Fraction(1, 2), Fraction(-1, 2)),
    (Fraction(0), Fraction(1, 2)),
    (Fraction(-1, 2), Fraction(1, 2)),
)
widths = (
    (Fraction(1), Fraction(1)),
    (Fraction(1, 2), Fraction(1)),
    (Fraction(1), Fraction(1, 2)),
    (Fraction(3, 2), Fraction(1, 2)),
)

shape_records: list[dict[str, object]] = []
maximum_shape_ratio_squared = Fraction(0)
worst_shape: dict[str, object] = {}

for mesh in meshes:
    for coefficient in coefficients:
        for center in centers:
            for width in widths:
                audit = p1_shape_audit(mesh, coefficient, center, width)
                ratio_squared = audit["shape_ratio_squared"]
                require(ratio_squared > 0, "positive shape quotient")
                require(
                    ratio_squared <= 9,
                    "uniform finite two-layer shape bound",
                )
                if ratio_squared > maximum_shape_ratio_squared:
                    maximum_shape_ratio_squared = ratio_squared
                    worst_shape = {
                        "mesh": mesh,
                        "coefficient": str(coefficient),
                        "center": [str(value) for value in center],
                        "width": [str(value) for value in width],
                        "shape_ratio_squared": str(ratio_squared),
                    }
                shape_records.append(
                    {
                        "mesh": mesh,
                        "coefficient": coefficient,
                        "center": center,
                        "width": width,
                        "ratio_squared": ratio_squared,
                    }
                )

# Exact physical scale ledger.  R_n=2^-n and h_n=2^-2n make the cross-section
# thin.  Every enumerated cancellation pattern inherits the same factor h/R.
previous_worst_scaled: Fraction | None = None
last_scaled_bound = Fraction(0)
for n in range(2, 31):
    major_radius = Fraction(1, 2**n)
    cross_scale = Fraction(1, 2 ** (2 * n))
    aspect_factor = cross_scale / major_radius
    require(aspect_factor == Fraction(1, 2**n), f"dyadic aspect n={n}")

    worst_scaled = Fraction(0)
    for record in shape_records:
        ratio_squared = record["ratio_squared"]
        require(isinstance(ratio_squared, Fraction), "fractional shape ratio")

        # Exact square of (velocity weak-cube upper proxy)/(vorticity
        # weak-cube proxy).  Amplitude cancels, and cylindrical scaling leaves
        # shape_ratio_squared*(h/R)^2.
        scaled_ratio_squared = ratio_squared * aspect_factor**2
        require(
            scaled_ratio_squared
            == ratio_squared * Fraction(1, 2 ** (2 * n)),
            f"two-layer scale identity n={n}",
        )
        worst_scaled = max(worst_scaled, scaled_ratio_squared)

    require(worst_scaled > 0, f"positive scaled ledger n={n}")
    if previous_worst_scaled is not None:
        require(
            worst_scaled * 4 == previous_worst_scaled,
            f"quartering squared endpoint ratio n={n}",
        )
    previous_worst_scaled = worst_scaled
    last_scaled_bound = worst_scaled


result = {
    "experiment": "TWO-LAYER-PURE-SWIRL-SUPPORT-GATE-1",
    "question": (
        "Can two shifted nonseparable compact swirl layers use pointwise "
        "cancellation to defeat thin-support weak-Lorentz velocity collapse?"
    ),
    "object": "continuous P1 meridional streamfunction on exact rational triangulations",
    "pde_discretization": "none; static curl kinematics only",
    "mesh_resolutions": list(meshes),
    "shape_count": len(shape_records),
    "random_seed": None,
    "arithmetic": (
        "fractions.Fraction exact; squared gradient magnitudes avoid square roots"
    ),
    "checks": CHECKS,
    "assertion_failure_count": len(FAILURES),
    "failures": FAILURES,
    "certified_finite_element_quantities": {
        "support_area": "exact union area of active P1 triangles",
        "velocity_cube_upper": "||F||_infinity^3 times support area, before ring factor",
        "gradient_weak_cube_squared": (
            "exact square of sup_lambda lambda^3 |{|grad F|>lambda}|^2"
        ),
        "scale_law": (
            "[(K_U^3 upper)/(K_W^3 proxy)]^2 = shape_ratio_squared (h/R)^2"
        ),
        "enumerated_shape_bound": "shape_ratio_squared <= 9 for all 384 declared masks",
        "dyadic_family": "R_n=2^-n, h_n=2^-2n, 2<=n<=30",
    },
    "maximum_shape_ratio_squared": str(maximum_shape_ratio_squared),
    "maximum_shape_ratio_squared_decimal": float(maximum_shape_ratio_squared),
    "worst_shape": worst_shape,
    "last_scaled_ratio_squared": str(last_scaled_bound),
    "analytic_lemmas_not_certified_by_the_mesh": [
        "the two-dimensional pointwise potential bound |F|<=C I_1(|grad F|)",
        "the Lorentz HLS map I_1:L^(3/2,infinity)->L^(6,infinity)",
        "the finite-support embedding L^(6,infinity)->L^(3,infinity)",
        "the cylindrical comparison between dr dz and r dr dtheta dz",
        "smooth approximation of the P1 fields with uniform constants",
    ],
    "adversarial_limits": [
        "the enumeration is finite and cannot prove a continuum universal constant",
        "the velocity weak norm is upper-bounded by support and L-infinity rather than computed exactly",
        "only pure azimuthal velocity is represented",
        "cross-sections of area comparable to R^2 are not forced into endpoint collapse",
        "no direction BMO, pressure, viscosity, stretching, or time evolution is computed",
    ],
}

print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
