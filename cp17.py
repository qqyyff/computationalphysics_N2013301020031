import numpy as np
import matplotlib.pyplot as plt
import math
def trajectory(z0,v0,ceta0,w,vw):
    tau=0.0001
    ca=ceta0*math.pi/180
    wo=w*2*math.pi
    x=[]
    y=[]
    z=[]
    Vx=[]
    Vy=[]
    Vz=[]
    t=[]
    vx0=v0*math.cos(ca)
    vz0=v0*math.sin(ca)
    x.append(0)
    y.append(0)
    z.append(z0)
    Vx.append(vx0)
    Vy.append(0)
    Vz.append(vz0)
    t.append(0)
    g=9.8
    b=0.00041
    while z[-1]>0:
          v=math.sqrt((Vx[-1]-vw)**2+Vz[-1]**2)
          a=0.0039+0.0058/(1+math.exp((v-35.0)/5.0))
          x.append(x[-1]+Vx[-1]*tau)
          y.append(y[-1]+Vy[-1]*tau)
          z.append(z[-1]+Vz[-1]*tau)
          Vx.append(Vx[-1]-a*v*(Vx[-1]-vw)*tau)
          Vy.append(Vy[-1])
          Vz.append(Vz[-1]-g*tau+b*wo*Vx[-1]*tau-a*v*Vz[-1]*tau)
          t.append(t[-1]+tau)
    return x,y,z,Vx,Vy,Vz,t
a,b,c,d,e,f,g=trajectory(1.8,50,35,0,0)
plt.plot(a,c,label='without backspin')
a,b,c,d,e,f,g=trajectory(1.8,50,35,10,0)
plt.plot(a,c,label='with backspin 10rps')
a,b,c,d,e,f,g=trajectory(1.8,50,35,20,0)
plt.plot(a,c,label='with backspin 20rps')
a,b,c,d,e,f,g=trajectory(1.8,50,35,30,0)
plt.plot(a,c,label='with backspin 30rps')
a,b,c,d,e,f,g=trajectory(1.8,50,35,40,0)
plt.plot(a,c,label='with backspin 40rps')
plt.legend(loc='upper right',frameon=True)
plt.title('trajectory of a baseball with backspin')
plt.xlabel('X(m)')
plt.ylabel('Y(m)')
plt.xlim(0,)
plt.ylim(0,)
plt.show()
