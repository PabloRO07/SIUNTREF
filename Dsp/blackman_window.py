import numpy as np 
from matplotlib import pyplot as plt 
import RFMM as rfmm

def bkack_w(xt,m):
    a0 = 0.42
    a1 = 0.5
    a2 = 0.08
    kernel=np.zeros(m)

    i=np.arange(m)
    print(len(i))
    kernel = a0 - a1*np.cos((2*np.pi*i)/(m-1))+a2*np.cos((4*np.pi*i)/(m-1))
   
    y=np.convolve(xt,kernel)
    return(y)

t=0.5
fs=44100
t=np.linspace(0,t,int(fs*t))
f=10000
xt= 2 + np.sin(2*np.pi*f*t)
ruidito3 = np.random.normal(0,3,len(t)) #Creo la señal del punto 3 para compararla
x3= (ruidito3+xt)
salida=bkack_w(x3,100)
salida2=rfmm.RFMM(x3,100)
print(len(salida))
t2=np.linspace(0,(len(salida)/fs),len(salida))
fig, axs =plt.subplots(2)
axs[0].plot(t2,salida)
axs[1].plot(salida2)
plt.show()