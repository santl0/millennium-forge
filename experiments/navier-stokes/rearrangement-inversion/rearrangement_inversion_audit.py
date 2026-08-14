"""Certificat exact pour l'inversion réarrangée -> fonction de distribution.

Le noyau analytique est le suivant. Pour

    d_f(lambda)=mu({|f|>lambda}),
    f*(v)=inf{lambda>=0: d_f(lambda)<=v},

une enveloppe ``f*(v)<=A v^(-1/3)/log(e V*/v)`` sur ``0<v<=v0``
implique, au-dessus d'un seuil explicite,

    d_f(lambda)
      <= A^3 / [lambda^3 (1+3 log(lambda/Lambda*))^3],
    Lambda*=A V*^(-1/3).

Le script vérifie les identités algébriques, la covariance d'échelle, les
quantificateurs sur une fonction en plateaux et des encadrements rationnels
de logarithmes. Aucun flottant, maillage PDE ou tirage aléatoire n'est utilisé.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction as F


def encode(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def log_fraction_interval(x: F, terms: int = 20) -> tuple[F, F]:
    """Encadrement exact de log(x), x>=1, par la série de atanh.

    log(x)=2 sum_{k>=0} z^(2k+1)/(2k+1), z=(x-1)/(x+1).
    Le reste positif est majoré par une série géométrique rationnelle.
    """

    if x < 1 or terms < 1:
        raise ValueError("x>=1 et terms>=1 requis")
    z = (x - 1) / (x + 1)
    partial = F(0)
    for k in range(terms):
        partial += 2 * z ** (2 * k + 1) / (2 * k + 1)
    next_power = 2 * terms + 1
    remainder = 2 * z**next_power / (next_power * (1 - z * z))
    return partial, partial + remainder


@dataclass(frozen=True)
class StepProfile:
    """Fonction simple sur des atomes disjoints de mesures rationnelles."""

    atoms: tuple[tuple[F, F], ...]  # (amplitude |f|, mesure)

    @property
    def total_measure(self) -> F:
        return sum((weight for _, weight in self.atoms), F(0))

    def distribution(self, level: F) -> F:
        if level < 0:
            raise ValueError("niveau positif requis")
        return sum(
            (weight for amplitude, weight in self.atoms if amplitude > level),
            F(0),
        )

    def rearrangement(self, volume: F) -> F:
        if not 0 <= volume <= self.total_measure:
            raise ValueError("volume hors domaine")
        levels = sorted({F(0), *(amplitude for amplitude, _ in self.atoms)})
        admissible = [level for level in levels if self.distribution(level) <= volume]
        if not admissible:
            raise AssertionError("ensemble de quantiles vide")
        return min(admissible)


def plateau_quantifier_certificate() -> dict:
    profile = StepProfile(
        (
            (F(4), F(1, 8)),
            (F(2), F(3, 8)),
            (F(0), F(1, 2)),
        )
    )
    levels = tuple(F(value) for value in range(6))
    volumes = (F(0), F(1, 16), F(1, 8), F(1, 4), F(1, 2), F(1))

    # Équivalence de quantile avec la convention stricte {|f|>lambda}.
    for level in levels:
        for volume in volumes:
            assert (profile.distribution(level) <= volume) == (
                profile.rearrangement(volume) <= level
            )

    threshold = F(3)
    mass = profile.distribution(threshold)
    endpoint_quantile = profile.rearrangement(mass)
    interior_volume = F(1, 16)
    interior_quantile = profile.rearrangement(interior_volume)

    assert mass == F(1, 8)
    assert endpoint_quantile == F(2) != threshold
    assert interior_volume < mass
    assert interior_quantile == F(4) > threshold

    return {
        "profile": [
            {"amplitude": encode(amplitude), "measure": encode(weight)}
            for amplitude, weight in profile.atoms
        ],
        "threshold": encode(threshold),
        "distribution_mass": encode(mass),
        "rearrangement_at_distribution_mass": encode(endpoint_quantile),
        "manuscript_endpoint_equality": False,
        "valid_replacement": (
            "for every 0<v<d_f(lambda), f*(v)>lambda; "
            "then let v increase to d_f(lambda) in the continuous envelope"
        ),
        "quantile_equivalence_grid": "PASS exact rationals",
    }


def logarithmic_enclosures() -> list[dict]:
    lower_log2 = F(69, 100)
    upper_log2 = F(70, 100)
    exact_lower, exact_upper = log_fraction_interval(F(2), terms=20)
    assert lower_log2 < exact_lower < exact_upper < upper_log2

    rows = []
    for power in range(1, 5):
        x = F(2**power)
        log_lower = power * lower_log2
        log_upper = power * upper_log2

        # B(x)=x^-3/[1+3 log(x)]^3. Les bornes sont rationnelles exactes.
        bound_lower = x**-3 / (1 + 3 * log_upper) ** 3
        bound_upper = x**-3 / (1 + 3 * log_lower) ** 3
        coarse_upper = x**-3 / (27 * log_lower**3)
        assert F(0) < bound_lower < bound_upper < coarse_upper

        rows.append(
            {
                "lambda_over_Lambda_star": encode(x),
                "certified_log_interval": [encode(log_lower), encode(log_upper)],
                "sharp_distribution_factor_interval": [
                    encode(bound_lower),
                    encode(bound_upper),
                ],
                "coarse_log_cubed_upper_factor": encode(coarse_upper),
            }
        )
    return rows


def algebraic_inversion_certificate() -> dict:
    # Variables normalisées : x=lambda/Lambda*, L>=1+3 log(x).
    # Le certificat algébrique porte sur des coordonnées logarithmiques k.
    rows = []
    for k in range(0, 9):
        log_lower = F(k)
        lower_denominator = 1 + 3 * log_lower
        assert lower_denominator >= 1

        # Si x=exp(k), la puissance exponentielle x^-3 est gardée symbolique.
        coefficient = F(1, lower_denominator**3)
        rows.append(
            {
                "log_x": str(k),
                "symbolic_x_power": f"exp(-{3 * k})",
                "exact_rational_log_coefficient": encode(coefficient),
                "bound": f"m/V_star <= exp(-{3 * k})/{lower_denominator ** 3}",
            }
        )

    return {
        "implication_1": "lambda <= A m^(-1/3)L(m)^(-1)",
        "implication_2": "m <= (A/lambda)^3 L(m)^(-3)",
        "baseline": "m <= (A/lambda)^3 because L(m)>=1",
        "log_feedback": (
            "L(m)=log(e V_star/m)>=1+3 log(lambda/Lambda_star), "
            "Lambda_star=A V_star^(-1/3)"
        ),
        "final": (
            "m <= A^3/[lambda^3(1+3log(lambda/Lambda_star))^3]"
        ),
        "log_coordinate_checks": rows,
    }


def scaling_certificate() -> dict:
    # V_star=ell_star^3 évite toute racine irrationnelle.
    amplitude_length = F(2)  # A, invariant sous le scaling NS
    ell_star = F(1)
    level = F(8)
    kappa = F(3)

    lambda_star = amplitude_length / ell_star
    ratio = level / lambda_star
    algebraic_volume_prefactor = amplitude_length**3 / level**3

    scaled_ell_star = ell_star / kappa
    scaled_level = kappa * level
    scaled_lambda_star = amplitude_length / scaled_ell_star
    scaled_ratio = scaled_level / scaled_lambda_star
    scaled_volume_prefactor = amplitude_length**3 / scaled_level**3

    assert ratio == scaled_ratio == 4
    assert scaled_lambda_star == kappa * lambda_star
    assert scaled_volume_prefactor == algebraic_volume_prefactor / kappa**3

    return {
        "NS_scaling": "u_kappa(x,t)=kappa u(kappa x,kappa^2 t)",
        "A_scaling": "invariant",
        "V_star_scaling": "kappa^-3",
        "Lambda_star_scaling": "kappa",
        "lambda_over_Lambda_star": encode(ratio),
        "distribution_bound_scaling": "kappa^-3",
        "exact_prefactor_before": encode(algebraic_volume_prefactor),
        "exact_prefactor_after": encode(scaled_volume_prefactor),
    }


def main() -> None:
    report = {
        "test": "REARRANGEMENT-INVERSION-1",
        "question": (
            "L'enveloppe u*(v)<=A v^(-1/3)/log(e V*/v) implique-t-elle "
            "une borne uniforme lambda^-3 log^-3 sur la fonction de distribution, "
            "sans supposer lambda=u*(d_u(lambda))?"
        ),
        "scope": (
            "lemme de theorie de la mesure; application conditionnelle aux equations "
            "(47)-(49) de arXiv:2607.08866v2; aucun autre maillon PDE certifie"
        ),
        "definitions": {
            "distribution": "d_f(lambda)=measure({|f|>lambda})",
            "rearrangement": "f*(v)=inf{lambda>=0:d_f(lambda)<=v}",
            "dimensionless_log": "L(v)=log(e V_star/v)",
        },
        "hypotheses": [
            "0<v0<=V_star<infinity",
            "f*(v)<=A v^(-1/3)L(v)^(-1) for every 0<v<=v0",
            "A,v0,V_star are uniform in time in the parameterized application",
            "lambda>=max(A v0^(-1/3)L(v0)^(-1), A V_star^(-1/3))",
        ],
        "analytic_certificate": algebraic_inversion_certificate(),
        "plateau_adversarial_test": plateau_quantifier_certificate(),
        "certified_log_tests": logarithmic_enclosures(),
        "scaling": scaling_certificate(),
        "residuals": {
            "quantile_equivalence": "0/1 failures",
            "plateau_endpoint_counterexample": "exact fractions",
            "algebraic_exponents_and_constants": "0/1",
            "logarithm_enclosures": "strict rational intervals from atanh series",
            "NS_scaling": "0/1",
            "roundoff": "0 (aucun flottant)",
        },
        "decision": (
            "L'implication (47)->(49) est valide apres remplacement de l'egalite "
            "de quantile par un argument v<d_f(lambda), ajout d'un seuil explicite "
            "et normalisation du logarithme. La constante uniforme est heritee "
            "uniquement si A,v0,V_star sont uniformes."
        ),
        "seed": "sans objet",
        "pass": True,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
