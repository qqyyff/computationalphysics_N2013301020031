import numpy as np
import matplotlib.pyplot as plt
import math
def trajectory(z0,v0,ceta0,cetah,w,vw):
    tau=0.0001
    ca=ceta0*math.pi/180
    cah=cetah*math.pi/180
    wo=w*2*math.pi
    x=[]
    y=[]
    z=[]
    Vx=[]
    Vy=[]
    Vz=[]
    t=[]
    vx0=v0*math.cos(ca)*math.cos(cah)
    vy0=v0*math.cos(ca)*math.sin(cah)
    vz0=v0*math.sin(ca)
    x.append(0)
    y.append(0)
    z.append(z0)
    Vx.append(vx0)
    Vy.append(vy0)
    Vz.append(vz0)
    t.append(0)
    g=9.8
    b=0.00041
    while z[-1]>0:
          v=math.sqrt((Vx[-1]-vw)**2+Vz[-1]**2+Vy[-1]**2)
          a=0.0039+0.0058/(1+math.exp((v-35.0)/5.0))
          x.append(x[-1]+Vx[-1]*tau)
          y.append(y[-1]+Vy[-1]*tau)
          z.append(z[-1]+Vz[-1]*tau)
          Vx.append(Vx[-1]-a*v*(Vx[-1]-vw)*tau)
          Vy.append(Vy[-1]+b*wo*Vx[-1]*tau)
          Vz.append(Vz[-1]-g*tau-a*v*Vz[-1]*tau)
          t.append(t[-1]+tau)
    return x,y,z,Vx,Vy,Vz,t
a,b,c,d,e,f,g=trajectory(1.8,50,0,0,30,0)
plt.plot(a,c,label='x-z vertical displacement with angle(0,0)')
plt.plot(a,b,label='x-y horizontal displacement with angle(0,0)')
plt.plot([a[-1],a[-1]],[0,25.0],color='orange',linewidth=1.0,linestyle='--')
a,b,c,d,e,f,g=trajectory(1.8,50,5,5,30,0)
plt.plot(a,c,label='x-z vertical displacement with angle(5,5)')
plt.plot(a,b,label='x-y horizontal displacement with angle(5,5)')
plt.plot([a[-1],a[-1]],[0,25.0],color='orange',linewidth=1.0,linestyle='--')
a,b,c,d,e,f,g=trajectory(1.8,50,10,10,30,0)
plt.plot(a,c,label='x-z vertical displacement with angle(10,10)')
plt.plot(a,b,label='x-y horizontal displacement with angle(10,10)')
plt.plot([a[-1],a[-1]],[0,25.0],color='orange',linewidth=1.0,linestyle='--')
plt.legend(loc='upper left',frameon=True)
plt.title('the trajectory of a curve ball') 
plt.xlabel('x/m')
plt.ylabel('y(z)/m')
plt.xlim(0,)
plt.ylim(0,)
plt.show()
