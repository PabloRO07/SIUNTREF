import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import singenerator as sg
from punto1 import desvio_str as ds
from punto1 import valor_medio as vm
from punto1 import desvio_medio as dm
from punto1 import RMS as rms

[señal,t]=sg.singenerator(44100, 10e3, 0.5, 1, 2)

v_m=vm.valor_medio(señal)
dm=dm.desvio_medio(señal)
ds=ds.desvio_str(señal)
rms=rms.RMS(señal)
print("el valor medio de la señal es:",v_m)
print("el desvio medio de la señal es:",dm)
print("el desvio standard de la señal es:",ds[0])
print("el valor rms de la señal es:",rms)

# PLOT

plt.style.use('seaborn')
fig, ax1 = plt.subplots(nrows=1, ncols=1, sharex=True)
ax1.plot(t, señal, color='r')
ax1.set_title('Señal')
ax1.set_ylabel('Amplitude')
ax1.set_xlabel('Time[s]')
plt.tight_layout()
plt.show()