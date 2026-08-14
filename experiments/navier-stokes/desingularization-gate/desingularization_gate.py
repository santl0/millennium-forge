"""Certificat exact du seuil radial pour une donnée homogène de degré -1.

On n'intègre pas une solution PDE. Pour un champ u_0(r,theta)=r^-1 A(theta),
avec A fixe et indépendant de epsilon, conservé sur la coquille
epsilon <= r <= 1, le script calcule exactement le facteur radial de
||u_0||_Lq^q et celui de ||grad u_0||_L2^2. Les constantes angulaires restent
symboliques. Le calcul de coquille est seulement une borne inférieure pour une
troncature globale dont les couches de raccord ne sont pas estimées.
"""

from __future__ import annotations

import json
from fractions import Fraction


def radial_lq_power(q: int, epsilon: Fraction) -> tuple[str, Fraction]:
    """Retourne l'étiquette et l'intégrale de r^(2-q) sur [epsilon,1]."""
    if q <= 0 or not 0 < epsilon < 1:
        raise ValueError("q>0 et 0<epsilon<1 sont requis")
    if q == 3:
        raise ValueError("q=3 est logarithmique et traité symboliquement")
    exponent = 3 - q
    value = (Fraction(1) - epsilon**exponent) / exponent
    return f"(1-epsilon^{exponent})/{exponent}", value


def encode(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    rows = []
    for decade in (1, 2, 4, 8, 16):
        epsilon = Fraction(1, 10**decade)
        _, l2 = radial_lq_power(2, epsilon)
        _, l4 = radial_lq_power(4, epsilon)
        _, l5 = radial_lq_power(5, epsilon)
        grad_l2_squared = epsilon**-1 - 1
        rows.append(
            {
                "decade": decade,
                "epsilon": encode(epsilon),
                "L2_squared_radial_factor": encode(l2),
                "L3_cubed_radial_factor": f"{decade}*log(10)",
                "L4_fourth_radial_factor": encode(l4),
                "L5_fifth_radial_factor": encode(l5),
                "grad_L2_squared_radial_factor": encode(grad_l2_squared),
                "shell_amplitude_scale": f"10^{decade}",
            }
        )

    # Résidus exacts pour les identités de puissance testées.
    for row in rows:
        decade = row["decade"]
        epsilon = Fraction(1, 10**decade)
        _, l2 = radial_lq_power(2, epsilon)
        _, l4 = radial_lq_power(4, epsilon)
        _, l5 = radial_lq_power(5, epsilon)
        assert l2 == 1 - epsilon
        assert l4 == epsilon**-1 - 1
        assert l5 == (epsilon**-2 - 1) / 2
        assert Fraction(row["grad_L2_squared_radial_factor"]) == epsilon**-1 - 1

    report = {
        "test": "DESINGULARIZATION-GATE-1",
        "equation": (
            "aucune évolution PDE; donnée initiale 3D homogène de degré -1 "
            "sur une coquille"
        ),
        "question": (
            "la contribution de coquille d'un profil r^-1 conserve-t-elle "
            "des bornes uniformes dans les normes critiques/de régularité ?"
        ),
        "arithmetic": "fractions rationnelles exactes et log(10) symbolique",
        "discretization": "aucune",
        "rounding_error_bound": "0",
        "angular_constants": (
            "A fixe; C_q=integrale_S2 |A|^q dans (0,infinity); pour le "
            "gradient A dans H1(S2) et C_grad=integrale_S2(|A|^2+|grad_S A|^2)>0"
        ),
        "identities": {
            "Lq_q_shell": "C_q * integral_epsilon^1 r^(2-q) dr",
            "q_less_than_3": "C_q*(1-epsilon^(3-q))/(3-q), borne",
            "q_equal_3": "C_3*log(1/epsilon), divergence logarithmique",
            "q_greater_than_3": "C_q*(epsilon^(3-q)-1)/(q-3), divergence",
            "gradient_L2_squared": "C_grad*(epsilon^-1-1), divergence",
            "norm_growth": (
                "||u||_3~log(1/epsilon)^(1/3); ||u||_q~epsilon^(3/q-1) "
                "pour q>3; ||grad u||_2~epsilon^-1/2"
            ),
        },
        "residuals": {
            "rational_identity_max": "0/1",
            "rounding": "0/1",
        },
        "rows": rows,
        "scope_warning": (
            "aucune divergence-free, couche de raccord, évolution PDE, durée "
            "locale ou stabilité dynamique n'est testée"
        ),
        "pass": True,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
