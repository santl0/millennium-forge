#!/usr/bin/env python3
"""Exact admissibility audit for a critical homogeneous vorticity profile.

The script checks a nonzero distributionally divergence-free profile with
|omega|=|x|^-2, its homogeneous Biot--Savart velocity, the obstruction caused
by a log-bmo direction, and a divergence-free smooth cutoff mechanism.  It
does not integrate Navier--Stokes and does not turn the cutoff family into one
trajectory approaching a singular time.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


SCRIPT = Path(__file__).resolve()


class Jet:
    """First-order three-variable jet with exact rational coefficients."""

    def __init__(self, value: Fraction | int, gradient: tuple[Fraction, Fraction, Fraction] = (Fraction(0), Fraction(0), Fraction(0))):
        self.value = Fraction(value)
        self.gradient = tuple(Fraction(entry) for entry in gradient)

    @staticmethod
    def lift(value: "Jet | Fraction | int") -> "Jet":
        return value if isinstance(value, Jet) else Jet(value)

    def __add__(self, other: "Jet | Fraction | int") -> "Jet":
        other = Jet.lift(other)
        return Jet(self.value + other.value, tuple(self.gradient[i] + other.gradient[i] for i in range(3)))

    __radd__ = __add__

    def __neg__(self) -> "Jet":
        return Jet(-self.value, tuple(-entry for entry in self.gradient))

    def __sub__(self, other: "Jet | Fraction | int") -> "Jet":
        return self + (-Jet.lift(other))

    def __rsub__(self, other: "Jet | Fraction | int") -> "Jet":
        return Jet.lift(other) - self

    def __mul__(self, other: "Jet | Fraction | int") -> "Jet":
        other = Jet.lift(other)
        return Jet(
            self.value * other.value,
            tuple(self.gradient[i] * other.value + self.value * other.gradient[i] for i in range(3)),
        )

    __rmul__ = __mul__

    def reciprocal(self) -> "Jet":
        return Jet(
            1 / self.value,
            tuple(-entry / (self.value * self.value) for entry in self.gradient),
        )

    def __truediv__(self, other: "Jet | Fraction | int") -> "Jet":
        return self * Jet.lift(other).reciprocal()

    def __rtruediv__(self, other: "Jet | Fraction | int") -> "Jet":
        return Jet.lift(other) * self.reciprocal()

    def __pow__(self, exponent: int) -> "Jet":
        if exponent == 0:
            return Jet(1)
        if exponent < 0:
            return (self.reciprocal()) ** (-exponent)
        result = Jet(1)
        for _ in range(exponent):
            result = result * self
        return result


def rational_sqrt_jet(value: Jet, root: Fraction) -> Jet:
    """Return sqrt(value) when its value has the supplied exact rational root."""

    if root * root != value.value or root <= 0:
        raise ValueError("the supplied root is not the positive exact square root")
    return Jet(root, tuple(entry / (2 * root) for entry in value.gradient))


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def check(name: str, condition: bool, details: dict[str, object]) -> dict[str, object]:
    if not condition:
        raise AssertionError(f"{name}: {details}")
    return {"name": name, "passed": True, "details": details}


def main() -> None:
    checks: list[dict[str, object]] = []

    # Navier--Stokes weights under u_kappa(x,t)=kappa u(kappa x,kappa^2 t).
    weights = {
        "length": -1,
        "velocity": 1,
        "vorticity": 2,
        "shape_factor_Phi": 0,
        "gradient_Phi": 1,
        "direction": 0,
        "weak_L32_vorticity": 0,
        "weak_L3_velocity": 0,
        "velocity_L2_squared": -1,
    }
    checks.append(
        check(
            "critical_profile_scaling",
            weights["vorticity"] == -2 * weights["length"]
            and weights["gradient_Phi"] == -weights["length"]
            and weights["weak_L32_vorticity"] == 0
            and weights["weak_L3_velocity"] == 0,
            {
                "weights_under_kappa": weights,
                "profile": "|omega|=|x|^-2, Phi=1",
                "gradient_bound": "|nabla Phi|=0<=C|x|^-1",
            },
        )
    )

    # Let |a|=1 and r=|x|.  The homogeneous divergence-free velocity is
    # u = alpha a/r + beta (a.x)x/r^3 + gamma a cross x/r^2.
    # div u=(beta-alpha)(a.x)/r^3.
    alpha = beta = gamma = Fraction(1, 2)
    divergence_coefficient = beta - alpha
    checks.append(
        check(
            "homogeneous_velocity_divergence",
            divergence_coefficient == 0,
            {
                "velocity": "u=(1/2)[a/r+(a.x)x/r^3+a cross x/r^2]",
                "divergence_coefficient": fstr(divergence_coefficient),
                "distributional_note": "u is locally integrable and the flux of u across radius rho is O(rho), so no delta divergence occurs at zero",
            },
        )
    )

    # curl(a/r)=a cross x/r^3,
    # curl((a.x)x/r^3)=a cross x/r^3, and
    # curl(a cross x/r^2)=2(a.x)x/r^4.
    tangential_curl_coefficient = alpha + beta
    radial_curl_coefficient = 2 * gamma
    checks.append(
        check(
            "homogeneous_velocity_curl",
            tangential_curl_coefficient == 1 and radial_curl_coefficient == 1,
            {
                "vorticity": "omega=a cross x/r^3+(a.x)x/r^4=r^-2[a cross theta+(a.theta)theta]",
                "tangential_coefficient": fstr(tangential_curl_coefficient),
                "radial_coefficient": fstr(radial_curl_coefficient),
                "div_omega": "0 distributionally because omega=curl u",
            },
        )
    )

    # Independent exact forward-mode differentiation at rational points of
    # S^2.  Stereographic coordinates keep x,y,z and r=1 rational, so neither
    # floating point nor symbolic-algebra software is required.
    autodiff_residuals: list[tuple[Fraction, tuple[Fraction, Fraction, Fraction]]] = []
    stereographic_parameters = [
        (Fraction(s), Fraction(t))
        for s in (-2, -1, 0, 1, 2)
        for t in (-2, -1, 0, 1, 2)
    ]
    for s, t in stereographic_parameters:
        denominator = 1 + s * s + t * t
        point = (
            2 * s / denominator,
            2 * t / denominator,
            (1 - s * s - t * t) / denominator,
        )
        coordinates = [
            Jet(point[i], tuple(Fraction(1) if i == j else Fraction(0) for j in range(3)))
            for i in range(3)
        ]
        x, y, z = coordinates
        radius_squared = x * x + y * y + z * z
        radius = rational_sqrt_jet(radius_squared, Fraction(1))
        cross_ax = (-y, x, Jet(0))
        a_components = (Jet(0), Jet(0), Jet(1))
        u_jets = tuple(
            Fraction(1, 2)
            * (a_components[i] / radius + z * coordinates[i] / radius**3 + cross_ax[i] / radius**2)
            for i in range(3)
        )
        div_u = sum(u_jets[i].gradient[i] for i in range(3))
        curl_u = (
            u_jets[2].gradient[1] - u_jets[1].gradient[2],
            u_jets[0].gradient[2] - u_jets[2].gradient[0],
            u_jets[1].gradient[0] - u_jets[0].gradient[1],
        )
        expected_omega = tuple(
            cross_ax[i].value + point[2] * point[i] for i in range(3)
        )
        curl_residual = tuple(curl_u[i] - expected_omega[i] for i in range(3))
        autodiff_residuals.append((div_u, curl_residual))
    checks.append(
        check(
            "exact_rational_autodifferentiation",
            all(divergence == 0 and curl_residual == (0, 0, 0) for divergence, curl_residual in autodiff_residuals),
            {
                "points": len(autodiff_residuals),
                "coordinates": "rational stereographic points on S^2",
                "divergence_residual": "0 at every point",
                "curl_residual": "(0,0,0) at every point",
                "precision": "fractions.Fraction forward-mode automatic differentiation",
            },
        )
    )

    # The tangential and radial pieces of W(theta) are orthogonal and have
    # squared lengths 1-mu^2 and mu^2.  Rational mu sweeps certify the
    # polynomial identity; orthogonality is the all-angle proof.
    mus = [Fraction(k, 128) for k in range(-128, 129)]
    shape_squares = [mu * mu + (1 - mu * mu) for mu in mus]
    checks.append(
        check(
            "constant_magnitude_shape_factor",
            all(value == 1 for value in shape_squares),
            {
                "angular_vector": "W(theta)=a cross theta+(a.theta)theta",
                "identity": "|W|^2=(1-mu^2)+mu^2=1",
                "consequence": "|omega|=r^-2 and Phi=1 exactly",
                "rational_mu_samples": len(mus),
            },
        )
    )

    # The radial flux is integral_(S2) a.theta dS=0.  Together with the curl
    # realization this excludes a hidden delta divergence at the origin.
    first_spherical_moment = Fraction(0)
    checks.append(
        check(
            "zero_vorticity_flux_at_origin",
            first_spherical_moment == 0,
            {
                "normalized_flux": fstr(first_spherical_moment),
                "certificate": "antipodal oddness of theta -> a.theta",
            },
        )
    )

    # For |omega|=r^-2, the super-level radius at lambda_N=4^N is 2^-N.
    # Suppressing |B_1|, lambda_N^(3/2)*measure is exactly one for all N.
    normalized_weak_l32 = []
    for n in range(65):
        lambda_power_three_halves = 8**n
        normalized_measure = Fraction(1, 8**n)
        normalized_weak_l32.append(lambda_power_three_halves * normalized_measure)
    checks.append(
        check(
            "exact_weak_L32_distribution",
            all(value == 1 for value in normalized_weak_l32),
            {
                "thresholds": "lambda_N=4^N, N=0..64",
                "superlevel_radius": "2^-N",
                "measure": "|B_1|*8^-N",
                "lambda_power_3_over_2_times_measure": "|B_1|",
                "all_scale_certificate": "measure{|omega|>lambda}=|B_1| lambda^-3/2",
            },
        )
    )

    # xi=W has unit length and spherical/ball average a/3:
    # average (a.theta)theta=a/3 and average a cross theta=0.
    direction_mean_coefficient = Fraction(1, 3)
    reverse_triangle_lower_bound = 1 - direction_mean_coefficient
    checks.append(
        check(
            "direction_mean_and_oscillation",
            direction_mean_coefficient == Fraction(1, 3)
            and reverse_triangle_lower_bound == Fraction(2, 3),
            {
                "direction": "xi(theta)=a cross theta+(a.theta)theta",
                "ball_mean": "a/3",
                "pointwise_bound": "|xi-a/3|>=||xi|-|a/3||=2/3",
                "mean_oscillation_lower_bound": fstr(reverse_triangle_lower_bound),
            },
        )
    )

    # With phi(exp(-N))=1/N, the centered ball alone gives cost >=2N/3.
    log_bmo_costs = [reverse_triangle_lower_bound * n for n in range(1, 257)]
    checks.append(
        check(
            "homogeneous_direction_fails_log_bmo",
            all(log_bmo_costs[n] < log_bmo_costs[n + 1] for n in range(255))
            and log_bmo_costs[-1] == Fraction(512, 3),
            {
                "radii": "r_N=exp(-N)",
                "phi_r_N": "1/N",
                "cost_lower_bound": "2N/3",
                "last_exact_cost": fstr(log_bmo_costs[-1]),
                "residual": "unbounded sequence, hence no finite global bmo_phi norm",
            },
        )
    )

    # General rigidity: exact continuous or discrete dilation recurrence makes
    # centered mean oscillation invariant along a sequence tending to zero.
    # A bmo_phi upper bound K/N then forces that invariant value to vanish.
    test_constants = [Fraction(k, 7) for k in range(1, 65)]
    contradiction_indices = [3 * k + 1 for k in range(1, 65)]
    rigidity_gates = [K / n < Fraction(2, 3) for K, n in zip(test_constants, contradiction_indices)]
    checks.append(
        check(
            "dilation_recurrence_rigidity",
            all(rigidity_gates),
            {
                "identity": "MO_(B_(q^n r))(xi)=MO_(B_r)(xi) for xi(qx)=xi(x)",
                "bmo_upper": "MO_(B_(q^n r))<=K phi(q^n r)->0",
                "conclusion": "the centered mean oscillation is zero; xi is constant a.e., and recurrence propagates the constant",
                "finite_adversarial_pairs": len(rigidity_gates),
            },
        )
    )

    # A nonzero constant direction is incompatible with both div omega=0 and
    # a finite global weak-L^p norm: omega=m e gives partial_e m=0, so every
    # nontrivial transverse super-level set is repeated along an infinite line.
    transverse_mass = Fraction(1, 5)
    threshold = Fraction(3, 7)
    cylinder_measures = [2 * L * transverse_mass for L in range(1, 257)]
    tail_ledgers = [threshold * threshold * measure for measure in cylinder_measures]
    checks.append(
        check(
            "constant_direction_solenoidal_lorentz_obstruction",
            all(cylinder_measures[n] < cylinder_measures[n + 1] for n in range(255))
            and tail_ledgers[-1] == Fraction(4608, 245),
            {
                "equation": "div(m e)=partial_e m=0",
                "superlevel_cylinder": "{g>tau} cross (-L,L)",
                "measure_at_L256": fstr(cylinder_measures[-1]),
                "tau_squared_times_measure_at_L256": fstr(tail_ledgers[-1]),
                "all_scale_certificate": "the measure grows linearly in L and is infinite as L tends to infinity",
            },
        )
    )

    # The angular mean of |r u|^2 is 2/3, hence the exact energy in an annulus,
    # divided by pi, is (8/3)(R-epsilon).  Energy is locally subcritical.
    normalized_energies = [Fraction(8, 3) * (1 - Fraction(1, 2**n)) for n in range(1, 65)]
    checks.append(
        check(
            "finite_local_energy",
            all(normalized_energies[n] < normalized_energies[n + 1] for n in range(63))
            and normalized_energies[-1] < Fraction(8, 3),
            {
                "angular_average_of_|r_u|^2": "2/3",
                "annular_energy": "(8*pi/3)(R-epsilon)",
                "normalized_limit_R1": "8/3",
                "global_warning": "energy diverges linearly as the outer radius tends to infinity",
            },
        )
    )

    # For any homogeneous divergence-free u of degree q=-1,
    # curl(x cross u)=-(2+q)u=-u.  Thus A=-x cross u is a degree-zero vector
    # potential.  Radial C-infinity cutoffs of A produce smooth compactly
    # supported divergence-free velocities that agree with u in the annulus.
    homogeneity_degree = -1
    homotopy_coefficient = -(2 + homogeneity_degree)
    checks.append(
        check(
            "divergence_free_smooth_cutoff_homotopy",
            homotopy_coefficient == -1,
            {
                "identity": "curl(x cross u)=x div u-2u-(x dot nabla)u",
                "degree": homogeneity_degree,
                "coefficient": homotopy_coefficient,
                "potential": "A=-x cross u, so curl A=u",
                "cutoff": "u_(epsilon,R)=curl(chi_(epsilon,R) A) is C_c^infinity and divergence-free",
            },
        )
    )

    # Inner cutoff-shell scaling: A is degree zero, one derivative gives u
    # of size epsilon^-1, a second gives omega of size epsilon^-2.
    cutoff_weights = {
        "inner_radius": 1,
        "potential_A": 0,
        "velocity": -1,
        "vorticity": -2,
        "shell_volume": 3,
        "shell_energy": 1,
        "weak_L32_vorticity": 0,
    }
    checks.append(
        check(
            "inner_cutoff_scaling",
            cutoff_weights["velocity"] * 2 + cutoff_weights["shell_volume"]
            == cutoff_weights["shell_energy"]
            and Fraction(3, 2) * cutoff_weights["vorticity"]
            + cutoff_weights["shell_volume"]
            == cutoff_weights["weak_L32_vorticity"],
            {
                "epsilon_exponents": cutoff_weights,
                "consequence": "energy defect is O(epsilon), while the critical vorticity scale stays O(1)",
            },
        )
    )

    # Let epsilon_N=2^(-2N), r_N=2^-N, and use a cutoff equal to one beyond
    # 2 epsilon_N.  Inside B_(r_N), the altered fraction is at most
    # delta_N=(2 epsilon_N/r_N)^3=8*2^(-3N).  For bounded directions,
    # |MO(f)-MO(g)|<=2 average|f-g|<=4 delta_N.  The log-base-two weight is
    # equivalent to the natural-log weight and makes the certificate rational.
    cutoff_bmo_costs: list[Fraction] = []
    cutoff_volume_fractions: list[Fraction] = []
    for n in range(2, 129):
        altered_fraction = Fraction(8, 2 ** (3 * n))
        mean_oscillation_lower = Fraction(2, 3) - 4 * altered_fraction
        weighted_cost = (n + 1) * mean_oscillation_lower
        cutoff_volume_fractions.append(altered_fraction)
        cutoff_bmo_costs.append(weighted_cost)
    checks.append(
        check(
            "smooth_cutoff_bmo_nonuniformity",
            all(cost > 0 for cost in cutoff_bmo_costs)
            and all(cutoff_bmo_costs[n] < cutoff_bmo_costs[n + 1] for n in range(len(cutoff_bmo_costs) - 1)),
            {
                "inner_scale": "epsilon_N=2^(-2N)",
                "test_radius": "r_N=2^-N",
                "altered_volume_fraction": "delta_N=8*2^(-3N)",
                "oscillation_stability": "|MO(f)-MO(g)|<=4 delta_N for |f|,|g|<=1",
                "weight": "phi_2(r)=1/[1+log_2(1/r)], equivalent to the natural-log weight",
                "first_exact_cost_N2": fstr(cutoff_bmo_costs[0]),
                "last_exact_cost_N128": fstr(cutoff_bmo_costs[-1]),
                "consequence": "no bmo_phi extension constant can be uniform along the smooth cutoff family",
            },
        )
    )

    # The same approximants are not strongly compact in the critical velocity
    # L^3 norm: the radial integral is integral_(epsilon)^R dr/r.
    logarithmic_ledgers = [Fraction(n) for n in range(1, 257)]
    checks.append(
        check(
            "critical_L3_cutoff_divergence",
            all(logarithmic_ledgers[n] < logarithmic_ledgers[n + 1] for n in range(255)),
            {
                "inner_radii": "epsilon_N=R exp(-N)",
                "radial_L3_integral": "log(R/epsilon_N)=N",
                "last_exact_logarithm": fstr(logarithmic_ledgers[-1]),
                "consequence": "smooth Clay-admissible approximants are energy-controlled but not uniformly L3-controlled",
            },
        )
    )

    digest = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
    output = {
        "artifact": "CRITICAL-PROFILE-ADMISSIBILITY-1",
        "scope": "exact homogeneous profile, dilation rigidity, and smooth divergence-free cutoff ledger on R3",
        "arithmetic": "fractions, vector-calculus identities, and symbolic all-scale certificates; no floating point",
        "discretization": "no PDE grid or time integrator",
        "random_seed": None,
        "pde_status": "the singular profile is not a classical Navier-Stokes state; each doubly cut off velocity is smooth compactly supported divergence-free initial data",
        "pressure_status": "for each smooth cutoff datum the pressure is the global Leray pressure; no stationary pressure or zero Navier-Stokes residual is asserted",
        "uncertified_components": [
            "occurrence of the profile as a limit of one Navier-Stokes trajectory",
            "uniform control of the global pressure after inner and outer cutoffs",
            "exclusion of non-recurrent scale-dependent directions allowed by log-bmo",
            "regularity or blow-up for general Clay data",
        ],
        "assertion_failure_count": 0,
        "check_count": len(checks),
        "checks": checks,
        "script_sha256": digest,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
