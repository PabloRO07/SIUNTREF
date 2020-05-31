import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import singenerator as sg
from punto1 import desvio_str as ds
from punto1 import valor_medio as vm
from punto1 import desvio_medio as dm
from punto1 import RMS as rms

[xt, t] = sg.singenerator(44100, 10e3, 0.5, 1, 2)
rng = np.random.default_rng()  # generador de ruido

ruidito1 = rng.normal(0, 0.1, len(t))
ruidito2 = rng.normal(0, 1, len(t))
ruidito3 = rng.normal(0, 3, len(t))

x1 = (ruidito1+xt)
x2 = (ruidito2+xt)
x3 = (ruidito3+xt)
# Calculo de señal ruido

snr1 = (max(abs(xt)) / ds.desvio_str(ruidito1)[0])
snr2 = (max(abs(xt)) / ds.desvio_str(ruidito2)[0])
snr3 = (max(abs(xt)) / ds.desvio_str(ruidito3)[0])

print("la relación SNR de x01 es:",snr1)
print("la relación SNR de x1 es:",snr2)
print("la relación SNR de x3 es:",snr3)

# Señal normalizada dividiendo por el max de la señal.
x1 = (ruidito1+xt) / abs(max(ruidito1+xt))
# Señal normalizada dividiendo por el max de la señal.
x2 = (ruidito2+xt) / abs(max(ruidito2+xt))
# Señal normalizada dividiendo por el max de la señal.
x3 = (ruidito3+xt) / abs(max(ruidito3+xt))


# PLOT
plt.style.use('seaborn')
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)

ax1.plot(t, x1, color='r')
ax2.plot(t, x2, color='y')
ax3.plot(t, x3)

ax1.set_title('X0.1')
ax1.set_ylabel('Amplitude')

ax2.set_title('X1')
ax2.set_ylabel('Amplitude')

ax3.set_title('X3')
ax3.set_ylabel('Amplitude')
ax3.set_xlabel('Time[s]')

plt.tight_layout()
plt.show()
