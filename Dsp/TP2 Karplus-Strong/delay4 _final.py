import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 


# Delay 
def delay4(signal,d,y):
    """Entry Parameters
    This function recive a entry signal and generate 4 delayed signals, amplified "y" times
    signal = Signal Entry
    d = Delay time
    y = amplitude  of delays
    """
    l = len(signal)
    d1 = y*np.hstack((np.zeros(d), signal))
    d2 = (y**2)*np.hstack((np.zeros(2*d), signal))
    d3 = (y**3)*np.hstack((np.zeros(3*d), signal))
    d4 = (y**4)*np.hstack((np.zeros(4*d), signal))
    l2 = len(d4)
    de1 = np.hstack((d1, np.zeros(l2-len(d1))))
    de2 = np.hstack((d2, np.zeros(l2-len(d2))))
    de3 = np.hstack((d3, np.zeros(l2-len(d3))))
    signal = np.hstack((signal, np.zeros((l2-l))))
    synthesis = (signal+de1+de2+de3+d4)
    return synthesis

# System 1 Finite Echoes

fs = 44100
d =  3 # Delay in samples
s = 0.5  # Time in seconds
d2 = round(s*44100)  # Samples to delay input signal 
alfa = 0.5  # Echoes Amplitude

audio, fs = sf.read('Midi69.wav')  # Test Audio
synt = delay4(audio, d2, alfa)

sf.write('Sistema_1.wav', synt, fs)  # Wav File

# System Analysis #
impulse = np.zeros(fs-1)  # Set zero vector for impulse vector
impulse[0] = 1
synt2 = delay4(impulse, d, alfa)  # Impulse Response system
transfer = sc.fft.fft(synt2)  # Output FFT
imag = np.imag(transfer)
real = np.real(transfer)
frecuency_response = abs(transfer)  # Frequency response
phase = np.arctan((imag/real))
t1 = np.linspace(0, (len(audio)/fs), len(audio))  # Time Vcetor for graph
t2 = np.linspace(0, (len(synt)/fs), len(synt))  # Time Vector for Y2[n]


# PLOT Section Finite Echoes
plt.style.use('seaborn')
fig, ((ax1, ax2), (ax3, ax4)) = \
    plt.subplots(nrows=2, ncols=2, sharex='col', figsize=(16, 10))
fig.suptitle(r'$ Analisis \ del \ sistema \ 1 \ ecos \ finito $',
             fontsize=18)
ax1.plot(20*np.log10(frecuency_response[0:round(fs/2)]),
         color='b', label='D = '+str(d))
ax2.plot(t1, audio,
         color='black')
ax3.plot(phase[0:round(fs/2)],
         color='b', label='D = '+str(d))
ax4.plot(t2, synt,
         color='black', label='Delay = '+str(s*1000)+'ms')


ax1.set_title(r'$ |H_1(e^{jw})| $', fontsize=14)
ax1.set_ylabel(r'$Amplitud$ \ [dB]', fontsize=14)
ax1.legend(loc='best')

ax2.set_title(r'$Señal \ Original \ x[n] $', fontsize=14)
ax2.set_ylabel(r'$Amplitud$', fontsize=14)
ax2.legend(loc='best')

ax3.set_title(r'$Fase \ \angle \ H_1(e^{jw})  $', fontsize=14)
ax3.set_ylabel(r'$Amplitud  \  \ [rad] $', fontsize=14)
ax3.set_xlabel(r'$Frecuencia [Hz]$', fontsize=14)
ax3.legend(loc='best')

ax4.set_title(r'$Señal \ de \ salida \ y_1[n]  $', fontsize=14)
ax4.set_ylabel(r'$Amplitud$', fontsize=14)
ax4.set_xlabel(r'$Tiempo [s]$', fontsize=14)
ax4.legend(loc='best')

plt.legend(fontsize=12)
plt.tight_layout()
plt.show()