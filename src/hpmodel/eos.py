from __future__ import annotations


def density_placeholder(P_bar: float, T_C: float, z_co2: float) -> float:
    """Placeholder density model.

    Replace with Peng-Robinson or another chosen EOS wrapper.
    """
    T_K = T_C + 273.15
    return max(1e-6, 0.001 * P_bar / max(T_K, 1.0) * (1.0 + z_co2))
