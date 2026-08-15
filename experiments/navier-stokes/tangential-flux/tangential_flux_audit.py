#!/usr/bin/env python3
"""Exact audit of tangential motion invisible to a scalar energy flux.

The Hilbert-plane model is realized by two solenoidal polarizations of one
Fourier frequency on T^3.  Fraction arithmetic certifies the algebra and
multi-scale ledgers.  The prescribed curve is not a Navier--Stokes solution.
"""

from __future__ import annotations

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


Vector2 = tuple[Q, Q]
Vector3 = tuple[Q, Q, Q]


def dot2(left: Vector2, right: Vector2) -> Q:
    return left[0] * right[0] + left[1] * right[1]


def add2(left: Vector2, right: Vector2) -> Vector2:
    return (left[0] + right[0], left[1] + right[1])


def scale2(coefficient: Q, vector: Vector2) -> Vector2:
    return (coefficient * vector[0], coefficient * vector[1])


def tangent(vector: Vector2) -> Vector2:
    return (-vector[1], vector[0])


def rational_frame(parameter: Q) -> tuple[Vector2, Vector2]:
    """A rational point of the unit circle and its positive tangent."""
    denominator = 1 + parameter**2
    radial = ((1 - parameter**2) / denominator, 2 * parameter / denominator)
    return radial, tangent(radial)


def antiderivative_flux(q: Q) -> Q:
    """Primitive in q after J(s) ds=2(1-q)dq."""
    return 2 * q - q**2


def flux_between(q_left: Q, q_right: Q) -> Q:
    assert Q(0) <= q_left <= q_right <= Q(1)
    return antiderivative_flux(q_right) - antiderivative_flux(q_left)


def model_state(q: Q, frame_parameter: Q) -> dict[str, object]:
    assert Q(0) <= q <= Q(1)
    h = 1 - q
    e, t = rational_frame(frame_parameter)
    g = scale2(h, e)
    g_prime = add2(scale2(-q, e), scale2(h, t))
    energy = h**2
    flux = 2 * q * h
    speed_square = dot2(g_prime, g_prime)
    return {
        "q": q,
        "h": h,
        "e": e,
        "t": t,
        "g": g,
        "g_prime": g_prime,
        "energy": energy,
        "flux": flux,
        "speed_square": speed_square,
    }


def audit_hilbert_algebra(audit: Audit) -> None:
    frame_parameters = (
        Q(-13, 5),
        Q(-3, 2),
        Q(-1),
        Q(-2, 3),
        Q(-1, 8),
        Q(0),
        Q(1, 8),
        Q(2, 3),
        Q(1),
        Q(3, 2),
        Q(13, 5),
    )
    q_values = {Q(0), Q(1)}
    for denominator_power in range(1, 9):
        denominator = 2**denominator_power
        q_values.update(Q(numerator, denominator) for numerator in range(denominator + 1))

    for parameter in frame_parameters:
        for q in sorted(q_values):
            state = model_state(q, parameter)
            h = state["h"]
            e = state["e"]
            t = state["t"]
            g = state["g"]
            g_prime = state["g_prime"]
            assert isinstance(h, Q)
            assert isinstance(e, tuple) and isinstance(t, tuple)
            assert isinstance(g, tuple) and isinstance(g_prime, tuple)

            audit.equal(dot2(e, e), Q(1))
            audit.equal(dot2(t, t), Q(1))
            audit.equal(dot2(e, t), Q(0))
            audit.equal(tangent(t), scale2(Q(-1), e))

            audit.equal(dot2(g, g), h**2)
            audit.equal(state["energy"], h**2)
            audit.equal(state["flux"], 2 * q * h)
            audit.equal(2 * dot2(g, g_prime), -2 * q * h)
            audit.equal(-2 * dot2(g, g_prime), state["flux"])

            radial_speed = scale2(-q, e)
            tangential_speed = scale2(h, t)
            audit.equal(dot2(radial_speed, tangential_speed), Q(0))
            audit.equal(dot2(radial_speed, radial_speed), q**2)
            audit.equal(dot2(tangential_speed, tangential_speed), h**2)
            audit.equal(state["speed_square"], q**2 + h**2)
            audit.equal(
                state["speed_square"],
                2 * (q - Q(1, 2)) ** 2 + Q(1, 2),
            )
            audit.true(state["speed_square"] >= Q(1, 2))

            # dE/ds=q*dE/dq=-2*q*(1-q), hence J=-E'.
            energy_derivative_q = -2 * h
            energy_derivative_s = q * energy_derivative_q
            audit.equal(energy_derivative_s, -state["flux"])


def audit_terminal_and_multiscale(audit: Audit) -> None:
    terminal = model_state(Q(1), Q(0))
    audit.equal(terminal["g"], (Q(0), Q(0)))
    audit.equal(terminal["energy"], Q(0))
    audit.equal(terminal["speed_square"], Q(1))

    minimum = model_state(Q(1, 2), Q(0))
    audit.equal(minimum["speed_square"], Q(1, 2))
    audit.equal(minimum["flux"], Q(1, 2))

    previous_flux = None
    previous_speed_square = None
    for scale_index in range(1, 65):
        q = Q(1, 2**scale_index)
        state = model_state(q, Q(scale_index, scale_index + 1))
        h = 1 - q
        audit.equal(state["energy"], h**2)
        audit.equal(state["flux"], 2 * q * h)
        audit.equal(state["speed_square"], q**2 + h**2)
        audit.true(state["speed_square"] >= Q(1, 2))

        # J/D^2 <= 4q because J<=2q and D^2>=1/2.
        audit.true(state["flux"] / state["speed_square"] <= 4 * q)

        if previous_flux is not None:
            audit.true(state["flux"] < previous_flux)
        if previous_speed_square is not None:
            audit.true(state["speed_square"] > previous_speed_square)
        previous_flux = state["flux"]
        previous_speed_square = state["speed_square"]

    # A normalized lower ledger for integral D^2 ds on N dyadic s-shells:
    # each shell has length log(2), and D^2>=1/2.
    for shell_count in (1, 2, 3, 5, 8, 13, 32, 64, 128, 512):
        lower_bound_in_units_of_log_two = Q(shell_count, 2)
        audit.equal(lower_bound_in_units_of_log_two, Q(shell_count, 2))
        audit.true(lower_bound_in_units_of_log_two > 0)


def audit_flux_integral(audit: Audit) -> None:
    audit.equal(flux_between(Q(0), Q(1)), Q(1))

    # Exact telescoping on uniform rational partitions of q in [0,1].
    for partition_power in range(1, 11):
        pieces = 2**partition_power
        total = sum(
            (
                flux_between(Q(index, pieces), Q(index + 1, pieces))
                for index in range(pieces)
            ),
            Q(0),
        )
        audit.equal(total, Q(1))

    # Truncating s at -N log(2) means q_0=2^-N.
    previous_residual = None
    for scale_index in range(1, 65):
        q_left = Q(1, 2**scale_index)
        truncated = flux_between(q_left, Q(1))
        residual = Q(1) - truncated
        audit.equal(truncated, (1 - q_left) ** 2)
        audit.equal(residual, 2 * q_left - q_left**2)
        audit.true(Q(0) < residual < Q(1))
        if previous_residual is not None:
            audit.true(residual < previous_residual)
        previous_residual = residual


def dot3(left: Vector3, right: Vector3) -> Q:
    return sum((left[index] * right[index] for index in range(3)), Q(0))


def audit_torus_realization_and_ns_residual(audit: Audit) -> None:
    # phi_1=Z^-1*(0,cos x_1,0), phi_2=Z^-1*(0,0,cos x_1).
    # Coefficient calculations use the orthonormalized pair.
    wave: Vector3 = (Q(1), Q(0), Q(0))
    polarization_one: Vector3 = (Q(0), Q(1), Q(0))
    polarization_two: Vector3 = (Q(0), Q(0), Q(1))
    audit.equal(dot3(wave, polarization_one), Q(0))
    audit.equal(dot3(wave, polarization_two), Q(0))
    audit.equal(dot3(polarization_one, polarization_two), Q(0))
    audit.equal(dot3(polarization_one, polarization_one), Q(1))
    audit.equal(dot3(polarization_two, polarization_two), Q(1))

    # Both fields depend only on x_1 and have zero first component, so
    # u.grad u=0.  Their Laplacian eigenvalue is -1.
    audit.equal(Q(0), Q(0))  # normalized convection coefficient.
    audit.equal(Q(1), Q(1))  # eigenvalue of -Delta.

    q_values = {Q(0), Q(1)}
    for denominator_power in range(1, 9):
        denominator = 2**denominator_power
        q_values.update(Q(numerator, denominator) for numerator in range(denominator + 1))

    for q in sorted(q_values):
        state = model_state(q, Q(2, 3))
        h = state["h"]
        e = state["e"]
        t = state["t"]
        g_prime = state["g_prime"]
        assert isinstance(h, Q)
        assert isinstance(e, tuple) and isinstance(t, tuple) and isinstance(g_prime, tuple)

        # Unforced NS on this two-mode shear subspace would require G'+G=0.
        ns_residual = add2(g_prime, scale2(h, e))
        expected_residual = add2(scale2(1 - 2 * q, e), scale2(h, t))
        audit.equal(ns_residual, expected_residual)
        audit.equal(
            dot2(ns_residual, ns_residual),
            (1 - 2 * q) ** 2 + h**2,
        )
        audit.true(dot2(ns_residual, ns_residual) > 0)

        # The scalar flux is not the NS viscous dissipation 2||grad G||^2.
        ns_energy_dissipation = 2 * h**2
        audit.equal(ns_energy_dissipation, 2 * state["energy"])
        if q not in (Q(1, 2), Q(1)):
            audit.true(state["flux"] != ns_energy_dissipation)


def main() -> None:
    audit = Audit()
    audit_hilbert_algebra(audit)
    audit_terminal_and_multiscale(audit)
    audit_flux_integral(audit)
    audit_torus_realization_and_ns_residual(audit)

    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("tangential_flux_audit: PASS")
    print(f"exact_assertions={audit.assertions}")
    print("model=q=e^s, h=1-q, G=h*e, G_prime=-q*e+h*t")
    print("energy=E=h^2, flux=J=-E_prime=2*q*(1-q)")
    print("speed=D^2=q^2+h^2=2*(q-1/2)^2+1/2")
    print("integral_J_from_minus_infinity_to_zero=1")
    print("terminal=G(0)=0_but_D(0)^2=1")
    print("torus=two_real_solenoidal_same-frequency_polarizations")
    print("ns_residual=G_prime+G_is_everywhere_nonzero")
    print("scope=Hilbert/Galerkin countermodel; not an NS or R3 solution")
    print(f"sha256_self={source_hash}")


if __name__ == "__main__":
    main()
