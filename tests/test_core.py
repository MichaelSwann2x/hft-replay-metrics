import numpy as np
from hft_replay_metrics import estimate_queue_position, fill_probability, fee_tick_impact, session_summary

def test_queue():
    q = estimate_queue_position(0.002, 1.0, ahead=0.3)
    assert 0 <= q["queue_fraction"] <= 1

def test_fill_prob():
    p = fill_probability(0.2, trade_through=0.5, level_size=1.0)
    assert 0 <= p <= 1

def test_fee():
    f = fee_tick_impact(413_000, tick_size=0.1, price=60000, maker_fee_bps=2.0)
    assert f["fee_usd"] > 0

def test_session():
    s = session_summary(np.array([100.0, 200.0]), np.array([1.0, 2.0, 3.0]), np.array([5.0, 6.0]), price=60000, tick_size=0.1)
    assert s["n_fills"] == 2
