WT = "D:/tb-renko-fix/backend/app/modules/strategy_engine/strategies/renko_trend.py"
raw = open(WT, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')


def sub(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:80])
    s = s.replace(old, new)


sub('    "no_progress_exit_candles",\n', '    "no_progress_exit_candles",\n    "entry_confirm_candles",\n    "candle_exit_confirm",\n')
sub('        no_progress_exit_candles: int = 0,\n', '        no_progress_exit_candles: int = 0,\n        entry_confirm_candles: int = 0,\n        candle_exit_confirm: int = 0,\n')
sub('''        if entry_mode not in ("breakout", "pullback"):
            raise ValueError(f"entry_mode must be 'breakout' or 'pullback', got {entry_mode!r}")''',
    '''        if entry_mode not in ("breakout", "pullback", "candle_confirm"):
            raise ValueError(
                f"entry_mode must be 'breakout', 'pullback' or 'candle_confirm', got {entry_mode!r}"
            )
        if entry_mode == "candle_confirm" and entry_confirm_candles < 1:
            raise ValueError("entry_mode='candle_confirm' requires entry_confirm_candles >= 1")
        if entry_confirm_candles < 0:
            raise ValueError("entry_confirm_candles must be >= 0")
        if entry_confirm_candles > 0 and entry_mode != "candle_confirm":
            raise ValueError("entry_confirm_candles > 0 requires entry_mode='candle_confirm'")
        if candle_exit_confirm < 0:
            raise ValueError("candle_exit_confirm must be >= 0")
        if candle_exit_confirm > 0 and reversal_exit_mode != "dynamic":
            raise ValueError("candle_exit_confirm > 0 requires reversal_exit_mode='dynamic'")''')
sub('''        if direction_filter_mode == "none" and entry_mode != "breakout":
            raise ValueError("direction_filter_mode='none' requires entry_mode='breakout'")''',
    '''        if direction_filter_mode == "none" and entry_mode == "pullback":
            raise ValueError("direction_filter_mode='none' does not support entry_mode='pullback'")''')
sub('        self.no_progress_exit_candles = no_progress_exit_candles\n',
    '        self.no_progress_exit_candles = no_progress_exit_candles\n        self.entry_confirm_candles = entry_confirm_candles\n        self.candle_exit_confirm = candle_exit_confirm\n')
sub('            "no_progress_exit_candles": int(self.no_progress_exit_candles),\n',
    '            "no_progress_exit_candles": int(self.no_progress_exit_candles),\n            "candle_exit_confirm": int(self.candle_exit_confirm),\n')
sub('''        else:
            option_type = self._pullback_signal(db, trend, close, reference_level)
''', '''        elif self.entry_mode == "candle_confirm":
            option_type = self._candle_confirm_signal(
                db, trend, close, reference_level, use_reference=self.direction_filter_mode != "none"
            )
        else:
            option_type = self._pullback_signal(db, trend, close, reference_level)
''')
sub('''    def _brick_only_signal(''', '''    def _candle_confirm_signal(
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

    def _brick_only_signal(''')
open(WT, 'wb').write((s.replace('\n', '\r\n') if crlf else s).encode('utf-8'))
print('strategy patched')
