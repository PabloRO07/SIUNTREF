import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
import scipy as sc




xn, fs = sf.read('Midi69.wav')
hn, fs = sf.read('RIR.wav')
m=len(xn)
l=len(hn)

hn1=np.concatenate([hn,np.zeros(abs(m-l))]) # para la consigna que pide extender la señal midi69 a la longitud de la IR
xn2=np.concatenate([xn,np.zeros(m+l-1)]) # para la consigna de conv circular = lineal
hn2=np.concatenate([hn1,np.zeros(m+l-1)]) # para la consigna de conv circular = lineal
conv_lineal = np.convolve(xn, hn,mode ='full')


yn1=sc.fft.ifft((sc.fft.fft(xn)*sc.fft.fft(hn1)))
yn2=sc.fft.ifft((sc.fft.fft(xn2)*sc.fft.fft(hn2)))
yn2=np.real(yn2)
yn1=np.real(yn1)
t_lineal = np.linspace(0, len(conv_lineal)/fs, len(conv_lineal))
t_convc1=np.linspace(0,(len(xn)/fs),len(xn))
t_convc2=np.linspace(0,(len(xn2)/fs),len(xn2))

########### crea archivo Wav ################
sf.write('Convolucion.wav',conv_lineal ,fs)
sf.write('conv_circular1.wav',yn1 ,fs)
sf.write('conv_circular2.wav',yn2 ,fs)


# PLOT

# Plot
plt.style.use('seaborn')

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)
ax1.plot(t_lineal ,conv_lineal, color='r')
ax2.plot(t_convc1, yn1, color='y')
ax3.plot(t_convc2,yn2 )

ax1.set_title('convolución x[n]*h[n]')
ax1.set_ylabel('Amplitud')
ax1.set_xlabel('Time[s]')

ax2.set_title('Zero pading a xn')
ax2.set_ylabel('Amplitud')

ax3.set_title('Zero pading a xn y hn')
ax3.set_xlabel('Time[s]')
ax3.set_ylabel('Amplitud')

plt.tight_layout()
plt.show()
