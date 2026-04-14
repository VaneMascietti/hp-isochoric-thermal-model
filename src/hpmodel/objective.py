from __future__ import annotations

import numpy as np
import pandas as pd


def pressure_sse(df: pd.DataFrame, weight: float = 1.0) -> float:
    """Weighted SSE between experimental and simulated pressure."""
    return float(weight * np.sum((df["P_sample_bar"] - df["P_calc_bar"]) ** 2))
