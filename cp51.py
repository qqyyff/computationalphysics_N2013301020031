import numpy as np
import matplotlib.pyplot as plt
import math
def wave(x01,x02,k,t,tt):
    c1=[]
    c2=[]
    c3=[]
    ct=[]
    cc=[]
    ca=[]
    ca1=[]
    for i in range(tt):
        x=i*2.0/tt
        tr=math.exp(-k*(x-x01)**2)+0*math.exp(-5*k*(x-x02)**2)
        c1.append(tr)
        c2.append(tr)
        cc.append(x)
    c1[0]=0
    c1[-1]=0
    c2[0]=0
    c1[-1]=0
    ca.append(c2[tt/20])
    ca1.append(0)
    for j in range(t):
        c3.append(c1[0])
        for k in range(1,tt-1):
            c3.append(c2[k+1]+c2[k-1]-c1[k])
        c3.append(c1[0])
        c1=[]
        for k in range(tt):
            c1.append(c2[k])
        c2=[]
        for k in range(tt):
            c2.append(c3[k])
        c3=[]
        ca.append(c2[tt/20])
        ca1.append(j+1)
    return c2,cc,ca,ca1
def wave2(x0,k,t,tt):
    c1=[]
    c2=[]
    c3=[]
    ct=[]
    cc=[]
    ca=[]
    ca1=[]
    for i in range(tt):
        x=i*2.0/tt
        if x<x0:
           c1.append(k*x)
           c2.append(k*x)
           cc.append(x)
        else:
           c1.append(k*x0/(x0-2.0)*(x-2))
           c2.append(k*x0/(x0-2.0)*(x-2))
           cc.append(x)
    c1[0]=0
    c1[-1]=0
    c2[0]=0
    c1[-1]=0
    ca.append(c2[tt/20])
    ca1.append(0)
    for j in range(t):
        c3.append(c1[0])
        for k in range(1,tt-1):
            c3.append(c2[k+1]+c2[k-1]-c1[k])
        c3.append(c1[0])
        c1=[]
        for k in range(tt):
            c1.append(c2[k])
        c2=[]
        for k in range(tt):
            c2.append(c3[k])
        c3=[]
        ca.append(c2[tt/20])
        ca1.append(j+1)
    return c2,cc,ca,ca1
ax1=plt.subplot(211)
ax2=plt.subplot(212)
plt.sca(ax1)
a,b,c,d=wave(1.0,1.5,200,4000,200)
plt.plot(d,c)
plt.xlabel('time/s')
plt.ylabel('signal')
plt.title('string signal of Guassian packet')

plt.sca(ax2)
a1,b1,c1,d1=wave2(1.0,30,4000,200)
plt.plot(d1,c1)
plt.xlabel('time/s')
plt.ylabel('signal')
plt.title('string signal of pluck')
plt.show()

#plt.ylim(0,5000)


