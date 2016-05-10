import numpy as np
import matplotlib.pyplot as plt
import math
def orbits(x0,y0,vx10,vy10,vx20,vy20,r,tt):
    au=149597870700.0
    yr=31558150.0
    G=6.67*10**(-11)
    Ms=1.989*10**(30)
    K=G*Ms
    x2=[]
    y2=[]
    vx2=[]
    vy2=[]
    vx2.append(vx20)
    vy2.append(vy20)
    x2.append(0)
    y2.append(0)
    x1=[]
    y1=[]
    vx1=[]
    vy1=[]
    vx1.append(vx10)
    vy1.append(vy10)
    x1.append(x0)
    y1.append(y0)
    t=[]
    t.append(0)
    tau=tt
    for i in range(100000):
        x1.append(x1[-1]+vx1[-1]*tau)
        y1.append(y1[-1]+vy1[-1]*tau)
        x2.append(x2[-1]+vx2[-1]*tau)
        y2.append(y2[-1]+vy2[-1]*tau)
        r1=math.sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
        vx1.append(vx1[-1]-(4*math.pi**2*(x1[-1]-x2[-1])/r1**3)*tau)
        vy1.append(vy1[-1]-(4*math.pi**2*(y1[-1]-y2[-1])/r1**3)*tau)
        vx2.append(vx2[-1]-(r*4*math.pi**2*(x2[-1]-x1[-1])/r1**3)*tau)
        vy2.append(vy2[-1]-(r*4*math.pi**2*(y2[-1]-y1[-1])/r1**3)*tau)
        t.append(t[-1]+tau)
    return x1,y1,x2,y2
c=math.sqrt(2.0)
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
plt.sca(ax1)
x,y,vx,vy=orbits(1.0,0,0,math.pi,0,-1*math.pi,2.0,0.00002)
plt.plot(x,y,label='the sun trajectory')
plt.plot(vx,vy,label='the planet trajectory')
plt.title('the two body problem with ms/mp=2.0,vp/vs=1.0')
plt.xlabel('X(AU)')
plt.ylabel('Y(AU)')
plt.legend(loc='upper right',frameon=True)
plt.sca(ax2)
x,y,vx,vy=orbits(1.0,0,0,math.pi,0,-2*math.pi,2.0,0.00002)
plt.plot(x,y,label='the sun trajectory')
plt.plot(vx,vy,label='the planet trajectory')
plt.title('the two body problem with ms/mp=2.0,vp/vs=2.0')
plt.xlabel('X(AU)')
plt.ylabel('Y(AU)')
plt.legend(loc='upper right',frameon=True)
plt.sca(ax3)
x,y,vx,vy=orbits(1.0,0,0,math.pi,0,-3*math.pi,2.0,0.00002)
plt.plot(x,y,label='the sun trajectory')
plt.plot(vx,vy,label='the planet trajectory')
plt.title('the two body problem with ms/mp=2.0,vp/vs=3.0')
plt.xlabel('X(AU)')
plt.ylabel('Y(AU)')
plt.legend(loc='upper right',frameon=True)
plt.sca(ax4)
x,y,vx,vy=orbits(1.0,0,0,math.pi,0,-4*math.pi,2.0,0.00002)
plt.plot(x,y,label='the sun trajectory')
plt.plot(vx,vy,label='the planet trajectory')
plt.title('the two body problem with ms/mp=2.0,vp/vs=4.0')
plt.xlabel('X(AU)')
plt.ylabel('Y(AU)')
plt.legend(loc='upper right',frameon=True)
plt.show()
