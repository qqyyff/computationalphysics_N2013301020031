from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
def part(a,b,tt,mm):
    v0=[]
    v00=[]
    v1=[]
    vt=[b]*tt
    v0.append(vt)
    vr=[]
    vr.append(b)
    vc=[]
    for k in range(1,tt-1):
        if abs(k*1.0/tt-0.5)<0.125:
           vr.append(a)
        else:
           vr.append(0)
    vr.append(b)
    v1.append(b)
    for i in range(1,tt-1):
        v1.append(0)
    v1.append(b)
    for i in range(tt-2):
        if abs(i*1.0/tt-0.5)<0.125:
           v0.append(vr)
        else: 
           v0.append(v1)
    v0.append(vt)
    v00.append(vt)
    for m in range(mm):
        for i in range(1,tt-1):
            vc.append(b)
            for j in range(1,tt-1):
                  if ((i-tt/2.0)**2+(j-tt/2.0)**2)<=(tt/4.0)**2:
                     vc.append(a)     
                  else:
                     vc.append((v0[i-1][j]+v0[i+1][j]+v0[i][j+1]+v0[i][j-1])/4.0)         
                        
            vc.append(b)
            v00.append(vc)
            vc=[]
        v00.append(vt)
        v0=[]
        v0.append(vt)
        for i in range(1,tt-1):
            vc.append(b)
            for j in range(1,tt-1):
                  if ((i-tt/2.0)**2+(j-tt/2.0)**2)<=(tt/4.0)**2:
                     vc.append(a)
                  else:
                     vc.append((v00[i-1][j]+v00[i+1][j]+v00[i][j+1]+v00[i][j-1])/4.0)
            vc.append(b)
            v0.append(vc)
            vc=[]
        v0.append(vt)
        v00=[]
        v00.append(vt)            
    return v0
#ax=plt.subplot(111,projection='3d') 
t1=64

X=np.arange(-1,1,2.0/t1)
Y=np.arange(-1,1,2.0/t1)
X,Y=np.meshgrid(X, Y)
Z=part(1,0,t1,1)
fig = plt.figure()
ax = fig.add_subplot(221, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.title('the two square field with iteration(2)')
plt.xlabel('X/m')
plt.ylabel('Y/m')
#ax.plot_trisurf(X, Y, Z)
Z=part(1,0,t1,10)
ax = fig.add_subplot(222, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.title('the two square field with iteration(20)')
plt.xlabel('X/m')
plt.ylabel('Y/m')
Z=part(1,0,t1,100)
ax = fig.add_subplot(223, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.title('the two square field with iteration(200)')
plt.xlabel('X/m')
plt.ylabel('Y/m')
Z=part(1,0,t1,1000)
Z=np.array(Z)
ax = fig.add_subplot(224, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.title('the two square field with iteration(2000)')
plt.xlabel('X/m')
plt.ylabel('Y/m')
plt.show()



           
