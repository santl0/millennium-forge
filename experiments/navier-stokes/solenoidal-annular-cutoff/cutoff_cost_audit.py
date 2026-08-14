"""Exact weak-Lorentz ledger for a critical annular cutoff.

This is an atomic/distributional certificate.  It does not construct a
Bogovskii corrector and does not discretize Navier--Stokes.
"""

from fractions import Fraction as Q


def mu_strict(amplitudes, volumes, threshold):
    """Measure of {|f| > threshold} for a disjoint step function."""
    return sum(
        (volume for amplitude, volume in zip(amplitudes, volumes)
         if abs(amplitude) > threshold),
        Q(0),
    )


def mu_left(amplitudes, volumes, threshold):
    """Left limit of the distribution at a positive atom amplitude."""
    return sum(
        (volume for amplitude, volume in zip(amplitudes, volumes)
         if abs(amplitude) >= threshold),
        Q(0),
    )


def weak_cube(amplitudes, volumes, exponent):
    """Cube of weak-L^3 or weak-L^(3/2), without fractional powers."""
    best = Q(0)
    thresholds = sorted({abs(value) for value in amplitudes if value})
    for threshold in thresholds:
        measure = mu_left(amplitudes, volumes, threshold)
        if exponent == 3:
            candidate = threshold**3 * measure
        elif exponent == Q(3, 2):
            candidate = threshold**3 * measure**2
        else:
            raise ValueError(exponent)
        best = max(best, candidate)
    return best


def scale_atoms(amplitudes, volumes, scale, field_degree):
    """Clay scaling: amplitude scale^degree, volume scale^-3."""
    return (
        [scale**field_degree * value for value in amplitudes],
        [volume / scale**3 for volume in volumes],
    )


checks = 0
CROWN_CONSTANT = Q(7)  # |(-R,R)^3 \ (-R/2,R/2)^3| / R^3

# Sharp plateau family on the cubic crown E_R.
for exponent in range(-40, 81):
    R = Q(2**exponent) if exponent >= 0 else Q(1, 2 ** (-exponent))
    volume = CROWN_CONSTANT * R**3
    velocity_amplitude = 1 / R
    collar_amplitude = velocity_amplitude / R

    velocity = [velocity_amplitude]
    collar = [collar_amplitude]
    volumes = [volume]

    assert mu_strict(velocity, volumes, velocity_amplitude) == 0
    assert mu_left(velocity, volumes, velocity_amplitude) == volume
    assert mu_strict(collar, volumes, collar_amplitude) == 0
    assert mu_left(collar, volumes, collar_amplitude) == volume

    ku3 = weak_cube(velocity, volumes, 3)
    kc3 = weak_cube(collar, volumes, Q(3, 2))
    assert ku3 == CROWN_CONSTANT
    assert kc3 == CROWN_CONSTANT**2
    assert kc3 == CROWN_CONSTANT * ku3
    checks += 7

# General finite step distributions: exact finite-measure embedding.
profiles = []
for length in range(1, 17):
    raw_volumes = [Q(i + 1, 2 ** (i + 4)) for i in range(length)]
    total = sum(raw_volumes, Q(0))
    normalized = [CROWN_CONSTANT * value / total for value in raw_volumes]
    amplitudes = [
        Q((-1) ** i * (3 * i + 2), 2 ** (i % 5))
        for i in range(length)
    ]
    profiles.append((amplitudes, normalized))

for radius_exponent in range(0, 65):
    R = Q(1, 2**radius_exponent)
    for base_amplitudes, base_volumes in profiles:
        amplitudes = [value / R for value in base_amplitudes]
        volumes = [value * R**3 for value in base_volumes]
        collar = [value / R for value in amplitudes]
        support_volume = sum(volumes, Q(0))

        ku3 = weak_cube(amplitudes, volumes, 3)
        kc3 = weak_cube(collar, volumes, Q(3, 2))

        # [K_(3/2)(U/R)]^3 <= (|E|/R^3) [K_3(U)]^3.
        assert kc3 * R**3 <= support_volume * ku3
        assert support_volume == CROWN_CONSTANT * R**3

        # Direct Clay covariance from the normalized R=1 atoms.
        scaled_u, scaled_volume = scale_atoms(
            base_amplitudes, base_volumes, 1 / R, 1
        )
        scaled_c, scaled_c_volume = scale_atoms(
            base_amplitudes, base_volumes, 1 / R, 2
        )
        assert scaled_u == amplitudes
        assert scaled_volume == volumes
        assert scaled_c == collar
        assert scaled_c_volume == volumes
        assert weak_cube(scaled_u, scaled_volume, 3) == weak_cube(
            base_amplitudes, base_volumes, 3
        )
        assert weak_cube(scaled_c, scaled_c_volume, Q(3, 2)) == weak_cube(
            base_amplitudes, base_volumes, Q(3, 2)
        )
        checks += 8

print("exact checks =", checks)
print("crown volume constant =", CROWN_CONSTANT)
print("plateau Ku^3 =", CROWN_CONSTANT)
print("plateau cutoff K_(3/2)^3 =", CROWN_CONSTANT**2)
print("sharp cube ratio =", CROWN_CONSTANT)
print("exact residual = 0")
