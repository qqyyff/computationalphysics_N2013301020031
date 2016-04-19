import numpy as np
import matplotlib.pyplot as plt
import math
def trajectory(z0,v0,ceta0,cetah,ct,vw):
    tau=0.0001
    ca=ceta0*math.pi/180
    cah=cetah*math.pi/180
    x=[]
    y=[]
    z=[]
    Vx=[]
    Vy=[]
    Vz=[]
    t=[]
    ome=0.2*2*math.pi
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
          gg=ome*t[-1]+ct
          ff=g*0.5*(math.sin(4.0*gg)-0.25*math.sin(8.0*gg)+0.08*math.sin(12.0*gg)-0.025*math.sin(16.0*gg))
          Vy.append(Vy[-1]-ff*tau)
          Vz.append(Vz[-1]-g*tau-a*v*Vz[-1]*tau)
          t.append(t[-1]+tau)
    return x,y,z,Vx,Vy,Vz,t
a,b,c,d,e,f,g=trajectory(1.8,29,0,0,120,0)
plt.plot(a,b,label='with initial orientation angle:120')
a,b,c,d,e,f,g=trajectory(1.8,29,0,0,60,0)
plt.plot(a,b,label='with initial orientation angle:60')
a,b,c,d,e,f,g=trajectory(1.8,29,0,0,90,0)
plt.plot(a,b,label='with initial orientation angle:90')
a,b,c,d,e,f,g=trajectory(1.8,29,0,0,30,0)
plt.plot(a,b,label='with initial orientation angle:30')
plt.plot([a[-1],a[-1]],[-0.8,0.3],color='orange',linewidth=1.0,linestyle='--')
plt.legend(loc='upper left',frameon=True)
plt.title('the trajectory of a knuckball') 
plt.xlabel('x/m')
plt.ylabel('horizontal displacement(z)/m')
plt.xlim(0,)
plt.show()
