"""Genuine higher-timeframe (5-min/15-min) bar construction and indicators
for the `id_*` intraday trend-continuation strategies.

Every strategy in this module resamples real OHLCV candles from the
system's one persisted timeframe (`common_rules.BAR_TIMEFRAME`, 60s) rather
than computing an indicator on a *stretched* 1-minute lookback the way
`strategies/atr_breakout.py` does (`breakout_lookback_bars=20` meaning 20
*minutes*, per that file's own docstring caveat) — that approach was
backtested and abandoned (`BACKTEST_LEARNINGS.md`, 2026-08-28: PF 0.09-0.21,
`atr_delta` r = -0.70 vs PnL, "needs volatility to keep expanding after
entry, which it rarely does" at 1-min granularity). A real 5-minute candle's
true range and a 20-minute-wide window of 1-minute true ranges are not the
same computation; the intraday strategies need the former.

`resample_to_htf` requires a *complete* set of sub-bars for a window and
returns nothing for one with a real feed gap — it never builds a candle
from partial data, matching this codebase's "missing data is not an
adverse regime, just skip" convention used throughout
`common_rules.py`/every strategy's own gates.

`SupertrendCalculator` is a new indicator (does not exist anywhere else in
this codebase) — same pure, stateful, fed-one-bar-at-a-time shape as
`ATRCalculator`/`EMACalculator` (`market_data/indicators/`).

`find_last_swing_high`/`find_last_swing_low` are fractal pivot detectors —
genuinely different from `common_rules.compute_range_high_low`, which is a
flat window high/low (Donchian-style), not a pivot.
"""

from __future__ import annotations

from datetime import datetime, time, timedelta
from typing import Literal

from app.core.clock import IST, to_ist
from app.domain.market.models import PriceBar
from app.modules.market_data.indicators import ATRCalculator, Bar, EMACalculator
from app.modules.market_data.indicators.rsi import RSICalculator

__all__ = [
    "SupertrendCalculator",
    "compute_atr_series",
    "compute_ema_series",
    "compute_rsi_series",
    "find_last_swing_high",
    "find_last_swing_low",
    "htf_touch_and_confirm",
    "is_htf_boundary_close",
    "resample_to_htf",
]


def resample_to_htf(
    bars: list[PriceBar],
    timeframe_seconds: int,
    session_open: time,
) -> list[Bar]:
    """Groups consecutive completed 60s `bars` (same instrument, ascending
    by `bucket_start`, assumed all from a single trading day — callers
    already scope their `get_recent_completed_bars` call with `since=
    day_start`, same convention `orb.py`/`vwap_pullback.py` use) into real
    OHLCV candles of `timeframe_seconds`, clock-boundary-aligned to
    `session_open` (the real 09:15 IST NSE open, not epoch/midnight —
    same anchoring reasoning `ORBStrategy`'s own docstring gives for using
    the bar's own timestamp rather than wall-clock `now()`).

    A window missing even one expected sub-bar (a real feed gap) is
    skipped entirely — never partially aggregated. Returns bars in
    ascending order, oldest first.
    """
    if timeframe_seconds % 60 != 0 or timeframe_seconds <= 0:
        raise ValueError("timeframe_seconds must be a positive multiple of 60")
    if not bars:
        return []

    sub_bars_needed = timeframe_seconds // 60
    by_bucket_start = {b.bucket_start: b for b in bars}
    day = to_ist(bars[0].bucket_start).date()
    anchor = datetime.combine(day, session_open, tzinfo=IST)

    last_bucket_start = max(by_bucket_start)
    if last_bucket_start < anchor:
        return []
    max_index = int((last_bucket_start - anchor).total_seconds() // timeframe_seconds)

    candles: list[Bar] = []
    for index in range(max_index + 1):
        window_start = anchor + timedelta(seconds=index * timeframe_seconds)
        sub_bars = [
            by_bucket_start.get(window_start + timedelta(seconds=k * 60))
            for k in range(sub_bars_needed)
        ]
        confirmed_bars = [b for b in sub_bars if b is not None]
        if len(confirmed_bars) != sub_bars_needed:
            continue  # a real gap in this window -- skip it, never partially build it
        candles.append(
            Bar(
                bucket_start=window_start,
                open=float(confirmed_bars[0].open),
                high=max(float(b.high) for b in confirmed_bars),
                low=min(float(b.low) for b in confirmed_bars),
                close=float(confirmed_bars[-1].close),
                volume=sum(b.volume for b in confirmed_bars),
            )
        )
    return candles


def is_htf_boundary_close(
    bar_bucket_start: datetime, timeframe_seconds: int, session_open: time
) -> bool:
    """True if the 60s bar starting at `bar_bucket_start` is the *last*
    sub-bar of an HTF window of `timeframe_seconds` anchored to
    `session_open` — i.e. this bar's completion is what closes a genuine
    HTF candle, not an intermediate sub-bar. Used inside a strategy's
    `check_setup` to no-op on the sub-bars that don't complete an HTF
    candle, without any new runner cadence, persisted timeframe, or thread —
    the runner still calls `evaluate()` on every completed 60s bar exactly
    as it does for every other strategy; this is a fast early-return inside
    that call.
    """
    bar_ist = to_ist(bar_bucket_start)
    anchor = datetime.combine(bar_ist.date(), session_open, tzinfo=IST)
    elapsed = (bar_bucket_start - anchor).total_seconds()
    if elapsed < 0:
        return False
    return (elapsed + 60) % timeframe_seconds == 0


def compute_atr_series(candles: list[Bar], period: int) -> list[float]:
    """Every warmed-up ATR value across `candles` (oldest first), computed
    from a fresh `ATRCalculator` fed the given candles in order — the
    *true* ATR for whatever timeframe `candles` already is (5-min, 15-min,
    ...), never a 1-minute-bar approximation. Shorter than `candles` by
    `period` entries (ATR needs `period` true-range samples to seed);
    empty if there aren't enough candles yet. A fresh calculator per call
    is deliberate — this is a bounded, read-time computation over a recent
    window (a strategy's `check_setup`/a backtest reconstruction), not a
    hot per-tick path, so correctness (always replaying from a known-clean
    state) is worth more than reusing a calculator instance.
    """
    atr = ATRCalculator(period=period)
    values: list[float] = []
    for candle in candles:
        value = atr.update(candle.high, candle.low, candle.close)
        if value is not None:
            values.append(value)
    return values


def compute_ema_series(candles: list[Bar], period: int) -> list[float]:
    """Same shape as `compute_atr_series`, for `EMACalculator` fed the
    candles' closes.
    """
    ema = EMACalculator(period=period)
    values: list[float] = []
    for candle in candles:
        value = ema.update(candle.close)
        if value is not None:
            values.append(value)
    return values


def compute_rsi_series(candles: list[Bar], period: int) -> list[float]:
    """Same shape as `compute_ema_series`, for `RSICalculator` (Wilder-
    smoothed, `market_data/indicators/rsi.py`) fed the candles' closes.
    RSI is a rolling-window momentum oscillator — genuinely timeframe-
    dependent, same as ATR/EMA (see this module's own top-of-file
    docstring) — so a 5-min-native series here is a real, different signal
    from the 1-min `"RSI14"` indicator `ConvictionGateMixin._rsi_alignment_reject`
    reads by default; never substitute one for the other.
    """
    rsi = RSICalculator(period=period)
    values: list[float] = []
    for candle in candles:
        value = rsi.update(candle.close)
        if value is not None:
            values.append(value)
    return values


def htf_touch_and_confirm(
    prev_candle: Bar, latest_candle: Bar, reference_level: float, tolerance_frac: float
) -> Literal["bullish", "bearish"] | None:
    """`common_rules.touch_and_confirm`'s identical logic, retyped against
    the resampled `Bar` dataclass instead of the ORM `PriceBar` — kept as
    its own small function rather than making the two call sites duck-type
    across mismatched type hints (this codebase's `mypy --strict`-adjacent
    bar is a real constraint, not a style preference). See that function's
    own docstring for the touch/confirm semantics themselves; nothing about
    the logic differs here, only the input type.
    """
    band = reference_level * tolerance_frac
    close = latest_candle.close

    touched_from_above = abs(prev_candle.low - reference_level) <= band
    bullish_confirmation = close > prev_candle.high and close > reference_level
    touched_from_below = abs(prev_candle.high - reference_level) <= band
    bearish_confirmation = close < prev_candle.low and close < reference_level

    if touched_from_above and bullish_confirmation:
        return "bullish"
    if touched_from_below and bearish_confirmation:
        return "bearish"
    return None


def _confirmed_pivot(bars: list[Bar], lookback: int, *, high: bool) -> float | None:
    n = len(bars)
    if n < 2 * lookback + 1:
        return None
    # Scan backward from the most recently *confirmed* candle -- a pivot
    # needs `lookback` bars after it too, so only a fully-formed pivot
    # (never the most recent 1..lookback candles, which could still be
    # exceeded) is ever returned. Same "unconfirmed data never trips a
    # signal" convention as `common_rules`'s own gates.
    for i in range(n - lookback - 1, lookback - 1, -1):
        window = bars[i - lookback : i + lookback + 1]
        pivot_value = bars[i].high if high else bars[i].low
        window_extreme = max(b.high for b in window) if high else min(b.low for b in window)
        if pivot_value == window_extreme:
            return pivot_value
    return None


def find_last_swing_high(bars: list[Bar], lookback: int = 2) -> float | None:
    """The most recent *confirmed* fractal swing high in `bars` (ascending,
    oldest first) — a candle whose high is the max within `lookback`
    candles on both sides. `None` if no confirmed pivot exists yet (not
    enough bars, or the price action never formed one) — genuinely
    different from `common_rules.compute_range_high_low`, which is a flat
    window high/low, not a pivot.
    """
    return _confirmed_pivot(bars, lookback, high=True)


def find_last_swing_low(bars: list[Bar], lookback: int = 2) -> float | None:
    """`find_last_swing_high`'s mirror, for swing lows."""
    return _confirmed_pivot(bars, lookback, high=False)


class SupertrendCalculator:
    """Standard Supertrend (basic bands = midpoint ± `multiplier` × ATR,
    then the usual ratchet-and-flip rule), fed one completed HTF candle's
    high/low/close at a time — same pure, stateful shape as
    `ATRCalculator`/`EMACalculator`. Does not exist anywhere else in this
    codebase; built fresh for the `id_ema_supertrend` strategy.

    Warms up once its internal `ATRCalculator` does (after `period`
    true-range samples); `update()` returns `None` until then, same
    "not enough history yet" convention as every other calculator here.
    """

    def __init__(self, period: int = 10, multiplier: float = 3.0) -> None:
        if period < 1:
            raise ValueError("period must be >= 1")
        if multiplier <= 0:
            raise ValueError("multiplier must be > 0")
        self.period = period
        self.multiplier = multiplier
        self._atr = ATRCalculator(period=period)
        self._final_upper: float | None = None
        self._final_lower: float | None = None
        self._trend: Literal["up", "down"] | None = None
        self._prev_close: float | None = None

    def update(self, high: float, low: float, close: float) -> Literal["up", "down"] | None:
        atr = self._atr.update(high, low, close)
        if atr is None:
            self._prev_close = close
            return None

        mid = (high + low) / 2
        basic_upper = mid + self.multiplier * atr
        basic_lower = mid - self.multiplier * atr

        if self._final_upper is None or self._final_lower is None:
            # First warmed-up bar: no prior band to ratchet from -- seed
            # both bands directly and pick a starting trend from where
            # close sits relative to the midpoint.
            final_upper = basic_upper
            final_lower = basic_lower
            trend: Literal["up", "down"] = "up" if close >= mid else "down"
        else:
            prev_close = self._prev_close if self._prev_close is not None else close
            final_upper = (
                basic_upper
                if basic_upper < self._final_upper or prev_close > self._final_upper
                else self._final_upper
            )
            final_lower = (
                basic_lower
                if basic_lower > self._final_lower or prev_close < self._final_lower
                else self._final_lower
            )
            if self._trend == "up" and close < final_lower:
                trend = "down"
            elif self._trend == "down" and close > final_upper:
                trend = "up"
            else:
                trend = self._trend  # type: ignore[assignment]

        self._final_upper = final_upper
        self._final_lower = final_lower
        self._trend = trend
        self._prev_close = close
        return trend

    @property
    def trend(self) -> Literal["up", "down"] | None:
        return self._trend

    @property
    def is_warmed_up(self) -> bool:
        return self._trend is not None

    @property
    def band_value(self) -> float | None:
        """The Supertrend line itself: the (support) lower band while
        trend is up, the (resistance) upper band while trend is down.
        `None` until warmed up.
        """
        if self._trend == "up":
            return self._final_lower
        if self._trend == "down":
            return self._final_upper
        return None
