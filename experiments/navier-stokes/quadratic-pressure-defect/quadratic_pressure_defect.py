"""Exact certificate for an oscillatory pressure/product trace defect.

On T^3=(R/2piZ)^3 and with viscosity nu=1, set

    psi_N = sin(x1) cos(N x2) / N,
    u_N^0 = curl(psi_N e3),
    u_N(t) = exp(-(N^2+1)t) u_N^0.

The nonlinear term is a gradient, so this is an exact smooth unforced
Navier--Stokes solution with the pressure stated below. At
t_N=log(2)/(N^2+1), the damping factor is exactly 1/2. All checks use rational
arithmetic; logarithm is retained symbolically and is never rounded.
"""

from fractions import Fraction
import json


def q(value: Fraction) -> str:
    """Canonical string for an exact rational."""
    return f"{value.numerator}/{value.denominator}"


def certificate(n: int) -> dict[str, object]:
    if n < 1:
        raise ValueError("N must be a positive integer")

    n_q = Fraction(n)
    a = Fraction(1, 2)
    a2 = a * a

    # Normalized torus average <f>=(2pi)^-3 integral_T3 f.
    initial_l2_sq = Fraction(1, 4) * (1 + 1 / (n_q * n_q))
    sampled_l2_sq = a2 * initial_l2_sq
    initial_kinetic_energy = initial_l2_sq / 2
    sampled_kinetic_energy = sampled_l2_sq / 2
    integrated_dissipation = (1 - a2) * initial_l2_sq / 2

    # Coefficients in the bases sin(2x1) and sin(2N x2).
    nonlinear_x = a2 / 2
    pressure_gradient_x = -a2 / 2
    nonlinear_y = -a2 / (2 * n_q)
    pressure_gradient_y = a2 / (2 * n_q)

    # Coefficients in cos(2x1), cos(2N x2) for -Delta p and div((u.grad)u).
    pressure_poisson = (a2, -a2)
    nonlinear_divergence = (a2, -a2)

    residuals = {
        "divergence": Fraction(-1) + Fraction(1),
        "momentum_x": nonlinear_x + pressure_gradient_x,
        "momentum_y": nonlinear_y + pressure_gradient_y,
        "laplacian_eigenvalue_u1": Fraction(-(n * n + 1))
        + Fraction(n * n + 1),
        "laplacian_eigenvalue_u2": Fraction(-(n * n + 1))
        + Fraction(n * n + 1),
        "pressure_poisson_x": pressure_poisson[0]
        - nonlinear_divergence[0],
        "pressure_poisson_y": pressure_poisson[1]
        - nonlinear_divergence[1],
        "energy_identity": sampled_kinetic_energy
        + integrated_dissipation
        - initial_kinetic_energy,
        "sample_damping": a - Fraction(1, 2),
    }
    if any(residual != 0 for residual in residuals.values()):
        raise AssertionError((n, residuals))

    return {
        "N": n,
        "t_N": f"log(2)/{n * n + 1}",
        "damping": q(a),
        "initial_L2_squared": q(initial_l2_sq),
        "sampled_L2_squared": q(sampled_l2_sq),
        "initial_kinetic_energy": q(initial_kinetic_energy),
        "sampled_kinetic_energy": q(sampled_kinetic_energy),
        "integrated_dissipation_0_to_t_N": q(integrated_dissipation),
        "weak_product_defect_u1_squared_sin_x1_squared": q(a2 / 2),
        "weak_pressure_limit_cos_2x1": q(a2 / 4),
        "oscillatory_pressure_cos_2N_x2": q(-a2 / (4 * n_q * n_q)),
        "small_velocity_component_amplitude": q(-a / n_q),
        "residuals": {name: q(value) for name, value in residuals.items()},
    }


def main() -> None:
    rows = [certificate(n) for n in (1, 2, 4, 8, 16, 32, 64, 128)]
    result = {
        "experiment": "QUADRATIC-PRESSURE-DEFECT-1",
        "equation": "3D incompressible unforced Navier-Stokes on T^3",
        "viscosity": "1/1",
        "arithmetic": "exact rational; t_N retained symbolically",
        "seed": "not applicable",
        "velocity_weak_limit_at_t_N": "0",
        "product_weak_limit": "diag((1/8) sin(x1)^2,0,0)",
        "pressure_weak_limit": "(1/16) cos(2x1)",
        "pressure_of_velocity_weak_limit": "0",
        "rows": rows,
        "maximum_exact_residual": "0/1",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
