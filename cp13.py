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
   tau=0.001
   x=0
   y=0
   g=9.8
   B=0.1
   while t_y[-1]>=0:
     V=math.sqrt(t_Vx[-1]**2+t_Vy[-1]**2)
     x=x+t_Vx[-1]*tau
     t_x.append(x)
     y=y+t_Vy[-1]*tau
     t_y.append(y)
     f1,f2=drag(t_Vx[-1],t_Vy[-1])
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
        t1,t2=transform(v,ceth)
        a,b,c,d=trajectary(t1,t2)
        e,f=zeropoint(a,b)
        return e,f,c,d
def compare(v_0,ccrf,uu):
    ll=[]
    d=math.sqrt(x0**2+y0**2)
    g,h,b0,n= data(ccrf,v_0)
    for k in range(len(g)):
        c=h[k]/(g[k]+0.0001)
        ll.append(abs(c-uu))
    tt=min(ll)
    j=ll.index(tt)        
    d1=math.sqrt(g[j]**2+h[j]**2)
    if d1>2*d:
       v0=v_0/2.0
       return compare(v0,ccrf,uu)
    elif d1-d>0.1*d:
         v0=v_0*9.0/10.0
         return compare(v0,ccrf,uu)
    elif d1-d>0.01*d:
         v0=v_0*99.0/100.0
         return compare(v0,ccrf,uu)
    elif abs(d1-d)<0.01*d:
         return v_0,abs(d1-d)
    elif d-d1>0.01*d:
         v0=v_0*100.0/99.0
         return compare(v0,ccrf,uu)
    elif d-d1>0.1*d:
         v0=v_0*10.0/9.0
         return compare(v0,ccrf,uu)
    elif d>2*d1:
         v0=v_0*2
         return compare(v0,ccrf,uu)
x0=input("the target coordinate-X is: ")
y0=input("the target coordinate-Y is: ")
#tau=math.sqrt(x0**2+y0**2)/100
v0=1.0
dd=y0/x0
#cr=input("the angle of emission is: ")
#gh,hk=compare(v0,cr,dd)
#b1,b2,b3,b4=data(cr,gh)
#plt.plot(b1,b2)
#print hk
eeth=(math.atan(y0/x0)*180)/math.pi
tau1=(90-eeth)/20
ceta=[]
tt=[]
yy=[]
for j in range(1,20):
    ceta.append(eeth+j*tau1)
for k in ceta:
    gh,hk=compare(v0,k,dd)
    tt.append(gh)
    yy.append(hk)
    b1,b2,b3,b4=data(k,gh)
    plt.plot(b1,b2)
    print k,gh,hk
plt.title('projection with air drag')
plt.xlabel('X/m')
plt.ylabel('Y/m')
plt.xlim(0,)
plt.ylim(0,)
plt.scatter([x0,],[y0,],20,color='red')
#plt.show()
#print yy
#plt.plot(ceta,tt)
plt.show()
                            
