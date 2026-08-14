"""Exact scaling and counterexample certificate for temporal trace moduli.

The Navier--Stokes scaling on R^3 is

    u_lambda(x,t) = lambda u(lambda x, lambda^2 t).

For the periodic exact family from QUADRATIC-PRESSURE-DEFECT-1, this script
tests the pair of times 0 and t_N=log(2)/(N^2+1).  It never approximates log(2):
fourth powers are multiplied by the exact symbolic power of log(2), leaving
rational certificates.
"""

from fractions import Fraction
import json


def q(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def scaling_exponent(sigma: Fraction, alpha: Fraction) -> Fraction:
    """Exponent of lambda for C_t^alpha dot-H_x^sigma under NS scaling."""
    return sigma - Fraction(1, 2) + 2 * alpha


def certificate(n: int) -> dict[str, object]:
    if n < 1:
        raise ValueError("N must be a positive integer")

    n2 = n * n
    eigenvalue = n2 + 1
    initial_l2_sq = Fraction(eigenvalue, 4 * n2)

    # At t_N the heat factor is 1/2, so delta u=(u(t_N)-u(0))=-u(0)/2.
    delta_l2_sq = initial_l2_sq / 4
    # Every Fourier mode of u_N^0 has |k|^2=N^2+1.
    delta_dot_hminus1_sq = delta_l2_sq / eigenvalue

    # If A_N=||delta u||_2/t_N^(1/4), then
    # 256 log(2) A_N^4=(N^2+1)^3/N^4.
    critical_l2_normalized_fourth = Fraction(eigenvalue**3, n2 * n2)

    # If B_N=||delta u||_dot-H^-1/t_N^(3/4), then
    # 256 log(2)^3 B_N^4 has the same rational value.
    critical_dot_hminus1_normalized_fourth = Fraction(
        eigenvalue**3, n2 * n2
    )

    # If E_N=||delta u||_dot-H^-1/t_N^(1/4), then
    # 256 log(2) E_N^4=(N^2+1)/N^4.
    energy_dot_hminus1_normalized_fourth = Fraction(eigenvalue, n2 * n2)

    common_asymptotic_ratio = critical_l2_normalized_fourth / n2
    energy_asymptotic_ratio = energy_dot_hminus1_normalized_fourth * n2

    residuals = {
        "dot_hminus1_eigenmode_identity": delta_dot_hminus1_sq
        - Fraction(1, 16 * n2),
        "critical_L2_equals_critical_dot_Hminus1": critical_l2_normalized_fourth
        - critical_dot_hminus1_normalized_fourth,
        "critical_growth_ratio": common_asymptotic_ratio
        - Fraction(eigenvalue**3, n2**3),
        "energy_decay_ratio": energy_asymptotic_ratio
        - Fraction(eigenvalue, n2),
        "scale_L2_alpha_quarter": scaling_exponent(
            Fraction(0), Fraction(1, 4)
        ),
        "scale_dot_Hminus1_alpha_three_quarters": scaling_exponent(
            Fraction(-1), Fraction(3, 4)
        ),
        "scale_dot_Hminus1_alpha_quarter_plus_one": scaling_exponent(
            Fraction(-1), Fraction(1, 4)
        )
        + 1,
    }
    if any(value != 0 for value in residuals.values()):
        raise AssertionError((n, residuals))

    return {
        "N": n,
        "t_N": f"log(2)/{eigenvalue}",
        "initial_L2_squared": q(initial_l2_sq),
        "delta_L2_squared": q(delta_l2_sq),
        "delta_dot_Hminus1_squared": q(delta_dot_hminus1_sq),
        "256_log2_times_L2_C1_4_pair_quotient_fourth": q(
            critical_l2_normalized_fourth
        ),
        "256_log2_cubed_times_dot_Hminus1_C3_4_pair_quotient_fourth": q(
            critical_dot_hminus1_normalized_fourth
        ),
        "256_log2_times_dot_Hminus1_C1_4_pair_quotient_fourth": q(
            energy_dot_hminus1_normalized_fourth
        ),
        "critical_value_divided_by_N_squared": q(common_asymptotic_ratio),
        "energy_value_times_N_squared": q(energy_asymptotic_ratio),
        "residuals": {name: q(value) for name, value in residuals.items()},
    }


def main() -> None:
    scaling = {
        "general_exponent": "sigma-1/2+2alpha",
        "L2_C1_4": q(
            scaling_exponent(Fraction(0), Fraction(1, 4))
        ),
        "dot_Hminus1_C3_4": q(
            scaling_exponent(Fraction(-1), Fraction(3, 4))
        ),
        "dot_Hminus1_C1_4": q(
            scaling_exponent(Fraction(-1), Fraction(1, 4))
        ),
    }
    result = {
        "experiment": "TRACE-MODULUS-1",
        "equation": "3D incompressible Navier-Stokes scaling on R^3; exact test family on T^3",
        "arithmetic": "exact rational with symbolic log(2)",
        "seed": "not applicable",
        "scaling": scaling,
        "rows": [certificate(n) for n in (1, 2, 4, 8, 16, 32, 64, 128)],
        "maximum_exact_residual": "0/1",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
