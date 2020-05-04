import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import singenerator as sg
from punto1 import desvio_str as ds
from punto1 import valor_medio as vm
from punto1 import desvio_medio as dm
from punto1 import RMS as rms

[xt,t]=sg.singenerator(44100, 10e3, 0.5, 1, 2)

ruidito01 = np.random.normal(0,0.1,len(t))
ruidito1 = np.random.normal(0,1,len(t))
ruidito3 = np.random.normal(0,3,len(t))

x01= (ruidito01+xt) / abs(max(ruidito01+xt)) # señal normalizada dividiendo por el max de la señal.
x1= (ruidito1+xt) / abs(max(ruidito1+xt))   # señal normalizada dividiendo por el max de la señal.
x3= (ruidito3+xt) / abs(max(ruidito3+xt))   # señal normalizada dividiendo por el max de la señal.

#calculo de señal ruido 

snr01 = (max(abs(x01)) / ds.desvio_str(x01)[0])
snr1 = (max(abs(x1)) / ds.desvio_str(x1)[0])
snr3 = (max(abs(x3)) / ds.desvio_str(x3)[0])
print(snr01)
print(snr1)
print(snr3)

plt.style.use('seaborn')
fig, ax1 = plt.subplots(nrows=3, ncols=1, sharex=True)
ax1[0].plot(t, x01, color='r')
ax1[0].set_title('X01')
ax1[0].set_ylabel('Amplitude')
ax1[0].set_xlabel('Time[s]')


ax1[1].plot(t, x1, color='r')
ax1[1].set_title('X1')
ax1[1].set_ylabel('Amplitude')
ax1[1].set_xlabel('Time[s]')


ax1[2].plot(t, x3, color='r')
ax1[2].set_title('X3')
ax1[2].set_ylabel('Amplitude')
ax1[2].set_xlabel('Time[s]')
plt.tight_layout()
plt.show()