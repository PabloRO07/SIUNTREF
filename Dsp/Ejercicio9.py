import numpy as np 
import scipy as sc 
from matplotlib import pyplot as plt 
from punto6 import fmmconv as fmmconv

# Creo vector impulso
fs = 44100
m = 1
impulse = np.zeros(fs-m+1)
impulse[0] = 1

# Filtrado del impulso
ir = fmmconv.fmmconv(impulse, m)
# Funcion de transferencia
ir_frec = sc.fft.fft(ir)
frec_response = abs(ir_frec)
print(len(frec_response))
print("con una ventana de", m, " muestras, para el valor de 10khz", "que en proporcion de pi es", ((10e3*np.pi)/(fs/2)),
      ",la magnitud del filtro es de ", frec_response[10000], "o", 20*np.log10(frec_response[10000]), "dB")

w = np.linspace(0, np.pi, round(fs/2))

# PLOT
plt.style.use('seaborn')

fig, ax1 = plt.subplots(nrows=1, ncols=1, sharex=True)
plt.plot(w, frec_response[0:round(fs/2)], color='r')

ax1.set_title('|H(jw)| Ventana Rectangular ')
ax1.set_ylabel('Amplitud')
ax1.set_xlabel('rad/[Hz]')


plt.tight_layout()
plt.show()
