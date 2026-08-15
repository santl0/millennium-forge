#!/usr/bin/env python3
"""Exact polynomial-Gaussian Haar/Reynolds transfer certificate on R^3.

All polynomial coefficients and normalized Gaussian moments use Fraction.
The common positive factor (pi/3)^(3/2) is kept symbolic.  This is an exact
finite algebra certificate, not a Navier--Stokes PDE solution.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path


Monomial = tuple[int, int, int]
Polynomial = dict[Monomial, Q]
PolyVector = tuple[Polynomial, Polynomial, Polynomial]
ZERO_EXPONENT: Monomial = (0, 0, 0)


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, left: object, right: object) -> None:
        self.assertions += 1
        assert left == right, (left, right)

    def true(self, statement: bool) -> None:
        self.assertions += 1
        assert statement


def clean(polynomial: Polynomial) -> Polynomial:
    return {exponent: coefficient for exponent, coefficient in polynomial.items() if coefficient}


def constant(value: int | Q) -> Polynomial:
    coefficient = Q(value)
    return {} if coefficient == 0 else {ZERO_EXPONENT: coefficient}


def monomial(exponent: Monomial, coefficient: int | Q = 1) -> Polynomial:
    value = Q(coefficient)
    return {} if value == 0 else {exponent: value}


def add_polynomials(*polynomials: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, Q(0)) + coefficient
    return clean(result)


def scale_polynomial(coefficient: int | Q, polynomial: Polynomial) -> Polynomial:
    scalar = Q(coefficient)
    return clean({exponent: scalar * value for exponent, value in polynomial.items()})


def multiply_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = tuple(
                left_exponent[axis] + right_exponent[axis]
                for axis in range(3)
            )
            result[exponent] = (
                result.get(exponent, Q(0))
                + left_coefficient * right_coefficient
            )
    return clean(result)


def derivative(polynomial: Polynomial, axis: int) -> Polynomial:
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        if exponent[axis] == 0:
            continue
        reduced = list(exponent)
        power = reduced[axis]
        reduced[axis] -= 1
        reduced_exponent = tuple(reduced)
        result[reduced_exponent] = coefficient * power
    return clean(result)


def multiply_coordinate(polynomial: Polynomial, axis: int) -> Polynomial:
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        raised = list(exponent)
        raised[axis] += 1
        result[tuple(raised)] = coefficient
    return result


def gaussian_derivative(polynomial: Polynomial, axis: int) -> Polynomial:
    # Polynomial factor of d_axis(P exp(-|x|^2)).
    return add_polynomials(
        derivative(polynomial, axis),
        scale_polynomial(-2, multiply_coordinate(polynomial, axis)),
    )


def gaussian_curl(potential: PolyVector) -> PolyVector:
    return (
        add_polynomials(
            gaussian_derivative(potential[2], 1),
            scale_polynomial(-1, gaussian_derivative(potential[1], 2)),
        ),
        add_polynomials(
            gaussian_derivative(potential[0], 2),
            scale_polynomial(-1, gaussian_derivative(potential[2], 0)),
        ),
        add_polynomials(
            gaussian_derivative(potential[1], 0),
            scale_polynomial(-1, gaussian_derivative(potential[0], 1)),
        ),
    )


def gaussian_divergence(field: PolyVector) -> Polynomial:
    return add_polynomials(
        gaussian_derivative(field[0], 0),
        gaussian_derivative(field[1], 1),
        gaussian_derivative(field[2], 2),
    )


def orbital_derivative(polynomial: Polynomial) -> Polynomial:
    # (-y d_x + x d_y)P, the spatial rotation generator.
    return add_polynomials(
        scale_polynomial(-1, multiply_coordinate(derivative(polynomial, 0), 1)),
        multiply_coordinate(derivative(polynomial, 1), 0),
    )


def field_action_generator(field: PolyVector) -> PolyVector:
    # Generator of rho(theta)U(x)=Q_theta U(Q_-theta x).
    component_rotation: PolyVector = (
        scale_polynomial(-1, field[1]),
        field[0],
        {},
    )
    return tuple(
        add_polynomials(
            component_rotation[index],
            scale_polynomial(-1, orbital_derivative(field[index])),
        )
        for index in range(3)
    )  # type: ignore[return-value]


def substitute_inverse_quarter(polynomial: Polynomial, quarter: int) -> Polynomial:
    phase = quarter % 4
    result: Polynomial = {}
    for (x_power, y_power, z_power), coefficient in polynomial.items():
        if phase == 0:
            exponent = (x_power, y_power, z_power)
            sign = 1
        elif phase == 1:
            exponent = (y_power, x_power, z_power)
            sign = (-1) ** y_power
        elif phase == 2:
            exponent = (x_power, y_power, z_power)
            sign = (-1) ** (x_power + y_power)
        else:
            exponent = (y_power, x_power, z_power)
            sign = (-1) ** x_power
        result[exponent] = result.get(exponent, Q(0)) + sign * coefficient
    return clean(result)


def quarter_field_action(field: PolyVector, quarter: int) -> PolyVector:
    phase = quarter % 4
    substituted = tuple(substitute_inverse_quarter(component, phase) for component in field)
    if phase == 0:
        return substituted  # type: ignore[return-value]
    if phase == 1:
        return (
            scale_polynomial(-1, substituted[1]),
            substituted[0],
            substituted[2],
        )
    if phase == 2:
        return (
            scale_polynomial(-1, substituted[0]),
            scale_polynomial(-1, substituted[1]),
            substituted[2],
        )
    return (
        substituted[1],
        scale_polynomial(-1, substituted[0]),
        substituted[2],
    )


def add_vectors(*vectors: PolyVector) -> PolyVector:
    return tuple(
        add_polynomials(*(vector[index] for vector in vectors))
        for index in range(3)
    )  # type: ignore[return-value]


def scale_vector(coefficient: int | Q, vector: PolyVector) -> PolyVector:
    return tuple(
        scale_polynomial(coefficient, component) for component in vector
    )  # type: ignore[return-value]


def reynolds_transfer_polynomial(w_field: PolyVector, v_field: PolyVector) -> Polynomial:
    result: Polynomial = {}
    for component in range(3):
        for derivative_axis in range(3):
            term = multiply_polynomials(
                multiply_polynomials(w_field[component], w_field[derivative_axis]),
                gaussian_derivative(v_field[component], derivative_axis),
            )
            result = add_polynomials(result, term)
    return result


def odd_double_factorial(index: int) -> int:
    if index <= 0:
        return 1
    result = 1
    for value in range(1, index + 1, 2):
        result *= value
    return result


def normalized_gaussian_moment(power: int, gaussian_rate: int) -> Q:
    # Integral x^power exp(-a x^2) dx divided by sqrt(pi/a).
    if power % 2:
        return Q(0)
    half_power = power // 2
    return Q(odd_double_factorial(2 * half_power - 1), (2 * gaussian_rate) ** half_power)


def normalized_gaussian_integral(polynomial: Polynomial, gaussian_rate: int) -> Q:
    # The actual R^3 integral is this rational times (pi/a)^(3/2).
    return sum(
        (
            coefficient
            * normalized_gaussian_moment(exponent[0], gaussian_rate)
            * normalized_gaussian_moment(exponent[1], gaussian_rate)
            * normalized_gaussian_moment(exponent[2], gaussian_rate)
            for exponent, coefficient in polynomial.items()
        ),
        Q(0),
    )


def canonical_polynomial_payload(polynomials: tuple[Polynomial, ...]) -> bytes:
    records = tuple(tuple(sorted(polynomial.items())) for polynomial in polynomials)
    return repr(records).encode("ascii")


def main() -> None:
    audit = Audit()

    # A_V=z(-y,x,0) exp(-|x|^2), invariant under rotations around e3.
    v_potential: PolyVector = (
        monomial((0, 1, 1), -1),
        monomial((1, 0, 1), 1),
        {},
    )
    # A_W=x e3 exp(-|x|^2), a real azimuthal mode m=1.
    w_potential: PolyVector = ({}, {}, monomial((1, 0, 0), 1))

    v_field = gaussian_curl(v_potential)
    w_field = gaussian_curl(w_potential)
    expected_v: PolyVector = (
        add_polynomials(monomial((1, 0, 0), -1), monomial((1, 0, 2), 2)),
        add_polynomials(monomial((0, 1, 0), -1), monomial((0, 1, 2), 2)),
        add_polynomials(
            monomial((0, 0, 1), 2),
            monomial((2, 0, 1), -2),
            monomial((0, 2, 1), -2),
        ),
    )
    expected_w: PolyVector = (
        monomial((1, 1, 0), -2),
        add_polynomials(monomial((2, 0, 0), 2), constant(-1)),
        {},
    )
    audit.equal(v_field, expected_v)
    audit.equal(w_field, expected_w)
    audit.equal(gaussian_divergence(v_field), {})
    audit.equal(gaussian_divergence(w_field), {})

    # Full infinitesimal SO(2) certificate: V is invariant.  W belongs to a
    # two-dimensional m=1 representation because A^2 W=-W, so Haar(W)=0.
    v_generator = field_action_generator(v_field)
    w_generator = field_action_generator(w_field)
    audit.equal(v_generator, ({}, {}, {}))
    audit.equal(field_action_generator(w_generator), scale_vector(-1, w_field))
    audit.true(w_field != ({}, {}, {}))
    audit.true(w_generator != ({}, {}, {}))

    rotated_v = tuple(quarter_field_action(v_field, quarter) for quarter in range(4))
    rotated_w = tuple(quarter_field_action(w_field, quarter) for quarter in range(4))
    for rotated in rotated_v:
        audit.equal(rotated, v_field)
    audit.equal(add_vectors(*rotated_w), ({}, {}, {}))

    transfer_polynomial = reynolds_transfer_polynomial(w_field, v_field)
    expected_transfer: Polynomial = {
        (0, 0, 0): Q(-1),
        (0, 0, 2): Q(2),
        (0, 2, 0): Q(2),
        (0, 2, 2): Q(-4),
        (2, 0, 0): Q(4),
        (2, 0, 2): Q(-8),
        (2, 2, 0): Q(-4),
        (2, 2, 2): Q(8),
        (4, 0, 0): Q(-4),
        (4, 0, 2): Q(8),
    }
    audit.equal(transfer_polynomial, expected_transfer)
    audit.equal(len(transfer_polynomial), 10)

    normalized_transfer = normalized_gaussian_integral(transfer_polynomial, 3)
    audit.equal(normalized_transfer, Q(-8, 27))
    audit.true(normalized_transfer != 0)

    negative_v = scale_vector(-1, v_field)
    negative_transfer_polynomial = reynolds_transfer_polynomial(w_field, negative_v)
    audit.equal(negative_transfer_polynomial, scale_polynomial(-1, transfer_polynomial))
    normalized_negative_transfer = normalized_gaussian_integral(
        negative_transfer_polynomial,
        3,
    )
    audit.equal(normalized_negative_transfer, Q(8, 27))
    audit.equal(normalized_negative_transfer, -normalized_transfer)

    field_hash = sha256(
        canonical_polynomial_payload(
            v_potential
            + w_potential
            + v_field
            + w_field
            + (transfer_polynomial,)
        )
    ).hexdigest()
    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("haar_reynolds_transfer: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("regularity=polynomial_times_exp(-|x|^2)_is_Schwartz")
    print("divergence=div(V)=div(W)=0_exact")
    print("symmetry=SO2_generator(V)=0_and_generator^2(W)=-W")
    print("haar=Haar(W)=0")
    print("transfer=T=-(8/27)*(pi/3)^(3/2)_nonzero")
    print("sign_flip=T(-V,W)=-T(V,W)")
    print(f"field_sha256={field_hash}")
    print("seed=n/a; arithmetic=Fraction; no Navier-Stokes PDE claim")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
