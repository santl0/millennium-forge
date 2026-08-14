"""Test multipolaire exact de la pression lointaine centrée.

Le tenseur ponctuel M=diag(1,1,0), placé en R e_1, représente le moment
quadratique principal d'un paquet divergence-free axisymétrique localisé. Avec
le noyau de pression K_ij=partial_i partial_j(1/(4*pi*|x|)), le script travaille
sur 4*pi*p et compare la pression brute en 0 à sa variation entre 0 et e_1.
Il ne remplace pas le paquet par une solution PDE.
"""

from __future__ import annotations

import json
from fractions import Fraction


def encode(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def axial_normalized_pressure(distance: int) -> Fraction:
    """Valeur de 4*pi*p pour M=diag(1,1,0) sur l'axe."""
    if distance <= 0:
        raise ValueError("la distance doit être positive")
    return Fraction(1, distance**3)


def analyze(radius: int) -> dict[str, int | str]:
    if radius < 2:
        raise ValueError("R>=2 est requis pour comparer x=0 et x=e_1")
    pressure_zero = axial_normalized_pressure(radius)
    pressure_one = axial_normalized_pressure(radius - 1)
    centered = pressure_one - pressure_zero
    scaled_centered = radius**4 * centered

    # Identité exacte : R^4[(R-1)^-3-R^-3]
    # = R(3R^2-3R+1)/(R-1)^3.
    identity_residual = (
        scaled_centered * (radius - 1) ** 3
        - radius * (3 * radius**2 - 3 * radius + 1)
    )
    assert radius**3 * pressure_zero == 1
    assert identity_residual == 0

    return {
        "R": radius,
        "four_pi_p_at_zero": encode(pressure_zero),
        "raw_R3_scaled_pressure": encode(radius**3 * pressure_zero),
        "four_pi_centered_difference": encode(centered),
        "centered_R4_scaled": encode(scaled_centered),
        "identity_residual": encode(identity_residual),
    }


def main() -> None:
    results = [analyze(radius) for radius in (2, 4, 8, 16, 32, 64, 128)]
    report = {
        "test": "PRESSURE-TAIL-1",
        "equation": (
            "noyau de pression de Navier-Stokes incompressible sur R^3; "
            "moment ponctuel, aucune evolution PDE"
        ),
        "question": (
            "la pression brute d'un moment distant est-elle d'ordre R^-3 "
            "tandis que la pression centree active est d'ordre R^-4 ?"
        ),
        "kernel": (
            "K_ij(z)=(3 z_i z_j-|z|^2 delta_ij)/(4*pi*|z|^5)"
        ),
        "moment": "M=diag(1,1,0) place en R e_1",
        "probe_points": "x=0 et x=e_1",
        "arithmetic": "fractions rationnelles exactes apres normalisation par 4*pi",
        "discretization": "aucune",
        "rounding_error_bound": "0",
        "asymptotics": {
            "raw": "4*pi*p_R(0)=R^-3 exactement",
            "centered": (
                "R^4*4*pi*(p_R(e_1)-p_R(0)) "
                "=R(3R^2-3R+1)/(R-1)^3 -> 3"
            ),
        },
        "scope_warning": (
            "le calcul ponctuel teste l'ordre multipolaire; la borne de paquet "
            "compact et son raccord a l'energie locale sont analytiques"
        ),
        "results": results,
        "pass": True,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
