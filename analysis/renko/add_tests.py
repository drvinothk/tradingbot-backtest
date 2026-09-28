T = "D:/tb-renko-fix/backend/tests/"


def rd(p):
    raw = open(p, 'rb').read()
    return raw.decode('utf-8').replace('\r\n', '\n'), b'\r\n' in raw


def wr(p, s, crlf):
    open(p, 'wb').write((s.replace('\n', '\r\n') if crlf else s).encode('utf-8'))


# ---- spec test ----
p = T + "unit/test_renko_dynamic_exit_spec.py"
s, crlf = rd(p)
assert s.count('        "flat_exit_candles": 0,\n    }') == 1
s = s.replace('        "flat_exit_candles": 0,\n    }', '        "flat_exit_candles": 0,\n        "no_progress_exit_candles": 0,\n    }')
s += '''

def test_spec_carries_no_progress_exit_candles() -> None:
    spec = _make(no_progress_exit_candles=3).dynamic_reversal_exit_spec
    assert spec is not None
    assert spec["no_progress_exit_candles"] == 3


@pytest.mark.parametrize(
    "overrides",
    [
        {"no_progress_exit_candles": -1},
        {"no_progress_exit_candles": 2, "reversal_exit_mode": "static"},
        {"allowed_directions": "long"},
        {"max_move_from_open_points": 0},
        {"max_move_from_open_points": -5.0},
        {"min_flips_today": -1},
        {"direction_filter_mode": "none", "entry_mode": "pullback"},
        {"direction_filter_mode": "bogus"},
    ],
)
def test_new_params_are_validated(overrides: dict) -> None:
    with pytest.raises(ValueError):
        _make(**overrides)


def test_none_direction_filter_and_new_gates_construct() -> None:
    s = _make(
        direction_filter_mode="none",
        allowed_directions="pe",
        max_move_from_open_points=45.0,
        min_flips_today=1,
        no_progress_exit_candles=2,
    )
    assert s.allowed_directions == "pe"
    assert s.max_move_from_open_points == 45.0
    assert s.min_flips_today == 1
'''
if 'import pytest' not in s:
    s = s.replace('import uuid\n', 'import uuid\n', 1)
    s = s.replace('from datetime import date\n', 'from datetime import date\n\nimport pytest\n', 1)
wr(p, s, crlf)

# ---- unit helper tests ----
p = T + "unit/test_renko.py"
s, crlf = rd(p)
s += '''

class TestSessionContextHelpers:
    """2026-09-24: `count_direction_flips`, `move_from_open_ok`."""

    @staticmethod
    def _bricks(dirs):
        return [RenkoBrick(d, 0.0, 0.0, i) for i, d in enumerate(dirs)]

    def test_flips_counts_adjacent_direction_changes(self):
        assert count_direction_flips([]) == 0
        assert count_direction_flips(self._bricks(["up"])) == 0
        assert count_direction_flips(self._bricks(["up", "up", "up"])) == 0
        assert count_direction_flips(self._bricks(["up", "down"])) == 1
        assert count_direction_flips(self._bricks(["up", "up", "down", "down", "up"])) == 2

    def test_move_from_open_ce_uses_upward_distance(self):
        assert move_from_open_ok(True, 24140.0, 24100.0, 40.0)  # exactly at the cap passes
        assert not move_from_open_ok(True, 24141.0, 24100.0, 40.0)

    def test_move_from_open_pe_uses_downward_distance(self):
        assert move_from_open_ok(False, 24060.0, 24100.0, 40.0)
        assert not move_from_open_ok(False, 24059.0, 24100.0, 40.0)

    def test_move_against_the_trade_always_passes(self):
        assert move_from_open_ok(True, 24000.0, 24100.0, 10.0)  # CE, price below the open
        assert move_from_open_ok(False, 24200.0, 24100.0, 10.0)  # PE, price above the open
'''
if 'count_direction_flips' not in s.split('class ')[0]:
    # add to the import from app.modules.strategy_engine.renko
    import re
    m = re.search(r'from app\.modules\.strategy_engine\.renko import \((.*?)\)', s, re.S)
    assert m, 'renko import block not found'
    names = [n.strip() for n in m.group(1).split(',') if n.strip()]
    names += ['count_direction_flips', 'move_from_open_ok']
    if 'RenkoBrick' not in names:
        names.append('RenkoBrick')
    block = 'from app.modules.strategy_engine.renko import (\n' + ''.join(f'    {n},\n' for n in sorted(set(names))) + ')'
    s = s.replace(m.group(0), block)
wr(p, s, crlf)

# ---- integration tests ----
p = T + "integration/test_renko_trend_strategy.py"
s, crlf = rd(p)
s += '''

class TestSessionContextGates:
    """2026-09-24: `allowed_directions`, `max_move_from_open_points`,
    `min_flips_today`, `direction_filter_mode="none"`. brick_size=20 (see
    `_strategy`); the day opens at 24100 (`_seed_first_candle`). Box seeded
    by the first fed close 24130 -> [24120, 24140]; an up brick needs a close
    >= top+20, a down brick <= bottom-20.
    """

    UP_RUN = [(24130, None), (24165, None), (24185, None)]  # 2 up bricks -> CE, 85 pts above the open
    FLIP_RUN = [(24130, None), (24165, None), (24115, None), (24095, None)]  # up, down, down -> PE, 1 flip

    def _feed(self, db, instrument, run, strategy, bars):
        proposal = None
        for i, (price, low) in enumerate(bars):
            bar = _seed_bar(
                db,
                instrument,
                SESSION_OPEN + timedelta(minutes=3 + i),
                o=price - 1,
                h=price + 1,
                low=low if low is not None else price - 2,
                c=price,
            )
            proposal = strategy.check_setup(db, run, bar)
            if proposal is not None:
                break
        return proposal

    def _setup(self, db, instrument, ce, pe, trading_session, strategy_config, user):
        run = _run(db, strategy_config, trading_session, user)
        _seed_chain(db, instrument, ce, pe)
        _seed_first_candle(db, instrument, high=24110, low=24090)
        return run

    def _fires(self, db, instrument, ce, pe, ts, cfg, user, bars, **params):
        run = self._setup(db, instrument, ce, pe, ts, cfg, user)
        strategy = _strategy(instrument, ema_timeframe_minutes=1, ema_period=2, **params)
        return self._feed(db, instrument, run, strategy, bars) is not None

    def test_none_mode_fires_without_any_ema(
        self, db, instrument, option_contract_ce, option_contract_pe, trading_session,
        strategy_config, user,
    ):
        args = (db, instrument, option_contract_ce, option_contract_pe, trading_session,
                strategy_config, user, self.UP_RUN)
        # An EMA500 can never warm up -> the crossover mode sits out ...
        assert not self._fires(*args, direction_filter_mode="ema_crossover", ema_period=500)
        db.query(PriceBar).filter(PriceBar.instrument_id == instrument.id).delete()
        db.flush()
        # ... while "none" needs no reference level at all.
        assert self._fires(*args, direction_filter_mode="none", ema_period=500)

    def test_allowed_directions_blocks_the_other_side(
        self, db, instrument, option_contract_ce, option_contract_pe, trading_session,
        strategy_config, user,
    ):
        for allowed, fires in (("pe", False), ("ce", True), ("both", True)):
            assert self._fires(
                db, instrument, option_contract_ce, option_contract_pe, trading_session,
                strategy_config, user, self.UP_RUN, direction_filter_mode="none",
                allowed_directions=allowed,
            ) is fires
            db.query(PriceBar).filter(PriceBar.instrument_id == instrument.id).delete()
            db.flush()

    def test_max_move_from_open_refuses_a_chase(
        self, db, instrument, option_contract_ce, option_contract_pe, trading_session,
        strategy_config, user,
    ):
        # CE entry at close 24185 is 85 pts above the 24100 open.
        for cap, fires in ((50.0, False), (85.0, True), (100.0, True)):
            assert self._fires(
                db, instrument, option_contract_ce, option_contract_pe, trading_session,
                strategy_config, user, self.UP_RUN, direction_filter_mode="none",
                max_move_from_open_points=cap,
            ) is fires
            db.query(PriceBar).filter(PriceBar.instrument_id == instrument.id).delete()
            db.flush()

    def test_refused_chase_does_not_consume_the_signal_budget(
        self, db, instrument, option_contract_ce, option_contract_pe, trading_session,
        strategy_config, user,
    ):
        run = self._setup(db, instrument, option_contract_ce, option_contract_pe,
                          trading_session, strategy_config, user)
        strategy = _strategy(instrument, ema_timeframe_minutes=1, ema_period=2,
                             direction_filter_mode="none", max_move_from_open_points=50.0)
        assert self._feed(db, instrument, run, strategy, self.UP_RUN) is None
        assert strategy._signal_counts == {}

    def test_min_flips_today(
        self, db, instrument, option_contract_ce, option_contract_pe, trading_session,
        strategy_config, user,
    ):
        cases = (
            (self.UP_RUN, 1, False),    # a one-way day: 0 flips < 1
            (self.FLIP_RUN, 1, True),   # up, down, down: 1 flip
            (self.FLIP_RUN, 2, False),  # ... but not 2
        )
        for bars, need, fires in cases:
            assert self._fires(
                db, instrument, option_contract_ce, option_contract_pe, trading_session,
                strategy_config, user, bars, direction_filter_mode="none",
                min_flips_today=need,
            ) is fires
            db.query(PriceBar).filter(PriceBar.instrument_id == instrument.id).delete()
            db.flush()

    def test_pe_move_from_open_counts_downward_distance(
        self, db, instrument, option_contract_ce, option_contract_pe, trading_session,
        strategy_config, user,
    ):
        # PE fires at close 24095 = 5 pts BELOW the open: passes any sane cap.
        assert self._fires(
            db, instrument, option_contract_ce, option_contract_pe, trading_session,
            strategy_config, user, self.FLIP_RUN, direction_filter_mode="none",
            max_move_from_open_points=10.0,
        )
'''
wr(p, s, crlf)
print('tests added')
