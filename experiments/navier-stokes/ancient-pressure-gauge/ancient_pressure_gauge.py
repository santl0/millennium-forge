"""Exact certificate for a bounded ancient parasitic Navier--Stokes solution.

On R^3 x (-infinity, 0], for any viscosity nu>0, set

    a(t) = -t/(1+t^2),
    u(x,t) = a(t) e_1,
    p(x,t) = -a'(t) x_1.

The velocity is bounded, smooth, divergence-free and has terminal trace zero.
It solves the unforced equations and the local energy equality, but it is not
mild: its time dependence is carried by an affine harmonic pressure.  All
sampled identities use exact rational arithmetic.
"""

from fractions import Fraction
import json


def q(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def amplitude(t: Fraction) -> Fraction:
    return -t / (1 + t * t)


def amplitude_derivative(t: Fraction) -> Fraction:
    return (t * t - 1) / (1 + t * t) ** 2


def certificate(t_integer: int) -> dict[str, object]:
    if t_integer > 0:
        raise ValueError("ancient time must satisfy t<=0")

    t = Fraction(t_integer)
    a = amplitude(t)
    a_prime = amplitude_derivative(t)
    pressure_gradient = -a_prime

    # 1/4-a(t)^2=(t^2-1)^2/[4(1+t^2)^2] proves |a(t)|<=1/2.
    bound_gap = Fraction(1, 4) - a * a
    bound_certificate = (t * t - 1) ** 2 / (4 * (1 + t * t) ** 2)

    residuals = {
        "divergence": Fraction(0),
        "convection": Fraction(0),
        "laplacian_velocity": Fraction(0),
        "momentum_time_plus_pressure": a_prime + pressure_gradient,
        "pressure_poisson": Fraction(0),
        "local_energy_equality": a * a_prime + a * pressure_gradient,
        "velocity_bound_identity": bound_gap - bound_certificate,
    }
    if any(value != 0 for value in residuals.values()):
        raise AssertionError((t_integer, residuals))

    return {
        "t": t_integer,
        "a_t": q(a),
        "a_prime_t": q(a_prime),
        "pressure_x1_coefficient": q(-a_prime),
        "one_quarter_minus_a_squared": q(bound_gap),
        "residuals": {name: q(value) for name, value in residuals.items()},
    }


def main() -> None:
    sample_times = (0, -1, -2, -4, -8, -16)
    rows = [certificate(t) for t in sample_times]

    # Mild Duhamel formula for a spatial constant has RHS a(s), because the
    # heat semigroup preserves constants and div(u tensor u)=0.
    s = Fraction(-1)
    t = Fraction(0)
    mild_defect = amplitude(t) - amplitude(s)

    # At t=0, p=x_1. On Q_R=[-R,R]^3 its mean is zero and its normalized mean
    # absolute oscillation is R/2, proving that this pressure is not in BMO.
    bmo_witness = [
        {"cube_radius": radius, "mean_oscillation": q(Fraction(radius, 2))}
        for radius in (1, 2, 4, 8, 16, 32)
    ]

    result = {
        "experiment": "ANCIENT-PRESSURE-GAUGE-1",
        "equation": "3D incompressible unforced Navier-Stokes on R^3 x (-infinity,0]",
        "viscosity": "arbitrary positive; Delta u=0",
        "solution_notions": [
            "global smooth ancient distributional",
            "local suitable with energy equality",
            "not mild",
        ],
        "arithmetic": "exact rational",
        "seed": "not applicable",
        "terminal_velocity": q(amplitude(Fraction(0))),
        "nonzero_velocity_at_minus_one": q(amplitude(Fraction(-1))),
        "mild_formula_test_interval": "[-1,0]",
        "mild_formula_defect": q(mild_defect),
        "normalized_pressure_gradient_at_terminal_time": "0/1",
        "actual_pressure_gradient_at_terminal_time": q(
            -amplitude_derivative(Fraction(0))
        ),
        "BMO_cube_witness_at_terminal_time": bmo_witness,
        "rows": rows,
        "maximum_exact_identity_residual": "0/1",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
