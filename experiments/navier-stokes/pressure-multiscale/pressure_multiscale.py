"""Contre-profil exact pour la tension de pression après zoom NS.

Le modèle ponctuel représente le moment de Reynolds d'un paquet lisse compact
divergence-free. Pour n>=1, on choisit la distance physique L=2^(-6n), le zoom
r=2^(-7n) et l'échelle de moment mu=2^(-3n). Après zoom, le centre est à
R=L/r=2^n et le moment vaut mu/r=R^4. La pression centrée ne tend donc pas vers
zéro malgré une énergie physique 2*mu qui tend vers zéro.

Le script certifie les identités d'échelle du moment ponctuel en rationnels.
Le raccord à un paquet C_c^infinity est une dérivation par développement
multipolaire uniforme, documentée dans le README de l'expérience.
"""

from __future__ import annotations

import json
from fractions import Fraction


def encode(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def analyze(n: int) -> dict[str, int | str]:
    if n < 1:
        raise ValueError("n>=1 est requis")

    rescaled_distance = 2**n
    physical_distance = Fraction(1, 2 ** (6 * n))
    zoom_scale = Fraction(1, 2 ** (7 * n))
    physical_moment = Fraction(1, 2 ** (3 * n))

    rescaled_moment = physical_moment / zoom_scale
    physical_l2_squared = 2 * physical_moment
    rescaled_l2_squared = 2 * rescaled_moment
    raw_pressure_four_pi = rescaled_moment / rescaled_distance**3
    centered_pressure_four_pi = rescaled_moment * (
        Fraction(1, (rescaled_distance - 1) ** 3)
        - Fraction(1, rescaled_distance**3)
    )
    weighted_point_energy = rescaled_l2_squared / rescaled_distance**4
    limit_error = centered_pressure_four_pi - 3

    residuals = {
        "distance_scaling": physical_distance / zoom_scale - rescaled_distance,
        "moment_scaling": rescaled_moment - rescaled_distance**4,
        "critical_balance": (
            physical_moment * zoom_scale**3 / physical_distance**4 - 1
        ),
        "weighted_tail": weighted_point_energy - 2,
        "centered_identity": (
            centered_pressure_four_pi * (rescaled_distance - 1) ** 3
            - rescaled_distance
            * (
                3 * rescaled_distance**2
                - 3 * rescaled_distance
                + 1
            )
        ),
        "limit_error_identity": (
            limit_error * (rescaled_distance - 1) ** 3
            - (
                6 * rescaled_distance**2
                - 8 * rescaled_distance
                + 3
            )
        ),
    }
    assert all(value == 0 for value in residuals.values())

    return {
        "n": n,
        "physical_distance_L": encode(physical_distance),
        "zoom_scale_r": encode(zoom_scale),
        "physical_moment_mu": encode(physical_moment),
        "physical_L2_squared": encode(physical_l2_squared),
        "physical_kinetic_energy": encode(physical_moment),
        "rescaled_distance_R": rescaled_distance,
        "rescaled_moment": encode(rescaled_moment),
        "rescaled_L2_squared": encode(rescaled_l2_squared),
        "rescaled_kinetic_energy": encode(rescaled_moment),
        "weighted_point_energy": encode(weighted_point_energy),
        "four_pi_raw_pressure": encode(raw_pressure_four_pi),
        "four_pi_centered_pressure": encode(centered_pressure_four_pi),
        "centered_limit": "3/1",
        "centered_limit_error": encode(limit_error),
        "residuals": {name: encode(value) for name, value in residuals.items()},
    }


def main() -> None:
    results = [analyze(n) for n in range(1, 13)]
    report = {
        "test": "PRESSURE-MULTISCALE-1",
        "equation": (
            "pression instantanee de Navier-Stokes incompressible sur R^3; "
            "famille de moments de paquets, aucune evolution PDE"
        ),
        "question": (
            "energie physique bornee et separation apres zoom imposent-elles "
            "la disparition uniforme de la pression distante centree ?"
        ),
        "scales": "L_n=2^(-6n), r_n=2^(-7n), mu_n=2^(-3n)",
        "arithmetic": "fractions rationnelles exactes apres normalisation 4*pi",
        "discretization": "aucune",
        "rounding_error_bound": "0",
        "certificate": (
            "R_n=L_n/r_n=2^n, mu_n/r_n=R_n^4, norme L2 physique "
            "au carre=2mu_n->0, "
            "queue ponderee ponctuelle=2 et 4*pi*(P_n(e1)-P_n(0))->3"
        ),
        "scope_warning": (
            "les identites ponctuelles sont exactes; l'existence du paquet "
            "lisse realisant le moment et la limite multipolaire sont analytiques"
        ),
        "results": results,
        "pass": True,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
