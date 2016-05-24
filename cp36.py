import numpy as np
import matplotlib.pyplot as plt
import math
def tra(a,c3,tt):
    aa=4*math.pi**2
    x1=[]
    y1=[]
    vx1=[]
    vy1=[]
    x2=[]
    y2=[]
    vx2=[]
    vy2=[]
    x3=[]
    y3=[]
    vx3=[]
    vy3=[]
    a1=a*0.001
    b1=0.3*0.001**2
    xx=(a1*5.2+b1)/(a1+1+b1)
    x1.append(1.0-xx)
    y1.append(0)
    x2.append(5.2-xx)
    y2.append(0)
    x3.append(-xx)
    y3.append(0)
    e1=0.017
    e2=0.048
    vi1=2*math.pi*math.sqrt((1-e1)/(1+e1))
    vi2=2*math.pi*math.sqrt((1-e2)/(5.2*(1+e2)))
    vi3=-c3*(vi1*a1+vi2*b1)
    v11=c3*vi1
    v22=c3*vi2
    v33=vi3
    vx1.append(0)
    vy1.append(v11)
    vx2.append(0)
    vy2.append(v22)
    vx3.append(0)
    vy3.append(v33)
    tau=0.00001
    for i in range(tt):
      x1.append(x1[-1]+vx1[-1]*tau)
      y1.append(y1[-1]+vy1[-1]*tau)
      x2.append(x2[-1]+vx2[-1]*tau)
      y2.append(y2[-1]+vy2[-1]*tau)
      x3.append(x3[-1]+vx3[-1]*tau)
      y3.append(y3[-1]+vy3[-1]*tau)
      r1=math.sqrt((x1[-1]-x3[-1])**2+(y1[-1]-y3[-1])**2)
      r2=math.sqrt((x2[-1]-x3[-1])**2+(y2[-1]-y3[-1])**2)
      r12=math.sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
      vx1.append(vx1[-1]-(aa*(x1[-1]-x3[-1])/r1**3+aa*a1*(x1[-1]-x2[-1])/r12**3)*tau)
      vy1.append(vy1[-1]-(aa*(y1[-1]-y3[-1])/r1**3+aa*a1*(y1[-1]-y2[-1])/r12**3)*tau)
      vx2.append(vx2[-1]-(aa*(x2[-1])-x3[-1]/r2**3+aa*b1*(x2[-1]-x1[-1])/r12**3)*tau)
      vy2.append(vy2[-1]-(aa*(y2[-1]-y3[-1])/r2**3+aa*b1*(y1[-1]-y2[-1])/r12**3)*tau)
      vx3.append(vx3[-1]-(aa*a1*(x3[-1]-x2[-1])/r2**3+aa*b1*(x3[-1]-x1[-1])/r1**3)*tau)
      vy3.append(vy3[-1]-(aa*a1*(y3[-1]-y2[-1])/r2**3+aa*b1*(y3[-1]-y1[-1])/r1**3)*tau)
    return x1,y1,x2,y2,x3,y3

for i in range(9,10):
    a,b,c,d,e,f=tra(265,0.6,1000000)
    plt.plot(a,b)
    plt.xlabel('X(AU)')
    plt.ylabel('Y(AU)')
    plt.title('the orbit of earth when jupiter=265MJ')
    plt.show()

