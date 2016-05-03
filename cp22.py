import numpy as np
import matplotlib.pyplot as plt
import math
def trajectory(x0,y0,z0,o,r,b):
    x=[]
    y=[]
    z=[]
    t=[]
    x.append(x0)
    y.append(y0)
    z.append(z0)
    t.append(0)
    tau=0.001
    for i in range(1,30000):
       x.append(x[-1]+o*(y[-1]-x[-1])*tau)
       y.append(y[-1]+(r*x[-1]-x[-1]*z[-1]-y[-1])*tau)
       z.append(z[-1]+(x[-1]*y[-1]-b*z[-1])*tau)
       t.append(t[-1]+tau)
    return x,y,z,t

ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)

a,b,c,d=trajectory(1.0,0,0,10,25,8.0/3.0)
"""
plt.plot(d,c)
plt.show()
"""

"""
plt.plot(a,c)
plt.show()
"""
plt.sca(ax1)
tt=[]
for i in range(len(d)):
    if abs(a[i]+10.0)<0.01:
       tt.append(i)
       plt.scatter([b[tt[-1]],],[c[tt[-1]],],1,color='red') 
plt.title('phase space plot:z versus y when x=-10')
plt.sca(ax2)
tt=[]
for i in range(len(d)):
    if abs(b[i]+10.0)<0.01:
       tt.append(i)
       plt.scatter([a[tt[-1]],],[c[tt[-1]],],1,color='red') 
plt.title('phase space plot:z versus x when y=-10')
plt.sca(ax3)
tt=[]
for i in range(len(d)):
    if abs(a[i]-10.0)<0.01:
       tt.append(i)
       plt.scatter([b[tt[-1]],],[c[tt[-1]],],1,color='red')
plt.title('phase space plot:z versus y when x=10')
plt.sca(ax4)
tt=[]
for i in range(len(d)):
    if abs(b[i]-10.0)<0.01:
       tt.append(i)
       plt.scatter([a[tt[-1]],],[c[tt[-1]],],1,color='red')
plt.title('phase space plot:z versus x when y=10')
plt.show()

