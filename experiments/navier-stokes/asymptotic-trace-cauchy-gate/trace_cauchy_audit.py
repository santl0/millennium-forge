"""Audit exact: trace asymptotique versus donnée de Cauchy à temps fini.

Le modèle principal est l'équation logistique instable

    b'(tau) = a b(tau) - b(tau)^2,  a > 0.

Elle possède un continuum de trajectoires b_A qui tendent toutes vers zéro
quand tau tend vers -infini, mais leurs états à tout temps fini sont distincts.
Le paramètre q=exp(a*tau) est gardé algébrique et évalué avec Fraction.

Le contrôle adverse x'=2 sqrt(x) n'est pas localement lipschitzien en zéro et
admet des solutions retardées distinctes depuis la même donnée finie. Le script
ne simule pas Navier--Stokes; il certifie les identités du contre-modèle qui
sépare les deux quantificateurs de données initiales.
"""

from __future__ import annotations

import json
from fractions import Fraction


ZERO = Fraction(0)
ONE = Fraction(1)


def encode(value: Fraction) -> str:
    """Encode une fraction sans conversion flottante."""

    return f"{value.numerator}/{value.denominator}"


def logistic_state(rate: Fraction, amplitude: Fraction, q: Fraction) -> Fraction:
    """b_A(q)=a A q/(a+Aq), avec q=exp(a*tau)."""

    assert rate > 0
    assert amplitude > 0
    assert q >= 0
    return rate * amplitude * q / (rate + amplitude * q)


def logistic_tau_derivative(
    rate: Fraction, amplitude: Fraction, q: Fraction
) -> Fraction:
    """Dérivée exacte par q'=a q."""

    denominator = rate + amplitude * q
    return rate**3 * amplitude * q / denominator**2


def logistic_rhs(rate: Fraction, state: Fraction) -> Fraction:
    return rate * state - state**2


def amplitude_from_finite_state(
    rate: Fraction, state: Fraction, q: Fraction
) -> Fraction:
    """Inverse de A -> b_A(q) pour 0<b<a et q>0."""

    assert ZERO < state < rate
    assert q > 0
    return rate * state / (q * (rate - state))


def positive_part(value: Fraction) -> Fraction:
    return value if value > 0 else ZERO


def delayed_non_lipschitz_state(time: Fraction, delay: Fraction) -> Fraction:
    """x_c(t)=(t-c)_+^2, solution de x'=2 sqrt(x)."""

    return positive_part(time - delay) ** 2


def delayed_non_lipschitz_derivative(time: Fraction, delay: Fraction) -> Fraction:
    return 2 * positive_part(time - delay)


def main() -> None:
    # Borne dynamique conservatrice du cycle HWY; l'algèbre vaut pour tout a>0.
    rate = Fraction(217, 2000)
    amplitudes = (Fraction(1, 3), ONE, Fraction(5, 2))
    q_values = (ZERO, Fraction(1, 1024), Fraction(1, 16), ONE, Fraction(16))

    ode_residuals: list[Fraction] = []
    asymptotic_identity_residuals: list[Fraction] = []
    inverse_residuals: list[Fraction] = []
    pair_difference_residuals: list[Fraction] = []
    strict_order_failures = 0

    rows = []
    for q in q_values:
        states = [logistic_state(rate, amplitude, q) for amplitude in amplitudes]
        if q == ZERO:
            assert states == [ZERO, ZERO, ZERO]
        else:
            assert all(ZERO < state < rate for state in states)
            assert states == sorted(states)
            assert len(set(states)) == len(states)

        for amplitude, state in zip(amplitudes, states, strict=True):
            derivative = logistic_tau_derivative(rate, amplitude, q)
            rhs = logistic_rhs(rate, state)
            residual = derivative - rhs
            ode_residuals.append(residual)
            assert residual == ZERO

            # A-b_A(q)/q=A^2 q/(a+Aq); l'identité donne le coefficient
            # asymptotique A quand q->0 sans approximation flottante.
            if q > ZERO:
                scaled_state = state / q
                asymptotic_error = amplitude - scaled_state
                expected_error = amplitude**2 * q / (rate + amplitude * q)
                asymptotic_residual = asymptotic_error - expected_error
                asymptotic_identity_residuals.append(asymptotic_residual)
                assert asymptotic_residual == ZERO

                recovered = amplitude_from_finite_state(rate, state, q)
                inverse_residual = recovered - amplitude
                inverse_residuals.append(inverse_residual)
                assert inverse_residual == ZERO

        for left_index in range(len(amplitudes)):
            for right_index in range(left_index + 1, len(amplitudes)):
                left_amplitude = amplitudes[left_index]
                right_amplitude = amplitudes[right_index]
                left_state = states[left_index]
                right_state = states[right_index]
                denominator = (
                    (rate + left_amplitude * q)
                    * (rate + right_amplitude * q)
                )
                expected_difference = (
                    rate**2 * (left_amplitude - right_amplitude) * q
                    / denominator
                )
                difference_residual = (
                    left_state - right_state - expected_difference
                )
                pair_difference_residuals.append(difference_residual)
                assert difference_residual == ZERO
                if q > ZERO and not left_state < right_state:
                    strict_order_failures += 1

        rows.append(
            {
                "q_equals_exp_a_tau": encode(q),
                "states_by_asymptotic_amplitude": {
                    encode(amplitude): encode(state)
                    for amplitude, state in zip(amplitudes, states, strict=True)
                },
            }
        )

    assert strict_order_failures == 0

    # Même donnée finie dans le modèle localement lipschitzien: l'inverse
    # algébrique impose le même paramètre asymptotique et donc la même branche.
    finite_q = Fraction(3, 5)
    reference_amplitude = Fraction(7, 4)
    finite_state = logistic_state(rate, reference_amplitude, finite_q)
    recovered_amplitude = amplitude_from_finite_state(rate, finite_state, finite_q)
    finite_cauchy_injectivity_residual = recovered_amplitude - reference_amplitude
    assert finite_cauchy_injectivity_residual == ZERO

    # Contrôle adverse: le champ de vecteurs sqrt(x) n'est pas localement
    # lipschitzien à zéro. Toutes les solutions retardées ont x(0)=0 mais sont
    # distinctes à t=3. La racine carrée est exacte car x=(t-c)_+^2.
    delays = (ZERO, ONE, Fraction(2))
    sample_times = (ZERO, Fraction(1, 2), ONE, Fraction(2), Fraction(3))
    non_lipschitz_residuals: list[Fraction] = []
    delayed_rows = []
    for delay in delays:
        states = []
        for time in sample_times:
            state = delayed_non_lipschitz_state(time, delay)
            derivative = delayed_non_lipschitz_derivative(time, delay)
            exact_square_root = positive_part(time - delay)
            residual = derivative - 2 * exact_square_root
            non_lipschitz_residuals.append(residual)
            assert residual == ZERO
            assert state == exact_square_root**2
            states.append(state)
        delayed_rows.append(
            {
                "delay": encode(delay),
                "states": {
                    encode(time): encode(state)
                    for time, state in zip(sample_times, states, strict=True)
                },
            }
        )

    common_initial_states = {
        delayed_non_lipschitz_state(ZERO, delay) for delay in delays
    }
    terminal_states = {
        delayed_non_lipschitz_state(Fraction(3), delay) for delay in delays
    }
    assert common_initial_states == {ZERO}
    assert len(terminal_states) == len(delays)

    zero_lists = (
        ode_residuals,
        asymptotic_identity_residuals,
        inverse_residuals,
        pair_difference_residuals,
        non_lipschitz_residuals,
    )
    assert all(value == ZERO for values in zero_lists for value in values)

    residuals = {
        "logistic_ode_max_abs": encode(max(map(abs, ode_residuals))),
        "asymptotic_coefficient_identity_max_abs": encode(
            max(map(abs, asymptotic_identity_residuals))
        ),
        "finite_state_inverse_max_abs": encode(max(map(abs, inverse_residuals))),
        "pair_difference_identity_max_abs": encode(
            max(map(abs, pair_difference_residuals))
        ),
        "finite_cauchy_injectivity": encode(
            abs(finite_cauchy_injectivity_residual)
        ),
        "strict_order_failure_count": strict_order_failures,
        "non_lipschitz_delayed_solution_max_abs": encode(
            max(map(abs, non_lipschitz_residuals))
        ),
        "non_lipschitz_common_initial_state_count": len(common_initial_states),
        "non_lipschitz_distinct_terminal_state_count": len(terminal_states),
        "roundoff_error": "0 (aucun flottant)",
    }

    report = {
        "test": "ASYMPTOTIC-TRACE-CAUCHY-GATE-1",
        "question": (
            "une multiplicite de trajectoires partageant une trace nulle a "
            "tau=-infini implique-t-elle une multiplicite depuis une meme "
            "donnee forte posee a un temps fini ?"
        ),
        "navier_stokes_scope": {
            "equation": (
                "partial_t u+(u dot nabla)u-Delta u+nabla p=0, div u=0"
            ),
            "domain": "R3, aucune frontiere, force nulle, viscosite 1",
            "solution_class": (
                "solution forte/classique sur un intervalle commun; extension "
                "a une solution Leray-Hopf par unicite faible-forte"
            ),
            "difference_energy_identity": (
                "(1/2)d||w||_2^2/dt+||nabla w||_2^2="
                "-integral (w dot nabla)u dot w"
            ),
            "gronwall_gate": (
                "si integral ||nabla u||_infinity dt est fini et w(t0)=0, "
                "alors w=0 sur l'intervalle commun"
            ),
        },
        "logistic_countermodel": {
            "ode": "b'=a b-b^2",
            "rate": encode(rate),
            "q": "q=exp(a tau)",
            "family": "b_A=a A q/(a+Aq), A>0",
            "common_asymptotic_trace": "lim_(tau->-infinity)b_A(tau)=0",
            "asymptotic_coordinate": "lim b_A/q=A",
            "finite_state_inverse": "A=a b/[q(a-b)] pour 0<b<a, q>0",
            "rows": rows,
        },
        "scaling_dictionary": {
            "hwy_trace": (
                "les coordonnees instables e^(a tau)A disparaissent dans la "
                "trace singuliere quand tau->-infini"
            ),
            "finite_time": (
                "a tout tau0 fini, q0>0 et l'etat b_A(tau0) encode A de "
                "facon injective"
            ),
            "navier_stokes": "u_lambda(x,t)=lambda u(lambda x,lambda^2 t)",
        },
        "adversarial_non_lipschitz_control": {
            "ode": "x'=2 sqrt(x), x>=0",
            "family": "x_c(t)=(t-c)_+^2",
            "common_finite_datum": "x_c(0)=0 pour c>=0",
            "delayed_rows": delayed_rows,
            "conclusion": (
                "l'injectivite peut echouer quand la dynamique quitte la "
                "classe localement lipschitzienne/forte"
            ),
        },
        "arithmetic": "fractions rationnelles exactes; q exponentiel symbolique",
        "discretization": "aucune grille spatiale ou temporelle",
        "precision": "exacte pour toutes les identites encodees",
        "seed": "sans objet",
        "residuals": residuals,
        "limits": [
            "le modele ODE n'est pas une reduction de Navier-Stokes",
            "l'identite d'energie NS est une derivation analytique, pas verifiee par le script",
            "le test ne prouve pas l'existence globale de la solution forte Clay",
            "il n'exclut pas une multiplicite faible apres perte de regularite forte",
            "il ne quantifie ni le projecteur HWY ni la pression d'une couche asymetrique",
        ],
        "decision": (
            "une trace asymptotique commune ne constitue pas une donnee de "
            "Cauchy finie commune; tout transfert vers une meme donnee Clay "
            "doit d'abord franchir la perte de la classe forte"
        ),
    }
    print(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=True))


if __name__ == "__main__":
    main()
