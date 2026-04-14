from __future__ import annotations

from .eos import density_placeholder


def pressure_from_mass_balance(T1_C: float, T2_C: float, T3_C: float, z_co2: float, V1_ml: float, V2_ml: float, V3_ml: float, target_mass: float) -> float:
    """Very simple root-search placeholder for the pressure closure."""
    best_P = 1.0
    best_err = float("inf")
    for P_bar in range(1, 801):
        rho1 = density_placeholder(P_bar, T1_C, z_co2)
        rho2 = density_placeholder(P_bar, T2_C, z_co2)
        rho3 = density_placeholder(P_bar, T3_C, z_co2)
        mass = rho1 * V1_ml + rho2 * V2_ml + rho3 * V3_ml
        err = abs(mass - target_mass)
        if err < best_err:
            best_err = err
            best_P = float(P_bar)
    return best_P
