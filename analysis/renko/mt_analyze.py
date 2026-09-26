import sys, re, math, statistics as st, collections
from datetime import date
import replay as R
DN=['Mon','Tue','Wed','Thu','Fri']
def dte(t):
    m=re.search(r'NIFTY(\d{2})(\d{2})(\d{2})',t['sym']); return (date(2000+int(m[1]),int(m[2]),int(m[3]))-t['e'].date()).days
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else 9.99
def mdd(p):
    c=pk=d=0
    for a in p: c+=a; pk=max(pk,c); d=max(d,pk-c)
    return d
def line(lab,p):
    if len(p)<2: return f"{lab:26} n={len(p)}"
    h=len(p)//2
    return f"{lab:26} n={len(p):3} net={sum(p):>8,.0f} PF={pf(p):4.2f} WR={100*sum(x>0 for x in p)/len(p):2.0f}% avg={st.mean(p):>6,.0f} DD={mdd(p):>7,.0f} ex2={sum(sorted(p)[:-2]):>8,.0f} H1={sum(p[:h]):>7,.0f} H2={sum(p[h:]):>7,.0f}"
def analyze(path, ref=None, label=''):
    T=sorted(R.load_trades(path),key=lambda t:t['e'])
    byd=collections.defaultdict(list)
    for t in T: byd[t['e'].date()].append(t)
    for ts in byd.values():
        for i,t in enumerate(ts): t['n']=i+1
    ndays=len(byd); p=[t['pnl'] for t in T]
    daily=collections.defaultdict(float)
    for t in T: daily[t['e'].date()]+=t['pnl']
    days=sorted(byd); sh=st.mean(daily[d] for d in days)/st.pstdev([daily[d] for d in days])*math.sqrt(252)
    print(f"=== {label or path}: {len(T)} trades on {ndays} days (max/day {max(len(v) for v in byd.values())}), daily Sharpe(traded days) {sh:.2f}")
    print(line('ALL multi-trade',p))
    print(line('  first trade of day',[t['pnl'] for t in T if t['n']==1]))
    for k in (2,3,4): print(line(f'  trade #{k}+' if k==4 else f'  trade #{k}',[t['pnl'] for t in T if (t['n']>=4 if k==4 else t['n']==k)]))
    print(line('  CE',[t['pnl'] for t in T if t['ce']])); print(line('  PE',[t['pnl'] for t in T if not t['ce']]))
    print('  by DTE:')
    for d in sorted({dte(t) for t in T}):
        ts=[t for t in T if dte(t)==d]
        print('   DTE',d,line('',[t['pnl'] for t in ts])[27:],'| trades/day',round(len(ts)/len({t['e'].date() for t in ts}),2))
    print('  exit reasons:',dict(collections.Counter(t['reason'] for t in T)))
    gates={'all':lambda t:True,'no Tue':lambda t:dte(t)!=0,'DTE>=5':lambda t:dte(t)>=5,'DTE6 only':lambda t:dte(t)==6}
    for g,fn in gates.items(): print('  gate',line(g,[t['pnl'] for t in T if fn(t)]))
    # loss streak / worst day
    wd=sorted(daily.items(),key=lambda kv:kv[1])[:3]; print('  worst days:',[(str(d),round(v)) for d,v in wd],' best days:',[(str(d),round(v)) for d,v in sorted(daily.items(),key=lambda kv:-kv[1])[:3]])
    if ref:
        base={t['e']:t for t in R.load_trades(ref)}
        f=[t for t in T if t['n']==1]
        ok=sum(1 for t in f if t['e'] in base and abs(base[t['e']]['pnl']-t['pnl'])<0.01)
        print(f"  PARITY first-trade-of-day vs one-trade/day file: {ok}/{len(f)} identical; one-trade/day days not matched: {sum(1 for e in base if e not in {t['e'] for t in f})}")
    return T
if __name__=='__main__':
    analyze(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None)
