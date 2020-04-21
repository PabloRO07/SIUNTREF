import numpy as np 
from matplotlib import pyplot as plt 

def FMM(x,M):
    L=len(x)
    y=np.zeros(L)
    N=L-M
    for i in range(N):
        y[i]= np.sum(x[i:M+i])/M
    return(y)


fs=192000
f = 10000
t = 0.5
T = np.linspace(0,t,int(fs*t))    #Vector tiempo
xt = 2+np.sin(2*np.pi*f*T)        # Señal x(t)
ruidito3 = np.random.normal(0,3,len(T)) #Creo la señal del punto 3 para compararla
x3= ruidito3+xt / max(ruidito3+xt)
salida=FMM(x3,50)

fig, axs = plt.subplots(2)
fig.suptitle('Filtro de media movil')
axs[0].plot(T,x3)
axs[1].plot(T,salida)
plt.show()