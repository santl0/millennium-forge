#!/usr/bin/env python3
"""Exact instantaneous SO(2)-modal sign search on polynomial-Gaussian fields.

The script uses only Fraction and symbolic polynomial dictionaries.  Gaussian
integrals are evaluated by exact moment formulas.  It evaluates an exact
instantaneous Navier--Stokes vector field, without time integration or any
ancient/Type-I orbit claim.
"""

from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path


Monomial = tuple[int, int, int]
Polynomial = dict[Monomial, Q]
PolyVector = tuple[Polynomial, Polynomial, Polynomial]
ZERO: PolyVector = ({}, {}, {})


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
        result[tuple(reduced)] = coefficient * power
    return clean(result)


def multiply_coordinate(polynomial: Polynomial, axis: int) -> Polynomial:
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        raised = list(exponent)
        raised[axis] += 1
        result[tuple(raised)] = coefficient
    return result


def gaussian_derivative(polynomial: Polynomial, axis: int) -> Polynomial:
    # Polynomial factor of partial_axis(P exp(-|y|^2)).
    return add_polynomials(
        derivative(polynomial, axis),
        scale_polynomial(-2, multiply_coordinate(polynomial, axis)),
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
    return add_polynomials(
        scale_polynomial(-1, multiply_coordinate(derivative(polynomial, 0), 1)),
        multiply_coordinate(derivative(polynomial, 1), 0),
    )


def action_generator(field: PolyVector) -> PolyVector:
    # Generator of rho(theta)U(y)=Q_theta U(Q_-theta y).
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


def vector_dot_polynomial(left: PolyVector, right: PolyVector) -> Polynomial:
    return add_polynomials(
        *(multiply_polynomials(left[index], right[index]) for index in range(3))
    )


def nonlinear_advection(field: PolyVector) -> PolyVector:
    # Polynomial factor of (Z dot nabla)Z; div Z is separately certified zero.
    return tuple(
        add_polynomials(
            *(
                multiply_polynomials(
                    field[axis],
                    gaussian_derivative(field[component], axis),
                )
                for axis in range(3)
            )
        )
        for component in range(3)
    )  # type: ignore[return-value]


def gaussian_laplacian(field: PolyVector) -> PolyVector:
    return tuple(
        add_polynomials(
            *(
                gaussian_derivative(
                    gaussian_derivative(field[component], axis),
                    axis,
                )
                for axis in range(3)
            )
        )
        for component in range(3)
    )  # type: ignore[return-value]


def similarity_generator(field: PolyVector) -> PolyVector:
    # Polynomial factor of (1+y dot nabla)(P exp(-|y|^2)).
    return tuple(
        add_polynomials(
            field[component],
            *(
                multiply_coordinate(
                    gaussian_derivative(field[component], axis),
                    axis,
                )
                for axis in range(3)
            ),
        )
        for component in range(3)
    )  # type: ignore[return-value]


def odd_double_factorial(index: int) -> int:
    if index <= 0:
        return 1
    result = 1
    for value in range(1, index + 1, 2):
        result *= value
    return result


def normalized_moment(power: int, gaussian_rate: int) -> Q:
    # Integral x^power exp(-a*x^2) dx divided by sqrt(pi/a).
    if power % 2:
        return Q(0)
    half_power = power // 2
    return Q(
        odd_double_factorial(2 * half_power - 1),
        (2 * gaussian_rate) ** half_power,
    )


def normalized_integral(polynomial: Polynomial, gaussian_rate: int) -> Q:
    # Actual R^3 integral = result * (pi/a)^(3/2).
    return sum(
        (
            coefficient
            * normalized_moment(exponent[0], gaussian_rate)
            * normalized_moment(exponent[1], gaussian_rate)
            * normalized_moment(exponent[2], gaussian_rate)
            for exponent, coefficient in polynomial.items()
        ),
        Q(0),
    )


def normalized_inner_product(
    left: PolyVector,
    right: PolyVector,
    gaussian_rate: int,
) -> Q:
    return normalized_integral(
        vector_dot_polynomial(left, right),
        gaussian_rate,
    )


def harmonic_polynomials() -> dict[str, Polynomial]:
    x_value = monomial((1, 0, 0))
    y_value = monomial((0, 1, 0))
    x_square = multiply_polynomials(x_value, x_value)
    y_square = multiply_polynomials(y_value, y_value)
    return {
        "1c": x_value,
        "1s": y_value,
        "2c": add_polynomials(x_square, scale_polynomial(-1, y_square)),
        "2s": scale_polynomial(2, multiply_polynomials(x_value, y_value)),
        "3c": add_polynomials(
            multiply_polynomials(x_square, x_value),
            scale_polynomial(
                -3,
                multiply_polynomials(x_value, y_square),
            ),
        ),
        "3s": add_polynomials(
            scale_polynomial(
                3,
                multiply_polynomials(x_square, y_value),
            ),
            scale_polynomial(
                -1,
                multiply_polynomials(y_square, y_value),
            ),
        ),
    }


def modal_basis() -> dict[str, PolyVector]:
    return {
        name: gaussian_curl(({}, {}, harmonic))
        for name, harmonic in harmonic_polynomials().items()
    }


def oriented_mode(
    basis: dict[str, PolyVector],
    mode: int,
    coefficients: tuple[int, int],
) -> PolyVector:
    return add_vectors(
        scale_vector(coefficients[0], basis[f"{mode}c"]),
        scale_vector(coefficients[1], basis[f"{mode}s"]),
    )


def modal_nonlinear_coefficient(
    nonlinear: PolyVector,
    mode_field: PolyVector,
) -> Q:
    # Coefficient of -<(Z dot nabla)Z, R Z_m>; common factor (pi/3)^(3/2).
    tangent = action_generator(mode_field)
    return -normalized_inner_product(nonlinear, tangent, 3)


def audit_isotypes_and_pressure_gate(
    audit: Audit,
    basis: dict[str, PolyVector],
) -> None:
    # These checks precede every removal of the Leray projection: all basis
    # modes and their rotational tangents are exactly solenoidal.
    for mode in (1, 2, 3):
        for orientation in ("c", "s"):
            field = basis[f"{mode}{orientation}"]
            tangent = action_generator(field)
            audit.equal(gaussian_divergence(field), {})
            audit.equal(gaussian_divergence(tangent), {})
            audit.equal(
                action_generator(action_generator(field)),
                scale_vector(-(mode**2), field),
            )


def audit_failed_two_mode_family(
    audit: Audit,
    basis: dict[str, PolyVector],
) -> int:
    # Family 1: all nonzero real orientations with coefficients in [-2,2]
    # for the axial-potential modes m=1 and m=2.
    choices = tuple(
        pair
        for pair in product(range(-2, 3), repeat=2)
        if pair != (0, 0)
    )
    trials = 0
    for coefficients_1 in choices:
        mode_1 = oriented_mode(basis, 1, coefficients_1)
        for coefficients_2 in choices:
            mode_2 = oriented_mode(basis, 2, coefficients_2)
            nonlinear = nonlinear_advection(add_vectors(mode_1, mode_2))
            coefficient_1 = modal_nonlinear_coefficient(nonlinear, mode_1)
            coefficient_2 = modal_nonlinear_coefficient(nonlinear, mode_2)
            audit.equal(coefficient_2, 2 * coefficient_1)
            audit.true(not (coefficient_1 * coefficient_2 < 0))
            trials += 1
    audit.equal(trials, 576)
    return trials


def find_three_mode_sign_split(
    audit: Audit,
    basis: dict[str, PolyVector],
) -> tuple[
    tuple[tuple[int, int], tuple[int, int], tuple[int, int]],
    tuple[PolyVector, PolyVector, PolyVector],
    tuple[Q, Q, Q],
    int,
]:
    # Family 2: deterministic scan of nonzero orientations in [-1,1].
    choices = tuple(
        pair
        for pair in product(range(-1, 2), repeat=2)
        if pair != (0, 0)
    )
    trials = 0
    for coefficients_1 in choices:
        mode_1 = oriented_mode(basis, 1, coefficients_1)
        for coefficients_2 in choices:
            mode_2 = oriented_mode(basis, 2, coefficients_2)
            for coefficients_3 in choices:
                mode_3 = oriented_mode(basis, 3, coefficients_3)
                modes = (mode_1, mode_2, mode_3)
                nonlinear = nonlinear_advection(add_vectors(*modes))
                coefficients = tuple(
                    modal_nonlinear_coefficient(nonlinear, mode)
                    for mode in modes
                )
                trials += 1
                if min(coefficients) < 0 < max(coefficients):
                    selected = (coefficients_1, coefficients_2, coefficients_3)
                    audit.equal(
                        selected,
                        ((-1, -1), (-1, -1), (-1, 1)),
                    )
                    audit.equal(coefficients, (Q(-8, 9), Q(16, 9), Q(-16, 3)))
                    audit.equal(trials, 3)
                    return selected, modes, coefficients, trials
    raise AssertionError("three-mode search found no sign split")


def audit_selected_field(
    audit: Audit,
    modes: tuple[PolyVector, PolyVector, PolyVector],
    nonlinear_coefficients: tuple[Q, Q, Q],
) -> tuple[tuple[Q, Q, Q], tuple[Q, Q, Q]]:
    total = add_vectors(*modes)
    audit.equal(gaussian_divergence(total), {})

    tangents = tuple(action_generator(mode) for mode in modes)
    grams = tuple(
        normalized_inner_product(tangent, tangent, 2)
        for tangent in tangents
    )
    audit.true(all(gram > 0 for gram in grams))

    # Orthogonality of distinct isotypes, checked directly in L2.
    for left_index in range(3):
        for right_index in range(3):
            if left_index == right_index:
                continue
            audit.equal(
                normalized_inner_product(
                    modes[left_index],
                    tangents[right_index],
                    2,
                ),
                Q(0),
            )

    laplacian = gaussian_laplacian(total)
    similarity = similarity_generator(total)
    diffusion_coefficients = tuple(
        normalized_inner_product(laplacian, tangent, 2)
        for tangent in tangents
    )
    similarity_coefficients = tuple(
        normalized_inner_product(similarity, tangent, 2)
        for tangent in tangents
    )
    audit.equal(diffusion_coefficients, (Q(0), Q(0), Q(0)))
    audit.equal(similarity_coefficients, (Q(0), Q(0), Q(0)))

    # Since each tangent is solenoidal, <P F,tangent>=<F,tangent>.
    # The full coefficient is therefore independent of kappa here.
    for kappa in (Q(-3), Q(-1), Q(0), Q(2), Q(5, 7)):
        full_coefficients = tuple(
            diffusion_coefficients[index]
            + nonlinear_coefficients[index]
            - kappa * similarity_coefficients[index]
            for index in range(3)
        )
        audit.equal(full_coefficients, nonlinear_coefficients)

    return grams, diffusion_coefficients


def audit_drift_sign_family(
    audit: Audit,
) -> tuple[
    tuple[PolyVector, PolyVector],
    tuple[Q, Q],
    tuple[Q, Q],
    tuple[Q, Q],
]:
    # Family 3, supplied as an independent adverse drift test:
    # Re[(x+iy)^m (1+i*a*|y|^2)] with (m,a)=(1,+1),(3,-1).
    harmonics = harmonic_polynomials()
    x_value = harmonics["1c"]
    y_value = harmonics["1s"]
    z_value = monomial((0, 0, 1))
    radius_square = add_polynomials(
        multiply_polynomials(x_value, x_value),
        multiply_polynomials(y_value, y_value),
        multiply_polynomials(z_value, z_value),
    )
    potential_1 = add_polynomials(
        harmonics["1c"],
        scale_polynomial(
            -1,
            multiply_polynomials(radius_square, harmonics["1s"]),
        ),
    )
    potential_3 = add_polynomials(
        harmonics["3c"],
        multiply_polynomials(radius_square, harmonics["3s"]),
    )
    mode_1 = gaussian_curl(({}, {}, potential_1))
    mode_3 = gaussian_curl(({}, {}, potential_3))
    modes = (mode_1, mode_3)

    for mode_number, mode in ((1, mode_1), (3, mode_3)):
        tangent = action_generator(mode)
        audit.equal(gaussian_divergence(mode), {})
        audit.equal(gaussian_divergence(tangent), {})
        audit.equal(
            action_generator(action_generator(mode)),
            scale_vector(-(mode_number**2), mode),
        )

    total = add_vectors(*modes)
    tangents = tuple(action_generator(mode) for mode in modes)
    nonlinear = nonlinear_advection(total)
    laplacian = gaussian_laplacian(total)
    similarity = similarity_generator(total)

    grams = tuple(
        normalized_inner_product(tangent, tangent, 2)
        for tangent in tangents
    )
    diffusion = tuple(
        normalized_inner_product(laplacian, tangent, 2)
        for tangent in tangents
    )
    convection = tuple(
        modal_nonlinear_coefficient(nonlinear, mode)
        for mode in modes
    )
    drift = tuple(
        normalized_inner_product(similarity, tangent, 2)
        for tangent in tangents
    )
    full_kappa_one = tuple(
        diffusion[index] + convection[index] - drift[index]
        for index in range(2)
    )

    audit.equal(grams, (Q(39, 16), Q(2349, 16)))
    audit.equal(diffusion, (Q(0), Q(0)))
    audit.equal(convection, (Q(0), Q(0)))
    audit.equal(drift, (Q(-7, 2), Q(99, 2)))
    audit.equal(full_kappa_one, (Q(7, 2), Q(-99, 2)))
    audit.true(full_kappa_one[0] > 0 > full_kappa_one[1])

    return modes, grams, drift, full_kappa_one


def canonical_payload(polynomials: tuple[Polynomial, ...]) -> bytes:
    records = tuple(tuple(sorted(polynomial.items())) for polynomial in polynomials)
    return repr(records).encode("ascii")


def main() -> None:
    audit = Audit()
    basis = modal_basis()
    audit_isotypes_and_pressure_gate(audit, basis)
    failed_trials = audit_failed_two_mode_family(audit, basis)
    selected, modes, coefficients, successful_trials = find_three_mode_sign_split(
        audit,
        basis,
    )
    grams, diffusion_coefficients = audit_selected_field(audit, modes, coefficients)
    drift_modes, drift_grams, drift_coefficients, drift_full = audit_drift_sign_family(
        audit,
    )

    total = add_vectors(*modes)
    nonlinear = nonlinear_advection(total)
    field_hash = sha256(
        canonical_payload(
            modes[0]
            + modes[1]
            + modes[2]
            + total
            + nonlinear
        )
    ).hexdigest()
    search_payload = (
        failed_trials,
        successful_trials,
        selected,
        coefficients,
        grams,
        diffusion_coefficients,
    )
    search_hash = sha256(repr(search_payload).encode("ascii")).hexdigest()
    drift_field_hash = sha256(
        canonical_payload(
            drift_modes[0]
            + drift_modes[1]
            + add_vectors(*drift_modes)
        )
    ).hexdigest()
    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()

    print("instantaneous_modal_sign: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("family_1=modes_1_2_trials=576_failure_C2=2*C1")
    print("family_2=modes_1_2_3_success_at_trial=3")
    print("selected_coefficients=m1(-1,-1)_m2(-1,-1)_m3(-1,1)")
    print("C1=-(8/9)*(pi/3)^(3/2)")
    print("C2=+(16/9)*(pi/3)^(3/2)")
    print("C3=-(16/3)*(pi/3)^(3/2)")
    print("Gram(RZ1,RZ2,RZ3)=(2,12,54)*(pi/2)^(3/2)")
    print("family_3=modes_1_3_drift_sign_split_at_kappa=1")
    print("family_3_Gram=(39/16,2349/16)*(pi/2)^(3/2)")
    print("family_3_diffusion=(0,0); convection=(0,0)")
    print("family_3_drift=(-7/2,+99/2)*(pi/2)^(3/2)")
    print("family_3_C_kappa1=(+7/2,-99/2)*(pi/2)^(3/2)")
    print("pressure_pairing=0_by_exact_solenoidal_tangents")
    print("family_2_diffusion_pairings=0; similarity_pairings=0; kappa=arbitrary")
    print("residuals=divergence:0,isotype:0,reported_pairing_identities:0")
    print(f"field_sha256={field_hash}")
    print(f"search_sha256={search_hash}")
    print(f"drift_field_sha256={drift_field_hash}")
    print("seed=n/a; arithmetic=Fraction; quadrature=none")
    print("scope=exact instantaneous NS vector field; no time integration / no ancient or Type-I orbit")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
