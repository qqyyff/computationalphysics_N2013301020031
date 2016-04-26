import numpy as np
import matplotlib.pyplot as plt
import math
def trajectory(a,vx0,x0):
    x=[]
    vx=[]
    t=[]
    x.append(x0)
    vx.append(vx0)
    t.append(0)
    tau=0.0001
    k=16
    for i in range(1,40000):
        x.append(x[i-1]+vx[i-1]*tau)
        vx.append(vx[i-1]-k*x[i]**a*tau)
        t.append(t[i-1]+tau)
    return x,vx,t
"""
a,b,c=trajectory(1,0,2)
plt.plot(c,a,color='red',label='first order(a=1)')
a,b,c=trajectory(3,0,2)
plt.plot(c,a,color='orange',label='third order(a=3)')
a,b,c=trajectory(5,0,2)
plt.plot(c,a,color='blue',label='fifth order(a=5)')


a,b,c=trajectory(7,0,1.0)
plt.plot(c,a,color='green',label='seven order(a=7)')
a,b,c=trajectory(9,0,1.0)
plt.plot(c,a,color='purple',label='ninth order(a=9)')
a,b,c=trajectory(11,0,1.0)
plt.plot(c,a,color='yellow',label='eleventh order(a=11)')

plt.title('the trajectory of the various order oscillation')
plt.xlabel('time/s')
plt.ylabel('displacement/m')
plt.legend(loc='lower left',frameon=True)
plt.show()
"""
"""
for i in range(1,5):
    a,b,c=trajectory(1,0,1.0/i)
    plt.plot(c,a)
plt.show()
"""
"""
a,b,c=trajectory(1.0/2,0,1.0)
plt.plot(c,a,label='the 1/2 order')
a,b,c=trajectory(1.0/3,0,1.0)
plt.plot(c,a,label='the 1/3 order')
a,b,c=trajectory(1.0/4,0,1.0)
plt.plot(c,a,label='the 1/4 order')
a,b,c=trajectory(1.0/5,0,1.0)
plt.plot(c,a,label='the 1/5 order')
a,b,c=trajectory(1.0/6,0,1.0)
plt.plot(c,a,label='the 1/6 order')
a,b,c=trajectory(1.0/7,0,1.0)
plt.plot(c,a,label='the 1/7 order')
a,b,c=trajectory(1.0,0,1.0)
plt.plot(c,a,label='the first order')
plt.legend(loc='lower left',frameon=True)
plt.show()
"""
"""
gg=[]
tg=[]
for j in range(1,13,2):
    a,b,c=trajectory(j,0,1.0)
    kk=0
    while a[kk]>=0:
          kk=kk+1
    gg.append(c[kk]*4)
    tg.append(j)
    plt.scatter([j,j],[c[kk]*4,c[kk]*4],10,color='red')
    plt.plot([j,j],[1.4,2.8],color='orange',linewidth=1.0,linestyle='--')
plt.plot(tg,gg,color='blue',label='configuration measurement period')
plt.ylim(1.4,2.8)
plt.xlabel('order(a)')
plt.ylabel('period/s')
plt.title('the period via order graph')
"""
"""
for tt in range(1,20):
    a1,b1,c1=trajectory(1,0,0.1*tt)
    tt1=0
    while a1[tt1]>=0:
          tt1=tt1+1
    print c1[tt1]*4

"""

def relation(x0,v0,k,a):
    b1=2*k/(a+1)
    c1=v0**2+2*k*x0**(a+1)/(a+1)
    gg=(c1/b1)**(1.0/(a+1))
    x=[]
    v=[]
    x.append(-gg)
    txu=2.0*gg/100000.0
    v.append(v0)
    tg=1.0/math.sqrt(c1-b1*(x[-1]+txu/2.0)**(a+1))*txu
    for i in range(1,100000):
        x.append(x[i-1]+txu)
        tg=tg+txu/math.sqrt(abs(c1-b1*(x[i]**(a+1))))
    tr=2*tg
    return tr

"""
e1=[]
tk=[]
for jj in range(1,13,2):
    ee=relation(1.0,0,16,jj)
    e1.append(ee)
    tk.append(jj)
    plt.scatter([jj,jj],[ee,ee],10,color='red')
plt.plot(tk,e1,color='purple',label='integration computation period')
plt.legend(loc='upper left',frameon=True)
plt.show()
"""

e1=[]
tk=[]
for k in range(1,80): 
    ee=relation(0.9+0.1*k,0,16,7)
    tk.append(ee)
    e1.append(0.9+0.1*k)
plt.plot(e1,tk,label='the first order')
e1=[]
tk=[]
k=1
for k in range(1,80):    
    ee=relation(0.9+0.1*k,0,16,9)
    tk.append(ee)
    e1.append(0.9+0.1*k)
plt.plot(e1,tk,label='the ninth order')
e1=[]
tk=[]
k=1
for k in range(1,80):    
    ee=relation(0.9+0.1*k,0,16,11)
    tk.append(ee)
    e1.append(0.9+0.1*k)
plt.plot(e1,tk,label='the eleventh order')
e1=[]
tk=[]
plt.legend(loc='upper right',frameon=True)
plt.xlabel('initial displacement(amplitude)/m')
plt.ylabel('oscillation period/s') 
plt.title('the period via amplitude')
plt.show()

"""
ec=[]
xe=[]
txx=10.0/20.0
xe.append(txx)
ec.append(relation(txx,0,16,1))
for k in range(1,20):
    ee=relation(xe[-1],0,16,1)
    ec.append(ee)
    xe.append(xe[-1]+txx)
plt.plot(xe,ec)
plt.show()
"""
