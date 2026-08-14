"""Contre-test triadique exact pour Navier–Stokes/Euler sur T^3.

Convention de Fourier : u(x)=sum_k u_hat(k) exp(i k.x), volume normalisé.
Le terme non linéaire projeté est
    N_k = -i P_k sum_{p+q=k} (q.u_p) u_q.

Tous les calculs utilisent des rationnels gaussiens exacts. Aucune FFT et aucune
arithmétique flottante ne participent au certificat.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from typing import Dict, Iterable, Tuple

Wave = Tuple[int, int, int]
QComplex = Tuple[F, F]
Vector = Tuple[QComplex, QComplex, QComplex]

ZERO: QComplex = (F(0), F(0))


def z(re: int | F = 0, im: int | F = 0) -> QComplex:
    return F(re), F(im)


def add(a: QComplex, b: QComplex) -> QComplex:
    return a[0] + b[0], a[1] + b[1]


def mul(a: QComplex, b: QComplex) -> QComplex:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def scale(a: QComplex, c: int | F) -> QComplex:
    return a[0] * F(c), a[1] * F(c)


def conj(a: QComplex) -> QComplex:
    return a[0], -a[1]


def minus_i(a: QComplex) -> QComplex:
    return a[1], -a[0]


def times_i(a: QComplex) -> QComplex:
    return -a[1], a[0]


def vadd(a: Vector, b: Vector) -> Vector:
    return tuple(add(x, y) for x, y in zip(a, b))  # type: ignore[return-value]


def vconj(a: Vector) -> Vector:
    return tuple(conj(x) for x in a)  # type: ignore[return-value]


def real_dot_complex(k: Wave, a: Vector) -> QComplex:
    out = ZERO
    for coefficient, component in zip(k, a):
        out = add(out, scale(component, coefficient))
    return out


def real_cross_complex(k: Wave, a: Vector) -> Vector:
    return (
        add(scale(a[2], k[1]), scale(a[1], -k[2])),
        add(scale(a[0], k[2]), scale(a[2], -k[0])),
        add(scale(a[1], k[0]), scale(a[0], -k[1])),
    )


def curl_mode(k: Wave, a: Vector) -> Vector:
    return tuple(times_i(x) for x in real_cross_complex(k, a))  # type: ignore[return-value]


def complex_dot(a: Vector, b: Vector) -> QComplex:
    out = ZERO
    for x, y in zip(a, b):
        out = add(out, mul(x, y))
    return out


def hermitian_real_dot(a: Vector, b: Vector) -> F:
    return complex_dot(vconj(a), b)[0]


def norm2(a: Vector) -> F:
    return hermitian_real_dot(a, a)


def leray(k: Wave, a: Vector) -> Vector:
    k2 = sum(component * component for component in k)
    if k2 == 0:
        raise ValueError("P_0 n'est pas utilisé")
    longitudinal = real_dot_complex(k, a)
    correction = tuple(scale(longitudinal, F(component, k2)) for component in k)
    return tuple(
        add(component, scale(corr, -1)) for component, corr in zip(a, correction)
    )  # type: ignore[return-value]


def subwave(k: Wave, p: Wave) -> Wave:
    return tuple(x - y for x, y in zip(k, p))  # type: ignore[return-value]


def negwave(k: Wave) -> Wave:
    return tuple(-x for x in k)  # type: ignore[return-value]


def nonlinear_raw(k: Wave, modes: Dict[Wave, Vector]) -> Vector:
    total: Vector = (ZERO, ZERO, ZERO)
    for p, up in modes.items():
        q = subwave(k, p)
        uq = modes.get(q)
        if uq is None:
            continue
        coefficient = real_dot_complex(q, up)
        total = vadd(total, tuple(mul(coefficient, x) for x in uq))  # type: ignore[arg-type]
    return total


def nonlinear_projected(k: Wave, modes: Dict[Wave, Vector]) -> Vector:
    return tuple(minus_i(x) for x in leray(k, nonlinear_raw(k, modes)))  # type: ignore[return-value]


def pressure_contribution(k: Wave, modes: Dict[Wave, Vector]) -> Vector:
    raw = nonlinear_raw(k, modes)
    projected = leray(k, raw)
    longitudinal = tuple(
        add(x, scale(y, -1)) for x, y in zip(raw, projected)
    )
    return tuple(minus_i(x) for x in longitudinal)  # type: ignore[return-value]


def triad_modes(n: int, phase: int) -> tuple[Dict[Wave, Vector], Wave, Wave, Wave]:
    if n <= 0 or phase not in (-1, 1):
        raise ValueError("n>0 et phase=±1")
    a = (n, 0, 0)
    b = (0, n, 0)
    c = (n, n, 0)
    ua: Vector = (z(), z(1), z(1))
    ub: Vector = (z(1), z(), z())
    uc: Vector = (z(0, phase), z(0, -phase), z(0, phase))
    modes = {a: ua, b: ub, c: uc}
    for k, value in list(modes.items()):
        modes[negwave(k)] = vconj(value)
    return modes, a, b, c


def encode(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def analyze(n: int, phase: int) -> dict:
    modes, a, b, c = triad_modes(n, phase)
    divergence = {str(k): real_dot_complex(k, u) for k, u in modes.items()}
    reality = {
        str(k): tuple(
            add(x, scale(y, -1))
            for x, y in zip(modes[negwave(k)], vconj(u))
        )
        for k, u in modes.items()
    }
    nonlinear = {k: nonlinear_projected(k, modes) for k in modes}
    transfers = {k: hermitian_real_dot(modes[k], nonlinear[k]) for k in modes}
    pressure_work = {
        k: hermitian_real_dot(modes[k], pressure_contribution(k, modes))
        for k in modes
    }

    energy = F(1, 2) * sum(norm2(u) for u in modes.values())
    enstrophy = F(1, 2) * sum(
        sum(x * x for x in k) * norm2(u) for k, u in modes.items()
    )
    modal_helicities = {
        k: hermitian_real_dot(u, curl_mode(k, u)) for k, u in modes.items()
    }
    helicity = sum(modal_helicities.values())
    low = {a, negwave(a), b, negwave(b)}
    d_energy_low = sum(transfers[k] for k in low)
    forward_flux = -d_energy_low
    absolute_transfer_sum = sum(abs(value) for value in transfers.values())
    normalized_ratio_squared = forward_flux * forward_flux / (n * n * energy**3)

    zero = (F(0), F(0))
    assert all(value == zero for value in divergence.values())
    assert all(all(component == zero for component in vector) for vector in reality.values())
    assert all(real_dot_complex(k, nonlinear[k]) == zero for k in modes)
    assert all(value == 0 for value in pressure_work.values())
    assert sum(transfers.values()) == 0
    assert energy == 6
    assert enstrophy == 9 * n * n
    assert all(value == 0 for value in modal_helicities.values())
    assert helicity == 0
    assert abs(forward_flux) == 2 * n
    assert absolute_transfer_sum == 4 * n
    assert normalized_ratio_squared == F(1, 54)

    return {
        "N": n,
        "phase": phase,
        "energy": encode(energy),
        "enstrophy": encode(enstrophy),
        "helicity": encode(helicity),
        "max_modal_helicity_imbalance": "0/1",
        "forward_flux_Pi_N": encode(forward_flux),
        "absolute_transfer_sum": encode(absolute_transfer_sum),
        "Pi_over_absolute_sum": encode(forward_flux / absolute_transfer_sum),
        "normalized_ratio_squared": encode(normalized_ratio_squared),
        "total_nonlinear_energy_residual": encode(sum(transfers.values())),
        "max_divergence_residual": "0/1",
        "max_reality_residual": "0/1",
        "max_projected_divergence_residual": "0/1",
        "max_pressure_work_residual": "0/1",
    }


def main(ns: Iterable[int] = (1, 2, 4, 8, 16, 32, 64)) -> None:
    results = [analyze(n, phase) for n in ns for phase in (-1, 1)]
    for n in ns:
        pair = [item for item in results if item["N"] == n]
        assert pair[0]["forward_flux_Pi_N"] == f"{2*n}/1"
        assert pair[1]["forward_flux_Pi_N"] == f"{-2*n}/1"
    report = {
        "test": "TRI-PHASE-1",
        "equation": "terme non lineaire de Navier-Stokes incompressible sur T^3",
        "arithmetic": "rationnels gaussiens exacts",
        "discretization": "support Fourier fini explicite; aucune grille physique",
        "rounding_error_bound": "0",
        "claim_refuted": (
            "Il existe epsilon_N->0 tel que |Pi_N(u)| <= epsilon_N N E(u)^(3/2) "
            "pour tout polynome trigonometrique divergence-free."
        ),
        "certificate": (
            "Pour les deux phases, E=6, |Pi_N|=2N et "
            "(|Pi_N|/(N E^(3/2)))^2=1/54 pour tout N teste et, "
            "par la formule exacte, pour tout entier N>=1."
        ),
        "results": results,
        "pass": True,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
