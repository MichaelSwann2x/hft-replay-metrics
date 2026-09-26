from __future__ import annotations
import numpy as np

def estimate_queue_position(our_size: float, level_size: float, ahead: float = 0.0) -> dict:
    level_size = max(float(level_size), 1e-12)
    ahead = max(float(ahead), 0.0)
    our_size = max(float(our_size), 0.0)
    pos = ahead / level_size
    return {"queue_fraction": float(min(1.0, pos)), "ahead": ahead, "our_size": our_size, "level_size": level_size, "behind": max(0.0, level_size - ahead - our_size)}

def fill_probability(queue_fraction: float, trade_through: float, level_size: float) -> float:
    if level_size <= 0:
        return 0.0
    consumed = trade_through / level_size
    return float(np.clip(consumed - queue_fraction, 0.0, 1.0))
