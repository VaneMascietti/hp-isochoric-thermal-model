from __future__ import annotations

import json
from pathlib import Path

from .geometry import Geometry
from .io import read_lvm
from .preprocessing import standardize_dataframe
from .simulation import simulate_pressure
from .objective import pressure_sse


def run_fit(raw_file: str, geometry_file: str, z_co2: float, tau3_s: float, output_json: str, output_csv: str) -> dict:
    geometry = Geometry.from_yaml(geometry_file)
    df = standardize_dataframe(read_lvm(raw_file))

    # Placeholder target mass. Replace with composition/charge-based calculation.
    target_mass = 1.0
    sim = simulate_pressure(df, geometry, z_co2=z_co2, tau3_s=tau3_s, target_mass=target_mass)
    obj = pressure_sse(sim)

    result = {
        "tau3_s": tau3_s,
        "lambda_env": 0.7,
        "V3_ml": geometry.V3_ml,
        "objective": obj,
    }

    Path(output_json).parent.mkdir(parents=True, exist_ok=True)
    Path(output_csv).parent.mkdir(parents=True, exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    sim.to_csv(output_csv, index=False)
    return result
