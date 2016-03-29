import numpy as np
import matplotlib.pyplot as plt
y=[]
z=[]
t=[]
dt=0.01
tau=1
z.append(1000.)
y.append(500.)
t.append(0.)
time=10
for i in range(int(time/dt)):
      tmp=y[i]+dt*(-y[i]/tau+z[i]/tau)
      gmp=z[i]+dt*(y[i]/tau-z[i]/tau)
      y.append(tmp)
      z.append(gmp)
      t.append(dt*i)
print y[-1],z[-1],t[-1]
plt.plot(t,y,color='red',linewidth=2.0,linestyle='-',label='the element A')
plt.plot(t,z,color='blue',linewidth=2.0,linestyle='-',label='the element B')
plt.legend(loc='upper right',frameon=True)
plt.title('the radioactive decay line')
plt.xlabel('time/s')
plt.ylabel('mass/kg')
plt.plot([0,10],[750,750],color='orange',linewidth=1.0,linestyle='--')
plt.annotate(r'$(750.0)$',
             xy=(8,750.0),xycoords='data',
             xytext=(+10,+30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
plt.show()

