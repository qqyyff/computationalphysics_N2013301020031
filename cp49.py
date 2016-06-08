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

ct=np.abs(np.fft.fft(c))
c=np.array(c)
timestep=0.01/300
freq = np.fft.fftfreq(c.shape[-1],timestep)
idx=np.argsort(freq)
plt.plot(freq[idx], ct[idx],color='red')
plt.xlim(0,4000)
plt.title('the power spectrum of guassian packets')
plt.xlabel('frequency(Hz)')
plt.ylabel('power')
#plt.ylim(0,5000)
plt.sca(ax2)
a1,b1,c1,d1=wave2(1.0,30,4000,200)
ct1=np.abs(np.fft.fft(c))
c1=np.array(c1)
timestep1=0.01/300
freq1 = np.fft.fftfreq(c1.shape[-1],timestep1)
idx1=np.argsort(freq1)
plt.plot(freq1[idx1], ct1[idx1])
plt.xlim(0,4000)
plt.title('the power spectrum of pluck')
plt.xlabel('frequency(Hz)')
plt.ylabel('power')
plt.show()
#plt.ylim(0,5000)

"""
plt.plot(d,c)
plt.xlabel('time/(iteration times)')
plt.ylabel('signal at middle')
plt.title('string signal versus time')
plt.show()
"""
"""
ax1=plt.subplot(811)
ax2=plt.subplot(812)
ax3=plt.subplot(813)
ax4=plt.subplot(814)
ax5=plt.subplot(815)
ax6=plt.subplot(816)
ax7=plt.subplot(817)
ax8=plt.subplot(818)
plt.sca(ax1)
a,b=wave(0.5,1.5,200,100,1200)
plt.plot(b,a)
plt.sca(ax2)
a1,b1=wave(0.5,1.5,200,200,1200)
plt.plot(b,a1)
plt.sca(ax3)
a,b=wave(0.5,1.5,200,300,1200)
plt.plot(b,a)
plt.sca(ax4)
a1,b1=wave(0.5,1.5,200,400,1200)
plt.plot(b,a1)
plt.sca(ax5)
a,b=wave(0.5,1.5,200,500,1200)
plt.plot(b,a)
plt.sca(ax6)
a1,b1=wave(0.5,1.5,200,600,1200)
plt.plot(b,a1)
plt.sca(ax7)
a,b=wave(0.5,1.5,200,700,1200)
plt.plot(b,a)
plt.sca(ax8)
a1,b1=wave(0.5,1.5,200,800,1200)
plt.plot(b,a1)
plt.show()
"""
