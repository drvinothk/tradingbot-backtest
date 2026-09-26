import glob, os, collections
import replay as R
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else 9.99
for f in sorted(glob.glob('renko7/*_current.csv')+glob.glob('renko6/renko6_tf5_x5_ema15tf_current.csv')):
    T=sorted(R.load_trades(f), key=lambda t:t['e']); p=[t['pnl'] for t in T]
    ce=[t['pnl'] for t in T if t['ce']]; pe=[t['pnl'] for t in T if not t['ce']]
    h=len(T)//2; ex2=sum(sorted(p)[:-2])
    print(f"{os.path.basename(f)[7:-12]:14} n={len(p)} net={sum(p):>7,.0f} PF={pf(p):.2f} WR={100*sum(x>0 for x in p)/len(p):.0f}% ex2={ex2:>7,.0f} CE({len(ce)})={sum(ce):>7,.0f} PE({len(pe)})={sum(pe):>7,.0f} H1={sum(p[:h]):>7,.0f} H2={sum(p[h:]):>7,.0f}")
