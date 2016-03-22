import numpy as np
import matplotlib.pyplot as plt
y=N_U=[]
z=[]
t=[]
dt=0.001
a=10
b=3
c=50
d=0.3
z.append(100.)
N_U.append(100.)
t.append(0)
time=2
for i in range(int(time/dt)):
      tmp=N_U[i]+dt*(a*N_U[i]-b*N_U[i]*N_U[i])
      gmp=z[i]+dt*(c*z[i]-d*z[i]*z[i])
      N_U.append(tmp)
      z.append(gmp)
      t.append(dt*i)
print N_U[-1],z[-1],t[-1]
plt.plot(t,y,color='red',linewidth=2.0,linestyle='-',label='decrease')
plt.plot(t,z,color='blue',linewidth=2.0,linestyle='-',label='increase')
plt.legend(loc='center right',frameon=True)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',100))
j=0.06426
k=166.71
plt.plot([j,j],[100,162.5],color='red',linewidth=1.5,linestyle='--')
plt.scatter([j,],[162.5,],20,color='red')
plt.annotate(r'$(0.064,162.5)$',
             xy=(j,162.5),xycoords='data',
             xytext=(+10,-30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
f=0.03449
g=10.7143
plt.plot([f,f],[g,100],color='blue',linewidth=1.5,linestyle='--')
plt.scatter([f,],[g,],20,color='blue')
plt.annotate(r'$(0.034,10.71)$',
             xy=(f,g),xycoords='data',
             xytext=(+10,+30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))


h=166.71
q=2.67857
plt.plot([1.5,1.5],[q,h],color='orange',linewidth=1.0,linestyle='--')
plt.scatter([j,],[162.5,],30,color='red')
plt.annotate(r'$z=166.71$',
             xy=(1.5,h),xycoords='data',
             xytext=(-90,-50),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))

plt.annotate(r'$z=2.68$',
             xy=(1.5,q),xycoords='data',
             xytext=(+10,+30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))

plt.xlim(0,2)
plt.ylim(0,170)
plt.show()

