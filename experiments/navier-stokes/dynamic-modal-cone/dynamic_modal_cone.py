#!/usr/bin/env python3
"""Exact outward derivative at a boundary of an instantaneous modal cone.

This extends the polynomial-Gaussian algebra from cycle 0062.  The Leray
pressure contribution to C'_3 is evaluated exactly in Fourier variables with
Fraction arithmetic and the multiplier 1/|xi|^2.  No time integration is run.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import product
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
CORE_PATH = (
    SCRIPT_PATH.parents[1]
    / "instantaneous-modal-sign"
    / "instantaneous_modal_sign.py"
)
CORE_SPEC = importlib.util.spec_from_file_location("instantaneous_modal_sign_core", CORE_PATH)
if CORE_SPEC is None or CORE_SPEC.loader is None:
    raise RuntimeError(f"cannot load exact polynomial core: {CORE_PATH}")
core = importlib.util.module_from_spec(CORE_SPEC)
CORE_SPEC.loader.exec_module(core)


Polynomial = core.Polynomial
PolyVector = core.PolyVector
RateVector = dict[int, PolyVector]
ComplexQ = tuple[Q, Q]
ComplexPolynomial = dict[core.Monomial, ComplexQ]


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, left: object, right: object) -> None:
        self.assertions += 1
        assert left == right, (left, right)

    def true(self, statement: bool) -> None:
        self.assertions += 1
        assert statement


def gaussian_derivative_rate(polynomial: Polynomial, axis: int, rate: int) -> Polynomial:
    return core.add_polynomials(
        core.derivative(polynomial, axis),
        core.scale_polynomial(
            -2 * rate,
            core.multiply_coordinate(polynomial, axis),
        ),
    )


def laplacian_rate(field: PolyVector, rate: int) -> PolyVector:
    return tuple(
        core.add_polynomials(
            *(
                gaussian_derivative_rate(
                    gaussian_derivative_rate(field[component], axis, rate),
                    axis,
                    rate,
                )
                for axis in range(3)
            )
        )
        for component in range(3)
    )  # type: ignore[return-value]


def divergence_rate(field: PolyVector, rate: int) -> Polynomial:
    return core.add_polynomials(
        *(
            gaussian_derivative_rate(field[component], component, rate)
            for component in range(3)
        )
    )


def rate_vector_add(*fields: RateVector) -> RateVector:
    rates = sorted({rate for field in fields for rate in field})
    result: RateVector = {}
    for rate in rates:
        components = tuple(field[rate] for field in fields if rate in field)
        value = core.add_vectors(*components)
        if value != core.ZERO:
            result[rate] = value
    return result


def rate_vector_scale(coefficient: int | Q, field: RateVector) -> RateVector:
    return {
        rate: core.scale_vector(coefficient, value)
        for rate, value in field.items()
    }


def laplacian_multirate(field: RateVector) -> RateVector:
    return {
        rate: laplacian_rate(value, rate)
        for rate, value in field.items()
    }


def advection_multirate(left: RateVector, right: RateVector) -> RateVector:
    result: RateVector = {}
    for left_rate, left_field in left.items():
        for right_rate, right_field in right.items():
            output_rate = left_rate + right_rate
            value: PolyVector = tuple(
                core.add_polynomials(
                    *(
                        core.multiply_polynomials(
                            left_field[axis],
                            gaussian_derivative_rate(
                                right_field[component],
                                axis,
                                right_rate,
                            ),
                        )
                        for axis in range(3)
                    )
                )
                for component in range(3)
            )  # type: ignore[assignment]
            result[output_rate] = core.add_vectors(
                result.get(output_rate, core.ZERO),
                value,
            )
    return {rate: value for rate, value in result.items() if value != core.ZERO}


def local_directional_derivative_by_rate(
    total: PolyVector,
    tangent: PolyVector,
) -> dict[int, Q]:
    # kappa=0.  A=Delta Z-(Z dot nabla)Z is the local, unprojected vector
    # field.  DA[A]=Delta A-B(A,Z)-B(Z,A).
    nonlinear = core.nonlinear_advection(total)
    raw_field: RateVector = {
        1: core.gaussian_laplacian(total),
        2: core.scale_vector(-1, nonlinear),
    }
    state: RateVector = {1: total}
    derivative = rate_vector_add(
        laplacian_multirate(raw_field),
        rate_vector_scale(-1, advection_multirate(raw_field, state)),
        rate_vector_scale(-1, advection_multirate(state, raw_field)),
    )
    pairing_polynomials: dict[int, Polynomial] = {}
    for rate, value in derivative.items():
        total_rate = rate + 1
        polynomial = core.vector_dot_polynomial(value, tangent)
        pairing_polynomials[total_rate] = core.add_polynomials(
            pairing_polynomials.get(total_rate, {}),
            polynomial,
        )
    return {
        rate: core.normalized_integral(polynomial, rate)
        for rate, polynomial in pairing_polynomials.items()
    }


def pressure_source(total: PolyVector) -> Polynomial:
    # -Delta p=S=div div(Z tensor Z)=div((Z dot nabla)Z).
    nonlinear = core.nonlinear_advection(total)
    return divergence_rate(nonlinear, 2)


def pressure_test(total: PolyVector, tangent: PolyVector) -> Polynomial:
    # The pressure part of DC_m is <p,Q_m>.  From H_pressure=-grad p:
    # Q=-d_j[(d_j Z_i)q_i]+d_i[Z_j(d_j q_i)].
    result: Polynomial = {}
    for component in range(3):
        for axis in range(3):
            first_product = core.multiply_polynomials(
                gaussian_derivative_rate(total[component], axis, 1),
                tangent[component],
            )
            second_product = core.multiply_polynomials(
                total[axis],
                gaussian_derivative_rate(tangent[component], axis, 1),
            )
            result = core.add_polynomials(
                result,
                core.scale_polynomial(
                    -1,
                    gaussian_derivative_rate(first_product, axis, 2),
                ),
                gaussian_derivative_rate(second_product, component, 2),
            )
    return result


def complex_clean(polynomial: ComplexPolynomial) -> ComplexPolynomial:
    return {
        exponent: coefficient
        for exponent, coefficient in polynomial.items()
        if coefficient != (Q(0), Q(0))
    }


def complex_add(*polynomials: ComplexPolynomial) -> ComplexPolynomial:
    result: ComplexPolynomial = {}
    for polynomial in polynomials:
        for exponent, (real, imaginary) in polynomial.items():
            old_real, old_imaginary = result.get(exponent, (Q(0), Q(0)))
            result[exponent] = old_real + real, old_imaginary + imaginary
    return complex_clean(result)


def complex_scale(coefficient: ComplexQ, polynomial: ComplexPolynomial) -> ComplexPolynomial:
    scalar_real, scalar_imaginary = coefficient
    return complex_clean(
        {
            exponent: (
                scalar_real * real - scalar_imaginary * imaginary,
                scalar_real * imaginary + scalar_imaginary * real,
            )
            for exponent, (real, imaginary) in polynomial.items()
        }
    )


def complex_derivative(polynomial: ComplexPolynomial, axis: int) -> ComplexPolynomial:
    result: ComplexPolynomial = {}
    for exponent, coefficient in polynomial.items():
        if exponent[axis] == 0:
            continue
        reduced = list(exponent)
        power = reduced[axis]
        reduced[axis] -= 1
        result[tuple(reduced)] = coefficient[0] * power, coefficient[1] * power
    return complex_clean(result)


def complex_multiply_coordinate(
    polynomial: ComplexPolynomial,
    axis: int,
) -> ComplexPolynomial:
    result: ComplexPolynomial = {}
    for exponent, coefficient in polynomial.items():
        raised = list(exponent)
        raised[axis] += 1
        result[tuple(raised)] = coefficient
    return result


def complex_multiply(
    left: ComplexPolynomial,
    right: ComplexPolynomial,
) -> ComplexPolynomial:
    result: ComplexPolynomial = {}
    for left_exponent, (left_real, left_imaginary) in left.items():
        for right_exponent, (right_real, right_imaginary) in right.items():
            exponent = tuple(
                left_exponent[axis] + right_exponent[axis]
                for axis in range(3)
            )
            real = left_real * right_real - left_imaginary * right_imaginary
            imaginary = left_real * right_imaginary + left_imaginary * right_real
            old_real, old_imaginary = result.get(exponent, (Q(0), Q(0)))
            result[exponent] = old_real + real, old_imaginary + imaginary
    return complex_clean(result)


def fourier_polynomial(polynomial: Polynomial, physical_rate: int) -> ComplexPolynomial:
    # hat(P exp(-a|x|^2))=(pi/a)^(3/2) T(P) exp(-|xi|^2/(4a)).
    result: ComplexPolynomial = {}
    for exponent, coefficient in polynomial.items():
        transformed: ComplexPolynomial = {(0, 0, 0): (coefficient, Q(0))}
        for axis, power in enumerate(exponent):
            for _ in range(power):
                differentiated = complex_derivative(transformed, axis)
                gaussian_term = complex_scale(
                    (Q(-1, 2 * physical_rate), Q(0)),
                    complex_multiply_coordinate(transformed, axis),
                )
                transformed = complex_scale(
                    (Q(0), Q(1)),
                    complex_add(differentiated, gaussian_term),
                )
        result = complex_add(result, transformed)
    return result


def inverse_laplacian_moment_quarter(exponent: core.Monomial) -> Q:
    # Integral xi^exponent |xi|^-2 exp(-|xi|^2/4) dxi / pi^(3/2).
    if any(power % 2 for power in exponent):
        return Q(0)
    half_powers = tuple(power // 2 for power in exponent)
    total_half_power = sum(half_powers)
    numerator = 1
    for half_power in half_powers:
        numerator *= core.odd_double_factorial(2 * half_power - 1)
    return Q(numerator * 2 ** (total_half_power + 2), 2 * total_half_power + 1)


def inverse_laplacian_pairing_rate_two(
    source: Polynomial,
    test: Polynomial,
) -> Q:
    # Both physical Gaussians have rate 2.  Parseval contributes 1/64 after
    # removing pi^(3/2); the Fourier Gaussian product has rate 1/4.
    source_hat = fourier_polynomial(source, 2)
    test_hat = complex_scale((Q(1), Q(0)), fourier_polynomial(test, 2))
    test_hat_conjugate = {
        exponent: (real, -imaginary)
        for exponent, (real, imaginary) in test_hat.items()
    }
    product_hat = complex_multiply(source_hat, test_hat_conjugate)
    real_integral = Q(0)
    imaginary_integral = Q(0)
    for exponent, (real, imaginary) in product_hat.items():
        moment = inverse_laplacian_moment_quarter(exponent)
        real_integral += real * moment
        imaginary_integral += imaginary * moment
    if imaginary_integral != 0:
        raise AssertionError(("non-real inverse-Laplacian pairing", imaginary_integral))
    return Q(1, 64) * real_integral


def audit_fourier_normalization(audit: Audit, test: Polynomial) -> None:
    # Manufactured phi=P exp(-2r^2), S=-Delta phi.  This verifies exactly
    # <S,(-Delta)^-1 test>=<phi,test> with the adopted Fourier convention.
    phi = core.add_polynomials(
        core.monomial((0, 0, 0), 1),
        core.monomial((2, 0, 0), 1),
        core.monomial((0, 2, 0), -1),
    )
    phi_field: PolyVector = (phi, {}, {})
    minus_laplacian_phi = core.scale_polynomial(
        -1,
        laplacian_rate(phi_field, 2)[0],
    )
    fourier_pairing = inverse_laplacian_pairing_rate_two(
        minus_laplacian_phi,
        test,
    )
    local_pairing = Q(1, 8) * core.normalized_integral(
        core.multiply_polynomials(phi, test),
        4,
    )
    audit.equal(fourier_pairing, local_pairing)
    audit.equal(
        inverse_laplacian_pairing_rate_two(minus_laplacian_phi, test),
        inverse_laplacian_pairing_rate_two(test, minus_laplacian_phi),
    )
    audit.true(
        inverse_laplacian_pairing_rate_two(
            minus_laplacian_phi,
            minus_laplacian_phi,
        )
        > 0
    )


def canonical_payload(polynomials: tuple[Polynomial, ...]) -> bytes:
    records = tuple(tuple(sorted(polynomial.items())) for polynomial in polynomials)
    return repr(records).encode("ascii")


def main() -> None:
    audit = Audit()
    basis = core.modal_basis()

    # Family 1 retained as a failure: the two-mode grid has C2=2*C1, so a
    # boundary point forces the apex rather than an active codimension-one face.
    failure_audit = core.Audit()
    failed_trials = core.audit_failed_two_mode_family(failure_audit, basis)
    audit.equal(failed_trials, 576)
    audit.true(failure_audit.assertions > 0)

    # Family 2: active boundary of the cone C_m>=0 at kappa=0.
    selected = ((-1, -1), (-1, -1), (-1, 0))
    modes = tuple(
        core.oriented_mode(basis, mode, selected[mode - 1])
        for mode in (1, 2, 3)
    )
    total = core.add_vectors(*modes)
    nonlinear = core.nonlinear_advection(total)
    coefficients = tuple(
        core.modal_nonlinear_coefficient(nonlinear, mode)
        for mode in modes
    )
    audit.equal(coefficients, (Q(8, 9), Q(16, 9), Q(0)))
    audit.true(coefficients[0] > 0 and coefficients[1] > 0)
    audit.equal(coefficients[2], Q(0))
    audit.equal(core.gaussian_divergence(total), {})

    tangent_3 = core.action_generator(modes[2])
    audit.equal(core.gaussian_divergence(tangent_3), {})
    audit.equal(
        core.action_generator(core.action_generator(modes[2])),
        core.scale_vector(-9, modes[2]),
    )

    local_by_rate = local_directional_derivative_by_rate(total, tangent_3)
    audit.equal(local_by_rate.get(2, Q(0)), Q(0))
    audit.equal(local_by_rate.get(3, Q(0)), Q(0))
    # A is not solenoidal: integrating B(A,Z) by parts as if div A=0
    # spuriously gives -1035/32.  The direct componentwise differentiation is
    # the safe computation and gives -675/32; the pressure restores the
    # solenoidal direction only after its nonlocal pairing is included.
    audit.equal(local_by_rate.get(4, Q(0)), Q(-675, 32))
    local_pi_coefficient = Q(1, 8) * local_by_rate[4]
    audit.equal(local_pi_coefficient, Q(-675, 256))

    source = pressure_source(total)
    test = pressure_test(total, tangent_3)
    audit.true(source != {})
    audit.true(test != {})
    audit_fourier_normalization(audit, test)
    pressure_pi_coefficient = inverse_laplacian_pairing_rate_two(source, test)
    audit.equal(pressure_pi_coefficient, Q(575457, 320320))

    cprime_3_pi_coefficient = local_pi_coefficient + pressure_pi_coefficient
    audit.equal(cprime_3_pi_coefficient, Q(-1076547, 1281280))
    audit.true(cprime_3_pi_coefficient < 0)

    field_hash = sha256(
        canonical_payload(modes[0] + modes[1] + modes[2] + total)
    ).hexdigest()
    pressure_hash = sha256(
        canonical_payload((source, test))
    ).hexdigest()
    core_hash = sha256(CORE_PATH.read_bytes()).hexdigest()
    source_hash = sha256(SCRIPT_PATH.read_bytes()).hexdigest()

    print("dynamic_modal_cone: PASS")
    print(f"exact_assertions={audit.assertions + failure_audit.assertions}")
    print("family_1=modes_1_2_trials=576_failure_boundary_only_at_apex")
    print("family_2=selected_m1(-1,-1)_m2(-1,-1)_m3(-1,0)_kappa=0")
    print("C=(8/9,16/9,0)*(pi/3)^(3/2)")
    print("C3prime_local_rates=(rate2:0,rate3:0,rate4:-675/32)")
    print("C3prime_local=-(675/256)*pi^(3/2)")
    print("C3prime_pressure=+(575457/320320)*pi^(3/2)")
    print("C3prime_total=-(1076547/1281280)*pi^(3/2)<0")
    print("cone_exit=C3=0_and_C3prime<0_while_C1,C2>0")
    print("pressure=exact_Fourier_1_over_|xi|^2; pointwise_pressure_not_reconstructed")
    print("normalization_tests=manufactured_-Delta_phi,symmetry,positivity:PASS")
    print("residuals=divergence:0,isotype:0,Fourier_imaginary:0,identity:0")
    print(f"field_sha256={field_hash}")
    print(f"pressure_sha256={pressure_hash}")
    print(f"core_sha256={core_hash}")
    print("seed=n/a; arithmetic=Fraction; quadrature=none")
    print("scope=exact instantaneous NS vector field; no time integration / no ancient or Type-I orbit")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
