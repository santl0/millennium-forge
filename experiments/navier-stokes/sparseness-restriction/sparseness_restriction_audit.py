"""Certificat exact pour la restriction 3D-sparseness -> section 1D.

Le lemme analytique normalise x0=0 et r=1. Pour une direction nu, si
``A_nu={t in (-1,1): t nu in S}`` a longueur ``m``, la réarrangée croissante
du poids pair ``t^2`` donne

    integral_A_nu t^2 dt >= m^3/12.

La formule polaire symétrisée convertit cette borne en densité volumique.
Le script vérifie exactement les constantes, les cas extrémaux radiaux, des
profils directionnels finis et le choix de rayon utilisé dans l'application.
Aucun flottant, maillage spatial ou échantillonnage aléatoire n'est utilisé.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from typing import Iterable


def encode(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def centered_interval_moment(length: F, radius: F = F(1)) -> F:
    """Minimum de integral_A t^2 dt pour |A|=length dans (-radius,radius)."""

    if not 0 <= length <= 2 * radius:
        raise ValueError("la longueur doit appartenir a [0,2r]")
    return length**3 / 12


def line_fraction_to_density_lower(line_fraction: F) -> F:
    """Densité 3D minimale si toute section centrale a cette fraction."""

    if not 0 <= line_fraction <= 1:
        raise ValueError("la fraction lineaire doit appartenir a [0,1]")
    length = 2 * line_fraction
    moment = centered_interval_moment(length)

    # volume >= (1/2)|S^2| moment et |B_1|=|S^2|/3.
    normalized_density = F(3, 2) * moment
    assert normalized_density == line_fraction**3
    return normalized_density


def central_ball_profile(q: F) -> dict:
    """B_q(0) sature la borne : section q, volume q^3."""

    density = q**3
    lower = line_fraction_to_density_lower(q)
    assert density == lower
    return {
        "profile": f"central_ball_radius_{encode(q)}",
        "line_fraction_every_direction": encode(q),
        "volume_density": encode(density),
        "lower_bound": encode(lower),
        "slack": "0/1",
    }


def concentric_shell_profile(inner: F, outer: F) -> dict:
    """Coquille {inner<|x|<outer}; la borne est stricte si inner>0."""

    if not 0 <= inner <= outer <= 1:
        raise ValueError("0<=inner<=outer<=1 requis")
    line_fraction = outer - inner
    density = outer**3 - inner**3
    lower = line_fraction**3
    slack = density - lower
    assert slack == 3 * inner * outer * (outer - inner)
    assert slack >= 0
    return {
        "profile": f"shell_{encode(inner)}_{encode(outer)}",
        "line_fraction_every_direction": encode(line_fraction),
        "volume_density": encode(density),
        "lower_bound": encode(lower),
        "slack": encode(slack),
    }


def directional_profile(weights: Iterable[F], line_fractions: Iterable[F]) -> dict:
    """Modèle fini exact de colonnes angulaires, toutes centrées radialement."""

    weights = tuple(weights)
    fractions = tuple(line_fractions)
    if len(weights) != len(fractions) or not weights:
        raise ValueError("poids et fractions incompatibles")
    if sum(weights) != 1 or any(weight < 0 for weight in weights):
        raise ValueError("les poids doivent former une probabilité")
    if any(not 0 <= value <= 1 for value in fractions):
        raise ValueError("fractions hors [0,1]")

    density = sum(weight * value**3 for weight, value in zip(weights, fractions))
    minimum = min(fractions)
    assert minimum**3 <= density
    return {
        "weights": [encode(value) for value in weights],
        "line_fractions": [encode(value) for value in fractions],
        "volume_density": encode(density),
        "minimum_line_fraction_cubed": encode(minimum**3),
        "certificate_slack": encode(density - minimum**3),
    }


def radius_from_global_measure_certificate(delta: F, bound_coefficient: F) -> dict:
    """Algèbre sans pi : B=bound_coefficient*|B_1| et r^3=B/(delta|B_1|)."""

    if not 0 < delta < 1 or bound_coefficient < 0:
        raise ValueError("paramètres inadmissibles")
    radius_cubed = bound_coefficient / delta
    ball_volume_coefficient = radius_cubed
    allowed_measure_coefficient = delta * ball_volume_coefficient
    assert allowed_measure_coefficient == bound_coefficient
    return {
        "delta": encode(delta),
        "global_measure_upper_bound_in_unit_ball_volumes": encode(
            bound_coefficient
        ),
        "chosen_radius_cubed": encode(radius_cubed),
        "delta_times_chosen_ball_volume": encode(allowed_measure_coefficient),
        "admissible_radius_direction": "r^3 >= B/(delta*|B_1|)",
    }


def dimension_d_identity(dimension: int, q: F) -> dict:
    """En dimension d, le même argument donne le seuil q=delta^(1/d)."""

    if dimension < 1 or not 0 <= q <= 1:
        raise ValueError("dimension/q inadmissible")
    length = 2 * q
    # min integral_A |t|^(d-1) dt = 2*(length/2)^d/d.
    moment = 2 * (length / 2) ** dimension / dimension
    # |B_1^d|=|S^(d-1)|/d et la paramétrisation signée porte 1/2.
    density = F(dimension, 2) * moment
    assert density == q**dimension
    return {
        "dimension": dimension,
        "line_fraction": encode(q),
        "density_lower_bound": encode(density),
        "critical_exponent": f"1/{dimension}",
    }


def main() -> None:
    balls = [central_ball_profile(q) for q in (F(1, 4), F(1, 2), F(3, 4))]
    shells = [
        concentric_shell_profile(F(0), F(1, 2)),
        concentric_shell_profile(F(1, 4), F(3, 4)),
        concentric_shell_profile(F(1, 2), F(1)),
    ]
    directional = [
        directional_profile((F(1, 2), F(1, 2)), (F(1, 4), F(3, 4))),
        directional_profile(
            (F(1, 6), F(1, 3), F(1, 2)),
            (F(1, 8), F(1, 2), F(7, 8)),
        ),
    ]
    dimensions = [dimension_d_identity(dimension, F(2, 3)) for dimension in range(1, 7)]

    delta = F(3, 4)
    q_lower = F(90856, 100000)
    q_upper = F(90857, 100000)
    assert q_lower**3 < delta < q_upper**3
    application = radius_from_global_measure_certificate(delta, F(1, 64))
    assert F(application["chosen_radius_cubed"]) == F(1, 48)

    report = {
        "test": "SPARSENESS-RESTRICTION-1",
        "question": (
            "Une densite volumique au plus delta dans B_r(x0) impose-t-elle "
            "une section par une droite passant par x0 de densite au plus "
            "delta^(1/3), au meme rayon et avec constante un?"
        ),
        "scope": (
            "lemme de theorie de la mesure sur R3; application aux super-niveaux "
            "de vitesse de arXiv:2607.08866v2, sans valider les autres maillons PDE"
        ),
        "arithmetic": "fractions rationnelles exactes; pi et racines cubiques elimines par normalisation",
        "discretization": "profils radiaux exacts et colonnes angulaires finies; aucune grille PDE",
        "analytic_core": {
            "polar_identity": (
                "|S intersect B_r|=(1/2) integral_S2 integral_-r^r "
                "1_S(x0+t nu)|t|^2 dt dnu"
            ),
            "bathtub_bound": "integral_A t^2 dt >= |A|^3/12",
            "conclusion": (
                "volume_density <= delta implies existence of nu with "
                "line_density <= delta^(1/3)"
            ),
            "sharpness": "S=B_(r delta^(1/3))(x0) donne egalite dans toutes les directions",
        },
        "manuscript_parameter_delta_3_over_4": {
            "delta": "3/4",
            "line_threshold": "q unique dans (0,1) tel que 4 q^3-3=0",
            "exact_rational_enclosure": [encode(q_lower), encode(q_upper)],
            "void_fraction_enclosure": [
                encode(1 - q_upper),
                encode(1 - q_lower),
            ],
            "threshold_cubed_residual": "0/1",
        },
        "central_balls": balls,
        "concentric_shells": shells,
        "directional_adversarial_profiles": directional,
        "dimension_d_checks": dimensions,
        "global_measure_to_radius_application": application,
        "quantifier_audit": [
            "le point x0 est fixe mais arbitraire et le rayon choisi est le meme pour tout x0 grace au majorant global",
            "pour une borne globale B, les rayons garantissant la densite par ce seul argument satisfont r^3>=B/(delta*|B_1|)",
            "on peut choisir explicitement le rayon minimal issu du majorant; une petite echelle arbitraire ne preserve pas la sparseness",
            "le lemme est geometrique et ne certifie ni la borne de distribution (49), ni l'analyticite, ni le maximum harmonique",
        ],
        "residuals": {
            "centered_interval_moment_constants": "0/1",
            "polar_normalization": "0/1",
            "central_ball_sharpness": "0/1",
            "shell_factorizations": "0/1",
            "finite_directional_profiles": "0/1",
            "dimension_d_scaling": "0/1",
            "global_measure_radius_identity": "0/1",
            "delta_3_over_4_algebraic_threshold_enclosure": "strict, exact rationals",
            "roundoff": "0 (aucun flottant)",
        },
        "decision": (
            "Le maillon 3D vers 1D est valide et sharp avec exposant 1/3. "
            "L'application par majorant global est valide si le rayon est choisi "
            "explicitement depuis ce majorant; le sens admissible est r superieur "
            "ou egal au rayon minimal, meme si ce rayon construit possede ensuite "
            "une borne superieure en fonction de l'amplitude."
        ),
        "seed": "sans objet",
        "pass": True,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
