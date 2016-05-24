import numpy as np
import matplotlib.pyplot as plt
import math
def tra(tt,jj):
    aa=4*math.pi**2
    x1=[]
    y1=[]
    vx1=[]
    vy1=[]
    x2=[]
    y2=[]
    vx2=[]
    vy2=[]
    a1=0.001
    b1=0.3*0.001**2
    y1.append(0)
    x2.append(5.2)
    y2.append(0)
    e2=0.048
    v22=2*math.pi*math.sqrt((1-e2)/(5.2*(1+e2)))
    vx1.append(0)
    vx2.append(0)
    vy2.append(v22)
    tau=0.001
    tr=[]
    ts=[]
    rr=[]
    for j in range(jj/4,jj):
        a=j*5.0/jj
        rr.append(a)
        x1.append(a)
        v11=2*math.pi*math.sqrt(1.0/a)
        vy1.append(v11)
        tr.append(math.sqrt(x1[-1]**2+y1[-1]**2))
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
            if r1>tr[-1]:
               tr.append(r1)
        ts.append(tr[-1]/a)
        tr=[]
        x1=[]
        x2=[]
        y1=[]
        y2=[]
        vx1=[]
        vy1=[]
        vx2=[]
        vy2=[]
        y1.append(0)
        x2.append(5.2)
        y2.append(0)
        e2=0.048
        v22=2*math.pi*math.sqrt((1-e2)/(5.2*(1+e2)))
        vx1.append(0)
        vx2.append(0)
        vy2.append(v22)
    return rr,ts
a,b=tra(10000,1000)
plt.plot(a,b)
plt.xlabel('radius(AU)')
plt.ylabel('eccentricity')
plt.title('the orbit radius versus eccentricity')
plt.show()


