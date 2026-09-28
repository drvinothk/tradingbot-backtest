T = "D:/tb-renko-fix/backend/tests/"
def rd(p):
    raw = open(p, 'rb').read(); return raw.decode('utf-8').replace('\r\n', '\n'), b'\r\n' in raw
def wr(p, s, crlf): open(p, 'wb').write((s.replace('\n', '\r\n') if crlf else s).encode('utf-8'))
p = T + "unit/test_renko_dynamic_exit_spec.py"; s, crlf = rd(p)
assert s.count('        "no_progress_exit_candles": 0,\n    }') == 1
s = s.replace('        "no_progress_exit_candles": 0,\n    }', '        "no_progress_exit_candles": 0,\n        "candle_exit_confirm": 0,\n    }')
s = s.replace('        {"direction_filter_mode": "bogus"},\n', '        {"direction_filter_mode": "bogus"},\n        {"entry_mode": "candle_confirm"},\n        {"entry_mode": "candle_confirm", "entry_confirm_candles": 0},\n        {"entry_confirm_candles": 3},\n        {"entry_confirm_candles": -1},\n        {"candle_exit_confirm": -1},\n        {"candle_exit_confirm": 2, "reversal_exit_mode": "static"},\n')
s += '''

def test_spec_carries_candle_exit_confirm_and_candle_mode_constructs() -> None:
    s = _make(entry_mode="candle_confirm", entry_confirm_candles=3, candle_exit_confirm=3)
    spec = s.dynamic_reversal_exit_spec
    assert spec is not None
    assert spec["candle_exit_confirm"] == 3
    assert s.entry_confirm_candles == 3
'''
wr(p, s, crlf)
p = T + "integration/test_renko_trend_strategy.py"; s, crlf = rd(p)
s += '''

class TestCandleConfirmEntry:
    """2026-09-24: `entry_mode="candle_confirm"` -- brick trend + N consecutive
    rising/falling 1-minute closes. 1-minute bricks of 20pt (see `_strategy`);
    closes 24130 (seed), 24165 (up brick 1), 24185 (up brick 2): a confirmed
    up-trend from the third bar on, with the closes rising each bar.
    """

    def _play(self, db, instrument, ce, pe, ts, cfg, user, closes, **params):
        run = _run(db, strategy_config=cfg, trading_session=ts, user=user) if False else _run(db, cfg, ts, user)
        _seed_chain(db, instrument, ce, pe)
        _seed_first_candle(db, instrument, high=24110, low=24090)
        kwargs: dict[str, Any] = dict(
            ema_timeframe_minutes=1, ema_period=2, entry_mode="candle_confirm",
            direction_filter_mode="none",
        )
        kwargs.update(params)
        strategy = _strategy(instrument, **kwargs)
        fired_at = None
        for i, price in enumerate(closes):
            bar = _seed_bar(db, instrument, SESSION_OPEN + timedelta(minutes=3 + i),
                            o=price - 1, h=price + 1, low=price - 2, c=price)
            if strategy.check_setup(db, run, bar) is not None:
                fired_at = i
                break
        return fired_at

    def test_fires_only_after_n_consecutive_rising_closes(
        self, db, instrument, option_contract_ce, option_contract_pe, trading_session,
        strategy_config, user,
    ):
        args = (db, instrument, option_contract_ce, option_contract_pe, trading_session,
                strategy_config, user)
        # n=2: the bar at 24185 is the first whose previous two moves both rose.
        assert self._play(*args, [24130, 24165, 24185], entry_confirm_candles=2) == 2

    def test_n3_waits_for_a_fourth_rising_bar_with_no_new_brick(
        self, db, instrument, option_contract_ce, option_contract_pe, trading_session,
        strategy_config, user,
    ):
        args = (db, instrument, option_contract_ce, option_contract_pe, trading_session,
                strategy_config, user)
        # 24190 prints no brick (breakout mode would never fire on it) but is the
        # third consecutive rising close.
        assert self._play(*args, [24130, 24165, 24185, 24190], entry_confirm_candles=3) == 3

    def test_a_down_close_breaks_the_run(
        self, db, instrument, option_contract_ce, option_contract_pe, trading_session,
        strategy_config, user,
    ):
        args = (db, instrument, option_contract_ce, option_contract_pe, trading_session,
                strategy_config, user)
        assert self._play(*args, [24130, 24165, 24185, 24180], entry_confirm_candles=3) is None

    def test_ema_reference_is_still_required(
        self, db, instrument, option_contract_ce, option_contract_pe, trading_session,
        strategy_config, user,
    ):
        args = (db, instrument, option_contract_ce, option_contract_pe, trading_session,
                strategy_config, user)
        # an EMA500 never warms up -> the EMA-guided mode sits out
        assert self._play(*args, [24130, 24165, 24185, 24190], entry_confirm_candles=3,
                          direction_filter_mode="ema_crossover", ema_period=500) is None
'''
wr(p, s, crlf)
print('tests added')
