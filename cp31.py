import numpy as np
import matplotlib.pyplot as plt
import math
def orbits(x0,vy10,a,tt):
    au=149597870700.0
    yr=31558150.0
    G=6.67*10**(-11)
    Ms=1.989*10**(30)
    K=G*Ms
    x1=[]
    y1=[]
    vx1=[]
    vy1=[]
    vx1.append(0)
    vy1.append(vy10)
    x1.append(x0)
    y1.append(0)
    t=[]
    t.append(0)
    tau=0.0001
    for i in range(tt):
        x1.append(x1[-1]+vx1[-1]*tau)
        y1.append(y1[-1]+vy1[-1]*tau)
        r1=math.sqrt((x1[-1])**2+(y1[-1])**2)
        vx1.append(vx1[-1]-4*math.pi**2*(x1[-1])*(1/r1**3+a/r1**5)*tau)
        vy1.append(vy1[-1]-4*math.pi**2*(y1[-1])*(1/r1**3+a/r1**5)*tau)
        t.append(t[-1]+tau)
    return x1,y1,vx1,vy1
c=1.2
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
plt.sca(ax1)
x,y,vx,vy=orbits(0.47,8.2*c,0.01,10000)
plt.title('procession of Mercury with a=0.01,t=1yr')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.plot(x,y)
plt.sca(ax2)
x,y,vx,vy=orbits(0.47,8.2*c,0.01,20000)
plt.title('procession of Mercury with a=0.01,t=2yr')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.plot(x,y)
plt.sca(ax3)
x,y,vx,vy=orbits(0.47,8.2*c,0.01,50000)
plt.title('procession of Mercury with a=0.01,t=5yr')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.plot(x,y)
plt.sca(ax4)
x,y,vx,vy=orbits(0.47,8.2*c,0.01,100000)
plt.title('procession of Mercury with a=0.01,t=10yr')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.plot(x,y)
plt.show()
