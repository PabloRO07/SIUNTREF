import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 


# Delay 
def delay4(signal, d, y):
    """Entry Parameters
    This function receive a entry signal and generate 4 delayed signals, amplified "y" times
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
d = 1  # Delay in samples
s = 1/44100  # Time in seconds
d2 = round(s*44100)  # Samples to delay input signal 
alfa = 1 # Echoes Amplitude

audio, fs = sf.read('Midi69.wav')  # Test Audio
synt = delay4(audio, d2, alfa)

sf.write('Sistema_1.wav', synt, fs)  # Wav File

# System Analysis #
impulse = np.zeros(fs)  # Set zero vector for impulse vector
impulse[0] = 1
synt2 = delay4(impulse, d, alfa)  # Impulse Response system

transfer = sc.fft.fft(synt2)  # Output FFT
print(len(transfer))
imag = np.imag(transfer)
real = np.real(transfer)
frecuency_response = abs(transfer)  # Frequency response
phase = np.arctan((imag/real))
t1 = np.linspace(0, (len(audio)/fs), len(audio))  # Time Vcetor for graph
t2 = np.linspace(0, (len(synt)/fs), len(synt))  # Time Vector for Y2[n]
w=np.linspace(0,len(transfer/2),len(transfer))


# PLOT Section Finite Echoes
plt.style.use('seaborn')
fig, ((ax1, ax2), (ax3, ax4)) = \
    plt.subplots(nrows=2, ncols=2,  figsize=(16, 10))
#fig.suptitle(r'$ System \ Analysis \ Finite \ Echoes$',
#             fontsize=18)
ax1.plot(w[0:round(len(transfer)/2)],20*np.log10(frecuency_response[0:round(len(transfer)/2)]) , color='b', label=r'$D = $'+str(d))
ax2.plot(t1, audio,
         color='black')
ax3.plot(w[0:round(len(phase)/2)],phase[0:round(len(phase)/2)],
         color='b', label=r'$D = $'+str(d))
ax4.plot(t2, synt,
         color='black', label=r'$Delay = $'+str(s*1000)+r'$ms$')


ax1.set_title(r'$ |H_1(e^{jw})| $', fontsize=14)
ax1.set_ylabel(r'$Amplitude \ [dB]$', fontsize=14)
ax1.set_xlabel(r'$Frequency \ [Hz]$', fontsize=14)
ax1.legend(loc='best')

ax2.set_title(r'$Primitive \ Signal \ x[n] $', fontsize=14)
ax2.set_ylabel(r'$Amplitude$', fontsize=14)

ax3.set_title(r'$Phase \ \angle \ H_1(e^{jw})  $', fontsize=14)
ax3.set_ylabel(r'$Amplitude \ [rad] $', fontsize=14)
ax3.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax3.legend(loc='best')

ax4.set_title(r'$Output \ Signal \ y_1[n]  $', fontsize=14)
ax4.set_ylabel(r'$Amplitude$', fontsize=14)
ax4.set_xlabel(r'$Time [s]$', fontsize=14)
ax4.legend(loc='best')

plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('sistema1_1d_1alfa.png')
plt.show()
