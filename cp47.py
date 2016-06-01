from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
def part(a,b,tt):
    tq=0
    ct=[]
    tc1=[]
    tc2=[]
    tc3=[]
    v0=[]
    v00=[]
    v1=[]
    vt=[b]*tt
    v0.append(vt)
    vr=[]
    vr2=[]
    vr2.append(b)
    vr.append(b)
    vc=[]
    for k in range(1,tt-1):
        if abs(k*1.0/tt-0.5)<0.25:
           vr.append(a)
           vr2.append(-a)
        else:
           vr2.append(0)
           vr.append(0)
    vr.append(b)
    vr2.append(b)
    v1.append(b)
    for i in range(1,tt-1):
        v1.append(0)
    v1.append(b)
    for i in range(1,tt-1):
        if i*1.0/tt==0.25:
           v0.append(vr)
        elif i*1.0/tt==0.75:
           v0.append(vr2)
        else: 
           v0.append(v1)
    v0.append(vt)
    v00.append(vt)
    for m in range(10000):
        for i in range(1,tt-1):
            vc.append(b)
            for j in range(1,tt-1):
                  if (i*1.0/tt==0.25 and abs(j*1.0/tt-0.5)<0.25):
                     vc.append(a) 
                  elif (i*1.0/tt==0.75 and abs(j*1.0/tt-0.5)<0.25):
                     vc.append(-a)       
                  else:
                     vc.append((v0[i-1][j]+v0[i+1][j]+v0[i][j+1]+v0[i][j-1])/4.0)
            vc.append(b)
            v00.append(vc)
            vc=[]
        ct.append(v00[tt/4][3*tt/4+1])
        v00.append(vt)
        v0=[]
        v0.append(vt)
        for i in range(1,tt-1):
            vc.append(b)
            for j in range(1,tt-1):
                  if (i*1.0/tt==0.25 and abs(j*1.0/tt-0.5)<0.25):
                     vc.append(a)
                  elif (i*1.0/tt==0.75 and abs(j*1.0/tt-0.5)<0.25):
                     vc.append(-a)
                  else:
                     vc.append((v00[i-1][j]+v00[i+1][j]+v00[i][j+1]+v00[i][j-1])/4.0)
            vc.append(b)
            v0.append(vc)
            vc=[]
        ct.append(v0[tt/4][3*tt/4+1])
        v0.append(vt)
        v00=[]
        v00.append(vt)
        if (abs(ct[0]-ct[1])<0.000001):
            tq=2*m
            break
        ct=[]
    return tq
#ax=plt.subplot(111,projection='3d') 
def part2(a,b,tt):
    tq=0
    ct=[]
    r=2.0/(1+math.pi/tt)
    v1=[b]*tt
    v0=[]
    v0.append(v1)
    tc1=[]
    tc2=[]
    tc3=[]
    for t in range(1,tt-1):
        v0.append([])
        if t*1.0/tt==0.25:
           v0[-1].append(b)
           for k in range(1,tt-1):
               if abs(k*1.0/tt-0.5)<0.25:
                  v0[-1].append(a)
               else:
                  v0[-1].append(0)
           v0[-1].append(b)
        elif t*1.0/tt==0.75:
           v0[-1].append(b)
           for k in range(1,tt-1):
               if abs(k*1.0/tt-0.5)<0.25:
                  v0[-1].append(-a)
               else:
                  v0[-1].append(0)
           v0[-1].append(b)
        else:
           v0[-1].append(b)
           for k in range(1,tt-1):
               v0[-1].append(0)
           v0[-1].append(b)
    v0.append(v1)
    for m in range(10000):
        ct.append(v0[tt/4][3*tt/4+1])
        for i in range(1,tt-1):
                for j in range(1,tt-1):
                    if (i*1.0/tt==0.25 and abs(j*1.0/tt-0.5)<0.25)or(i*1.0/tt==0.75 and abs(j*1.0/tt-0.5)<0.25):
                       v0[i][j]=v0[i][j]
                    else:
                       v0[i][j]=r*(v0[i-1][j]+v0[i+1][j]+v0[i][j+1]+v0[i][j-1])/4.0+(1-r)*v0[i][j]  
        ct.append(v0[tt/4][3*tt/4+1])
        if (abs(ct[0]-ct[1]))<0.000001:
           tq=m
           break
        ct=[]
    return tq
"""
t1=96
X=np.arange(-1,1,2.0/t1)
Y=np.arange(-1,1,2.0/t1)
X,Y=np.meshgrid(X, Y)
Z,c=part2(1,0,t1)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()
"""
c=[]
d=[]
f=[]
for i in range(1,4):
    a=part2(1,0,i*24)
    a1=part(1,0,i*24)
    c.append(i*24)
    d.append(a)
    f.append(a1)
ax1=plt.subplot(121)
ax2=plt.subplot(122)
plt.sca(ax1)
plt.plot(c,f,label='Jacobi method')
plt.legend(loc='upper center',frameon=True)
plt.xlabel('step length(L)')
plt.ylabel('iteration time')
for j in range(len(c)):
    t=f[j]
    plt.plot([c[j],c[j]],[0,f[j]], color ='orange', linewidth=2.5, linestyle="--")
    plt.scatter([c[j],],[f[j],], 10, color ='red')
plt.ylim(0,)
plt.sca(ax2)
plt.plot(c,d,label='SOR method')
plt.legend(loc='upper center',frameon=True)
plt.xlabel('step length(L)')
plt.ylabel('iteration time')
for j in range(len(c)):
    t=d[j]
    plt.plot([c[j],c[j]],[0,d[j]], color ='orange', linewidth=2.5, linestyle="--")
    plt.scatter([c[j],],[d[j],], 10, color ='red')
plt.ylim(0,)
plt.show()


           
