from __future__ import annotations

import argparse
from pathlib import Path

from hpmodel.fit import run_fit
from hpmodel.utils import load_yaml


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    cfg = load_yaml(args.config)
    experiments = load_yaml(cfg["experiments_file"])["experiments"]
    exp = experiments[cfg["experiment_id"]]

    run_fit(
        raw_file=exp["raw_file"],
        geometry_file=cfg["geometry_file"],
        z_co2=exp["composition"]["x_co2"],
        tau3_s=float(cfg["parameters"]["tau3_s"]["initial"]),
        output_json=cfg["output"]["json"],
        output_csv=cfg["output"]["csv"],
    )
    print(f"Fit output written under {Path(cfg['output']['json']).parent}")


if __name__ == "__main__":
    main()
