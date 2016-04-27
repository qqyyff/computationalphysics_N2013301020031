import numpy as np
import matplotlib.pyplot as plt
import math
def trajectory(x0,fd,w0):
    q=0.5
    g=1.0
    x=[]
    v=[]
    t=[]
    x.append(x0)
    v.append(0)
    t.append(0)
    tau=0.1
    for i in range(1,100000):
        x.append(x[i-1]+v[i-1]*tau)
        t.append(t[i-1]+tau)
        v.append(v[i-1]-(g*math.sin(x[i])+q*v[i-1]-fd*math.sin(w0*t[i]))*tau)
        if x[-1]>=math.pi:
           x[-1]=-2*math.pi+x[-1]
           #v[-1]=-v[-1]
        elif x[-1]<=-math.pi:
           x[-1]=x[-1]+2*math.pi
           #v[-1]=-v[-1]
    return x,v,t
"""
a,b,c=trajectory(0.1,1.44,2.0/3.0)
plt.plot(c,a,label='x0= 0.1')
a,b,c=trajectory(0.2,1.44,2.0/3.0)
plt.plot(c,a,label='x0= 0.2')
a,b,c=trajectory(0.3,1.44,2.0/3.0)
plt.plot(c,a,label='x0= 0.3')
a,b,c=trajectory(0.4,1.44,2.0/3.0)
plt.plot(c,a,label='x0= 0.4')
plt.legend(loc='lower left', frameon=True)
plt.xlabel('time/s')
plt.ylabel('radius')
plt.show()
"""
"""
a,b,c=trajectory(0.02,0.5,2.0/3.0)
a1,b1,c1=trajectory(0.021,0.5,2.0/3.0)

t=[]
for j in range(len(a)):
    t.append(math.log10(abs(a[j]-a1[j])))
plt.plot(c,t)
plt.yticks([0,-10,-8,-6,-4,-2])
plt.show()
"""
"""
a,b,c=trajectory(0.02,1.2,2.0/3.0)
a1,b1,c1=trajectory(0.021,1.2,2.0/3.0)
t=[]
for j in range(len(a)):
    t.append(math.log10(abs(a[j]-a1[j])))
plt.plot(c,t)
plt.show()
"""
"""
a,b,c=trajectory(0.2,0.5,2.0/3.0)
plt.plot(a,b)
plt.xlabel('radians')
plt.ylabel('radians/s')
plt.show()
"""
"""
a,b,c=trajectory(0.2,1.2,2.0/3.0)
plt.plot(a,b)
plt.xlabel('radians')
plt.ylabel('radians/s')
plt.show()
"""

w1=[]
theta=[]
a,b,c=trajectory(3.0,1.2,4.0/3.0)
for i in range(len(c)):
    gh=(c[i]-9*math.pi/16.0)*2.0/(math.pi*3.0)
    if abs(gh-round(gh))<=0.001:
       w1.append(c[i])
       plt.scatter([a[i],],[b[i],], 1, color ='red')
print len(w1)
plt.xlabel('radians')
plt.ylabel('radians/s')
plt.show()

"""
t1=[]
a,b,c=trajectory(0.2,1.34,2.0/3.0)
for j in c:
       gh=j/(math.pi*3.0)
       if 980*math.pi>j>900*math.pi and abs(gh-round(gh))<=0.005:
          tt=c.index(j)
          t1.append(tt)
for i in range(1,100):
    ff=1.40+i*0.001
    a,b,c=trajectory(0.2,ff,2.0/3.0)
    for k in t1:
        if abs(a[k]-a[t1[0]])>0.1:
           plt.scatter([ff,],[a[k],], 1, color ='red')
plt.show()
"""
