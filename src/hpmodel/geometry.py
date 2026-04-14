from __future__ import annotations

from dataclasses import dataclass
import yaml


@dataclass
class Geometry:
    V1_ml: float
    V2_ml: float
    V3_ml: float

    @classmethod
    def from_yaml(cls, path: str) -> "Geometry":
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return cls(
            V1_ml=float(data["cell"]["V1_ml"]),
            V2_ml=float(data["line"]["V2_ml"]),
            V3_ml=float(data["upper_region"]["V3_ml"]),
        )
