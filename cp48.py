import numpy as np
import matplotlib.pyplot as plt
import math
def wave(x0,k,t,tt):
    c1=[]
    c2=[]
    c3=[]
    cc=[]
    for i in range(tt):
        x=i*2.0/tt
        tr=math.exp(-k*(x-x0)**2)
        c1.append(tr)
        c2.append(tr)
        cc.append(x)
    c1[0]=0
    c1[-1]=0
    c2[0]=0
    c1[-1]=0
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
    return c2,cc
ax1=plt.subplot(811)
ax2=plt.subplot(812)
ax3=plt.subplot(813)
ax4=plt.subplot(814)
ax5=plt.subplot(815)
ax6=plt.subplot(816)
ax7=plt.subplot(817)
ax8=plt.subplot(818)
plt.sca(ax1)
a,b=wave(1.0,200,0,1200)
plt.plot(b,a)
plt.sca(ax2)
a1,b1=wave(1.0,200,100,1200)
plt.plot(b,a1)
plt.sca(ax3)
a,b=wave(1.0,200,300,1200)
plt.plot(b,a)
plt.sca(ax4)
a1,b1=wave(1.0,200,500,1200)
plt.plot(b,a1)
plt.sca(ax5)
a,b=wave(1.0,200,700,1200)
plt.plot(b,a)
plt.sca(ax6)
a1,b1=wave(1.0,200,900,1200)
plt.plot(b,a1)
plt.sca(ax7)
a,b=wave(1.0,200,1100,1200)
plt.plot(b,a)
plt.sca(ax8)
a1,b1=wave(1.0,200,1300,1200)
plt.plot(b,a1)
plt.show()
