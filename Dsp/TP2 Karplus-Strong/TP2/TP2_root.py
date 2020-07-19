import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 
import delay4 as dl4
import echo_infinito as ec
import karplus as ks
import extended_ks as ks

# This script binds the fourth systems proposed to analyze


# System 1 Finite Echoes

fs = 44100
d = 4  # Delay in samples
s = 0.5  # Time in seconds
d2 = round(s*44100)  # Samples to delay input signal
alfa = 0.5  # Echoes Amplitude

audio, fs = sf.read('Midi69.wav')  # Test Audio
synt = dl4.delay4(audio, d2, alfa)

sf.write('System_1.wav', synt, fs)  # Wav File

# System Analysis #
impulse = np.zeros(fs-1)  # Set zero vector for impulse vector
impulse[0] = 1
synt2 = dl4.delay4(impulse, d, alfa)  # Impulse Response system
transfer = sc.fft.fft(synt2)  # Output FFT
imag = np.imag(transfer)
real = np.real(transfer)
frequency_response = abs(transfer)  # Frequency response
phase = np.arctan((imag/real))
t1 = np.linspace(0, (len(audio)/fs), len(audio))  # Time Vector for graph
t2 = np.linspace(0, (len(synt)/fs), len(synt))  # Time Vector for Y2[n]

# PLOT Section Finite Echoes
plt.style.use('seaborn')
fig, ((ax1, ax2), (ax3, ax4)) = \
    plt.subplots(nrows=2, ncols=2, sharex='col', figsize=(16, 10))
fig.suptitle(r'$ System\ 1\ Analysis\ 1\ Finite\ Echoes  $',
             fontsize=18)
ax1.plot(frequency_response[0:round(fs/2)],
         color='b', label=r'$D=4$')
ax2.plot(t1, audio,
         color='black')
ax3.plot(phase[0:round(fs/2)],
         color='b', label=r'$D=4$')
ax4.plot(t2, synt,
         color='black', label=r'$ S= 500 ms $')


ax1.set_title(r'$ Signal Spectre $', fontsize=14)
ax1.set_ylabel(r'$Amplitude$', fontsize=14)
ax1.legend(loc='best')

ax2.set_title(r'$Original \ Signal \ x[n] $', fontsize=14)
ax2.set_ylabel(r'$Amplitude$', fontsize=14)
ax2.legend(loc='best')

ax3.set_title(r'$Fase \ \angle \ H_1(e^{jw}) $', fontsize=14)
ax3.set_ylabel(r'$Amplitude$', fontsize=14)
ax3.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax3.legend(loc='best')

ax4.set_title(r'$Ouput \ Signal \ y_1[n]  $', fontsize=14)
ax4.set_ylabel(r'$Amplitude$', fontsize=14)
ax4.set_xlabel(r'$Time [s]$', fontsize=14)
ax4.legend(loc='best')

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

sf.write('System_2.wav', synth, fs)


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
fig.suptitle(r'$ System \ Analysis \ 2\ Infinite Echoes\ delay $', fontsize=18)
ax1.plot(frecuency_response2[0:round(fs/2)],
         color='b', label=r'$D=4$')
ax2.plot(t1, audio,
         color='black')
ax3.plot(phase2[0:round(fs/2)],
         color='b', label=r'$D=4$')
ax4.plot(t2, synth,
         color='black', label=r'$ S= 500 ms $')


ax1.set_title(r'$ Signal Spectre$', fontsize=14)
ax1.set_ylabel(r'$Amplitude$', fontsize=14)
ax1.legend(loc='best')


ax2.set_title(r'$Original \ Signal \ x[n] $', fontsize=14)
ax2.set_ylabel(r'$Amplitud$', fontsize=14)
ax2.legend(loc='best')


ax3.set_title(r'$Fase \ \angle \ H_2(e^{jw}) $', fontsize=14)
ax3.set_ylabel(r'$Amplitude$', fontsize=14)
ax3.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax3.legend(loc='best')


ax4.set_title(r'$Output\ Signal\ y_2[n] \ Normalized  $', fontsize=14)
ax4.set_ylabel(r'$Amplitude$', fontsize=14)
ax4.set_xlabel(r'$Time [s]$', fontsize=14)
ax4.legend(loc='best')


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()


# System 3 Analysis #String Synthesizing
# Karplus with High sampling Frequency

for i in range(4):
    fs = np.array([44100, 96000, 44100, 96000])
    f = np.array([440, 440, 200, 200])
    n = 1
    b = np.array([1, 1, 0.5, 0.5])
    System3_wav = (['string_440_44.1khz.wav', 'string_440_96khz.wav', 'snare_44.1khz.wav', 'snare_96khz.wav'])
    if i == 0:
        ks_0 = ks.karplus(f[i], fs[i], n, b[i])
        transfer = abs(sc.fft.fft(ks_0))
        transfer = transfer/abs(max(transfer))
        w = np.linspace(0, (fs[i]/2), round(len(transfer)/2))
        sf.write(System3_wav[i], ks_0, fs[i])
    elif i == 1:
        ks1 = ks.karplus(f[i], fs[i], n, b[i])
        transfer1 = abs(sc.fft.fft(ks1))
        transfer1 = transfer1/abs(max(transfer1))
        w1 = np.linspace(0, (fs[i]/2), round(len(transfer1)/2))
        sf.write(System3_wav[i], ks1, fs[i])
    elif i == 2:
        ks2 = ks.karplus(f[i], fs[i], n, b[i])
        transfer2 = abs(sc.fft.fft(ks2))
        transfer2 = transfer2/abs(max(transfer2))
        w2 = np.linspace(0, (fs[i]/2), round(len(transfer2)/2))
        sf.write(System3_wav[i], ks2, fs[i])
    elif i == 3:
        ks3 = ks.karplus(f[i], fs[i], n, b[i])
        transfer3 = abs(sc.fft.fft(ks3))
        transfer3 = transfer3/abs(max(transfer3))
        w3 = np.linspace(0, (fs[i]/2), round(len(transfer3)/2))
        sf.write(System3_wav[i], ks3, fs[i])


# w2,transfer2[0:round(len(transfer2)/2)]

# w3,transfer3[0:round(len(transfer3)/2)]

t=np.linspace(0, (len(ks_0)/fs[0]), len(ks_0))
t2=np.linspace(0, (len(ks1)/fs[1]), len(ks1))

# PLOT String Section
plt.style.use('seaborn')  # ploteos del sistema 3 para cuerda
fig, ((ax1, ax2), (ax3, ax4)) =\
    plt.subplots(nrows=2, ncols=2, sharex='col', figsize=(16, 10))
fig.suptitle(r'$Karplus\ Strong\ Synthesizing \ String$', fontsize=18)

ax1.plot(w, transfer[0:round(len(transfer)/2)],
         color='b', label=r'$Fs=44.1k Hz$')
ax2.plot(t, ks_0,
         color='black', label=r'$Fs=44.1k Hz$')
ax3.plot(w1[0:round(len(transfer1)/4)], transfer1[0:round(len(transfer1)/4)],
         color='b', label=r'$Fs=96k Hz$')
ax4.plot(t2, ks1,
         color='black', label=r'$Fs=96k Hz$')

ax1.set_title(r'$Signal Spectre$', fontsize=14)
ax1.set_ylabel(r'$Amplitude$', fontsize=14)
ax1.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax1.legend(loc='best')

ax2.set_title(r'$ String \ 440 \ Hz  $', fontsize=14)
ax2.set_ylabel(r'$Amplitude$', fontsize=14)
ax2.set_xlabel(r'$Time [S]$', fontsize=14)
ax2.legend(loc='best')

ax3.set_title(r'$Signal Spectre$', fontsize=14)
ax3.set_ylabel(r'$Amplitude$', fontsize=14)
ax3.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax3.legend(loc='best')

ax4.set_title(r'$ String \ 440\ Hz $', fontsize=14)
ax4.set_ylabel(r'$Amplitude$', fontsize=14)
ax4.set_xlabel(r'$Time [S]$', fontsize=14)
ax4.legend(loc='best')


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

# PLOT Drum Section
t3 = np.linspace(0, (len(ks2)/fs[2]), len(ks2))
t4 = np.linspace(0, (len(ks3)/fs[3]), len(ks3))

plt.style.use('seaborn')  # System 3 PLOTS
fig, ((ax1, ax2), (ax3, ax4)) =\
    plt.subplots(nrows=2, ncols=2, sharex='col', figsize=(16, 10))
fig.suptitle(r'$Karplus\ Strong\ Synthesizing \ Drum$', fontsize=18)

ax1.plot(w2, transfer2[0:round(len(transfer2)/2)],
         color='b', label=r'$Fs=44.1k Hz$')
ax2.plot(t3, ks2,
         color='black', label=r'$Fs=44.1k Hz$')
ax3.plot(w3[0:round(len(transfer3)/4)], transfer3[0:round(len(transfer3)/4)],
         color='b', label=r'$Fs=96k Hz$')
ax4.plot(t4, ks3,
         color='black', label=r'$Fs=96k Hz$')

ax1.set_title(r'$ Signal Spectre| $', fontsize=14)
ax1.set_ylabel(r'$Amplitude$', fontsize=14)
ax1.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax1.legend(loc='best')

ax2.set_title(r'$ Drum \ 200 \ Hz  $', fontsize=14)
ax2.set_ylabel(r'$Amplitude$', fontsize=14)
ax2.set_xlabel(r'$Time [S]$', fontsize=14)
ax2.legend(loc='best')

ax3.set_title(r'$Signal Spectre$', fontsize=14)
ax3.set_ylabel(r'$Amplitude$', fontsize=14)
ax3.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax3.legend(loc='best')

ax4.set_title(r'$ Drum \ 200\ Hz $', fontsize=14)
ax4.set_ylabel(r'$Amplitude$', fontsize=14)
ax4.set_xlabel(r'$Time [S]$', fontsize=14)
ax4.legend(loc='best')


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

# KS Extended
ks.extended_ks()





