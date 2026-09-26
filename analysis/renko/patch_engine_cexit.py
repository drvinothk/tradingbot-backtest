p = "C:/Users/drvin/Trading Bot/backtest_engine/backend/scripts/run_backtest.py"
raw = open(p, 'rb').read(); assert b'\r\n' not in raw
s = raw.decode('utf-8')
def sub(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70]); s = s.replace(old, new)
sub('''    dyn_net_favourable = 0
    dyn_peak_favourable = 0
    if renko_dynamic_exit is not None:
''', '''    dyn_net_favourable = 0
    dyn_peak_favourable = 0
    dyn_candle_exit = 0
    dyn_adverse_run = 0
    dyn_ucl: dict[datetime, float] = {}
    if renko_dynamic_exit is not None:
''')
sub('''        dyn_noprog_candles = int(renko_dynamic_exit.get("no_progress_exit_candles", 0))
''', '''        dyn_noprog_candles = int(renko_dynamic_exit.get("no_progress_exit_candles", 0))
        dyn_candle_exit = int(renko_dynamic_exit.get("candle_exit_confirm", 0))
        if dyn_candle_exit > 0:
            _d = entry_time.date()
            dyn_ucl = {ts_: c_ for ts_, c_ in underlying_series if ts_.date() == _d}
''')
sub('''                return _exit(bar.ts, close, "no_progress")
''', '''                return _exit(bar.ts, close, "no_progress")
            # Candle exit (2026-09-24): `candle_exit_confirm` consecutive
            # ADVERSE 1-minute underlying closes (close below the previous
            # minute's for a CE, above for a PE) exit at that bar's option
            # close. A flat/favourable minute resets the run.
            if dyn_candle_exit > 0:
                cur_u = dyn_ucl.get(bar.ts)
                prev_u = dyn_ucl.get(bar.ts - timedelta(minutes=1))
                if cur_u is not None and prev_u is not None:
                    is_adverse = cur_u < prev_u if structure_favorable else cur_u > prev_u
                    dyn_adverse_run = dyn_adverse_run + 1 if is_adverse else 0
                    if dyn_adverse_run >= dyn_candle_exit:
                        return _exit(bar.ts, close, "candle_reversal")
                else:
                    dyn_adverse_run = 0
''')
open(p, 'wb').write(s.encode('utf-8')); print('engine candle-exit patched')
