import numpy as np
import matplotlib.pyplot as plt
import math
def tra(a,tt):
    aa=4*math.pi**2
    x1=[]
    y1=[]
    vx1=[]
    vy1=[]
    x2=[]
    y2=[]
    vx2=[]
    vy2=[]
    a1=a*0.001
    b1=0.3*0.001**2
    x1.append(1.0)
    y1.append(0)
    x2.append(5.2)
    y2.append(0)
    e1=0.017
    e2=0.048
    v11=2*math.pi*math.sqrt((1-e1)/(1+e1))
    v22=2*math.pi*math.sqrt((1-e2)/(5.2*(1+e2)))
    vx1.append(0)
    vy1.append(v11)
    vx2.append(0)
    vy2.append(v22)
    tau=0.01
    for i in range(tt):
      x1.append(x1[-1]+vx1[-1]*tau)
      y1.append(y1[-1]+vy1[-1]*tau)
      x2.append(x2[-1]+vx2[-1]*tau)
      y2.append(y2[-1]+vy2[-1]*tau)
      r1=math.sqrt((x1[-1])**2+(y1[-1])**2)
      r2=math.sqrt((x2[-1])**2+(y2[-1])**2)
      r12=math.sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
      vx1.append(vx1[-1]-(aa*(x1[-1])*(1/r1**3)-aa*a1*(x1[-1]-x2[-1])/r12**3)*tau)
      vy1.append(vy1[-1]-(aa*(y1[-1])*(1/r1**3)-aa*a1*(y1[-1]-y2[-1])/r12**3)*tau)
      vx2.append(vx2[-1]-(aa*(x2[-1])*(1/r2**3)-aa*b1*(x2[-1]-x1[-1])/r12**3)*tau)
      vy2.append(vy2[-1]-(aa*(y2[-1])*(1/r2**3)-aa*b1*(y1[-1]-y2[-1])/r12**3)*tau)
    return x1,y1,x2,y2
"""
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
plt.sca(ax1)
a,b,c,d=tra(1,2000)
plt.plot(a,b,color='orange',label='trajectory of earth')
plt.plot(c,d,color='purple',label='trajectory of jupiter')
plt.legend(loc='upper right')
plt.xlabel('X(AU)')
plt.ylabel('Y(AU)')
plt.title('mass of jupiter=MJ')
plt.sca(ax2)
a,b,c,d=tra(10,2000)
plt.plot(a,b,color='orange',label='trajectory of earth')
plt.plot(c,d,color='purple',label='trajectory of jupiter')
plt.legend(loc='upper right')
plt.xlabel('X(AU)')
plt.ylabel('Y(AU)')
plt.title('mass of jupiter=10MJ')
plt.sca(ax3)
a,b,c,d=tra(100,500)
plt.plot(a,b,color='orange',label='trajectory of earth')
plt.plot(c,d,color='purple',label='trajectory of jupiter')
plt.legend(loc='upper right')
plt.xlabel('X(AU)')
plt.ylabel('Y(AU)')
plt.title('mass of jupiter=100MJ')
plt.sca(ax4)
a,b,c,d=tra(1000,2000)
plt.plot(a,b,color='orange',label='trajectory of earth')
plt.plot(c,d,color='purple',label='trajectory of jupiter')
plt.legend(loc='upper right')
plt.xlabel('X(AU)')
plt.ylabel('Y(AU)')
plt.title('mass of jupiter=1000MJ')
plt.show()
"""

