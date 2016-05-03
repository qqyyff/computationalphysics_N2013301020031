import numpy as np
import matplotlib.pyplot as plt
import math
def heart(a):
    tau=2*math.pi/10000
    x=[]
    y=[]
    theta=[]
    theta.append(0)
    for i in range(10000):
        r=a*(1-math.cos(theta[-1]))
        x.append(r*math.cos(theta[-1]))
        y.append(r*math.sin(theta[-1]))
        theta.append(theta[-1]+tau)
    return x,y
def trajectory(x0,y0,vx0,vy0,a1,tt):
    x=[]
    y=[]
    x.append(x0)
    y.append(y0)
    vx=vx0
    vy=vy0
    tau=0.001
    for i in range(tt):
        x.append(x[-1]+vx*tau)
        y.append(y[-1]+vy*tau)
        dd=math.sqrt(x[-1]**2+y[-1]**2)
        if (a1*(1-x[-1]/dd))<dd:
            r=a1*(1-x[-1]/dd)
            d1=2*r-dd
            x.append(x[-1]*d1/dd)
            y.append(y[-1]*d1/dd)
            ce=a1/dd-2
            dt=math.sqrt(y[-1]**2+(x[-1]-a1/ce)**2)
            cs=(x[-1]-a1/ce)/dt
            ss=y[-1]/dt
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
    return x,y
"""
        if -a1+x[-1]<tau and abs(y[-1])<tau/2.0:
            x[-1]=2*a1-x[-1]
            vx=-vx
"""
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
plt.sca(ax1)
c,d=heart(1.0)
v,f=trajectory(0,0,1.0,2.0,1.0,20000)
plt.title('elliptical stadium20s')
plt.xlim(-2.0,2.0)
plt.ylim(-2.0,0.5)
plt.plot(d,c)
plt.plot(f,v)
plt.sca(ax2)
c,d=heart(1.0)
v,f=trajectory(0,0,1.0,2.0,1.0,50000)
plt.title('elliptical stadium50s')
plt.xlim(-2.0,2.0)
plt.ylim(-2.0,0.5)
plt.plot(d,c)
plt.plot(f,v)
plt.sca(ax3)
c,d=heart(1.0)
v,f=trajectory(0,0,1.0,2.0,1.0,100000)
plt.title('elliptical stadium100s')
plt.xlim(-2.0,2.0)
plt.ylim(-2.0,0.5)
plt.plot(d,c)
plt.plot(f,v)
plt.sca(ax4)
c,d=heart(1.0)
v,f=trajectory(0,0,1.0,2.0,1.0,200000)
plt.title('elliptical stadium200s')
plt.xlim(-2.0,2.0)
plt.ylim(-2.0,0.5)
plt.plot(d,c)
plt.plot(f,v)
plt.show()
