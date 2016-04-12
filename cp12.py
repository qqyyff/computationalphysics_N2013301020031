import numpy as np
import matplotlib.pyplot as plt
import math
def density(Y):
    d_a=0.0065
    T0=300
    d=2.5
    P=(1-(d_a*Y)/T0)**d
    return P
def drag(vx,vy):
    B=0.00004
    v=math.sqrt(vx**2+vy**2)
    fx=-B*vx*v
    fy=-B*vy*v
    return fx,fy
def transform(v,teth):
    a=math.pi/180
    vx=v*math.cos(teth*a)
    vy=v*math.sin(teth*a)
    return vx,vy
def trajectary(Vx0,Vy0):
   t_x=[]
   t_y=[]
   t_Vx=[]
   t_Vy=[]
   t_x.append(0)
   t_y.append(0)
   t_Vx.append(Vx0)
   t_Vy.append(Vy0)
   x=0
   y=0
   tau=0.001
   g=9.8
   B=0.1
   while t_y[-1]>=0:
     V=math.sqrt(t_Vx[-1]**2+t_Vy[-1]**2)
     x=x+t_Vx[-1]*tau
     t_x.append(x)
     y=y+t_Vy[-1]*tau
     t_y.append(y)
     f1,f2=0,0 #drag(t_Vx[-1],t_Vy[-1])
     Vy=t_Vy[-1]-g*tau+f2*density(y)
     t_Vy.append(Vy)
     Vx=t_Vx[-1]+f1*density(y)
     t_Vx.append(Vx)
   return t_x,t_y,t_Vx,t_Vy
def zeropoint(t1,t2):
    yt=-t2[-2]/t2[-1]
    xt=(t1[-2]+yt*t1[-1])/(1+yt)
    t1[-1]=xt
    t2[-1]=0
    return t1,t2
def data(ceth,v):
    XX=[]
    YY=[]
    VVX=[]
    VVY=[]
    for k in v:
        t1,t2=transform(k,ceth)
        a,b,c,d=trajectary(t1,t2)
        e,f=zeropoint(a,b)
        XX.append(e)
        YY.append(f)
        VVX.append(c)
        VVY.append(d)
    return XX,YY,VVX,VVY
def speed(ccet,x0,y0):
    v=[]
    for i in ccet:
        g=i*math.pi/180
        c=abs((x0*math.sin(g)-y0*math.cos(g))*math.cos(g))
        d=math.sqrt(4.9*x0*x0/c)
        v.append(d)
    return v
x0=400.0
y0=500.0
eeth=(math.atan(y0/x0)*180)/math.pi
tau1=(90-eeth)/10
ceta=[]
for j in range(1,10):
    ceta.append(eeth+j*tau1)
v1=speed(ceta,x0,y0)
g=[]
h=[]
b0=[]
n=[]
for i in v1:
    a0=[]
    a0.append(i)
    b=i*1.5
    a0.append(b)
    j=v1.index(i)
    g,h,b0,n=data(ceta[j],a0)
    plt.plot(g[0],h[0])
plt.scatter([x0,],[y0,],20,color='red')
plt.title('projection without air drag')
plt.xlabel('X/m')
plt.ylabel('Y/m') 
plt.xlim(0,)
plt.ylim(0,)
plt.show()    
print ceta,v1
