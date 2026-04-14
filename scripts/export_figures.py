from __future__ import annotations

import argparse
import pandas as pd

from hpmodel.plotting import plot_pressure_comparison


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    plot_pressure_comparison(df, args.output)


if __name__ == "__main__":
    main()
