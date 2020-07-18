import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 
import delay4 as dl4
import echo_infinito as ec
import ks as ks

#This script binds the fourth systems proposed to analyze


# System 1 Finite Echoes

fs = 44100
d = 4  # Delay in samples
s = 0.5  # Time in seconds
d2 = round(s*44100)  # Samples to delay input signal
alfa = 0.5  # Echoes Amplitude

audio, fs = sf.read('Midi69.wav')  # Test Audio
synt = dl4.delay4(audio, d2, alfa)

sf.write('Sistema_1.wav', synt, fs)  # Wav File

# System Analysis #
impulse = np.zeros(fs-1)  # Set zero vector for impulse vector
impulse[0] = 1
synt2 = dl4.delay4(impulse, d, alfa)  # Impulse Response system
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
ax1.plot(frecuency_response[0:round(fs/2)],
         color='b', label=r'$D=4$')
ax2.plot(t1, audio,
         color='black')
ax3.plot(phase[0:round(fs/2)],
         color='b', label=r'$D=4$')
ax4.plot(t2, synt,
         color='black', label=r'$ S= 500 ms $')


ax1.set_title(r'$ |H_1(e^{jw})| $', fontsize=14)
ax1.set_ylabel(r'$Amplitud$', fontsize=14)


ax2.set_title(r'$Señal \ Original \ x[n] $', fontsize=14)
ax2.set_ylabel(r'$Amplitud$', fontsize=14)


ax3.set_title(r'$Fase \ \angle \ H_1(e^{jw}) $', fontsize=14)
ax3.set_ylabel(r'$Amplitud$', fontsize=14)
ax3.set_xlabel(r'$Frecuencia [Hz]$', fontsize=14)


ax4.set_title(r'$Señal \ de \ salida \ y_1[n]  $', fontsize=14)
ax4.set_ylabel(r'$Amplitud$', fontsize=14)
ax4.set_xlabel(r'$Tiempo [s]$', fontsize=14)


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()


# System 2 Infinite Echoes
fs = 44100
d = 4  # Delay in samples
s = 0.5  # Time in secods for test signal
d2 = round(s*44100)  # Samples to delay the Signal
alfa = 0.5  # Echoes Amplitude
c = 0.01
synth = ec.echo_infinito(audio, alfa, d2, c)

sf.write('Sistema_2.wav', synth, fs)


# System 2 Analisis
impulse = np.zeros(fs-1)  # Set zero vector for impulse
impulse[0] = 1
synth2 = ec.echo_infinito(impulse, alfa, d, c)  # Impulse Response
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


ax2.set_title(r'$Original \ Signal \ x[n] $', fontsize=14)
ax2.set_ylabel(r'$Amplitud$', fontsize=14)


ax3.set_title(r'$Fase \ \angle \ H_2(e^{jw}) $', fontsize=14)
ax3.set_ylabel(r'$Amplitud$', fontsize=14)
ax3.set_xlabel(r'$Frecuencia [Hz]$', fontsize=14)


ax4.set_title(r'$Señal \ de \ salida \ y_2[n] \ Normalizada  $', fontsize=14)
ax4.set_ylabel(r'$Amplitud$', fontsize=14)
ax4.set_xlabel(r'$Tiempo [s]$', fontsize=14)


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()


# System 3 Analysis #String Synthesizing
# Karplus with High sampling Frequency
fs = 196000
f = 880
ks = ks.ks(f, fs, 3, 1)
transfer = sc.fft.fft(ks)
transfer = abs(transfer)
transfer = transfer/abs(max(transfer))
w = np.linspace(0, (fs/2), round(len(transfer)/2))

# Karplus with Low Sampling Frequency
fs = 44100
f = 880
ks1 = ks.ks(f, fs, 3, 1)
transfer1 = sc.fft.fft(ks1)
transfer1 = abs(transfer1)
transfer1 = transfer1/abs(max(transfer1))
w1 = np.linspace(0, (fs/2), round(len(transfer1)/2))


plt.plot(w, transfer[0:round((fs*3)/2)])
plt.show()
sf.write('Sistema_5.wav', ks, fs)

# PLOT String Section
plt.style.use('seaborn')  # ploteos del sistema 3
fig, (ax1, ax2) =\
    plt.subplots(nrows=1, ncols=2, sharex='col', figsize=(16, 10))
fig.suptitle(r'$Karplus\ Strong\ String\ Synthesizing$', fontsize=18)

ax1.plot(w, transfer[0:round((fs*3)/2)], color='b', label=r'$Fs=96000$')
ax2.plot(w1, transfer1[0:round((fs*3)/2)], color='black', label=r'$Fs=44100$')


ax1.set_title(r'$ |H_2(e^{jw})| $', fontsize=14)
ax1.set_ylabel(r'$Amplitud$', fontsize=14)


ax2.set_title(r'$|H_2(e^{jw})|$', fontsize=14)
ax2.set_ylabel(r'$Amplitud$', fontsize=14)


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()


# System 4 Analysis #Drum Synthesizing
# Karplus with High sampling Frequency
fs = 8000
f = 50
ks2 = ks.ks(f, fs, 3, np.random.randint(1, 9))
transfer2 = sc.fft.fft(ks)
transfer2 = abs(transfer2)
transfer2 = transfer2/abs(max(transfer2))
w2 = np.linspace(0, (fs/2), round(len(transfer2)/2))

# Karplus with Low Sampling Frequency
fs = 2000
f = 50
ks1 = ks.ks(f, fs, 3, np.random.randint(1, 9))
transfer3 = sc.fft.fft(ks1)
transfer3 = abs(transfer3)
transfer3 = transfer3/abs(max(transfer3))
w3 = np.linspace(0, (fs/2), round(len(transfer3)/2))

# PLOT Drum Section
plt.style.use('seaborn')  # ploteos del sistema 3
fig, (ax1, ax2) =\
    plt.subplots(nrows=1, ncols=2, sharex='col', figsize=(16, 10))
fig.suptitle(r'$ Karplus\ Strong\ Drum\ Synthesizing $', fontsize=18)

ax1.plot(w2, transfer2[0:round((fs*3)/2)], color='b', label=r'$Fs=8000$')
ax2.plot(w3, transfer3[0:round((fs*3)/2)], color='black', label=r'$Fs=2000$')


ax1.set_title(r'$ |H_2(e^{jw})| $', fontsize=14)
ax1.set_ylabel(r'$Amplitud$', fontsize=14)


ax2.set_title(r'$ |H_2(e^{jw})| $', fontsize=14)
ax2.set_ylabel(r'$Amplitud$', fontsize=14)


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
