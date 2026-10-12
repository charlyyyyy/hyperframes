import numpy as np, wave, sys
SR=48000; DUR=37.8
L=np.zeros(int(SR*DUR)); R=np.zeros_like(L)
rng=np.random.default_rng(7)
def add(sig,t,gain=1.0,pan=0.0):
    i=int(t*SR); n=min(len(sig),len(L)-i)
    L[i:i+n]+=sig[:n]*gain*np.sqrt((1-pan)/2); R[i:i+n]+=sig[:n]*gain*np.sqrt((1+pan)/2)
def tt(d): return np.arange(int(d*SR))/SR
def biquad_bp(x,fc,q):
    y=np.zeros_like(x); x1=x2=y1=y2=0.0
    for n in range(len(x)):
        w=2*np.pi*fc[n]/SR; al=np.sin(w)/(2*q); c=np.cos(w); a0=1+al
        b0=al/a0; b2=-al/a0; a1=-2*c/a0; a2=(1-al)/a0
        v=b0*x[n]+b2*x2-a1*y1-a2*y2; x2=x1; x1=x[n]; y2=y1; y1=v; y[n]=v
    return y
def click():
    t=tt(0.09)
    n=rng.standard_normal(len(t)); n=np.diff(n,prepend=0)*np.exp(-t/0.0018)
    body=np.sin(2*np.pi*1900*t)*np.exp(-t/0.010)*0.35+np.sin(2*np.pi*180*t)*np.exp(-t/0.025)*0.55
    return n*0.35+body
def pop(f):
    t=tt(0.16); f_t=f*(1+0.5*np.exp(-t/0.012)); ph=2*np.pi*np.cumsum(f_t)/SR
    return (np.sin(ph)+0.25*np.sin(2*ph))*np.exp(-t/0.05)*np.minimum(1,t/0.002)
def tick():
    t=tt(0.06); return np.sin(2*np.pi*720*t)*np.exp(-t/0.012)*np.minimum(1,t/0.001)
def whoosh(d,f0=350,f1=2600,f2=700):
    t=tt(d); u=t/d; peak=0.62
    fc=np.where(u<peak, f0+(f1-f0)*(u/peak)**1.5, f1+(f2-f1)*((u-peak)/(1-peak)))
    env=np.where(u<peak,(u/peak)**2,((1-u)/(1-peak))**1.6)
    return biquad_bp(rng.standard_normal(len(t)),fc,1.1)*env*1.6
def riser(d):
    t=tt(d); u=t/d; fc=300+2200*u**2
    return biquad_bp(rng.standard_normal(len(t)),fc,2.0)*(u**1.5)*(1-u**8)*1.2
def chime():
    t=tt(1.8); s=0
    for f,a,dc in [(1046.5,1,0.9),(1568,0.6,0.6),(2093,0.35,0.4),(2637,0.2,0.3)]:
        s=s+a*np.sin(2*np.pi*f*t)*np.exp(-t/dc)
    return s*np.minimum(1,t/0.004)*0.45
def sparkle():
    t=tt(0.5); s=0
    for k,f in enumerate([2349,2794,3136,3520]):
        d=k*0.05; m=t>=d; tt2=np.where(m,t-d,0)
        s=s+m*np.sin(2*np.pi*f*tt2)*np.exp(-tt2/0.08)*0.25
    return s
E=[7.35,13.9,18.95,27.0]; X=[13.85,18.9,26.95,32.0]; O=31.8
for i in range(5): add(tick(),0.2+i*0.16,0.18,-0.3+i*0.15)
add(whoosh(0.5,500,3000,900),1.08,0.18)
add(whoosh(0.85),2.55,0.32)
add(riser(1.6),3.05,0.16)
add(pop(660),4.62,0.22)
add(pop(520),3.72,0.25)
add(click(),5.2,0.7,0.1); add(sparkle(),5.26,0.35)
add(pop(560),5.4,0.12)
for t in [6.97]+[x-0.3 for x in X[:3]]: add(whoosh(0.6),t,0.42)
add(whoosh(0.8),X[3]-0.5,0.4)
pent=[880,988,1109,1319,1480]
for i,e in enumerate(E):
    add(click(),e+1.3,0.7,0.15)
    for k in range(5): add(pop(pent[k]),e+1.32+k*0.07,0.2,-0.4+k*0.2)
    add(sparkle(),e+1.38,0.25)
for x in X[:3]: add(click(),x-0.4,0.65,-0.1)
add(pop(520),O+1.65,0.25)
add(click(),O+3.1,0.75); add(chime(),O+3.12,0.6); add(sparkle(),O+3.15,0.35)
m=max(np.abs(L).max(),np.abs(R).max()); g=10**(-3/20)/m
st=np.stack([L*g,R*g],1); st=(st*32767).astype(np.int16)
with wave.open(sys.argv[1],'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
print('peak gain',g)
