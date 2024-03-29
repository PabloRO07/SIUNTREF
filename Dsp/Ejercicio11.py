import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
import scipy as sc

xn, fs = sf.read('Midi69.wav')
hn, fs = sf.read('RIR.wav')
m = len(xn)
l = len(hn)
n = m+l-1
nxn = abs(m-n)
nhn = abs(l-n)

conv_lineal = np.convolve(xn, hn, mode='full')
xn = np.concatenate([xn, np.zeros(nxn)]) # para la consigna de conv circular = lineal
hn = np.concatenate([hn, np.zeros(nhn)]) # para la consigna de conv circular = lineal

yn = sc.fft.ifft((sc.fft.fft(xn)*sc.fft.fft(hn))) #DFT
yn = np.real(yn) # tomo la parte real porque la parte imaginaria queda como 0.00000i y me trae problemas con el plot.

t_convc = np.linspace(0, (len(xn)/fs), len(xn))
t_lineal = np.linspace(0, len(conv_lineal)/fs, len(conv_lineal))

plt.style.use('seaborn')

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
ax1.plot(t_lineal, conv_lineal, color='black')
ax2.plot(t_convc, yn, color='b')


ax1.set_title(r'$Convolución \ h[n] \ast x[n]$',fontsize=14)
ax1.set_ylabel(r'$Amplitud$', fontsize=14)

ax2.set_title(r'$Convolución \ por \ DFT \ h_p[n] \otimes x_p[n]$', fontsize=14)
ax2.set_ylabel(r'$Amplitud$', fontsize=14)
ax2.set_xlabel(r'$Time[s]$', fontsize=14)

plt.tight_layout()
plt.show()
