import glob, os, math, statistics as st
from datetime import date, timedelta
import replay as R
files=sorted(glob.glob('renko7/*_current.csv'))+['renko6/renko6_tf5_x5_ema15tf_current.csv']
D={f:sorted(R.load_trades(f),key=lambda t:t['e']) for f in files}
alld=[t['e'].date() for T in D.values() for t in T]; d0,d1=min(alld),max(alld)
bdays=[d0+timedelta(i) for i in range((d1-d0).days+1) if (d0+timedelta(i)).weekday()<5]
yrs=(d1-d0).days/365.25
print(f"span {d0}..{d1}  {len(bdays)} weekdays  {yrs:.2f}y  (qty=65=1 lot, gross)")
print("cfg|n|net|avgW|avgL|W/L|PF|WR|exp/trade|maxDD|Calmar|Sharpe(d,ann)|Sh(trade)|ex2")
rows=[]
for f,T in D.items():
    p=[t['pnl'] for t in T]; w=[x for x in p if x>0]; l=[x for x in p if x<0]
    net=sum(p); pf=sum(w)/-sum(l)
    cum=pk=dd=0
    for x in p:
        cum+=x; pk=max(pk,cum); dd=max(dd,pk-cum)
    daily={}
    for t in T: daily[t['e'].date()]=daily.get(t['e'].date(),0)+t['pnl']
    s=[daily.get(d,0) for d in bdays]
    sh=st.mean(s)/st.pstdev(s)*math.sqrt(252)
    sht=st.mean(p)/st.stdev(p)
    calmar=(net/yrs)/dd if dd else float('nan')
    name=os.path.basename(f)[:-12].replace('renko7_','').replace('renko6_','BASE ')
    rows.append((net,f"{name}|{len(p)}|{net:,.0f}|{st.mean(w):,.0f}|{st.mean(l):,.0f}|{st.mean(w)/-st.mean(l):.2f}|{pf:.2f}|{100*len(w)/len(p):.0f}%|{net/len(p):,.0f}|{dd:,.0f}|{calmar:.2f}|{sh:.2f}|{sht:.2f}|{sum(sorted(p)[:-2]):,.0f}"))
for _,r in sorted(rows,reverse=True): print(r)
