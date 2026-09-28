import sys
from datetime import datetime
from types import SimpleNamespace
sys.path.insert(0,"D:/TradingBot/backtest_engine/backend/scripts"); sys.path.insert(0,"D:/TradingBot/backtest_engine/backend")
import run_backtest as rb
from app.domain.strategy.models import SignalSide
import replay as R, bricks as BR
ub=rb._load_csv_bars(__import__('pathlib').Path(R.H+'underlyings/NIFTY_alice_index_1min.csv')); useries=[(b.ts,b.close) for b in ub]
def check(name,N):
    T,B,tf=BR.load(name); ok=bad=0; reasons={}
    for t in T:
        ep=t['ep']
        ti=SimpleNamespace(created_at=datetime.combine(t['e'].date(),t['e'].time(),tzinfo=rb.IST),entry_price=ep,stop_price=R.rt(ep*0.65),target_price=R.rt(ep*10),side=SignalSide.BUY,
            trail_activation_fraction=20.0,trail_lock_fraction=0.6,structure_level=1.0,structure_break_buffer=0.0,structure_break_persistence_seconds=6.0)
        bars=[rb.Bar(ts=ts.replace(tzinfo=rb.IST),open=o,high=h,low=l,close=c,volume=0,oi=0) for ts,o,h,l,c in R.obars(t['sym'])]
        ot=rb.DomainOptionType.CE if t['ce'] else rb.DomainOptionType.PE
        spec={"brick_size":B,"timeframe_minutes":tf,"confirm_bricks":1,"flat_exit_candles":0,"no_progress_exit_candles":N}
        r=rb._reconstruct_exit_current(ti,t['sym'],bars,65,1,underlying_series=useries,option_type=ot,renko_dynamic_exit=spec)
        x,xp,why=BR.sim(t,B,tf,noprog=N)
        m=(x==r.exit_time.replace(tzinfo=None) and abs(xp-r.exit_price)<0.06)
        ok+=m; bad+=(not m); reasons[r.exit_reason]=reasons.get(r.exit_reason,0)+1
        if not m: print('   MISMATCH',t['sym'],t['e'],r.exit_time,r.exit_price,r.exit_reason,'| replay',x,xp,why)
    print(f"{name:10} noprog={N}: match {ok} mismatch {bad}  engine exits {reasons}")
for name,N in (('tf5',0),('tf5',2),('tf5',3),('tf5',4),('b625',2),('base15',2),('fresh_ext',2),('tf20',2)): check(name,N)
