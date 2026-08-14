"""Certificat exact de la porte de parite du mode instable HWY.

Ce script ne simule pas Navier--Stokes et ne reproduit pas la CAP de
Hou--Wang--Yang. Il encode deux consequences algebriques de la reflexion

    (J u)(x) = S u(Sx),  S = diag(1, 1, -1),

et la loi d'echelle exacte d'une couche interieure au temps parabolique
``t = kappa * epsilon**2``. Dans une base abstraite adaptee a la parite,
les deux premieres coordonnees sont paires et les deux dernieres impaires.
Les calculs matriciels sont effectues avec ``fractions.Fraction``.
"""

from __future__ import annotations

import json
from fractions import Fraction


Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]


DIMENSION = 4
ZERO = Fraction(0)
ONE = Fraction(1)


def encode(value: Fraction) -> str:
    """Encode une fraction sans conversion flottante."""

    return f"{value.numerator}/{value.denominator}"


def identity() -> Matrix:
    return tuple(
        tuple(ONE if i == j else ZERO for j in range(DIMENSION))
        for i in range(DIMENSION)
    )


def zero_matrix() -> Matrix:
    return tuple(tuple(ZERO for _ in range(DIMENSION)) for _ in range(DIMENSION))


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(DIMENSION))
        for i in range(DIMENSION)
    )


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(DIMENSION))
        for i in range(DIMENSION)
    )


def scalar_matrix(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(tuple(scalar * value for value in row) for row in matrix)


def matrix_product(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (left[i][k] * right[k][j] for k in range(DIMENSION)),
                ZERO,
            )
            for j in range(DIMENSION)
        )
        for i in range(DIMENSION)
    )


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((matrix[i][j] * vector[j] for j in range(DIMENSION)), ZERO)
        for i in range(DIMENSION)
    )


def vector_subtract(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right, strict=True))


def dot(left: Vector, right: Vector) -> Fraction:
    return sum((a * b for a, b in zip(left, right, strict=True)), ZERO)


def matrix_max_abs(matrix: Matrix) -> Fraction:
    return max((abs(value) for row in matrix for value in row), default=ZERO)


def vector_max_abs(vector: Vector) -> Fraction:
    return max((abs(value) for value in vector), default=ZERO)


def diagonal(entries: tuple[Fraction, ...]) -> Matrix:
    assert len(entries) == DIMENSION
    return tuple(
        tuple(entries[i] if i == j else ZERO for j in range(DIMENSION))
        for i in range(DIMENSION)
    )


def main() -> None:
    identity_matrix = identity()
    zero = zero_matrix()

    # J est l'involution abstraite: +1 sur le secteur pair, -1 sur l'impair.
    reflection = diagonal((ONE, ONE, -ONE, -ONE))
    even_projector = scalar_matrix(
        Fraction(1, 2), matrix_add(identity_matrix, reflection)
    )
    odd_projector = scalar_matrix(
        Fraction(1, 2), matrix_subtract(identity_matrix, reflection)
    )

    reflection_residual = matrix_subtract(
        matrix_product(reflection, reflection), identity_matrix
    )
    even_idempotence_residual = matrix_subtract(
        matrix_product(even_projector, even_projector), even_projector
    )
    odd_idempotence_residual = matrix_subtract(
        matrix_product(odd_projector, odd_projector), odd_projector
    )
    orthogonality_residual = matrix_product(even_projector, odd_projector)
    decomposition_residual = matrix_subtract(
        matrix_add(even_projector, odd_projector), identity_matrix
    )

    assert reflection_residual == zero
    assert even_idempotence_residual == zero
    assert odd_idempotence_residual == zero
    assert orthogonality_residual == zero
    assert decomposition_residual == zero

    # La borne dynamique sourcée a >= 0.1085 donne 2a >= 0.217.
    source_growth_lower = Fraction(217, 2000)
    critical_tuning_exponent_lower = 2 * source_growth_lower
    assert critical_tuning_exponent_lower == Fraction(217, 1000)

    # Modele fini uniquement logique: L commute avec J, son premier mode
    # impair a le taux a_min, et le fonctionnel adjoint est e_3^*.
    commuting_operator = diagonal(
        (Fraction(-1), Fraction(-2), source_growth_lower, Fraction(-3))
    )
    commutator = matrix_subtract(
        matrix_product(commuting_operator, reflection),
        matrix_product(reflection, commuting_operator),
    )
    assert commutator == zero

    symmetric_layer: Vector = (Fraction(3), Fraction(-2), ZERO, ZERO)
    odd_mode: Vector = (ZERO, ZERO, ONE, ZERO)
    left_odd_functional: Vector = odd_mode
    odd_part_of_symmetric_layer = matvec(odd_projector, symmetric_layer)
    symmetric_projection_coefficient = dot(
        left_odd_functional, symmetric_layer
    )
    assert odd_part_of_symmetric_layer == (ZERO, ZERO, ZERO, ZERO)
    assert symmetric_projection_coefficient == ZERO
    assert matvec(commuting_operator, odd_mode) == tuple(
        source_growth_lower * value for value in odd_mode
    )

    asymmetric_layer: Vector = (Fraction(3), Fraction(-2), ONE, ZERO)
    asymmetric_projection_coefficient = dot(
        left_odd_functional, asymmetric_layer
    )
    assert asymmetric_projection_coefficient == ONE

    # Test adverse: un couplage pair -> impair brise [L,J]=0 et excite le
    # secteur impair en une application. Il montre que la commutation est une
    # hypothese mathematique essentielle, pas une consequence dimensionnelle.
    noncommuting_operator: Matrix = (
        (Fraction(-1), ZERO, ZERO, ZERO),
        (ZERO, Fraction(-2), ZERO, ZERO),
        (ONE, ZERO, source_growth_lower, ZERO),
        (ZERO, ZERO, ZERO, Fraction(-3)),
    )
    bad_commutator = matrix_subtract(
        matrix_product(noncommuting_operator, reflection),
        matrix_product(reflection, noncommuting_operator),
    )
    bad_odd_excitation = matvec(
        odd_projector, matvec(noncommuting_operator, symmetric_layer)
    )
    assert bad_commutator != zero
    assert bad_odd_excitation == (ZERO, ZERO, Fraction(3), ZERO)

    # Couche g_epsilon(x)=epsilon^-1 g(x/epsilon), t=kappa epsilon^2.
    # sqrt(t) e^(t Delta)g_epsilon(sqrt(t)xi)
    # =sqrt(kappa)(e^(kappa Delta)g)(sqrt(kappa)xi): exposant epsilon nul.
    datum_amplitude_exponent = Fraction(-1)
    similarity_prefactor_exponent = Fraction(1)
    heat_rescaling_exponent = datum_amplitude_exponent + similarity_prefactor_exponent
    assert heat_rescaling_exponent == ZERO

    # Depuis tau_epsilon=log(kappa)+2log(epsilon) jusqu'a tau=0, un mode
    # impair de taux a porte le facteur kappa^-a epsilon^-2a. Une asymetrie
    # epsilon^beta reste bornee au niveau lineaire seulement si beta>=2a.
    untuned_amplification_epsilon_exponent_upper = -critical_tuning_exponent_lower
    tuning_at_lower_rate_net_exponent = (
        critical_tuning_exponent_lower - 2 * source_growth_lower
    )
    assert untuned_amplification_epsilon_exponent_upper == Fraction(-217, 1000)
    assert tuning_at_lower_rate_net_exponent == ZERO

    residuals = {
        "reflection_involution": encode(matrix_max_abs(reflection_residual)),
        "even_projector_idempotence": encode(
            matrix_max_abs(even_idempotence_residual)
        ),
        "odd_projector_idempotence": encode(
            matrix_max_abs(odd_idempotence_residual)
        ),
        "projector_orthogonality": encode(matrix_max_abs(orthogonality_residual)),
        "parity_decomposition": encode(matrix_max_abs(decomposition_residual)),
        "commuting_operator": encode(matrix_max_abs(commutator)),
        "symmetric_layer_odd_part": encode(
            vector_max_abs(odd_part_of_symmetric_layer)
        ),
        "symmetric_layer_left_odd_pairing": encode(
            abs(symmetric_projection_coefficient)
        ),
        "similarity_epsilon_exponent": encode(abs(heat_rescaling_exponent)),
        "tuned_net_exponent_at_source_lower_rate": encode(
            abs(tuning_at_lower_rate_net_exponent)
        ),
        "rational_assertion_failure_count": 0,
        "roundoff_error": "0 (aucun flottant)",
    }
    assert all(
        value == "0/1" or value == 0 or value == "0 (aucun flottant)"
        for value in residuals.values()
    )

    report = {
        "test": "HWY-PARITY-PROJECTION-GATE-1",
        "question": (
            "une regularisation interieure qui respecte la reflexion z -> -z "
            "peut-elle exciter lineairement le mode HWY certifie impair ?"
        ),
        "equation": (
            "NS incompressible 3D non force sur R3, nu=1, au niveau de "
            "l'equivariance et de la linearisation autour du profil HWY; "
            "aucune trajectoire PDE simulee"
        ),
        "solution_scope": (
            "donnees lisses divergence-free et solution forte locale unique "
            "pour la preservation de parite; profil singulier HWY seulement "
            "pour l'information spectrale sourcee"
        ),
        "parity": {
            "physical_involution": "(J u)(x)=S u(Sx), S=diag(1,1,-1)",
            "even_components": (
                "u_x(x,y,-z)=u_x(x,y,z), u_y idem, "
                "u_z(x,y,-z)=-u_z(x,y,z)"
            ),
            "odd_sector_projector": "Q_-=(I-J)/2",
            "symmetric_layer_odd_projection": encode(
                symmetric_projection_coefficient
            ),
        },
        "analytic_commutations": {
            "heat": "Delta J=J Delta, donc exp(t Delta)J=J exp(t Delta)",
            "leray": (
                "P(S xi)=S P(xi) S pour P(xi)=I-xi tensor xi/|xi|^2"
            ),
            "nonlinearity": "B(Ju,Jv)=J B(u,v)",
            "linearized_operator": (
                "si JU=U, alors [L_U,J]=0 et les secteurs pairs/impairs "
                "sont invariants"
            ),
        },
        "scaling": {
            "navier_stokes": "u_lambda(x,t)=lambda u(lambda x,lambda^2 t)",
            "inner_layer": "g_epsilon(x)=epsilon^-1 g(x/epsilon)",
            "parabolic_time": "t=kappa epsilon^2",
            "similarity_time": "tau_epsilon=log(kappa)+2log(epsilon)",
            "similarity_profile": (
                "sqrt(t) exp(t Delta)g_epsilon(sqrt(t)xi)="
                "sqrt(kappa)(exp(kappa Delta)g)(sqrt(kappa)xi)"
            ),
            "epsilon_exponent_in_profile": encode(heat_rescaling_exponent),
        },
        "source_spectral_rate": {
            "elliptic_candidate": "tilde_lambda approximately -0.113142",
            "sign_dictionary": "dynamic a=-tilde_lambda>0",
            "certified_conservative_lower_a": encode(source_growth_lower),
            "linear_amplification": "kappa^-a epsilon^-2a",
            "lower_amplification_epsilon_exponent": encode(
                untuned_amplification_epsilon_exponent_upper
            ),
            "necessary_tuning_beta_lower": encode(
                critical_tuning_exponent_lower
            ),
        },
        "adversarial_test": {
            "perturbation": "ajouter un couplage pair vers impair dans L",
            "commutator_max_abs": encode(matrix_max_abs(bad_commutator)),
            "odd_excitation_max_abs": encode(vector_max_abs(bad_odd_excitation)),
            "conclusion": (
                "sans [L,J]=0, une couche paire peut exciter le secteur impair"
            ),
        },
        "arithmetic": "fractions rationnelles exactes; exponentielles symboliques",
        "discretization": "aucune grille spatiale ou temporelle",
        "precision": "exacte pour les identites finies et les exposants",
        "seed": "sans objet",
        "residuals": residuals,
        "limits": [
            "le modele matriciel ne discretise pas l'operateur HWY",
            "aucun coefficient adjoint quantitatif asymetrique n'est calcule",
            "aucun shadowing non lineaire jusqu'a un temps fixe n'est prouve",
            "la parite n'exclut pas un autre mode instable pair",
            "la preservation forte de la symetrie n'interdit pas des branches faibles brisant la symetrie apres perte d'unicite forte",
        ],
        "decision": (
            "la couche symetrique a une projection impaire exactement nulle; "
            "le transfert generique doit donc introduire une asymetrie controlee "
            "et un vrai fonctionnel adjoint certifie"
        ),
    }
    print(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=True))


if __name__ == "__main__":
    main()
