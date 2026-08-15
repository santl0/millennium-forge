#!/usr/bin/env python3
"""Exact Fourier-triad audit on the three-dimensional torus.

All coefficients are Gaussian rationals.  The script checks reality,
incompressibility, Leray projection, signed triad-energy exchange, frequency
scaling, and a viscous-time ledger.  It does not construct an ancient
solution on R^3 or a Navier--Stokes singularity.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, left: object, right: object) -> None:
        self.assertions += 1
        assert left == right, (left, right)

    def true(self, statement: bool) -> None:
        self.assertions += 1
        assert statement


@dataclass(frozen=True)
class GQ:
    """Gaussian rational r+i*s."""

    real: Q = Q(0)
    imag: Q = Q(0)

    def __add__(self, other: "GQ") -> "GQ":
        return GQ(self.real + other.real, self.imag + other.imag)

    def __neg__(self) -> "GQ":
        return GQ(-self.real, -self.imag)

    def __sub__(self, other: "GQ") -> "GQ":
        return self + (-other)

    def __mul__(self, other: "GQ") -> "GQ":
        return GQ(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def conjugate(self) -> "GQ":
        return GQ(self.real, -self.imag)


ZERO = GQ()
ONE = GQ(Q(1))
I = GQ(Q(0), Q(1))
MINUS_I = GQ(Q(0), Q(-1))

Wave = tuple[int, int, int]
Vector = tuple[GQ, GQ, GQ]


def scalar(value: int | Q) -> GQ:
    return GQ(Q(value))


def real_vector(values: tuple[int | Q, int | Q, int | Q]) -> Vector:
    return tuple(scalar(value) for value in values)  # type: ignore[return-value]


def vector_add(left: Vector, right: Vector) -> Vector:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def vector_scale(coefficient: GQ, vector: Vector) -> Vector:
    return tuple(coefficient * component for component in vector)  # type: ignore[return-value]


def vector_conjugate(vector: Vector) -> Vector:
    return tuple(component.conjugate() for component in vector)  # type: ignore[return-value]


def dot_wave(vector: Vector, wave: Wave) -> GQ:
    result = ZERO
    for component, frequency in zip(vector, wave):
        result = result + component * scalar(frequency)
    return result


def hermitian_dot(left: Vector, right: Vector) -> GQ:
    result = ZERO
    for left_component, right_component in zip(left, right):
        result = result + left_component.conjugate() * right_component
    return result


def wave_add(left: Wave, right: Wave) -> Wave:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def wave_negate(wave: Wave) -> Wave:
    return tuple(-component for component in wave)  # type: ignore[return-value]


def wave_norm_square(wave: Wave) -> int:
    return sum(component * component for component in wave)


def leray(wave: Wave, vector: Vector) -> Vector:
    norm_square = wave_norm_square(wave)
    assert norm_square > 0
    longitudinal = dot_wave(vector, wave)
    correction = tuple(
        longitudinal * scalar(Q(component, norm_square)) for component in wave
    )
    return tuple(vector[index] - correction[index] for index in range(3))  # type: ignore[return-value]


def ordered_pair_force(
    receiving: Wave,
    first_wave: Wave,
    first_coefficient: Vector,
    second_wave: Wave,
    second_coefficient: Vector,
) -> Vector:
    assert wave_add(first_wave, second_wave) == receiving
    first_order = vector_scale(
        dot_wave(first_coefficient, second_wave), second_coefficient
    )
    second_order = vector_scale(
        dot_wave(second_coefficient, first_wave), first_coefficient
    )
    return leray(receiving, vector_add(first_order, second_order))


def nonlinear_derivative(force: Vector) -> Vector:
    return vector_scale(MINUS_I, force)


def pair_energy_transfer(receiving_coefficient: Vector, derivative: Vector) -> Q:
    """Energy derivative of the conjugate pair +/- receiving wave."""
    single_mode = hermitian_dot(receiving_coefficient, derivative)
    return 2 * single_mode.real


def triad_data(
    frequency_ratio: int,
    common_scale: int,
    amplitude_a: Q,
    amplitude_b: Q,
    amplitude_c: Q,
) -> dict[str, object]:
    n = frequency_ratio
    scale = common_scale
    k: Wave = (scale * n, 0, 0)
    ell: Wave = (-scale * n, 0, scale)
    q: Wave = (0, 0, scale)

    a = real_vector((0, 0, 1))
    b = real_vector((0, 1, 0))
    c = b

    u_k = vector_scale(scalar(amplitude_a), a)
    u_ell = vector_scale(scalar(amplitude_b), b)
    u_q = vector_scale(I * scalar(amplitude_c), c)

    force_q = ordered_pair_force(q, k, u_k, ell, u_ell)
    derivative_q = nonlinear_derivative(force_q)

    minus_k = wave_negate(k)
    minus_ell = wave_negate(ell)
    u_minus_k = vector_conjugate(u_k)
    u_minus_ell = vector_conjugate(u_ell)

    force_k = ordered_pair_force(k, q, u_q, minus_ell, u_minus_ell)
    force_ell = ordered_pair_force(ell, q, u_q, minus_k, u_minus_k)
    derivative_k = nonlinear_derivative(force_k)
    derivative_ell = nonlinear_derivative(force_ell)

    return {
        "k": k,
        "ell": ell,
        "q": q,
        "a": a,
        "b": b,
        "c": c,
        "u_k": u_k,
        "u_ell": u_ell,
        "u_q": u_q,
        "force_q": force_q,
        "transfer_q": pair_energy_transfer(u_q, derivative_q),
        "transfer_k": pair_energy_transfer(u_k, derivative_k),
        "transfer_ell": pair_energy_transfer(u_ell, derivative_ell),
    }


def audit_reality_divergence_projection(audit: Audit) -> None:
    for n in (2, 3, 5, 8, 13, 32, 128):
        for scale in (1, 2, 3, 5):
            data = triad_data(n, scale, Q(2, 3), Q(3, 5), Q(5, 7))
            k = data["k"]
            ell = data["ell"]
            q = data["q"]
            u_k = data["u_k"]
            u_ell = data["u_ell"]
            u_q = data["u_q"]
            assert isinstance(k, tuple) and isinstance(ell, tuple) and isinstance(q, tuple)
            assert isinstance(u_k, tuple) and isinstance(u_ell, tuple) and isinstance(u_q, tuple)

            audit.equal(wave_add(k, ell), q)
            audit.equal(dot_wave(u_k, k), ZERO)
            audit.equal(dot_wave(u_ell, ell), ZERO)
            audit.equal(dot_wave(u_q, q), ZERO)

            # Fourier reality: coefficient(-m)=conjugate(coefficient(m)).
            audit.equal(vector_conjugate(u_k), u_k)
            audit.equal(vector_conjugate(u_ell), u_ell)
            audit.equal(vector_conjugate(u_q), vector_scale(GQ(Q(-1)), u_q))

            force_q = data["force_q"]
            assert isinstance(force_q, tuple)
            expected_force = real_vector((0, Q(2, 3) * Q(3, 5) * scale, 0))
            audit.equal(force_q, expected_force)
            audit.equal(leray(q, force_q), force_q)
            audit.equal(dot_wave(force_q, q), ZERO)


def audit_signed_energy_exchange(audit: Audit) -> None:
    amplitudes = (
        (Q(1), Q(1), Q(1)),
        (Q(-1), Q(1), Q(1)),
        (Q(1), Q(-1), Q(1)),
        (Q(1), Q(1), Q(-1)),
        (Q(2, 3), Q(3, 5), Q(5, 7)),
        (Q(-2, 3), Q(3, 5), Q(-5, 7)),
    )
    for n in (2, 3, 5, 8, 13, 32, 128):
        for scale in (1, 2, 3, 5):
            for amplitude_a, amplitude_b, amplitude_c in amplitudes:
                data = triad_data(
                    n,
                    scale,
                    amplitude_a,
                    amplitude_b,
                    amplitude_c,
                )
                expected = 2 * amplitude_a * amplitude_b * amplitude_c * scale
                audit.equal(data["transfer_q"], -expected)
                audit.equal(data["transfer_k"], Q(0))
                audit.equal(data["transfer_ell"], expected)
                audit.equal(
                    data["transfer_q"]
                    + data["transfer_k"]
                    + data["transfer_ell"],
                    Q(0),
                )

    # Changing only the receiving phase C reverses signed energy transfer but
    # leaves the high-high output force unchanged.
    positive = triad_data(32, 1, Q(1), Q(1), Q(1))
    negative = triad_data(32, 1, Q(1), Q(1), Q(-1))
    audit.equal(positive["force_q"], negative["force_q"])
    audit.equal(positive["transfer_q"], -negative["transfer_q"])


def audit_zero_and_sign_outputs(audit: Audit) -> None:
    for n in (2, 3, 5, 8, 13, 32, 128):
        k: Wave = (n, 0, 0)
        ell: Wave = (-n, 0, 1)
        q: Wave = (0, 0, 1)
        e_two = real_vector((0, 1, 0))
        e_three = real_vector((0, 0, 1))

        positive = ordered_pair_force(q, k, e_three, ell, e_two)
        negative = ordered_pair_force(
            q, k, vector_scale(GQ(Q(-1)), e_three), ell, e_two
        )
        zero = ordered_pair_force(q, k, e_two, ell, e_two)
        audit.equal(positive, e_two)
        audit.equal(negative, vector_scale(GQ(Q(-1)), e_two))
        audit.equal(zero, real_vector((0, 0, 0)))


def audit_frequency_scaling_and_limits(audit: Audit) -> None:
    previous_ratio = None
    previous_viscous_window = None
    for n in (2, 3, 5, 8, 13, 32, 128, 512):
        data = triad_data(n, 1, Q(1), Q(1), Q(1))
        k = data["k"]
        ell = data["ell"]
        q = data["q"]
        assert isinstance(k, tuple) and isinstance(ell, tuple) and isinstance(q, tuple)
        audit.equal(wave_norm_square(q), 1)
        audit.equal(wave_norm_square(k), n**2)
        audit.equal(wave_norm_square(ell), n**2 + 1)

        squared_scale_ratio = Q(wave_norm_square(q), wave_norm_square(k))
        audit.equal(squared_scale_ratio, Q(1, n**2))
        if previous_ratio is not None:
            audit.true(squared_scale_ratio < previous_ratio)
        previous_ratio = squared_scale_ratio

        # The projected output and instantaneous signed transfer stay fixed.
        audit.equal(data["force_q"], real_vector((0, 1, 0)))
        audit.equal(data["transfer_q"], Q(-2))

        # With viscosity one, the high-frequency time ledger is n^-2.  The
        # product of the fixed instantaneous transfer and this window tends
        # to zero; this is a limitation, not a nonlinear evolution theorem.
        viscous_window_transfer = Q(2, n**2)
        if previous_viscous_window is not None:
            audit.true(viscous_window_transfer < previous_viscous_window)
        previous_viscous_window = viscous_window_transfer

    # Scaling every wavevector by M multiplies the one-derivative output and
    # all nonlinear triad transfers by M.
    for scale in (1, 2, 3, 5, 8, 13, 32):
        data = triad_data(13, scale, Q(1), Q(1), Q(1))
        audit.equal(data["force_q"], real_vector((0, scale, 0)))
        audit.equal(data["transfer_q"], Q(-2 * scale))
        audit.equal(data["transfer_ell"], Q(2 * scale))


def main() -> None:
    audit = Audit()
    audit_reality_divergence_projection(audit)
    audit_signed_energy_exchange(audit)
    audit_zero_and_sign_outputs(audit)
    audit_frequency_scaling_and_limits(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("infrared_triad_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("triad=k:(N,0,0), ell:(-N,0,1), q:(0,0,1)")
    print("polarizations=a:e3, b:e2, projected_low_output=e2")
    print("energy_transfer=(T_q,T_k,T_ell)=(-2ABC,0,+2ABC)")
    print("sign=receiving_phase_or_high_amplitude_reverses_transfer")
    print("coercivity=unit_divergence_free_polarizations_can_also_give_zero_output")
    print("scaling=|q|^2/|k|^2=N^-2 while output_is_N-independent")
    print("limitation=viscous_unit-amplitude_window_ledger_is_2*N^-2")
    print("scope=instantaneous triad algebra on T3; no ancient R3 solution")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
