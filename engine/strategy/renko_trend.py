"""Modified Renko trend-following option-buying strategy — intraday, not
scalping (deliberately excludes the research spec's own "scalping" flavour,
per explicit user direction: Renko's whole point here is noise reduction
and holding positions longer, not fast in/out).

Built from a two-document user research spec (a Renko-based intraday
option-buying strategy spec, and its entry/exit refinement covering brick
construction + multi-timeframe sizing). Core idea: a brick size B is
derived from ATR on a **higher timeframe** (30-min/15-min/10-min, tunable —
`htf_timeframe_minutes`/`atr_period`), computed once per day from real,
multi-day-resampled candles (see `renko.resample_multi_day_htf`'s own
docstring for why ATR on a 30-min/1hr chart is inherently a multi-day
indicator, not an intraday-only one). That B then drives a Renko brick
series built from every 1-minute bar close for the rest of the day (see
`renko.py`'s module docstring for the 1-second/tick -> 1-minute-close
resolution substitution — no tick archive exists to backtest against).

**Structure**: the first `first_candle_minutes` (default 5) of the day
define a Point-of-Balance (Fib 50%) and Fib 38.2%/61.8% bands
(`renko.compute_fib_levels`) — a bullish (CE) setup requires price above
POB; a bearish (PE) setup requires price below it. `renko.trend_run_direction`
requires at least `confirm_bricks` (default 2) consecutive same-direction
bricks before a direction counts as "trend" at all — the spec's own QC
guidance against trading the first colour flip / checkerboard whipsaws.

**Two entry flavours, one class** (`entry_mode`), matching the spec's
"breakout strategy" and "pullback strategy" sections — same inputs
(bricks, Fib, EMA), different trigger:
- `"breakout"`: fires on the bar that completes the `confirm_bricks`-th
  consecutive brick in a direction (the earliest a "trend" exists at all).
- `"pullback"`: once a trend is confirmed, fires on a pullback that
  touches the Fib 38.2%-50% band and closes back through POB in the trend
  direction — reuses `common_rules.touch_and_confirm`'s exact touch/confirm
  mechanics (already proven by VWAP Pullback/EMA Micro-pullback), applied
  against the Fib POB reference instead of VWAP/EMA9. Allows more than one
  signal per direction per day (`max_signals_per_direction`), since a later
  pullback in a still-intact trend is a legitimately different setup, not
  a re-chase — same reasoning `id_ema.py`'s Supertrend-flip strategy gives
  for having no fired-direction latch, adapted here to a bounded count
  rather than unlimited (Section 7's own "cap trades per day" risk
  mitigation).

**Exit**: dual-layer per the spec's own QC ("exit when either hits, not
waiting for both") —
- premium-based (`stop_pct`/`target_pct`, `common_rules.compute_stop_target`,
  the spec's 25-35% premium-loss SL / 1-2 brick target translated to a
  premium %), plus the existing generic premium trail
  (`trail_activation_fraction`/`trail_lock_fraction` — the spec's brick-count
  TSL is approximated by this same existing mechanism, same documented
  approximation `atr_breakout.py`'s chandelier-trail note already uses for
  the identical reason: no bespoke brick-based trailing engine exists, and
  building one is out of this pass's scope).
- index-structural (`structure_level`): the spec's "Fib 61.8% break against
  you = hard invalidation, independent of brick SL." Since Fib here is
  anchored `low=0%/high=100%` on the first candle, "the far band opposite
  your entry side" is Fib 38.2% for a CE (bullish, entered above the 50%
  POB) and Fib 61.8% for a PE (bearish, entered below POB) — symmetric
  counterparts (100-61.8=38.2) of the same "give back more than the far
  retracement band" concept the spec states in PE/general terms. Checked
  via the same buffered/persistence-confirmed structure-break machinery
  every other strategy here uses (`resolve_structure_break_buffer`,
  1-minute ATR14-derived noise buffer — never a single-tick fire).

**Day-scoped state, not run-scoped**: unlike ORB/ATRBreakout's
`_fired_directions` (documented in `run_backtest.py`'s own module
docstring as persisting for the whole backtest run, not resetting daily —
an accepted fidelity limitation for those strategies), every Renko-specific
concept here (bricks, Fib/POB, brick size, signal counts) is inherently a
per-trading-day concept, so this strategy explicitly resets all of it the
moment the evaluated bar's IST calendar date changes from the last one
seen — self-contained, needs no harness support, and is strictly more
faithful to what the spec actually describes (a new brick series/Fib
anchor every session) than reusing the run-scoped convention would be.

**No-trade filters** (spec Section 5/7): a whole day is skipped if the
computed brick size falls outside `[min_brick_size, max_brick_size]` for
the underlying (too narrow = chop the spec says Renko performs poorly in;
too wide = an already-extreme/gap day) — the fixed-B sanity-band and
low-volatility-day guards folded into one check, picked by underlying via
the existing `pick_by_underlying` convention. `entry_start_time`/
`entry_cutoff_time` bound the trading window (mirrors `atr_breakout.py`).
Gap-open protection is structural: no Fib/POB exists (and therefore no
entry is possible) until the first candle completes.

**2026-09-22 extension — three more axes, all additive/opt-in (every
default preserves the exact behaviour above byte-for-byte)**, added for a
follow-up user variant: a fixed (not ATR-derived) brick size at a small,
non-adaptive point value, bricks built directly from a resampled 5-min/
15-min candle series instead of every 1-minute close, a single EMA
crossover deciding direction instead of Fib/POB, and an explicit
brick-reversal exit.
- `brick_size_mode` (`"atr"`/`"fixed"`) + `fixed_brick_size_points`: a
  fixed value skips the ATR sanity-band check entirely (that check exists
  to catch a bad *derived* value — a human-chosen fixed value doesn't need
  it, and the band defaults are tuned for ATR-scale bricks, not a
  deliberately small fixed one).
- `brick_source_timeframe_minutes` (default 1, byte-identical to before):
  when >1, the brick engine updates only on real HTF-boundary closes
  (`higher_timeframe.is_htf_boundary_close`), fed that boundary's own
  resampled candle close, not every 1-minute bar — genuinely different
  bricks from a genuinely coarser series, not just a slower-updating view
  of the same 1-minute bricks.
- `direction_filter_mode` (`"fib_pob"`/`"ema_crossover"`): in
  `"ema_crossover"`, the resampled EMA value (not Fib POB) is the
  reference level `_breakout_signal`/`_pullback_signal` compare price
  against, and the separate EMA confirmation gate is skipped (it would
  just be checking the same condition twice).
- `exit_on_reversal` + `reversal_confirm_bricks` (defaults to
  `confirm_bricks`): overrides the Fib 38.2%/61.8% `structure_level` with
  the price level at which `reversal_confirm_bricks` bricks would have
  printed *against* the held direction — "confirm at least 2 previous
  boxes... or reverse, then exit," computed directly from the live
  `RenkoState`'s own box boundaries at signal-fire time
  (`_reversal_structure_level`), not a new exit-engine concept: still a
  single static price level through the same buffered/persistence-
  confirmed `structure_level` machinery every other strategy here uses.
"""

from __future__ import annotations

import logging
import uuid
from datetime import date, datetime, time, timedelta

from sqlalchemy.orm import Session

from app.core.clock import IST, to_ist
from app.domain.market.models import Instrument, OptionType, PriceBar
from app.domain.strategy.models import SignalSide, StrategyRun
from app.modules.market_data.indicators import Bar
from app.modules.market_data.market_hours import NORMAL_MARKET_OPEN
from app.modules.strategy_engine.common_rules import (
    BAR_TIMEFRAME,
    DEFAULT_STRUCTURE_BREAK_ATR_MULTIPLIER,
    DEFAULT_STRUCTURE_BREAK_PERSISTENCE_SECONDS,
    ConfirmationFilterStrategy,
    _parse_hhmm,
    compute_stop_target,
    get_recent_completed_bars,
    pick_by_underlying,
    resolve_structure_break_buffer,
    touch_and_confirm,
)
from app.modules.strategy_engine.env_metrics import get_latest_env_metrics
from app.modules.strategy_engine.higher_timeframe import (
    compute_atr_series,
    compute_ema_series,
    is_htf_boundary_close,
    resample_to_htf,
)
from app.modules.strategy_engine.interface import TradePayload, TradeProposal
from app.modules.strategy_engine.renko import (
    BrickDirection,
    FibLevels,
    RenkoBrick,
    RenkoState,
    compute_fib_levels,
    count_direction_flips,
    ema_side_ok,
    entry_run_allowed,
    move_from_open_ok,
    resample_multi_day_htf,
    trend_run_direction,
    trend_run_length,
)
from app.modules.strategy_engine.strike_ranking.engine import (
    StrikeRankingConfig,
    pick_top_by_type,
    rank_from_latest_snapshot,
)

logger = logging.getLogger("app.strategy_engine.renko_trend")

RENKO_TREND_PARAM_KEYS = {
    "qty_lots",
    "htf_timeframe_minutes",
    "atr_period",
    "atr_lookback_days",
    "brick_atr_multiplier",
    "brick_size_mode",
    "fixed_brick_size_points",
    "brick_source_timeframe_minutes",
    "min_brick_size_nifty_points",
    "max_brick_size_nifty_points",
    "min_brick_size_banknifty_points",
    "max_brick_size_banknifty_points",
    "confirm_bricks",
    "first_candle_minutes",
    "ema_timeframe_minutes",
    "ema_period",
    "ema_lookback_days",
    "entry_mode",
    "direction_filter_mode",
    "pullback_tolerance_frac",
    "max_signals_per_direction",
    "stop_pct",
    "target_pct",
    "trail_activation_fraction",
    "trail_lock_fraction",
    "structure_break_atr_multiplier",
    "structure_break_persistence_seconds",
    "exit_on_reversal",
    "reversal_confirm_bricks",
    "reversal_exit_mode",
    "flat_exit_candles",
    "entry_run_rule",
    "ema_cross_lookback_candles",
    "ema_candle_position",
    "no_progress_exit_candles",
    "entry_confirm_candles",
    "candle_exit_confirm",
    "breakeven_after_bricks",
    "allowed_directions",
    "max_move_from_open_points",
    "min_flips_today",
    "entry_start_time",
    "entry_cutoff_time",
}


def _fetch_bars_by_day(
    db: Session, instrument_id: uuid.UUID, timeframe: str, since: datetime, until: datetime
) -> dict[date, list[PriceBar]]:
    bars = get_recent_completed_bars(db, instrument_id, timeframe, since=since, until=until)
    by_day: dict[date, list[PriceBar]] = {}
    for bar in bars:
        by_day.setdefault(to_ist(bar.bucket_start).date(), []).append(bar)
    return by_day


class RenkoTrendStrategy(ConfirmationFilterStrategy):
    def __init__(
        self,
        instrument_id: uuid.UUID,
        expiry_date: date,
        ranking_config: StrikeRankingConfig = StrikeRankingConfig(),
        qty_lots: int = 1,
        htf_timeframe_minutes: int = 30,
        atr_period: int = 14,
        atr_lookback_days: int = 20,
        brick_atr_multiplier: float = 1.0,
        brick_size_mode: str = "atr",
        fixed_brick_size_points: float | None = None,
        brick_source_timeframe_minutes: int = 1,
        min_brick_size_nifty_points: float = 10.0,
        max_brick_size_nifty_points: float = 60.0,
        min_brick_size_banknifty_points: float = 30.0,
        max_brick_size_banknifty_points: float = 180.0,
        confirm_bricks: int = 2,
        first_candle_minutes: int = 5,
        ema_timeframe_minutes: int = 5,
        ema_period: int = 10,
        ema_lookback_days: int = 20,
        entry_mode: str = "breakout",
        direction_filter_mode: str = "fib_pob",
        pullback_tolerance_frac: float = 0.0015,
        max_signals_per_direction: int = 1,
        stop_pct: float = 0.30,
        target_pct: float = 0.40,
        trail_activation_fraction: float = 0.4,
        trail_lock_fraction: float = 0.4,
        structure_break_atr_multiplier: float = DEFAULT_STRUCTURE_BREAK_ATR_MULTIPLIER,
        structure_break_persistence_seconds: float = DEFAULT_STRUCTURE_BREAK_PERSISTENCE_SECONDS,
        exit_on_reversal: bool = False,
        reversal_confirm_bricks: int | None = None,
        reversal_exit_mode: str = "static",
        flat_exit_candles: int = 0,
        entry_run_rule: str = "any",
        ema_cross_lookback_candles: int = 1,
        ema_candle_position: str = "close",
        no_progress_exit_candles: int = 0,
        entry_confirm_candles: int = 0,
        candle_exit_confirm: int = 0,
        breakeven_after_bricks: int = 0,
        allowed_directions: str = "both",
        max_move_from_open_points: float | None = None,
        min_flips_today: int = 0,
        entry_start_time: str = "09:30",
        entry_cutoff_time: str = "14:30",
    ) -> None:
        super().__init__(instrument_id, BAR_TIMEFRAME)
        if entry_mode not in ("breakout", "pullback", "candle_confirm"):
            raise ValueError(
                f"entry_mode must be 'breakout', 'pullback' or 'candle_confirm', got {entry_mode!r}"
            )
        if entry_mode == "candle_confirm" and entry_confirm_candles < 1:
            raise ValueError("entry_mode='candle_confirm' requires entry_confirm_candles >= 1")
        if entry_confirm_candles < 0:
            raise ValueError("entry_confirm_candles must be >= 0")
        if entry_confirm_candles > 0 and entry_mode != "candle_confirm":
            raise ValueError("entry_confirm_candles > 0 requires entry_mode='candle_confirm'")
        if breakeven_after_bricks < 0:
            raise ValueError("breakeven_after_bricks must be >= 0")
        if breakeven_after_bricks > 0 and reversal_exit_mode != "dynamic":
            raise ValueError("breakeven_after_bricks > 0 requires reversal_exit_mode='dynamic'")
        if candle_exit_confirm < 0:
            raise ValueError("candle_exit_confirm must be >= 0")
        if candle_exit_confirm > 0 and reversal_exit_mode != "dynamic":
            raise ValueError("candle_exit_confirm > 0 requires reversal_exit_mode='dynamic'")
        if brick_size_mode not in ("atr", "fixed"):
            raise ValueError(f"brick_size_mode must be 'atr' or 'fixed', got {brick_size_mode!r}")
        if brick_size_mode == "fixed" and fixed_brick_size_points is None:
            raise ValueError("fixed_brick_size_points is required when brick_size_mode='fixed'")
        if direction_filter_mode not in ("fib_pob", "ema_crossover", "none"):
            raise ValueError(
                f"direction_filter_mode must be 'fib_pob', 'ema_crossover' or 'none', "
                f"got {direction_filter_mode!r}"
            )
        if direction_filter_mode == "none" and entry_mode == "pullback":
            raise ValueError("direction_filter_mode='none' does not support entry_mode='pullback'")
        if reversal_exit_mode not in ("static", "dynamic"):
            raise ValueError(
                f"reversal_exit_mode must be 'static' or 'dynamic', got {reversal_exit_mode!r}"
            )
        if no_progress_exit_candles < 0:
            raise ValueError("no_progress_exit_candles must be >= 0")
        if no_progress_exit_candles > 0 and reversal_exit_mode != "dynamic":
            raise ValueError("no_progress_exit_candles > 0 requires reversal_exit_mode='dynamic'")
        if allowed_directions not in ("both", "ce", "pe"):
            raise ValueError(
                f"allowed_directions must be 'both', 'ce' or 'pe', got {allowed_directions!r}"
            )
        if max_move_from_open_points is not None and max_move_from_open_points <= 0:
            raise ValueError("max_move_from_open_points must be > 0 when set")
        if min_flips_today < 0:
            raise ValueError("min_flips_today must be >= 0")
        if reversal_exit_mode == "dynamic" and not exit_on_reversal:
            raise ValueError("reversal_exit_mode='dynamic' requires exit_on_reversal=True")
        if reversal_exit_mode == "dynamic" and brick_size_mode != "fixed":
            raise ValueError(
                "reversal_exit_mode='dynamic' requires brick_size_mode='fixed' -- the backtest "
                "engine rebuilds the brick series from one constant brick size"
            )
        if flat_exit_candles < 0:
            raise ValueError("flat_exit_candles must be >= 0")
        if flat_exit_candles > 0 and reversal_exit_mode != "dynamic":
            raise ValueError("flat_exit_candles > 0 requires reversal_exit_mode='dynamic'")
        if entry_run_rule not in ("any", "fresh", "fresh_or_cross"):
            raise ValueError(
                f"entry_run_rule must be 'any', 'fresh' or 'fresh_or_cross', got {entry_run_rule!r}"
            )
        if entry_run_rule == "fresh_or_cross" and direction_filter_mode != "ema_crossover":
            raise ValueError(
                "entry_run_rule='fresh_or_cross' requires direction_filter_mode='ema_crossover'"
            )
        if ema_cross_lookback_candles < 1:
            raise ValueError("ema_cross_lookback_candles must be >= 1")
        if ema_candle_position not in ("close", "extreme"):
            raise ValueError(
                f"ema_candle_position must be 'close' or 'extreme', got {ema_candle_position!r}"
            )
        if ema_candle_position == "extreme" and (
            direction_filter_mode != "ema_crossover" or entry_mode != "breakout"
        ):
            raise ValueError(
                "ema_candle_position='extreme' requires direction_filter_mode='ema_crossover' "
                "and entry_mode='breakout'"
            )
        self.expiry_date = expiry_date
        self.ranking_config = ranking_config
        self.qty_lots = qty_lots
        self.htf_timeframe_minutes = htf_timeframe_minutes
        self.atr_period = atr_period
        self.atr_lookback_days = atr_lookback_days
        self.brick_atr_multiplier = brick_atr_multiplier
        self.brick_size_mode = brick_size_mode
        self.fixed_brick_size_points = fixed_brick_size_points
        self.brick_source_timeframe_minutes = brick_source_timeframe_minutes
        self.min_brick_size_nifty_points = min_brick_size_nifty_points
        self.max_brick_size_nifty_points = max_brick_size_nifty_points
        self.min_brick_size_banknifty_points = min_brick_size_banknifty_points
        self.max_brick_size_banknifty_points = max_brick_size_banknifty_points
        self.confirm_bricks = confirm_bricks
        self.first_candle_minutes = first_candle_minutes
        self.ema_timeframe_minutes = ema_timeframe_minutes
        self.ema_period = ema_period
        self.ema_lookback_days = ema_lookback_days
        self.entry_mode = entry_mode
        self.direction_filter_mode = direction_filter_mode
        self.pullback_tolerance_frac = pullback_tolerance_frac
        self.max_signals_per_direction = max_signals_per_direction
        self.stop_pct = stop_pct
        self.target_pct = target_pct
        self.trail_activation_fraction = trail_activation_fraction
        self.trail_lock_fraction = trail_lock_fraction
        self.structure_break_atr_multiplier = structure_break_atr_multiplier
        self.structure_break_persistence_seconds = structure_break_persistence_seconds
        self.exit_on_reversal = exit_on_reversal
        self.reversal_confirm_bricks = reversal_confirm_bricks
        self.reversal_exit_mode = reversal_exit_mode
        self.flat_exit_candles = flat_exit_candles
        self.entry_run_rule = entry_run_rule
        self.ema_cross_lookback_candles = ema_cross_lookback_candles
        self.ema_candle_position = ema_candle_position
        self.no_progress_exit_candles = no_progress_exit_candles
        self.entry_confirm_candles = entry_confirm_candles
        self.candle_exit_confirm = candle_exit_confirm
        self.breakeven_after_bricks = breakeven_after_bricks
        self.allowed_directions = allowed_directions
        self.max_move_from_open_points = max_move_from_open_points
        self.min_flips_today = min_flips_today
        self.entry_start_time = _parse_hhmm(entry_start_time)
        self.entry_cutoff_time = _parse_hhmm(entry_cutoff_time)

        # Day-scoped state -- see module docstring "Day-scoped state, not
        # run-scoped". Reset in full whenever `_roll_day` sees the bar's
        # calendar date change.
        self._current_day: date | None = None
        self._brick_size: float | None = None
        self._day_disabled = False
        self._renko: RenkoState | None = None
        self._fib: FibLevels | None = None
        self._signal_counts: dict[OptionType, int] = {}
        self._day_open: float | None = None

    def _brick_size_band(self, symbol: str) -> tuple[float, float]:
        return pick_by_underlying(
            symbol,
            nifty=(self.min_brick_size_nifty_points, self.max_brick_size_nifty_points),
            banknifty=(self.min_brick_size_banknifty_points, self.max_brick_size_banknifty_points),
        )

    def _roll_day(self, bar_day: date) -> None:
        if bar_day == self._current_day:
            return
        self._current_day = bar_day
        self._brick_size = None
        self._day_disabled = False
        self._renko = None
        self._fib = None
        self._signal_counts = {}
        self._day_open = None
        self._logged_keys = set()  # a new day's skip reasons deserve fresh log lines

    def _resolve_brick_size(self, db: Session, symbol: str, day: date) -> float | None:
        """Multi-day HTF ATR -> brick size, computed once per day from
        bars strictly before `day` (see module docstring). `None` if not
        enough prior-day history exists yet (early in the archive) —
        callers treat this as "sit out today", not an error.

        `brick_size_mode="fixed"` skips all of this and returns
        `fixed_brick_size_points` directly, with no band check -- see the
        module docstring's 2026-09-22 extension note for why.
        """
        if self.brick_size_mode == "fixed":
            assert self.fixed_brick_size_points is not None  # validated in __init__
            return self.fixed_brick_size_points
        day_start = datetime.combine(day, time.min, tzinfo=IST)
        since = day_start - timedelta(days=self.atr_lookback_days)
        bars_by_day = _fetch_bars_by_day(db, self.instrument_id, self.timeframe, since, day_start)
        candles = resample_multi_day_htf(
            bars_by_day, self.htf_timeframe_minutes * 60, NORMAL_MARKET_OPEN
        )
        atr_values = compute_atr_series(candles, self.atr_period)
        if not atr_values:
            return None
        brick_size = atr_values[-1] * self.brick_atr_multiplier
        min_band, max_band = self._brick_size_band(symbol)
        if not (min_band <= brick_size <= max_band):
            self._log_once(
                logger,
                "brick_size_out_of_band",
                "%s-min ATR%d brick size %.2f outside [%.2f, %.2f] for %s -- sitting out today",
                self.htf_timeframe_minutes,
                self.atr_period,
                brick_size,
                min_band,
                max_band,
                symbol,
            )
            return None
        return brick_size

    def _update_renko(self, db: Session, latest_bar: PriceBar, bar_day: date) -> list[RenkoBrick]:
        """Feeds the brick engine and returns whatever new bricks this call
        produced (possibly empty). `brick_source_timeframe_minutes=1`
        (default) is byte-identical to the original design: every
        1-minute close feeds the engine directly. `>1` only feeds it on a
        real HTF-boundary close (`is_htf_boundary_close`), using that
        boundary's own resampled candle close -- genuinely coarser bricks,
        not a slower-updating view of the same 1-minute ones.
        """
        assert self._brick_size is not None
        if self.brick_source_timeframe_minutes == 1:
            if self._renko is None:
                self._renko = RenkoState.seed(float(latest_bar.close), self._brick_size)
            return self._renko.update(float(latest_bar.close))

        htf_seconds = self.brick_source_timeframe_minutes * 60
        if not is_htf_boundary_close(latest_bar.bucket_start, htf_seconds, NORMAL_MARKET_OPEN):
            return []
        day_start = datetime.combine(bar_day, NORMAL_MARKET_OPEN, tzinfo=IST)
        bars = get_recent_completed_bars(
            db,
            self.instrument_id,
            self.timeframe,
            since=day_start,
            until=latest_bar.bucket_start + timedelta(seconds=60),
        )
        candles = resample_to_htf(bars, htf_seconds, NORMAL_MARKET_OPEN)
        if not candles:
            return []
        candle_close = candles[-1].close
        if self._renko is None:
            self._renko = RenkoState.seed(candle_close, self._brick_size)
        return self._renko.update(candle_close)

    @property
    def dynamic_reversal_exit_spec(self) -> dict[str, float | int] | None:
        """2026-09-23: backtest-engine hook (read via `getattr(strategy_obj,
        "dynamic_reversal_exit_spec", None)`, the same pattern as
        `max_loss_per_lot`/`time_stop_minutes`) for the *dynamic* Renko
        exit: exit as soon as `n` COMPLETED reverse bricks have printed
        against the held direction since entry, evaluated only on
        `brick_source_timeframe_minutes` candle closes -- i.e. the exit level
        follows the brick series (each new favourable brick lifts it) instead
        of the static, fixed-at-signal-time `structure_level` (which, after a
        long run, sits far behind price and gives most of the trend back).
        `None` unless `reversal_exit_mode="dynamic"`. The static
        `structure_level` is still put on the `TradeProposal` as the fallback
        for any consumer that doesn't understand the dynamic exit (live/paper
        `PositionManager` today); the backtest engine ignores it when this
        spec is present.
        """
        if self.reversal_exit_mode != "dynamic":
            return None
        assert self.fixed_brick_size_points is not None  # validated in __init__
        n = (
            self.reversal_confirm_bricks
            if self.reversal_confirm_bricks is not None
            else self.confirm_bricks
        )
        return {
            "brick_size": float(self.fixed_brick_size_points),
            "timeframe_minutes": int(self.brick_source_timeframe_minutes),
            "confirm_bricks": int(n),
            "flat_exit_candles": int(self.flat_exit_candles),
            "no_progress_exit_candles": int(self.no_progress_exit_candles),
            "candle_exit_confirm": int(self.candle_exit_confirm),
            "breakeven_after_bricks": int(self.breakeven_after_bricks),
        }

    def _reversal_structure_level(self, option_type: OptionType) -> float:
        """The price level at which `reversal_confirm_bricks` bricks would
        have printed *against* the held direction, computed from the live
        `RenkoState`'s own current box boundaries at signal-fire time --
        "confirm at least 2 previous boxes... or reverse, then exit" (see
        module docstring's 2026-09-22 extension note). N consecutive
        bricks against a box with bottom/top `B` require price to reach
        `B -/+ N * brick_size` (see `RenkoState.update`'s own continuation
        condition), so this is exact, not an approximation.
        """
        assert self._renko is not None
        n = (
            self.reversal_confirm_bricks
            if self.reversal_confirm_bricks is not None
            else self.confirm_bricks
        )
        if option_type == OptionType.CE:
            return self._renko.bottom - n * self._renko.brick_size
        return self._renko.top + n * self._renko.brick_size

    def check_setup(
        self, db: Session, strategy_run: StrategyRun, latest_bar: PriceBar
    ) -> TradeProposal | None:
        bar_ist = to_ist(latest_bar.bucket_start)
        bar_day = bar_ist.date()
        self._roll_day(bar_day)

        if self._day_disabled:
            return None

        instrument = db.get(Instrument, self.instrument_id)
        symbol = instrument.symbol if instrument is not None else ""

        if self._brick_size is None:
            resolved = self._resolve_brick_size(db, symbol, bar_day)
            if resolved is None:
                self._day_disabled = True
                self._log_once(
                    logger,
                    "brick_size_not_ready",
                    "run %s: brick size not resolvable yet (%s-min ATR%d needs "
                    "%d prior trading days) -- sitting out",
                    strategy_run.id,
                    self.htf_timeframe_minutes,
                    self.atr_period,
                    self.atr_lookback_days,
                )
                return None
            self._brick_size = resolved
            logger.info(
                "run %s: %s brick size resolved for %s -- B=%.2f (%s-min ATR%d x %.2f)",
                strategy_run.id,
                symbol,
                bar_day.isoformat(),
                self._brick_size,
                self.htf_timeframe_minutes,
                self.atr_period,
                self.brick_atr_multiplier,
            )

        assert self._brick_size is not None
        new_bricks = self._update_renko(db, latest_bar, bar_day)

        if self._fib is None:
            day_start = datetime.combine(bar_day, NORMAL_MARKET_OPEN, tzinfo=IST)
            window_end = day_start + timedelta(minutes=self.first_candle_minutes)
            if latest_bar.bucket_start < window_end:
                return None  # still inside the first candle
            first_bars = get_recent_completed_bars(
                db, self.instrument_id, self.timeframe, since=day_start, until=window_end
            )
            if len(first_bars) < self.first_candle_minutes:
                self._log_once(
                    logger,
                    "first_candle_gap",
                    "run %s: gap in the first %d-minute candle -- sitting out today",
                    strategy_run.id,
                    self.first_candle_minutes,
                )
                self._day_disabled = True
                return None
            high = max(float(b.high) for b in first_bars)
            low = min(float(b.low) for b in first_bars)
            fib = compute_fib_levels(high, low)
            if fib is None:
                self._log_once(
                    logger,
                    "first_candle_flat",
                    "run %s: first %d-minute candle has zero range -- sitting out today",
                    strategy_run.id,
                    self.first_candle_minutes,
                )
                self._day_disabled = True
                return None
            self._fib = fib
            logger.info(
                "run %s: POB/Fib resolved for %s -- low=%.2f high=%.2f POB=%.2f",
                strategy_run.id,
                bar_day.isoformat(),
                fib.low,
                fib.high,
                fib.pob,
            )

        if not (self.entry_start_time <= bar_ist.time() <= self.entry_cutoff_time):
            return None

        if self._renko is None:
            return None  # brick_source_timeframe_minutes > 1, no HTF candle yet today
        assert self._fib is not None
        trend = trend_run_direction(self._renko.bricks, self.confirm_bricks)
        if trend is None:
            self._log_once(
                logger,
                "no_confirmed_trend",
                "run %s: no confirmed (>= %d consecutive) brick run yet",
                strategy_run.id,
                self.confirm_bricks,
            )
            return None

        close = float(latest_bar.close)
        fib = self._fib

        if self.direction_filter_mode == "ema_crossover":
            ema_tail = self._resolve_ema_tail(
                db,
                latest_bar,
                bar_day,
                self.ema_cross_lookback_candles + 1
                if self.entry_run_rule == "fresh_or_cross"
                else 1,
            )
            if ema_tail is None:
                self._log_once(
                    logger,
                    "ema_not_ready",
                    "run %s: resampled %d-min EMA%d not warmed up yet",
                    strategy_run.id,
                    self.ema_timeframe_minutes,
                    self.ema_period,
                )
                return None
            reference_level = ema_tail[-1][1]
        elif self.direction_filter_mode == "none":
            ema_tail = None
            reference_level = 0.0  # unused -- no reference level in "none" mode
        else:
            ema_tail = None
            reference_level = fib.pob

        option_type: OptionType | None = None
        if self.entry_mode == "breakout" and self.direction_filter_mode == "none":
            option_type = self._brick_only_signal(new_bricks, trend)
        elif self.entry_mode == "breakout":
            extreme = ema_tail is not None and self.ema_candle_position == "extreme"
            option_type = self._breakout_signal(
                new_bricks,
                trend,
                close,
                reference_level,
                candle_low=ema_tail[-1][0].low if extreme else None,  # type: ignore[index]
                candle_high=ema_tail[-1][0].high if extreme else None,  # type: ignore[index]
            )
        elif self.entry_mode == "candle_confirm":
            option_type = self._candle_confirm_signal(
                db,
                trend,
                close,
                reference_level,
                use_reference=self.direction_filter_mode != "none",
            )
        else:
            option_type = self._pullback_signal(db, trend, close, reference_level)

        if option_type is None:
            return None

        if (
            self.allowed_directions != "both"
            and option_type.value.lower() != self.allowed_directions
        ):
            self._log_once(
                logger,
                f"direction_not_allowed_{option_type.value}",
                "run %s: %s rejected -- allowed_directions=%s",
                strategy_run.id,
                option_type.value,
                self.allowed_directions,
            )
            return None

        if self._signal_counts.get(option_type, 0) >= self.max_signals_per_direction:
            return None

        if self.entry_run_rule != "any":
            run_length = trend_run_length(self._renko.bricks)
            fresh_cross = (
                self._ema_fresh_cross(ema_tail, option_type == OptionType.CE)
                if ema_tail is not None and self.entry_run_rule == "fresh_or_cross"
                else False
            )
            if not entry_run_allowed(
                self.entry_run_rule, run_length, self.confirm_bricks, fresh_cross
            ):
                self._log_once(
                    logger,
                    "run_not_fresh",
                    "run %s: %s rejected -- brick run of %d is not fresh (entry_run_rule=%s, "
                    "no fresh EMA cross)",
                    strategy_run.id,
                    option_type.value,
                    run_length,
                    self.entry_run_rule,
                )
                return None

        if self.max_move_from_open_points is not None:
            day_open = self._resolve_day_open(db, latest_bar, bar_day)
            if day_open is None:
                return None
            if not move_from_open_ok(
                option_type == OptionType.CE, close, day_open, self.max_move_from_open_points
            ):
                self._log_once(
                    logger,
                    f"move_from_open_{option_type.value}",
                    "run %s: %s rejected -- already moved > %.0f pts from the day's open %.2f "
                    "(close %.2f)",
                    strategy_run.id,
                    option_type.value,
                    self.max_move_from_open_points,
                    day_open,
                    close,
                )
                return None

        if self.min_flips_today > 0:
            flips = count_direction_flips(self._renko.bricks)
            if flips < self.min_flips_today:
                self._log_once(
                    logger,
                    f"too_few_flips_{option_type.value}",
                    "run %s: %s rejected -- only %d direction flip(s) in today's bricks "
                    "(min_flips_today=%d)",
                    strategy_run.id,
                    option_type.value,
                    flips,
                    self.min_flips_today,
                )
                return None

        if self.direction_filter_mode == "fib_pob":
            ema_ok: bool | None = self._ema_filter_ok(db, latest_bar, bar_day, option_type)
        else:
            ema_ok = True  # already decided by the crossover itself
        if ema_ok is None:
            self._log_once(
                logger,
                "ema_not_ready",
                "run %s: resampled %d-min EMA%d not warmed up yet",
                strategy_run.id,
                self.ema_timeframe_minutes,
                self.ema_period,
            )
            return None
        if not ema_ok:
            self._log_once(
                logger,
                f"ema_filter_{option_type.value}",
                "run %s: %s rejected -- %d-min EMA%d filter disagrees",
                strategy_run.id,
                option_type.value,
                self.ema_timeframe_minutes,
                self.ema_period,
            )
            return None

        if self.exit_on_reversal:
            structure_level = self._reversal_structure_level(option_type)
        else:
            structure_level = fib.fib_382 if option_type == OptionType.CE else fib.fib_618

        ranked = rank_from_latest_snapshot(
            db, self.instrument_id, self.expiry_date, self.ranking_config
        )
        top = pick_top_by_type(ranked, option_type)
        if top is None:
            return None

        self._signal_counts[option_type] = self._signal_counts.get(option_type, 0) + 1

        entry_price = top.ltp
        tick_size = float(instrument.tick_size) if instrument is not None else 0.0
        stop_price, target_price = compute_stop_target(
            entry_price, self.stop_pct, self.target_pct, tick_size
        )

        logger.info(
            "run %s: %s Renko %s entry fired -- brick_size=%.2f trend_run=%d close=%.2f "
            "POB=%.2f entry=%.2f stop=%.2f target=%.2f",
            strategy_run.id,
            option_type.value,
            self.entry_mode,
            self._renko.brick_size,
            len(self._renko.bricks),
            close,
            fib.pob,
            entry_price,
            stop_price,
            target_price,
        )

        payload: TradePayload = {
            "strategy": "renko_trend",
            "env": get_latest_env_metrics(db, self.instrument_id, self.expiry_date),
        }
        return TradeProposal(
            option_contract_id=top.option_contract_id,
            side=SignalSide.BUY,
            qty_lots=self.qty_lots,
            entry_price=entry_price,
            stop_price=stop_price,
            target_price=target_price,
            trail_activation_fraction=self.trail_activation_fraction,
            trail_lock_fraction=self.trail_lock_fraction,
            structure_level=structure_level,
            structure_break_buffer=resolve_structure_break_buffer(
                db, self.instrument_id, self.structure_break_atr_multiplier, self.timeframe
            ),
            structure_break_persistence_seconds=self.structure_break_persistence_seconds,
            payload=payload,
        )

    def _breakout_signal(
        self,
        new_bricks: list[RenkoBrick],
        trend: BrickDirection,
        close: float,
        reference_level: float,
        *,
        candle_low: float | None = None,
        candle_high: float | None = None,
    ) -> OptionType | None:
        """Fires on the bar that just printed a brick completing the
        confirmed trend run, provided price already clears `reference_level`
        (Fib POB, or the EMA crossover value -- see `direction_filter_mode`).
        With `candle_low`/`candle_high` supplied (`ema_candle_position=
        "extreme"`) the WHOLE source candle must clear it instead of just the
        close: low above the EMA for a CE, high below it for a PE.
        """
        if not new_bricks:
            return None
        latest_direction = new_bricks[-1].direction
        if latest_direction != trend:
            return None
        if candle_low is not None and candle_high is not None:
            if latest_direction == "up" and candle_low > reference_level:
                return OptionType.CE
            if latest_direction == "down" and candle_high < reference_level:
                return OptionType.PE
            return None
        if latest_direction == "up" and close > reference_level:
            return OptionType.CE
        if latest_direction == "down" and close < reference_level:
            return OptionType.PE
        return None

    def _candle_confirm_signal(
        self,
        db: Session,
        trend: BrickDirection,
        close: float,
        reference_level: float,
        *,
        use_reference: bool,
    ) -> OptionType | None:
        """`entry_mode="candle_confirm"` (2026-09-24): two-timeframe entry. The
        Renko series (`brick_source_timeframe_minutes`, e.g. 5-min bricks) sets
        the trend (`trend`, a confirmed run); the TRIGGER is evaluated on every
        1-minute candle: the last `entry_confirm_candles` completed 1-minute
        closes must each be strictly beyond the previous one in the trend's
        direction (higher for an up-trend, lower for a down-trend), and -- unless
        `direction_filter_mode="none"` -- the latest 1-minute close must also be
        on the right side of `reference_level` (the EMA). Fires on the first bar
        satisfying all of it, which is generally later than the brick print.
        """
        n = self.entry_confirm_candles
        bars = get_recent_completed_bars(db, self.instrument_id, self.timeframe, limit=n + 1)
        if len(bars) < n + 1:
            return None
        closes = [float(b.close) for b in bars]
        rising = all(closes[i] > closes[i - 1] for i in range(1, n + 1))
        falling = all(closes[i] < closes[i - 1] for i in range(1, n + 1))
        if trend == "up" and rising and (not use_reference or close > reference_level):
            return OptionType.CE
        if trend == "down" and falling and (not use_reference or close < reference_level):
            return OptionType.PE
        return None

    def _brick_only_signal(
        self, new_bricks: list[RenkoBrick], trend: BrickDirection
    ) -> OptionType | None:
        """`direction_filter_mode="none"`: no reference level at all -- fires
        on the bar that just printed a brick completing the confirmed run,
        CE for an up-run, PE for a down-run. The control arm for measuring
        what the EMA guidance is worth.
        """
        if not new_bricks or new_bricks[-1].direction != trend:
            return None
        return OptionType.CE if trend == "up" else OptionType.PE

    def _resolve_day_open(self, db: Session, latest_bar: PriceBar, bar_day: date) -> float | None:
        """Open of the day's first 1-minute bar (the 09:15 open), cached for
        the day. `None` (and no entry) if the day has no bars yet."""
        if self._day_open is None:
            day_start = datetime.combine(bar_day, NORMAL_MARKET_OPEN, tzinfo=IST)
            bars = get_recent_completed_bars(
                db,
                self.instrument_id,
                self.timeframe,
                since=day_start,
                until=latest_bar.bucket_start + timedelta(seconds=60),
            )
            if not bars:
                return None
            self._day_open = float(bars[0].open)
        return self._day_open

    def _pullback_signal(
        self, db: Session, trend: BrickDirection, close: float, reference_level: float
    ) -> OptionType | None:
        recent = get_recent_completed_bars(db, self.instrument_id, self.timeframe, limit=2)
        if len(recent) < 2:
            return None
        prev_bar, latest_bar = recent
        result = touch_and_confirm(
            prev_bar, latest_bar, reference_level, self.pullback_tolerance_frac
        )
        if result == "bullish" and trend == "up" and close > reference_level:
            return OptionType.CE
        if result == "bearish" and trend == "down" and close < reference_level:
            return OptionType.PE
        return None

    def _resolve_ema_reference(
        self, db: Session, latest_bar: PriceBar, bar_day: date
    ) -> tuple[float, float] | None:
        """`(resampled_close, ema_value)` on `ema_timeframe_minutes`/
        `ema_period`, or `None` if not warmed up yet -- shared by
        `_ema_filter_ok` (secondary confirmation in `"fib_pob"` mode) and
        the direct direction decision in `"ema_crossover"` mode.

        **2026-09-23 fix**: originally resampled only from `bar_day`'s own
        09:15 open (single-day-scoped), the same trap `_resolve_brick_size`
        already avoids for ATR. A trading session is ~375 minutes, so
        `ema_period=30` (the user's requested EMA(30)) could never seed at
        `ema_timeframe_minutes` >= 15 -- `ema_series` was always empty,
        every day, forever, regardless of market conditions (confirmed via
        a live pilot run: 4/4 completed configs at 15/30-min, 0 trades
        each). Also inconsistent with this codebase's own live `EMACalculator`
        convention, which is explicitly continuous/never resets across days
        (see CLAUDE.md's 2026-09-23 EMA30 entry). Fixed the same way ATR
        already is: `resample_multi_day_htf` over a real
        `ema_lookback_days`-day rolling window (default 20, matching
        `atr_lookback_days`'s own default) instead of a single day, so the
        EMA genuinely warms up and carries through across sessions.
        """
        since = datetime.combine(bar_day, time.min, tzinfo=IST) - timedelta(
            days=self.ema_lookback_days
        )
        until = latest_bar.bucket_start + timedelta(seconds=60)
        bars_by_day = _fetch_bars_by_day(db, self.instrument_id, self.timeframe, since, until)
        candles = resample_multi_day_htf(
            bars_by_day, self.ema_timeframe_minutes * 60, NORMAL_MARKET_OPEN
        )
        ema_series = compute_ema_series(candles, self.ema_period)
        if not ema_series:
            return None
        return candles[-1].close, ema_series[-1]

    def _resolve_ema_tail(
        self, db: Session, latest_bar: PriceBar, bar_day: date, k: int
    ) -> list[tuple[Bar, float]] | None:
        """The last `k` resampled candles paired with their EMA value,
        oldest first (fewer than `k` if the EMA has warmed up on fewer --
        callers treat a short list as "no evidence of a prior state").
        `None` if the EMA has not warmed up at all. Same multi-day candle
        window as `_resolve_ema_reference`; the EMA series is aligned to the
        END of the candle list (one value per candle once warmed up).
        """
        since = datetime.combine(bar_day, time.min, tzinfo=IST) - timedelta(
            days=self.ema_lookback_days
        )
        until = latest_bar.bucket_start + timedelta(seconds=60)
        bars_by_day = _fetch_bars_by_day(db, self.instrument_id, self.timeframe, since, until)
        candles = resample_multi_day_htf(
            bars_by_day, self.ema_timeframe_minutes * 60, NORMAL_MARKET_OPEN
        )
        ema_series = compute_ema_series(candles, self.ema_period)
        if not ema_series:
            return None
        n = min(k, len(ema_series))
        return list(zip(candles[-n:], ema_series[-n:], strict=True))

    def _ema_fresh_cross(self, ema_tail: list[tuple[Bar, float]], bullish: bool) -> bool:
        """True if the EMA side condition holds on the newest candle but did
        NOT hold on at least one of the preceding `ema_cross_lookback_candles`
        candles -- i.e. the trend filter itself has only just turned positive
        for this direction (`ema_candle_position` decides what "holds" means).
        No earlier candle available -> False (no evidence of a cross).
        """

        def holds(candle: Bar, ema: float) -> bool:
            return ema_side_ok(
                bullish,
                close=candle.close,
                high=candle.high,
                low=candle.low,
                ema=ema,
                position=self.ema_candle_position,
            )

        newest_candle, newest_ema = ema_tail[-1]
        if not holds(newest_candle, newest_ema):
            return False
        return any(not holds(c, e) for c, e in ema_tail[:-1])

    def _ema_filter_ok(
        self, db: Session, latest_bar: PriceBar, bar_day: date, option_type: OptionType
    ) -> bool | None:
        """`None` means "not warmed up yet" (distinct from `False`, a real
        reject) -- same convention every other gate in this codebase uses.
        """
        resolved = self._resolve_ema_reference(db, latest_bar, bar_day)
        if resolved is None:
            return None
        close, ema_value = resolved
        if option_type == OptionType.CE:
            return close > ema_value
        return close < ema_value
