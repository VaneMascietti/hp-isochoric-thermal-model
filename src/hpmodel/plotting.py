from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def plot_pressure_comparison(df: pd.DataFrame, output_path: str) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(df["time_s"], df["P_sample_bar"], label="P_exp")
    ax.plot(df["time_s"], df["P_calc_bar"], label="P_calc")
    ax.set_xlabel("time / s")
    ax.set_ylabel("pressure / bar")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    plt.close(fig)
