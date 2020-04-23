import numpy as np 
from matplotlib import pyplot as plt 
import RFMM as rfmm
import FMM as fmm
def FMM_conv(x,m):
    kernel= np.ones(m)/(m+1)
    salida=np.convolve(x,kernel)
    return(salida)

t=0.5
fs=44100
t=np.linspace(0,t,int(fs*t))
f=10000
xt= 2 + np.sin(2*np.pi*f*t)
ruidito3 = np.random.normal(0,3,len(t)) #Creo la señal del punto 3 para compararla
x3= (ruidito3+xt) 
m=round(0.01*len(x3))
señal_filtrada=FMM_conv(x3,m)
señal_filtrada2=rfmm.RFMM(x3,m)
señal_filtrada3=fmm.FMM(x3,m)


t2=np.linspace(0,0.5,len(señal_filtrada))


fig, axs = plt.subplots(4)
fig.suptitle('Filtro de media movil')
axs[0].plot(t,x3)
axs[1].plot(t2,señal_filtrada)
axs[2].plot(t,señal_filtrada2)
axs[3].plot(t,señal_filtrada3)
plt.show()