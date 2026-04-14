from __future__ import annotations

import numpy as np


def compute_T2(T1: np.ndarray) -> np.ndarray:
    """Starter approximation for the line temperature."""
    return T1.copy()


def compute_T3(time_s: np.ndarray, T2: np.ndarray, tau3_s: float) -> np.ndarray:
    """First-order dynamic response for the upper-region effective temperature."""
    T3 = np.zeros_like(T2, dtype=float)
    if len(T2) == 0:
        return T3
    T3[0] = T2[0]
    for i in range(1, len(T2)):
        dt = max(float(time_s[i] - time_s[i - 1]), 1e-9)
        alpha = min(dt / max(tau3_s, 1e-9), 1.0)
        T3[i] = T3[i - 1] + alpha * (T2[i] - T3[i - 1])
    return T3
