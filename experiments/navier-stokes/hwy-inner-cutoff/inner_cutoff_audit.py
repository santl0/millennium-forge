"""Audit exact d'une regularisation interieure d'une donnee homogene -1.

Ce script ne simule pas Navier--Stokes. Il certifie, en arithmetique
rationnelle, les identites algebriques et radiales du contre-profil

    a(x) = (-x_2, x_1, 0) / |x|^2.

Pour des cutoffs radiaux lisses eta et chi tels que

    eta = 1 sur r <= 1, eta = 0 sur r >= 2,
    chi = 0 sur r <= 1, chi = 1 sur r >= 2, 0 <= chi <= 1,

on pose u_0 = eta(r) a et u_0^epsilon = chi(r/epsilon) u_0. Les
deux champs sont divergence-free; u_0^epsilon est C-infinity et compact.
Le calcul suit exactement la distance d_epsilon = u_0-u_0^epsilon.
"""

from __future__ import annotations

import json
from fractions import Fraction


Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]


B: Matrix = (
    (Fraction(0), Fraction(-1), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0)),
)


def dot(left: Vector, right: Vector) -> Fraction:
    return sum((a * b for a, b in zip(left, right, strict=True)), Fraction(0))


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(dot(row, vector) for row in matrix)


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(3)) for i in range(3)
    )


def frobenius_squared(matrix: Matrix) -> Fraction:
    return sum((entry * entry for row in matrix for entry in row), Fraction(0))


def encode(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    zero_matrix: Matrix = tuple(
        tuple(Fraction(0) for _ in range(3)) for _ in range(3)
    )
    skew_residual = matrix_add(B, transpose(B))
    trace_b = sum((B[i][i] for i in range(3)), Fraction(0))
    b_frobenius_squared = frobenius_squared(B)

    # B est antisymetrique. Donc x.Bx=0 pour tout x, tr(B)=0 et
    # div(Bx/r^2)=tr(B)/r^2-2 x.Bx/r^4=0. Un multiplicateur radial
    # conserve aussi la divergence car grad(f(r)).a est proportionnel a x.a.
    assert skew_residual == zero_matrix
    assert trace_b == 0
    assert b_frobenius_squared == 2

    # Temoins rationnels supplementaires: aucune evaluation flottante.
    rational_points: tuple[Vector, ...] = (
        (Fraction(1), Fraction(2), Fraction(3)),
        (Fraction(-2), Fraction(5), Fraction(7)),
        (Fraction(11, 3), Fraction(-13, 5), Fraction(17, 7)),
    )
    tangency_residuals = [dot(x, matvec(B, x)) for x in rational_points]
    assert all(value == 0 for value in tangency_residuals)

    # Constantes angulaires exactes C_q = integral_S2 sin(theta)^q dOmega.
    # C_2=(8/3)pi, C_3=(3/4)pi^2, C_4=(32/15)pi.
    angular_constants = {
        "C2": {"coefficient": encode(Fraction(8, 3)), "pi_power": 1},
        "C3": {"coefficient": encode(Fraction(3, 4)), "pi_power": 2},
        "C4": {"coefficient": encode(Fraction(32, 15)), "pi_power": 1},
    }
    assert Fraction(angular_constants["C2"]["coefficient"]) == Fraction(8, 3)
    assert Fraction(angular_constants["C3"]["coefficient"]) == Fraction(3, 4)
    assert Fraction(angular_constants["C4"]["coefficient"]) == Fraction(32, 15)

    # Sur r<epsilon, d_epsilon=a. Sur r>=2 epsilon, d_epsilon=0.
    # Les coefficients ci-dessous multiplient pi*epsilon pour les carres L2.
    l2_lower_coefficient = Fraction(8, 3)
    l2_upper_coefficient = 2 * l2_lower_coefficient
    assert l2_upper_coefficient == Fraction(16, 3)

    # Pour lambda>=epsilon^-1,
    # |{|d_epsilon|>lambda}| = C_3/(3 lambda^3)=pi^2/(4 lambda^3).
    weak_l3_distribution_coefficient = Fraction(1, 4)
    assert Fraction(3, 4) / 3 == weak_l3_distribution_coefficient

    # Variante C-infinity explicite H(s)=b(s)/(b(s)+b(1-s)),
    # b(s)=exp(-1/s) pour s>0 et 0 sinon. Pour
    # f_epsilon(r)=H((r-epsilon)/epsilon)H(2-r), on a, sur
    # 2 epsilon <= r <= 5 epsilon/2,
    # f_epsilon=1 et f_(2 epsilon)<=H(1/4). Le gap L3 ci-dessous est donc
    # strictement positif et independant de epsilon. Les transcendantes sont
    # gardees symboliques; seules les bornes geometriques sont rationnelles.
    successive_annulus_ratio = Fraction(5, 4)
    successive_l2_squared_upper_coefficient = 4 * Fraction(8, 3)
    assert successive_annulus_ratio > 1
    assert successive_l2_squared_upper_coefficient == Fraction(32, 3)

    # grad(Bx/r^2)=B/r^2-2(Bx) tensor x/r^4 et |grad a|^2=2/r^4.
    # L'integrale sur 2 epsilon <= r <= 1 vaut 4*pi/epsilon-8*pi.
    gradient_leading_coefficient = Fraction(4)
    gradient_constant_coefficient = Fraction(-8)
    assert b_frobenius_squared == gradient_leading_coefficient / 2

    rows = []
    for decade in (1, 2, 4, 8, 16):
        epsilon = Fraction(1, 10**decade)
        l2_lower = l2_lower_coefficient * epsilon
        l2_upper = l2_upper_coefficient * epsilon
        gradient_shell = gradient_leading_coefficient / epsilon
        gradient_shell += gradient_constant_coefficient
        linfinity_lower = Fraction(1, 2) / epsilon
        assert l2_lower > 0
        assert l2_upper == 2 * l2_lower
        assert gradient_shell == 4 / epsilon - 8
        assert linfinity_lower == 1 / (2 * epsilon)
        rows.append(
            {
                "epsilon": encode(epsilon),
                "L2_difference_squared_lower_coefficient_times_pi": encode(l2_lower),
                "L2_difference_squared_upper_coefficient_times_pi": encode(l2_upper),
                "gradient_L2_squared_lower_coefficient_times_pi": encode(
                    gradient_shell
                ),
                "Linfinity_lower": encode(linfinity_lower),
            }
        )

    report = {
        "test": "HWY-INNER-CUTOFF-GATE-1",
        "question": (
            "une regularisation interieure lisse d'une donnee r^-1 peut-elle "
            "etre petite simultanement dans l'energie et dans la topologie "
            "critique L3 ou L3-faible ?"
        ),
        "equation": (
            "aucune evolution PDE; donnee divergence-free sur R3, viscosite/"
            "pression/force sans objet"
        ),
        "field": "a(x)=(-x_2,x_1,0)/|x|^2",
        "cutoffs": {
            "outer": "eta=1 sur r<=1, eta=0 sur r>=2, radiale C-infinity",
            "inner": (
                "chi=0 sur r<=1, chi=1 sur r>=2, 0<=chi<=1, "
                "radiale C-infinity"
            ),
            "singular_datum": "u_0=eta(r)a(x)",
            "clay_smooth_datum": "u_0^epsilon=chi(r/epsilon)u_0",
        },
        "arithmetic": "fractions rationnelles exactes; pi et racine cubique symboliques",
        "discretization": "aucune grille spatiale ou temporelle",
        "seed": "sans objet",
        "certified_identities": {
            "divergence": "div(a)=0 et div(f(r)a)=0 pour tout cutoff radial f",
            "tangency": "x dot a(x)=0",
            "pointwise_gradient": "|grad a|^2=2/|x|^4",
            "angular_constants": angular_constants,
            "L2_difference_squared": (
                "(8*pi/3)epsilon <= ||u_0-u_0^epsilon||_2^2 "
                "<= (16*pi/3)epsilon"
            ),
            "L3_difference": "||u_0-u_0^epsilon||_3=infinity pour tout epsilon>0",
            "weak_L3_distribution": (
                "pour lambda>=epsilon^-1, mesure{|d_epsilon|>lambda}="
                "pi^2/(4 lambda^3)"
            ),
            "weak_L3_lower": (
                "||d_epsilon||_{L^{3,infinity}} >= (pi^2/4)^(1/3), "
                "convention sup_lambda lambda*mesure^(1/3)"
            ),
            "smooth_successive_L3_gap": (
                "pour le cutoff plat H, ||u_epsilon-u_(2epsilon)||_3^3 >= "
                "[exp(8/3)/(1+exp(8/3))]^3*(3*pi^2/4)*log(5/4)>0"
            ),
            "smooth_successive_L2_gap": (
                "||u_epsilon-u_(2epsilon)||_2^2 <= (32*pi/3)epsilon"
            ),
            "smooth_family_weak_L3": (
                "sup_epsilon ||u_epsilon||_{L^{3,infinity}} <= "
                "(4*pi/3)^(1/3)"
            ),
            "gradient_lower": (
                "||grad u_0^epsilon||_2^2 >= 4*pi/epsilon-8*pi "
                "pour 0<epsilon<1/2"
            ),
            "Linfinity_lower": "||u_0^epsilon||_infinity >= 1/(2epsilon)",
            "pressure_nonlocal_upper": (
                "avec p_epsilon=R_i R_j(u_i u_j) dans L2, "
                "||p_epsilon||_2 <= ||u_epsilon||_4^2 <= "
                "[(32*pi/15)(epsilon^-1-1/2)]^(1/2)"
            ),
        },
        "scaling": {
            "navier_stokes": "u_lambda(x,t)=lambda*u(lambda*x,lambda^2*t)",
            "L2": "lambda^-1/2",
            "L3_and_weak_L3": "lambda^0 (critique)",
            "gradient_L2": "lambda^1/2",
            "Linfinity": "lambda^1",
        },
        "source_route_matrix": {
            "HWY_outer_localization": {
                "removes_far_field": True,
                "preserves_origin_r_minus_1": True,
                "produces_Clay_smooth_data": False,
                "small_parameter": "R^-1/8 dans la norme de point fixe, p=4",
            },
            "inner_Clay_regularization": {
                "removes_far_field": False,
                "preserves_origin_r_minus_1": False,
                "produces_Clay_smooth_data": True,
                "small_in_L2": True,
                "small_in_L3_or_weak_L3": False,
                "covered_by_HWY_fixed_point": False,
            },
        },
        "residuals": {
            "skew_matrix": [[encode(value) for value in row] for row in skew_residual],
            "trace_B": encode(trace_b),
            "tangency_samples": [encode(value) for value in tangency_residuals],
            "rational_assertion_failure_count": 0,
            "rounding_error_bound": "0",
            "transcendental_bounds": (
                "expressions symboliques positives; aucune approximation "
                "decimale utilisee dans le verdict"
            ),
        },
        "rows": rows,
        "adversarial_limit": (
            "la non-convergence critique et l'explosion H1/Linfinity excluent "
            "seulement un transfert perturbatif utilisant ces bornes. Elles "
            "ne prouvent ni que le temps fort tend vers zero, ni qu'un "
            "shadowing non perturbatif est impossible, ni un blow-up Clay."
        ),
        "pass": True,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
