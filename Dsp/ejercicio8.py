import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
import scipy as sc

xn, fs = sf.read('Midi69.wav')
hn, fs = sf.read('RIR.wav')
m = len(xn)
l = len(hn)
n = m + l - 1
nxn = abs(m - n)
nhn = abs(l - n)

# para la consigna que pide extender la señal midi69 a la longitud de la IR
hn1 = np.concatenate([hn, np.zeros(abs(m - l))])
xn2 = np.concatenate([xn, np.zeros(nxn)])  # para la consigna de conv circular = lineal
hn2 = np.concatenate([hn, np.zeros(nhn)])  # para la consigna de conv circular = lineal
conv_lineal = np.convolve(xn, hn, mode='full')

yn1 = sc.fft.ifft((sc.fft.fft(xn) * sc.fft.fft(hn1)))
yn2 = sc.fft.ifft((sc.fft.fft(xn2) * sc.fft.fft(hn2)))
yn2 = np.real(yn2)  # tomo la parte real porque la parte imaginaria queda como 0.00000i y me trae problemas con el plot.
yn1 = np.real(yn1)  # tomo la parte real porque la parte imaginaria queda como 0.00000i y me trae problemas con el plot.
t_lineal = np.linspace(0, len(conv_lineal) / fs, len(conv_lineal))
t_convc1 = np.linspace(0, (len(xn) / fs), len(xn))
t_convc2 = np.linspace(0, (len(xn2) / fs), len(xn2))

# Creacion wav
sf.write('E8_Convolucion.wav', conv_lineal, fs)
sf.write('E8_conv_circular_zeroP.wav', yn1, fs)
sf.write('E8_conv_circular=lineal_zeroP.wav', yn2, fs)

# PLOT
plt.style.use('seaborn')

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)
ax1.plot(t_lineal, conv_lineal, color='black')
ax2.plot(t_convc1, yn1, color='b')
ax3.plot(t_convc2, yn2,color='orange')

ax1.set_title(r'$Convolucion \ h[n] \ast x[n]$',fontsize=16)
ax1.set_ylabel(r'$Amplitud$')


ax2.set_title(r'$Convolucion \ h_p[n] \otimes  x[n]$',fontsize=16)
ax2.set_ylabel(r'$Amplitud$',fontsize=14)

ax3.set_title(r'$Convolucion \ h_p[n] \otimes  x_p[n]$',fontsize=16)
ax3.set_ylabel(r'$Amplitud$',fontsize=14)
ax3.set_xlabel(r'$Time[s]$',fontsize=14)

plt.tight_layout()
plt.show()
