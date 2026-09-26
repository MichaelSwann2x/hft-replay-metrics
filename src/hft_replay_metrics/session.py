from __future__ import annotations
import numpy as np
from .latency import latency_stats, fee_tick_impact

def session_summary(fills_notional: np.ndarray, feed_latency_ms: np.ndarray, order_latency_ms: np.ndarray, price: float, tick_size: float, maker_fee_bps: float = 2.0) -> dict:
    fills = np.asarray(fills_notional, dtype=float)
    total = float(fills.sum()) if fills.size else 0.0
    return {"n_fills": int(fills.size), "total_notional": total, "feed_latency": latency_stats(feed_latency_ms), "order_latency": latency_stats(order_latency_ms), "fees": fee_tick_impact(total, tick_size, price, maker_fee_bps=maker_fee_bps)}
