"""How many calendar days of history reproduce the 20-day ATR14(30-min) brick size and EMA30(15-min candle closes)? Compare lookback L to L=20 per day."""
import bisect, statistics as st
from datetime import datetime, timedelta, time, date
import replay as R
def wilder(vals, n):
    a=None; buf=[]
    for v in vals:
        if a is None:
            buf.append(v)
            if len(buf)==n: a=sum(buf)/n
        else: a=(a*(n-1)+v)/n
    return a
def htf(labels, tf):
    by={}
    for ts in labels: by.setdefault(ts.date(),[]).append(ts)
    out=[]
    for d in sorted(by):
        s=set(by[d]); a0=datetime.combine(d,time(9,15))
        for i in range(375//tf):
            ws=a0+timedelta(minutes=tf*i); subs=[ws+timedelta(minutes=k) for k in range(tf)]
            if all(x in s for x in subs):
                out.append((max(R.U[x][1] for x in subs),min(R.U[x][2] for x in subs),R.U[subs[-1]][3]))
    return out
def atr(cs,n=14):
    tr=[];pc=None
    for h,l,c in cs:
        tr.append(h-l if pc is None else max(h-l,abs(h-pc),abs(l-pc))); pc=c
    return wilder(tr,n)
def ema(cs,n=30):
    k=2/(n+1); e=None; buf=[]
    for h,l,c in cs:
        if e is None:
            buf.append(c)
            if len(buf)==n: e=sum(buf)/n
        else: e=c*k+e*(1-k)
    return e
allb=sorted(R.U); days=[d for d in sorted(R.Ub) if len(R.Ub[d])>=300 and d>=date(2025,8,28)]
Ls=[5,7,9,10,12,14]
res={L:{'atr':[],'ema':[]} for L in Ls}
for d in days[::2]:
    i=bisect.bisect_left(allb,datetime.combine(d,time.min))
    def get(L):
        lo=datetime.combine(d,time.min)-timedelta(days=L); j=bisect.bisect_left(allb,lo); seg=allb[j:i]
        return atr(htf(seg,30)), ema(htf(seg,15))
    ra,re_=get(20)
    for L in Ls:
        a,e=get(L)
        if a and ra: res[L]['atr'].append(abs(a-ra)/ra)
        if e and re_: res[L]['ema'].append(abs(e-re_))   # EMA in index points
print('L  | ATR brick rel diff vs 20d: mean / p95 / max | EMA30 diff (index pts): mean / p95 / max')
for L in Ls:
    a=sorted(res[L]['atr']); e=sorted(res[L]['ema'])
    q=lambda x,p: x[int(p*(len(x)-1))]
    print(f"{L:2d} | {100*st.mean(a):5.2f}% / {100*q(a,.95):5.2f}% / {100*a[-1]:5.2f}% | {st.mean(e):6.2f} / {q(e,.95):6.2f} / {e[-1]:6.2f}   (n={len(a)})")
