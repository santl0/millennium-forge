"""Certificat exact : cohérence locale de vorticité et étirement signé.

Le champ périodique, sur le tore de volume normalisé, est

    u_a(x,y,z) = (sin(y) + a sin(x) cos(z), 0, -a cos(x) sin(z)).

Tous les calculs spectraux et les bornes de cohérence utilisent ``Fraction``.
Les inégalités trigonométriques employées sont seulement
``|sin(s)| <= |s|`` et ``cos(s) >= 1-s^2/2``. Aucune FFT, grille ou
arithmétique flottante ne participe au certificat.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from typing import Dict, Iterable, Tuple

Wave = Tuple[int, int, int]
QComplex = Tuple[F, F]
Vector = Tuple[QComplex, QComplex, QComplex]
Matrix = Tuple[Tuple[QComplex, QComplex, QComplex], ...]

ZERO: QComplex = (F(0), F(0))
ZVECTOR: Vector = (ZERO, ZERO, ZERO)


def z(re: int | F = 0, im: int | F = 0) -> QComplex:
    return F(re), F(im)


def add(lhs: QComplex, rhs: QComplex) -> QComplex:
    return lhs[0] + rhs[0], lhs[1] + rhs[1]


def mul(lhs: QComplex, rhs: QComplex) -> QComplex:
    return (
        lhs[0] * rhs[0] - lhs[1] * rhs[1],
        lhs[0] * rhs[1] + lhs[1] * rhs[0],
    )


def scale(value: QComplex, factor: int | F) -> QComplex:
    return value[0] * F(factor), value[1] * F(factor)


def conj(value: QComplex) -> QComplex:
    return value[0], -value[1]


def times_i(value: QComplex) -> QComplex:
    return -value[1], value[0]


def vconj(value: Vector) -> Vector:
    return tuple(conj(component) for component in value)  # type: ignore[return-value]


def vscale(value: Vector, factor: int | F) -> Vector:
    return tuple(scale(component, factor) for component in value)  # type: ignore[return-value]


def vadd(lhs: Vector, rhs: Vector) -> Vector:
    return tuple(add(x, y) for x, y in zip(lhs, rhs))  # type: ignore[return-value]


def real_dot_complex(k: Wave, value: Vector) -> QComplex:
    result = ZERO
    for coefficient, component in zip(k, value):
        result = add(result, scale(component, coefficient))
    return result


def real_cross_complex(k: Wave, value: Vector) -> Vector:
    return (
        add(scale(value[2], k[1]), scale(value[1], -k[2])),
        add(scale(value[0], k[2]), scale(value[2], -k[0])),
        add(scale(value[1], k[0]), scale(value[0], -k[1])),
    )


def curl_mode(k: Wave, value: Vector) -> Vector:
    return tuple(
        times_i(component) for component in real_cross_complex(k, value)
    )  # type: ignore[return-value]


def complex_dot(lhs: Vector, rhs: Vector) -> QComplex:
    result = ZERO
    for x, y in zip(lhs, rhs):
        result = add(result, mul(x, y))
    return result


def hermitian_real_dot(lhs: Vector, rhs: Vector) -> F:
    return complex_dot(vconj(lhs), rhs)[0]


def norm2(value: Vector) -> F:
    return hermitian_real_dot(value, value)


def negwave(k: Wave) -> Wave:
    return -k[0], -k[1], -k[2]


def base_modes(a: F) -> Dict[Wave, Vector]:
    """Coefficients exacts de u_a pour exp(i k.x)."""

    modes: Dict[Wave, Vector] = {
        (0, 1, 0): (z(0, F(-1, 2)), ZERO, ZERO),
        (1, 0, 1): (z(0, -a / 4), ZERO, z(0, a / 4)),
        (1, 0, -1): (z(0, -a / 4), ZERO, z(0, -a / 4)),
    }
    for k, value in list(modes.items()):
        modes[negwave(k)] = vconj(value)
    return modes


def scaled_modes(a: F, n: int) -> Dict[Wave, Vector]:
    """Modes de u_{a,n}(x)=n u_a(nx), pour n entier positif."""

    if n <= 0:
        raise ValueError("n doit être positif")
    return {
        (n * k[0], n * k[1], n * k[2]): vscale(value, n)
        for k, value in base_modes(a).items()
    }


def lifted_modes(a: F, n: int) -> Dict[Wave, Vector]:
    """Modes du lift fréquentiel v_{a,n}(x)=u_a(nx)."""

    if n <= 0:
        raise ValueError("n doit être positif")
    return {
        (n * k[0], n * k[1], n * k[2]): value
        for k, value in base_modes(a).items()
    }


def curl_modes(modes: Dict[Wave, Vector]) -> Dict[Wave, Vector]:
    return {k: curl_mode(k, value) for k, value in modes.items()}


def sum_vectors(values: Iterable[Vector]) -> Vector:
    result = ZVECTOR
    for value in values:
        result = vadd(result, value)
    return result


def gradient_at_origin(modes: Dict[Wave, Vector]) -> Matrix:
    rows = []
    for component in range(3):
        row = []
        for derivative in range(3):
            entry = ZERO
            for k, value in modes.items():
                entry = add(
                    entry,
                    times_i(scale(value[component], k[derivative])),
                )
            row.append(entry)
        rows.append(tuple(row))
    return tuple(rows)


def symmetric_part(matrix: Matrix) -> Matrix:
    rows = []
    for i in range(3):
        rows.append(
            tuple(scale(add(matrix[i][j], matrix[j][i]), F(1, 2)) for j in range(3))
        )
    return tuple(rows)


def real_quadratic(vector: Vector, matrix: Matrix) -> F:
    product: Vector = tuple(
        sum_complex(mul(matrix[i][j], vector[j]) for j in range(3))
        for i in range(3)
    )  # type: ignore[assignment]
    return hermitian_real_dot(vector, product)


def sum_complex(values: Iterable[QComplex]) -> QComplex:
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


def pressure_contraction_modes(modes: Dict[Wave, Vector]) -> Dict[Wave, QComplex]:
    """Modes de q=partial_i u_j partial_j u_i, sans flottants."""

    result: Dict[Wave, QComplex] = {}
    for k, left in modes.items():
        for ell, right in modes.items():
            wave = tuple(k[index] + ell[index] for index in range(3))
            coefficient = ZERO
            for i in range(3):
                for j in range(3):
                    left_derivative = times_i(scale(left[j], k[i]))
                    right_derivative = times_i(scale(right[i], ell[j]))
                    coefficient = add(
                        coefficient, mul(left_derivative, right_derivative)
                    )
            result[wave] = add(result.get(wave, ZERO), coefficient)
    return {wave: value for wave, value in result.items() if value != ZERO}


def encode(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def encode_vector(value: Vector) -> list[list[str]]:
    return [[encode(component[0]), encode(component[1])] for component in value]


def encode_matrix(value: Matrix) -> list[list[list[str]]]:
    return [
        [[encode(component[0]), encode(component[1])] for component in row]
        for row in value
    ]


def analyze_field(a: F, n: int = 1) -> dict:
    modes = scaled_modes(a, n)
    curls = curl_modes(modes)

    divergence = {k: real_dot_complex(k, value) for k, value in modes.items()}
    reality = {
        k: tuple(
            add(x, scale(y, -1))
            for x, y in zip(modes[negwave(k)], vconj(value))
        )
        for k, value in modes.items()
    }
    gradient = gradient_at_origin(modes)
    strain = symmetric_part(gradient)
    omega0 = sum_vectors(curls.values())
    omega_gradient0 = gradient_at_origin(curls)

    energy = F(1, 2) * sum(norm2(value) for value in modes.values())
    enstrophy = F(1, 2) * sum(norm2(value) for value in curls.values())
    palinstrophy = sum(
        sum(component * component for component in k) * norm2(value)
        for k, value in curls.items()
    )
    helicity = sum(
        hermitian_real_dot(modes[k], curls[k]) for k in modes
    )
    omega_norm2 = norm2(omega0)
    production = real_quadratic(omega0, strain)
    stretching_eigenvalue = production / omega_norm2

    expected_gradient: Matrix = (
        (z(a * n * n), z(n * n), ZERO),
        (ZERO, ZERO, ZERO),
        (ZERO, ZERO, z(-a * n * n)),
    )
    expected_omega: Vector = (ZERO, ZERO, z(-n * n))
    expected_pressure_modes = {
        (2 * n, 0, 0): z(a * a * n**4 / 2),
        (-2 * n, 0, 0): z(a * a * n**4 / 2),
        (0, 0, 2 * n): z(a * a * n**4 / 2),
        (0, 0, -2 * n): z(a * a * n**4 / 2),
    }
    pressure_contraction = pressure_contraction_modes(modes)

    assert all(value == ZERO for value in divergence.values())
    assert all(
        all(component == ZERO for component in residual)
        for residual in reality.values()
    )
    assert gradient == expected_gradient
    assert omega0 == expected_omega
    assert omega_gradient0 == (
        (ZERO, ZERO, ZERO),
        (ZERO, ZERO, ZERO),
        (ZERO, ZERO, ZERO),
    )
    assert energy == n * n * (1 + a * a) / 4
    assert enstrophy == n**4 * (F(1, 4) + a * a / 2)
    assert palinstrophy == n**6 * (F(1, 2) + 2 * a * a)
    assert helicity == 0
    assert omega_norm2 == n**4
    assert stretching_eigenvalue == -a * n * n
    assert production == -a * n**6
    assert pressure_contraction == expected_pressure_modes

    return {
        "a": encode(a),
        "N": n,
        "energy": encode(energy),
        "enstrophy": encode(enstrophy),
        "palinstrophy": encode(palinstrophy),
        "helicity": encode(helicity),
        "gradient_at_origin": encode_matrix(gradient),
        "vorticity_at_origin": encode_vector(omega0),
        "stretching_eigenvalue_alpha_at_origin": encode(stretching_eigenvalue),
        "enstrophy_production_density_at_origin": encode(production),
        "max_divergence_residual": "0/1",
        "max_reality_residual": "0/1",
        "vorticity_first_jet_residual": "0/1",
        "pressure_Poisson_Fourier_residual": "0/1",
    }


def coherence_certificate(amplitude: F, radii: Iterable[F]) -> list[dict]:
    """Bornes sur Q_r={|x|,|y|,|z|<=r}, 0<r<=1/2.

    La vorticité est (0,-2a sin(x)sin(z),-cos(y)). En posant
    theta=2a sin(x)sin(z)/cos(y), l'angle avec la direction au centre est
    contrôlé par |theta| et l'angle entre deux points par |theta(p)-theta(q)|.
    """

    rows = []
    for r in radii:
        if not (0 < r <= F(1, 2)):
            raise ValueError("le certificat exige 0<r<=1/2")
        cosine_lower = 1 - r * r / 2
        center_oscillation = 2 * amplitude * r * r / cosine_lower
        pairwise_l1_lipschitz = 2 * amplitude * r / cosine_lower
        transverse_y_bound = 2 * amplitude * r**3 / cosine_lower**2
        stretching_density_lower = cosine_lower**4

        assert cosine_lower > 0
        assert r * r <= cosine_lower
        assert transverse_y_bound <= pairwise_l1_lipschitz
        assert center_oscillation == r * pairwise_l1_lipschitz

        rows.append(
            {
                "radius_r": encode(r),
                "cos_y_lower_bound": encode(cosine_lower),
                "center_sine_angle_upper_bound": encode(center_oscillation),
                "pairwise_sine_angle_L1_lipschitz_constant": encode(
                    pairwise_l1_lipschitz
                ),
                "y_derivative_auxiliary_bound": encode(transverse_y_bound),
                "abs_alpha_over_center_bound": encode(
                    amplitude / center_oscillation
                ),
                "abs_stretching_density_lower_bound": encode(
                    stretching_density_lower
                ),
                "stretching_sign_on_Q_r": "-sign(a)",
            }
        )
    for previous, current in zip(rows, rows[1:]):
        assert F(current["center_sine_angle_upper_bound"]) < F(
            previous["center_sine_angle_upper_bound"]
        )
        assert F(current["pairwise_sine_angle_L1_lipschitz_constant"]) < F(
            previous["pairwise_sine_angle_L1_lipschitz_constant"]
        )
    return rows


def main() -> None:
    amplitude = F(1)
    plus = analyze_field(amplitude)
    minus = analyze_field(-amplitude)

    assert plus["energy"] == minus["energy"] == "1/2"
    assert plus["enstrophy"] == minus["enstrophy"] == "3/4"
    assert plus["palinstrophy"] == minus["palinstrophy"] == "5/2"
    assert plus["helicity"] == minus["helicity"] == "0/1"
    assert plus["stretching_eigenvalue_alpha_at_origin"] == "-1/1"
    assert minus["stretching_eigenvalue_alpha_at_origin"] == "1/1"
    assert plus["vorticity_at_origin"] == minus["vorticity_at_origin"]

    scaling_rows = []
    lift_rows = []
    base_plus = analyze_field(amplitude)
    for n in (1, 2, 4, 8, 16, 32):
        row = analyze_field(amplitude, n)
        assert F(row["energy"]) == n * n * F(base_plus["energy"])
        assert F(row["enstrophy"]) == n**4 * F(base_plus["enstrophy"])
        assert F(row["palinstrophy"]) == n**6 * F(base_plus["palinstrophy"])
        assert F(row["stretching_eigenvalue_alpha_at_origin"]) == n * n * F(
            base_plus["stretching_eigenvalue_alpha_at_origin"]
        )
        assert F(row["enstrophy_production_density_at_origin"]) == n**6 * F(
            base_plus["enstrophy_production_density_at_origin"]
        )
        scaling_rows.append(
            {
                key: row[key]
                for key in (
                    "N",
                    "energy",
                    "enstrophy",
                    "palinstrophy",
                    "helicity",
                    "stretching_eigenvalue_alpha_at_origin",
                    "enstrophy_production_density_at_origin",
                )
            }
        )
        lift_modes = lifted_modes(amplitude, n)
        lift_curls = curl_modes(lift_modes)
        lift_energy = F(1, 2) * sum(norm2(value) for value in lift_modes.values())
        lift_enstrophy = F(1, 2) * sum(
            norm2(value) for value in lift_curls.values()
        )
        lift_gradient = gradient_at_origin(lift_modes)
        lift_strain = symmetric_part(lift_gradient)
        lift_omega0 = sum_vectors(lift_curls.values())
        lift_production = real_quadratic(lift_omega0, lift_strain)
        assert lift_energy == F(base_plus["energy"])
        assert lift_enstrophy == n * n * F(base_plus["enstrophy"])
        assert lift_production == -n**3
        lift_rows.append(
            {
                "N": n,
                "energy": encode(lift_energy),
                "enstrophy": encode(lift_enstrophy),
                "enstrophy_production_density_at_origin": encode(lift_production),
            }
        )

    coherence = coherence_certificate(
        amplitude, (F(1, 2**power) for power in range(2, 11))
    )

    report = {
        "test": "VORTICITY-LOCAL-COHERENCE-SIGN-GATE-1",
        "question": (
            "La coherence de direction de vorticite sur un voisinage local, "
            "meme jointe a l'energie, l'enstrophie et l'helicite globale, "
            "determine-t-elle le signe ou impose-t-elle une petite borne "
            "sans echelle sur alpha=xi.S.xi au centre?"
        ),
        "equation_scope": (
            "donnee initiale C-infinity periodique divergence-free pour "
            "Navier-Stokes incompressible 3D sur T3, viscosite positive, force nulle"
        ),
        "field": (
            "u_a=(sin(y)+a sin(x)cos(z),0,-a cos(x)sin(z)); "
            "omega_a=(0,-2a sin(x)sin(z),-cos(y))"
        ),
        "arithmetic": "fractions rationnelles gaussiennes exactes",
        "discretization": "six modes Fourier explicites; aucune grille",
        "precision": "exacte; aucun flottant",
        "paired_sign_fields": [plus, minus],
        "coherence_bounds_on_Q_r": coherence,
        "integer_scaling_u_N_equals_N_u_of_Nx": scaling_rows,
        "integer_frequency_lift_v_N_equals_u_of_Nx": lift_rows,
        "residuals": {
            "divergence": "0/1",
            "Fourier_reality": "0/1",
            "energy_pair_difference": "0/1",
            "enstrophy_pair_difference": "0/1",
            "palinstrophy_pair_difference": "0/1",
            "helicity_both_signs": "0/1",
            "vorticity_at_origin_pair_difference": "0/1",
            "vorticity_first_jet": "0/1",
            "pressure_Poisson_Fourier": "0/1",
            "roundoff_error": "0 (aucun flottant)",
            "coherence_bound_failure_count": 0,
            "scaling_failure_count": 0,
        },
        "decision": (
            "Le signe de l'etirement ponctuel et une depletion sans facteur "
            "d'echelle ne se deduisent pas de la seule coherence locale de xi "
            "ni des quantites quadratiques globales testees. Le strain contient une "
            "contribution non locale que le voisinage ne determine pas."
        ),
        "limits": [
            "le champ est une tranche initiale admissible, pas une trajectoire de blow-up",
            "le test ne satisfait ni n'invalide une hypothese uniforme sur toute la region de haute vorticite",
            "il ne refute pas les estimations integrees de Constantin-Fefferman ou leurs commutateurs",
            "le cube Q_r est choisi localement; aucun rayon uniforme en temps n'est produit",
            "la pression n'est pas requise pour l'identite instantanee de vorticite, mais reste non locale dans l'evolution",
            "la pression initiale de moyenne nulle est reconstruite exactement; aucun controle uniforme de sa queue apres localisation sur R3 n'est obtenu",
        ],
        "seed": "sans objet",
        "pass": True,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
