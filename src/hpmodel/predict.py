from __future__ import annotations

import json
from pathlib import Path

from .geometry import Geometry
from .io import read_lvm
from .preprocessing import standardize_dataframe
from .simulation import simulate_pressure


def run_prediction(raw_file: str, geometry_file: str, z_co2: float, params_json: str, output_csv: str) -> None:
    geometry = Geometry.from_yaml(geometry_file)
    df = standardize_dataframe(read_lvm(raw_file))
    with open(params_json, "r", encoding="utf-8") as f:
        params = json.load(f)

    target_mass = 1.0
    sim = simulate_pressure(df, geometry, z_co2=z_co2, tau3_s=float(params["tau3_s"]), target_mass=target_mass)
    Path(output_csv).parent.mkdir(parents=True, exist_ok=True)
    sim.to_csv(output_csv, index=False)
