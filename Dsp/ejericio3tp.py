import numpy as np 
from matplotlib import pyplot as plt 
import desvio_medio as dm
import desvio_str as ds
import RMS as rms
import valor_medio as vm
import energy as en

fs = 44100
f = 10000
t = 0.5
t = np.linspace(0,t,int(fs*t))    #Vector tiempo
xt = 2+np.sin(2*np.pi*f*t)        # Señal x(t)

ruidito01 = np.random.normal(0,0.1,len(t))
ruidito1 = np.random.normal(0,1,len(t))
ruidito3 = np.random.normal(0,3,len(t))

#x01 = ruidito01+xt /np.sqrt(en.energy(ruidito01+xt)/len(ruidito01+xt)) #suma de señal + ruido + normalizado.
#x1 = ruidito1+xt / np.sqrt(en.energy(ruidito1+xt)/len(ruidito1+xt))
#x3 = ruidito3+xt / np.sqrt(en.energy(ruidito3+xt)/len(ruidito3+xt))
x01= ruidito01+xt / max(ruidito01+xt) # señal normalizada dividiendo por el max de la señal.
x1= ruidito1+xt / max(ruidito1+xt)
x3= ruidito3+xt / max(ruidito3+xt)

#calculo de señal ruido 

snr01 = (max(abs(x01)) / ds.desvio_str(x01)[0])
snr1 = (max(abs(x1)) / ds.desvio_str(x1)[0])
snr3 = (max(abs(x3)) / ds.desvio_str(x3)[0])
print(snr01)
print(snr1)
print(snr3)

fig, axs = plt.subplots(3)
fig.suptitle('señal + desviasión')
axs[0].plot(t, x01)
axs[1].plot(t, x1)
axs[2].plot(t,x3)

plt.show()