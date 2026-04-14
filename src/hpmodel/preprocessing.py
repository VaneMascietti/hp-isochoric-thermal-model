from __future__ import annotations

import pandas as pd


def standardize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with only the columns needed by the reduced model."""
    required = ["time_s", "P_sample_bar", "T_sample_C"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df.copy()
