from __future__ import annotations

from pathlib import Path
import pandas as pd


COLUMN_MAP = {
    0: "P_pump_bar",
    1: "V_pump_ml",
    2: "P_sample_bar",
    4: "T_sample_C",
    5: "T_oven_C",
    6: "HF_uV",
    7: "HF_mW",
}


def read_lvm(filepath: str | Path) -> pd.DataFrame:
    """Read a LabVIEW .lvm-like file into a DataFrame.

    This is a conservative starter implementation. Update the parser once the exact
    export format is fixed for the current acquisition files.
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Raw data file not found: {filepath}")

    df = pd.read_csv(filepath, sep=None, engine="python", comment="#", header=None)
    df = df.rename(columns={i: name for i, name in COLUMN_MAP.items() if i in df.columns})
    if "time_s" not in df.columns:
        df.insert(0, "time_s", range(len(df)))
    return df
