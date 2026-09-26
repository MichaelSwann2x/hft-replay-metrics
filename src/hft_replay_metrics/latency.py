from __future__ import annotations
import numpy as np

def latency_stats(latencies_ms: np.ndarray) -> dict:
    x = np.asarray(latencies_ms, dtype=float)
    x = x[np.isfinite(x)]
    if x.size == 0:
        return {"n": 0, "mean": float("nan"), "p50": float("nan"), "p99": float("nan")}
    return {"n": int(x.size), "mean": float(x.mean()), "p50": float(np.percentile(x, 50)), "p99": float(np.percentile(x, 99)), "max": float(x.max())}

def fee_tick_impact(notional: float, tick_size: float, price: float, maker_fee_bps: float = 2.0, rebate_bps: float = 0.5) -> dict:
    if price <= 0 or tick_size <= 0:
        raise ValueError("price and tick_size must be positive")
    tick_bps = (tick_size / price) * 1e4
    fee_ticks = maker_fee_bps / tick_bps if tick_bps > 0 else float("inf")
    rebate_ticks = rebate_bps / tick_bps if tick_bps > 0 else float("inf")
    fee_usd = notional * (maker_fee_bps / 1e4)
    rebate_usd = notional * (rebate_bps / 1e4)
    return {"tick_bps": float(tick_bps), "fee_in_ticks": float(fee_ticks), "rebate_in_ticks": float(rebate_ticks), "fee_usd": float(fee_usd), "rebate_usd": float(rebate_usd), "net_fee_vs_rebate_usd": float(fee_usd - rebate_usd)}
