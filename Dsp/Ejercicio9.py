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

print("con una ventana de", m, " muestras, para el valor de 10khz", "que en proporcion de pi es", ((10e3*np.pi)/(fs/2)),
      ",la magnitud del filtro es de ", frec_response[10000], "o", 20*np.log10(frec_response[10000]), "dB")

w = np.linspace(0, np.pi, round(fs/2))

# PLOT
plt.style.use('seaborn')

fig, ax1 = plt.subplots(nrows=1, ncols=1, sharex=True)
plt.plot(w, frec_response[0:round(fs/2)], color='b', label=(r'$|H(jw)| \$', fs, r'$M=1$'))

ax1.set_title(r'$|H(jw)| \ Ventana \ Rectangular $', fontsize=16)
ax1.set_ylabel(r'$Amplitud$', fontsize=14)
ax1.set_xlabel(r'$ \frac{rad}{Hz}$', fontsize=16)

x_coord = [0, 10000*np.pi/22050]
y_coord = [frec_response[10000], frec_response[10000]]
x_coord1 = [10000*np.pi/22050, 10000*np.pi/22050]
y_coord1 = [0, frec_response[10000]]

plt.plot(x_coord, y_coord, color='black', linestyle='dashed')
plt.plot(x_coord1, y_coord1, color='black', linestyle='dashed')
plt.plot(10000*np.pi/22050, frec_response[10000], color='black',marker='o',label=(r'$[1.42;0.75]$'))
plt.legend(fontsize=14)
plt.tight_layout()

plt.show()
