"""Brick size (30-min ATR14 x1.0) the strategy would resolve per day: production-like (bars of the prior 20 calendar days) vs the per-day
harness (only the last 1000 underlying 1-min bars before the day are in the fresh DB). Band [10,60]."""
from datetime import datetime,timedelta,time,date
import replay as R
class ATRCalculator:  # verbatim logic of app/modules/market_data/indicators/atr.py
    def __init__(s,period=14): s.period=period; s._value=None; s._warmup=[]; s._pc=None
    def update(s,h,l,c):
        tr=h-l if s._pc is None else max(h-l,abs(h-s._pc),abs(l-s._pc)); s._pc=c
        if s._value is not None: s._value=(s._value*(s.period-1)+tr)/s.period; return s._value
        s._warmup.append(tr)
        if len(s._warmup)<s.period: return None
        s._value=sum(s._warmup)/s.period; return s._value
TF=30; P=14
days=sorted(d for d in R.Ub if len(R.Ub[d])>=300)
allb=sorted(R.U)  # 1-min labels
def candles(bars_labels):
    by={}
    for ts in bars_labels: by.setdefault(ts.date(),[]).append(ts)
    out=[]
    for d in sorted(by):
        s=set(by[d]); a0=datetime.combine(d,time(9,15))
        for i in range(12):
            ws=a0+timedelta(minutes=TF*i); subs=[ws+timedelta(minutes=k) for k in range(TF)]
            if all(x in s for x in subs):
                o=R.U[subs[0]][0]; h=max(R.U[x][1] for x in subs); l=min(R.U[x][2] for x in subs); c=R.U[subs[-1]][3]; out.append((h,l,c))
    return out
def atr_of(cs):
    a=ATRCalculator(P); v=None
    for h,l,c in cs:
        r=a.update(h,l,c); v=r if r is not None else v
    return v
import bisect
rows=[]
for d in days:
    if d<date(2025,8,28): continue
    day0=datetime.combine(d,time.min); i=bisect.bisect_left(allb,day0)
    short=allb[max(0,i-1000):i]; lo=day0-timedelta(days=20); j=bisect.bisect_left(allb,lo); long_=allb[j:i]
    s=atr_of(candles(short)); l=atr_of(candles(long_))
    rows.append((d,s,l,len(candles(short)),len(candles(long_))))
ok=[r for r in rows if r[1] and r[2]]
import statistics as st
print('days',len(rows),'no-ATR short',sum(1 for r in rows if not r[1]),'no-ATR long',sum(1 for r in rows if not r[2]))
rel=[(r[1]-r[2])/r[2] for r in ok]
print('candles short/long median',st.median(r[3] for r in ok),st.median(r[4] for r in ok))
print('brick short mean %.1f long mean %.1f; rel diff mean %.1f%% abs-mean %.1f%% max %.0f%%'%(st.mean(r[1] for r in ok),st.mean(r[2] for r in ok),100*st.mean(rel),100*st.mean(abs(x) for x in rel),100*max(abs(x) for x in rel)))
print('days |diff|>5%%: %d, >10%%: %d, >20%%: %d'%tuple(sum(1 for x in rel if abs(x)>t) for t in(.05,.10,.20)))
inb=lambda v:10<=v<=60
print('band disagreement (in band under one, out under other):',sum(1 for r in ok if inb(r[1])!=inb(r[2])),'; out of band short',sum(1 for r in ok if not inb(r[1])),'long',sum(1 for r in ok if not inb(r[2])))
print('brick size distribution long: min %.1f med %.1f max %.1f'%(min(r[2] for r in ok),st.median(r[2] for r in ok),max(r[2] for r in ok)))
