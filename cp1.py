import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2,500,endpoint=True)
z=np.exp(x)*100
y=N_U=[]
t=[]
dt=0.001
a=1
b=0.003
N_U.append(100.)
t.append(0)
time=2
for i in range(int(time/dt)):
      tmp=N_U[i]+dt*a*N_U[i]
      N_U.append(tmp)
      t.append(dt*i)
print N_U[-1],t[-1]
plt.plot(t,y,color='red',linewidth=2.0,linestyle='-',label='simulation')
plt.plot(x,z,color='blue',linewidth=2.0,linestyle=':',label='theoretical')
plt.legend(loc='upper left',frameon=True)
j=1
plt.plot([j,j],[0,100*np.exp(j)],color='red',linewidth=1.5,linestyle='--')
plt.plot([0,j],[100*np.exp(j),100*np.exp(j)],color='blue',linewidth=1.5,linestyle='--')
plt.scatter([j,],[100*np.exp(j),],50,color='red')
plt.annotate(r'$z=e^x$',
             xy=(j,100*np.exp(j)),xycoords='data',
             xytext=(+10,+30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))


plt.ylim(100,800)
plt.xlim(0,2)
ax=plt.gca()
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.65))
plt.show()
     
