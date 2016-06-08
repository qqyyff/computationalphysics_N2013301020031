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
def waved(x01,L,k,r,M,e,t,tt):
    c1=[]
    c2=[]
    c3=[]
    ct=[]
    cc=[]
    ca=[]
    ca1=[]
    for i in range(tt):
        x=i*L/tt
        tr=math.exp(-k*(x-x01)**2)
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
        c3.append(c1[1])
        for k in range(2,tt-2):
            c3.append((2-2*r**2-6*e*r**2*M**2)*c2[k]-c1[k]+r**2*(1+4*e*M**2)*(c2[k+1]+c2[k-1])-e*r**2*M**2*(c2[k+2]+c2[k-2]))
        c3.append(c1[0])
        c3.append(-c3[-2])
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
"""
#a,b,c,d=waved(1.0,200,0.25,200,0.000001,1000,200)
ax1=plt.subplot(211)
ax2=plt.subplot(212)
plt.sca(ax1)
a,b,c,d=wave(1.0,1.5,200,4000,200)
plt.plot(d,c)
plt.xlabel('time/s')
plt.ylabel('signal')
plt.title('string signal of Guassian packet')

plt.sca(ax2)
a1,b1,c1,d1=waved(1.0,200,0.25,200,0.000001,4000,200)
plt.plot(d1,c1)
plt.xlabel('time/s')
plt.ylabel('signal')
plt.title('damp string signal')
plt.show()
"""
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
plt.sca(ax1)
a,b,c,d=waved(1.0,1.9,200,0.25,200,0.0000075,4000,200)
ct=np.abs(np.fft.fft(c))
c=np.array(c)
timestep=1.9/(200*4*250)
freq = np.fft.fftfreq(c.shape[-1],timestep)
idx=np.argsort(freq)
plt.plot(freq, ct,color='red')
plt.xlim(0,4000)
plt.title('the power spectrum of C2')
plt.xlabel('frequency(Hz)')
plt.ylabel('power')
#plt.ylim(0,5000)

plt.sca(ax2)
a1,b1,c1,d1=waved(1.0,0.62,200,0.25,200,0.0000038,4000,200)
ct1=np.abs(np.fft.fft(c1))
c1=np.array(c1)
timestep1=0.62/(200*4*330)
freq1 = np.fft.fftfreq(c1.shape[-1],timestep1)
idx1=np.argsort(freq1)
plt.plot(freq1, ct1)
plt.xlim(0,50000)
plt.title('the power spectrum of C4')
plt.xlabel('frequency(Hz)')
plt.ylabel('power')
plt.sca(ax3)
a1,b1,c1,d1=waved(1.0,0.09,200,0.25,200,0.000087,4000,200)
ct1=np.abs(np.fft.fft(c1))
c1=np.array(c1)
timestep1=0.09/(200*4*380)
freq1 = np.fft.fftfreq(c1.shape[-1],timestep1)
idx1=np.argsort(freq1)
plt.plot(freq1, ct1)
plt.xlim(0,500000)
plt.title('the power spectrum of C7')
plt.xlabel('frequency(Hz)')
plt.ylabel('power')
plt.show()

"""
ax1=plt.subplot(811)
ax2=plt.subplot(812)
ax3=plt.subplot(813)
ax4=plt.subplot(814)
ax5=plt.subplot(815)
ax6=plt.subplot(816)
ax7=plt.subplot(817)
ax8=plt.subplot(818)
ax9=plt.subplot(811)
ax10=plt.subplot(812)
ax11=plt.subplot(813)
ax12=plt.subplot(814)
ax13=plt.subplot(815)
ax14=plt.subplot(816)
ax15=plt.subplot(817)
ax16=plt.subplot(818)
plt.sca(ax1)
a,b,c,d=waved(1.0,200,0.25,200,0.000001,100,200)
plt.plot(b,a)
plt.sca(ax2)
a,b,c,d=waved(1.0,200,0.25,200,0.000001,200,200)
plt.plot(b,a)
plt.sca(ax3)
a,b,c,d=waved(1.0,200,0.25,200,0.000001,300,200)
plt.plot(b,a)
plt.sca(ax4)
a,b,c,d=waved(1.0,200,0.25,200,0.000001,400,200)
plt.plot(b,a)
plt.sca(ax5)
a,b,c,d=waved(1.0,200,0.25,200,0.000001,500,200)
plt.plot(b,a)
plt.sca(ax6)
a,b,c,d=waved(1.0,200,0.25,200,0.000001,600,200)
plt.plot(b,a)
plt.sca(ax7)
a,b,c,d=waved(1.0,200,0.25,200,0.000001,700,200)
plt.plot(b,a)
plt.sca(ax8)
a,b,c,d=waved(1.0,200,0.25,200,0.000001,800,200)
plt.plot(b,a)
plt.sca(ax1)
a,b,c,d=waved(1.0,200,0.25,200,0.00002,100,200)
plt.plot(b,a)
plt.sca(ax2)
a,b,c,d=waved(1.0,200,0.25,200,0.00002,200,200)
plt.plot(b,a)
plt.sca(ax3)
a,b,c,d=waved(1.0,200,0.25,200,0.00002,300,200)
plt.plot(b,a)
plt.sca(ax4)
a,b,c,d=waved(1.0,200,0.25,200,0.00002,400,200)
plt.plot(b,a)
plt.sca(ax5)
a,b,c,d=waved(1.0,200,0.25,200,0.00002,500,200)
plt.plot(b,a)
plt.sca(ax6)
a,b,c,d=waved(1.0,200,0.25,200,0.00002,600,200)
plt.plot(b,a)
plt.sca(ax7)
a,b,c,d=waved(1.0,200,0.25,200,0.00002,700,200)
plt.plot(b,a)
plt.sca(ax8)
a,b,c,d=waved(1.0,200,0.25,200,0.00002,800,200)
plt.plot(b,a)

plt.show()
"""
