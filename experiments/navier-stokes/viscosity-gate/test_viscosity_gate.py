"""Test exact du seuil visqueux VAS-1.

Aucune discrétisation PDE : toutes les identités et bornes sont calculées en
arithmétique rationnelle. La sortie JSON est déterministe.
"""

from __future__ import annotations

import json
from fractions import Fraction


def q(x: str) -> Fraction:
    return Fraction(x)


def exact_decimal(value: Fraction) -> str:
    """Écriture décimale exacte pour un rationnel à dénominateur 2^a 5^b."""
    denominator = value.denominator
    twos = fives = 0
    while denominator % 2 == 0:
        denominator //= 2
        twos += 1
    while denominator % 5 == 0:
        denominator //= 5
        fives += 1
    if denominator != 1:
        raise ValueError(f"décimale non terminante: {value}")
    places = max(twos, fives)
    scaled = value.numerator * 2 ** (places - twos) * 5 ** (places - fives)
    sign = "-" if scaled < 0 else ""
    digits = str(abs(scaled)).rjust(places + 1, "0")
    if places == 0:
        return f"{sign}{digits}"
    integer, fraction = digits[:-places], digits[-places:]
    fraction = fraction.rstrip("0")
    return f"{sign}{integer}.{fraction}" if fraction else f"{sign}{integer}"


def encode(value: Fraction) -> dict[str, str]:
    return {
        "fraction": f"{value.numerator}/{value.denominator}",
        "decimal_exact": exact_decimal(value),
    }


def interval_for_lambda(lo: Fraction, hi: Fraction, decades: int) -> dict:
    assert lo <= hi
    gamma_lo = 1 + 2 * lo
    gamma_hi = 1 + 2 * hi
    return {
        "lambda": [encode(lo), encode(hi)],
        "gamma_1_plus_2lambda": [encode(gamma_lo), encode(gamma_hi)],
        "delta_log10_ratio_after_decades": [
            encode(decades * gamma_lo),
            encode(decades * gamma_hi),
        ],
    }


def main() -> None:
    # Exposants symboliques représentés par leurs coefficients en a et leur constante.
    # e(a)=coef*a+constant.
    time = (1, -1)       # a-1
    advection = (2, 0)   # 2a-b, avant substitution b=a+1
    pressure = (2, 0)    # 2a-b
    viscosity = (1, 0)   # a-2b, avant substitution

    # Substitution b=a+1.
    adv_balanced = (advection[0] - 1, advection[1] - 1)
    pressure_balanced = (pressure[0] - 1, pressure[1] - 1)
    visc_balanced = (viscosity[0] - 2, viscosity[1] - 2)

    residuals = {
        "time_minus_advection_coeff_a": time[0] - adv_balanced[0],
        "time_minus_advection_constant": time[1] - adv_balanced[1],
        "time_minus_pressure_coeff_a": time[0] - pressure_balanced[0],
        "time_minus_pressure_constant": time[1] - pressure_balanced[1],
        # (viscous - inertial) - (-1-2a)
        "ratio_exponent_coeff_a": (visc_balanced[0] - time[0]) - (-2),
        "ratio_exponent_constant": (visc_balanced[1] - time[1]) - (-1),
    }
    assert all(value == 0 for value in residuals.values())

    decades = 12
    cases = {
        # 0.4703 est affiché à quatre décimales dans P1 : intervalle d'arrondi.
        "CCF_lambda2_diagnostic_only": interval_for_lambda(
            q("0.47025"), q("0.47035"), decades
        ),
        # Fenêtre explicitement testée autour du quatrième profil IPM dans P2.
        "IPM_fourth_search_window_diagnostic_only": interval_for_lambda(
            q("0.1980"), q("0.2000"), decades
        ),
        "NS_critical_lambda": interval_for_lambda(q("-0.5"), q("-0.5"), decades),
        "adversarial_subcritical_lambda": interval_for_lambda(
            q("-0.75"), q("-0.75"), decades
        ),
    }

    result = {
        "test": "VAS-1",
        "arithmetic": "fractions rationnelles exactes",
        "discretization": "aucune",
        "rounding_error_bound": "0",
        "certified_identity_residuals": residuals,
        "interpretation": (
            "Si tau est divisé par 10, log10(visqueux/inertiel) augmente de "
            "gamma=1+2*lambda."
        ),
        "boussinesq_euler_empirical_ladder": {
            "assumption_from_P1": "lambda_n > 1",
            "certified_consequence_per_decade": "delta_log10_ratio > 3",
            "certified_consequence_after_12_decades": "delta_log10_ratio > 36",
        },
        "cases": cases,
        "pass": True,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
