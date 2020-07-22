import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 


def karplus(f, fs, n, b):
    """
    :param f: Frequency to synthesize
    :param fs: Sampling frequency
    :param n: Long time in second of the output signal
    :param b: Probabilistic parameter b>9 for string synthesizing  and 0>=b<9 for drum synthesizing
    :return: Signal of "f" frequency, drum or string, of time "n"
    """
    n = n*fs
    b = int(b*10)
    p = fs // f
# Wave Table Desing #
    wavetable = (2 * np.random.randint(0, 2, p) - 1).astype(np.float)  # Noise Generator (1;-1)

    v_anterior = 0
    karplus = np.zeros(n)

    a = 0

    for i in range(n):
        h = np.random.randint(0, 9)
        if h <= b:
            wavetable[a] = 0.5 * (wavetable[a]+v_anterior)
        else:
            wavetable[a] = -0.5 * (wavetable[a]+v_anterior)

        karplus[i] = wavetable[a]
        v_anterior = karplus[i]
        a += 1
        a = a % len(wavetable)
    return karplus

# System 3 Analysis #String Synthesizing
# Karplus with High sampling Frequency


for i in range(4):
    fs = np.array([44100,22050,44100,44100]) # Sample frequency 
    f = np.array([120, 120,120, 120]) # pitch frequency 
    n = 1 # Time of audio syntethize 
    b = np.array([1, 1, 0.5, 0.5]) # Blend Factor, if b=1 String sound , other wise Drum
    sistema3_wav = (['string'+str(f[0])+'Hz_'+str(fs[0]/1000)+'khz.wav', 'string_'+str(f[1])
                     + 'Hz_'+str(fs[1]/1000) + 'khz.wav', 'snare_'+str(f[2])+'Hz_'+str(fs[2]/1000)+
                     'khz.wav', 'snare_'+str(f[3])+'Hz_'+str(fs[3]/1000)+'khz.wav'])
    if i == 0:
        ks_0 = karplus(f[i], fs[i], n, b[i])
        transfer = abs(sc.fft.fft(ks_0))
        transfer = transfer/abs(max(transfer))
        w = np.linspace(0, round(len(transfer)/(2*n)), round(len(transfer)/2))
        sf.write(sistema3_wav[i], ks_0, fs[i])
    elif i == 1:
        ks1 = karplus(f[i], fs[i], n, b[i])
        transfer1 = abs(sc.fft.fft(ks1))
        transfer1 = transfer1/abs(max(transfer1))
        w1 = np.linspace(0,  round(len(transfer1)/(2*n)), round(len(transfer1)/2))
        sf.write(sistema3_wav[i], ks1, fs[i])
    elif i == 2:
        ks2 = karplus(f[i], fs[i], n, b[i])
        transfer2 = abs(sc.fft.fft(ks2))
        transfer2 = transfer2/abs(max(transfer2))
        w2 = np.linspace(0, round(len(transfer2)/(2*n)), round(len(transfer2)/2))
        sf.write(sistema3_wav[i], ks2, fs[i])
    elif i == 3:
        ks3 = karplus(f[i], fs[i], n, b[i])
        transfer3 = abs(sc.fft.fft(ks3))
        transfer3 = transfer3/abs(max(transfer3))
        w3 = np.linspace(0, round(len(transfer3)/(2*n)), round(len(transfer3)/2))
        sf.write(sistema3_wav[i], ks3, fs[i])


t = np.linspace(0, (len(ks_0)/fs[0]), len(ks_0))
t2 = np.linspace(0, (len(ks1)/fs[1]), len(ks1))

# PLOT String Section
plt.style.use('seaborn')  # ploteos del sistema 3 para cuerda
fig, ((ax1, ax2), (ax3, ax4)) =\
plt.subplots(nrows=2, ncols=2, figsize=(16, 10))
fig.suptitle(r'$Karplus\ Strong\ Synthesizing \ String$', fontsize=18, y=0.99)

ax1.plot(w, 20*np.log10(transfer[0:round(len(transfer)/2)]),
         color='b', label=r'$Fs=$'+str(int(fs[0]/1000))+r'$kHz$')

ax2.plot(t, ks_0, color='black', label=r'$Fs=$'+str(int(fs[0]/1000))+r'$kHz$')

ax3.plot(w1, 20*np.log10(transfer1[0:round(len(transfer1)/2)]),
         color='b', label=r'$Fs=$'+str(int(fs[1]/1000))+r'$kHz$')

ax4.plot(t2, ks1, color='black', label=r'$Fs=$'+str(int(fs[1]/1000))+r'$kHz$')

ax1.set_title(r'$ String \ Spectre $', fontsize=14, y=0.999, x=0.1)

ax1.set_ylabel(r'$Amplitude \ [dB]$', fontsize=14)

ax1.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax1.legend(loc='best')

ax2.set_title(r'$ String\ $'+str(f[0])+r'$Hz $', fontsize=14, y=0.999, x=0.9)
ax2.set_ylabel(r'$Amplitude$', fontsize=14)

ax2.set_xlabel(r'$Time [S]$', fontsize=14)

ax2.legend(loc='best')

ax3.set_title(r'$String \ Spectre$', fontsize=14, y=0.999, x=0.1)

ax3.set_ylabel(r'$Amplitude \ [dB]$', fontsize=14)

ax3.set_xlabel(r'$Frequency [Hz]$', fontsize=14)

ax3.legend(loc='best')

ax4.set_title(r'$ String\ $'+str(f[1])+r'$Hz $', fontsize=14, y=0.999, x=0.9)

ax4.set_ylabel(r'$Amplitude$', fontsize=14)

ax4.set_xlabel(r'$Time [S]$', fontsize=14)

ax4.legend(loc='best')


plt.tight_layout()
plt.savefig('String_100Hz_Fs=22.05kHz.png')
plt.show()

# PLOT Drum Section
t3 = np.linspace(0, (len(ks2)/fs[2]), len(ks2))
t4 = np.linspace(0, (len(ks3)/fs[3]), len(ks3))

plt.style.use('seaborn')  # ploteos del sistema 3 para Drums
fig, ((ax1, ax2), (ax3, ax4)) =\
plt.subplots(nrows=2, ncols=2, figsize=(16, 10))
fig.suptitle(r'$Karplus\ Strong\ Synthesizing \ Drum$', fontsize=18, y=0.99)

ax1.plot(w2, 20*np.log10(transfer2[0:round(len(transfer2)/2)]),
         color='b', label=r'$Fs=$'+str(int(fs[2]/1000))+r'$kHz$')

ax2.plot(t3, ks2, color='black', label=r'$Fs=$'+str(int(fs[2]/1000))+r'$kHz$')

ax3.plot(w3, 20*np.log10(transfer3[0:round(len(transfer3)/2)]),
         color='b', label=r'$Fs=$'+str(int(fs[3]/1000))+r'$kHz$')

ax4.plot(t4, ks3, color='black', label=r'$Fs=$'+str(int(fs[3]/1000))+r'$kHz$')

ax1.set_title(r'$Drum \ Spectre$', fontsize=14, y=0.999, x=0.1)
ax1.set_ylabel(r'$Amplitude \ [dB]$', fontsize=14)
ax1.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax1.legend(loc='best')

ax2.set_title(r'$ Drum\ $'+str(f[2])+r'$Hz $', fontsize=14, y=0.999, x=0.9)
ax2.set_ylabel(r'$Amplitude  $', fontsize=14)
ax2.set_xlabel(r'$Time [S]$', fontsize=14)
ax2.legend(loc='best')

ax3.set_title(r'$Drum \ Spectre$', fontsize=14, y=0.999, x=0.1)
ax3.set_ylabel(r'$Amplitude \ [dB]$', fontsize=14)
ax3.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax3.legend(loc='best')

ax4.set_title(r'$ Drum\ $'+str(f[3])+r'$Hz $', fontsize=14, y=0.999, x=0.9)
ax4.set_ylabel(r'$Amplitude$', fontsize=14)
ax4.set_xlabel(r'$Time \  [S]$', fontsize=14)
ax4.legend(loc='best')


plt.tight_layout()
plt.show()