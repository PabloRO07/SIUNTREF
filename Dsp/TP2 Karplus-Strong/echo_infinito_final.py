import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 


def echo_infinito(xn, a, d, c):
    """
    :param xn: Entry Signal
    :param a: Echoes Amplitude
    :param d: Delay time in samples
    :param c: Stop condition, Amplitude of delays
    :return: Entry signal with dealy until the echoes amplitude is under "c"
    """
    b = 1
    xn2 = xn
    while b > c:
        delay = a*np.hstack((np.zeros(d), xn))
        xn2 = np.hstack((xn2, np.zeros(d)))
        xn2 = xn2+delay
        xn = delay
        b = abs(max(delay))
    
    return xn2

# System 2 Infinite Echoes
fs = 44100
d = 4  # Delay in samples
s = 0.5  # Time in secods for test signal
d2 = round(s*44100)  # Samples to delay the Signal
alfa = 0.5  # Echoes Amplitude
c = 0.01
audio, fs = sf.read('Midi69.wav')  # Test Audio
synth = echo_infinito(audio, alfa, d2, c)

sf.write('Sistema_2.wav', synth, fs)


# System 2 Analisis
impulse = np.zeros(fs-1)  # Set zero vector for impulse
impulse[0] = 1
synth2 = echo_infinito(impulse, alfa, d, c)  # Impulse Response
transfer2 = sc.fft.fft(synth2)  # Output FFT
imag2 = np.imag(transfer2)
real2 = np.real(transfer2)
frecuency_response2 = abs(transfer2)  # Frequency response
phase2 = np.arctan((imag2/real2))  # Fase response
t1 = np.linspace(0, (len(audio)/fs), len(audio))  # Time vector for graph
t2 = np.linspace(0, (len(synth)/fs), len(synth))  # Time vector for Y2[n]

# PLOT Section Infinite Echoes
plt.style.use('seaborn')
fig, ((ax1, ax2), (ax3, ax4)) =\
plt.subplots(nrows=2, ncols=2, sharex='col', figsize=(16, 10))
fig.suptitle(r'$ Analisis \ del \ sistema \ 2 \ Infinite Echoes \ delay $', fontsize=18)
ax1.plot(frecuency_response2[0:round(fs/2)], color='b', label=r'$D=4$')
ax2.plot(t1, audio, color='black')
ax3.plot(phase2[0:round(fs/2)], color='b', label=r'$D=4$')
ax4.plot(t2, synth, color='black', label=r'$ S= 500 ms $')


ax1.set_title(r'$ |H_2(e^{jw})| $', fontsize=14)
ax1.set_ylabel(r'$Amplitude$', fontsize=14)
ax1.legend(loc='best')


ax2.set_title(r'$Original \ Signal \ x[n] $', fontsize=14)
ax2.set_ylabel(r'$Amplitud$', fontsize=14)
ax2.legend(loc='best')


ax3.set_title(r'$Fase \ \angle \ H_2(e^{jw}) $', fontsize=14)
ax3.set_ylabel(r'$Amplitud$', fontsize=14)
ax3.set_xlabel(r'$Frecuencia [Hz]$', fontsize=14)
ax3.legend(loc='best')


ax4.set_title(r'$Señal \ de \ salida \ y_2[n] \ Normalizada  $', fontsize=14)
ax4.set_ylabel(r'$Amplitud$', fontsize=14)
ax4.set_xlabel(r'$Tiempo [s]$', fontsize=14)
ax4.legend(loc='best')


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
