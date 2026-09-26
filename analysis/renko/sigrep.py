"""Offline replica of renko_trend breakout signal timing (ema_crossover mode, fixed brick, htf source)."""
import replay as R
from datetime import datetime,timedelta,time
from collections import defaultdict
def candles_for_day(day,tf):
    """list of candle closes (complete windows only) for a day, in order, with boundary label."""
    out=[]; a0=datetime.combine(day,time(9,15)); labs=set(R.Ub[day])
    if day not in R.Ub: return out
    idx=0
    while True:
        ws=a0+timedelta(minutes=idx*tf)
        if ws>R.Ub[day][-1]: break
        subs=[ws+timedelta(minutes=k) for k in range(tf)]
        if all(s in R.U for s in subs): out.append((subs[-1],R.U[subs[-1]][3]))
        idx+=1
    return out
_cd={}
def cdays(day,tf):
    if (day,tf) not in _cd: _cd[(day,tf)]=candles_for_day(day,tf)
    return _cd[(day,tf)]
def ema_at(day,tf,period,upto_ts):
    days=[d for d in sorted(R.Ub) if day-timedelta(days=20)<=d<=day]
    vals=[]
    for d in days:
        for lab,c in cdays(d,tf):
            if d==day and lab>upto_ts: break
            vals.append(c)
    if len(vals)<period: return None
    e=sum(vals[:period])/period; a=2/(period+1)
    for c in vals[period:]: e=c*a+e*(1-a)
    return e
def signals(day,B,tf,confirm=2,max_run=None,ema_period=30,start=time(9,30),cutoff=time(14,30)):
    """yield (boundary_label, 'CE'/'PE', run_len) for every eligible bar (first is the trade under the 1-trade/day harness)."""
    ev=R.renko_events(day,B,tf); bricks=[]; out=[]
    for ts in sorted(ev):
        new=ev[ts][0]; bricks+=new
        if not new: continue
        if not (start<=ts.time()<=cutoff): continue
        if not bricks: continue
        rd=bricks[-1]; run=1
        for d in reversed(bricks[:-1]):
            if d==rd: run+=1
            else: break
        if run<confirm: continue
        if new[-1]!=rd: continue
        if max_run is not None and run>max_run: continue
        e=ema_at(day,tf,ema_period,ts)
        if e is None: continue
        c=R.U[ts][3]
        if rd=='up' and c>e: out.append((ts,'CE',run))
        elif rd=='down' and c<e: out.append((ts,'PE',run))
    return out
if __name__=='__main__':
    import sys
    path,B,tf=sys.argv[1],float(sys.argv[2]),int(sys.argv[3])
    T=R.load_trades(path); byday={t['e'].date():t for t in T}
    ok=bad=0; miss=[]
    for day,t in sorted(byday.items()):
        if day not in R.Ub: continue
        s=signals(day,B,tf)
        if not s: miss.append((day,'no signal replicated',t['e'])); bad+=1; continue
        first=s[0]; m=(first[0]+timedelta(minutes=1)==t['e'] and ((first[1]=='CE')==t['ce']))
        ok+=m; bad+=(not m)
        if not m: miss.append((day,first,t['e'],'CE' if t['ce'] else 'PE'))
    print('signal replica vs actual entries: match',ok,'mismatch',bad)
    for m in miss[:8]: print('  ',m)
