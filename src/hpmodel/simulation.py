from __future__ import annotations

import pandas as pd

from .geometry import Geometry
from .thermal_model import compute_T2, compute_T3
from .pressure_model import pressure_from_mass_balance


def simulate_pressure(df: pd.DataFrame, geometry: Geometry, z_co2: float, tau3_s: float, target_mass: float) -> pd.DataFrame:
    """Run the reduced-model pressure simulation."""
    time_s = df["time_s"].to_numpy()
    T1 = df["T_sample_C"].to_numpy()
    T2 = compute_T2(T1)
    T3 = compute_T3(time_s, T2, tau3_s=tau3_s)

    P_calc = [
        pressure_from_mass_balance(
            T1_C=float(t1),
            T2_C=float(t2),
            T3_C=float(t3),
            z_co2=float(z_co2),
            V1_ml=geometry.V1_ml,
            V2_ml=geometry.V2_ml,
            V3_ml=geometry.V3_ml,
            target_mass=float(target_mass),
        )
        for t1, t2, t3 in zip(T1, T2, T3)
    ]

    out = df.copy()
    out["T2_C"] = T2
    out["T3_C"] = T3
    out["P_calc_bar"] = P_calc
    return out
