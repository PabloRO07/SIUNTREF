import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc


def extended_ks(f, fs, n, b,bw,rho,beta):
    """

    :param f: Frecuency to synthesize
    :param fs: Sampling frequency
    :param n: Long time in second of the output signal
    :param b: Probabilistic parameter b>9 for string synthesizing  and 0>=b<9 for drum synthesizing
    :param bw: cut frequency
    :param rho: Low pass filtering between 0<rho<1, Going from 0 to non filter, to 1 total filter
    :param beta: picking parameter, if dont want to use this parameter, can input a "0", else 0<beta<1
    :return: Signal of "f" frequency, drum or string, of time "n"
    """
    n = n*fs
    b = int(b*10)
    p = fs // f
# Wave Table Desing #
    wavetable = (2 * np.random.randint(0, 2, p) - 1).astype(np.float)  # Noise Generator (1;-1)
    v_anterior = 0
    karplus = np.zeros(n)
    
# Pick direction Low pass filter  Hf
    l = len(wavetable)
    y = 0
    acumulador = 0
    wavetable_pick = np.zeros(l)
    if rho!=0:
        for i in range(l):
            wavetable_pick[i] = wavetable[i] - rho*(wavetable[i]-acumulador)
            acumulador = wavetable_pick[i]
        wavetable = wavetable_pick
# Pick position Comb filter He
    if beta !=0:
        wavetable_d = np.hstack((np.zeros(round(l*beta)), wavetable))
        wavetable_comb_pick = np.zeros(l)
        a1 = 0
        for i in range(l):
            wavetable_comb_pick[i] = wavetable[a1]-wavetable_d[i]
            a1 += 1
            a1 = a1 % len(wavetable)
    
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
    
# Dynamic Low pass Filter  Butterworth first order Hd
    if bw != 0:
        r = np.exp(-np.pi*bw*(2/fs))
        for i in range(n):
            karplus[i] = (1-r)*karplus[i] + r*y
            y = karplus[i]

    return karplus


# Function Run KSM
f0 = 100
fs0 = 44100
n0 = 1
b0 = 0.5
bw0 = fs0  # So is not filtering
rho0 = 0.8
beta0 = 0.5
karplus0 = extended_ks(f0, fs0, n0, b0, bw0, rho0, beta0)
sf.write('KSM_bw44100_rho0.8_beta0.5.wav', karplus0, 44100)
f1 = 100
fs1 = 44100
n1 = 1
b1 = 0.5
bw1 = 100  # Wc in 100Hz
rho1 = 0
beta1 = 0
karplus2 = extended_ks(f1, fs1, n1, b1, bw1, rho1, beta1)
sf.write('KSM_bw100.wav', karplus2, 44100)


# Data Process KSM
scpectre = sc.fft.fft(karplus0)  # Output FFT
spectre1 = sc.fft.fft(karplus2)
spectre = abs(scpectre)  # Frequency response
spectre1 = abs(spectre1)  # Frequency response

t0 = np.linspace(0, (len(karplus0)/fs0), len(karplus0))  # Time vector for graph
t1 = np.linspace(0, (len(karplus2)/fs1), len(karplus2))  # Time vector for Y2[n]
w0 = np.linspace(0, (fs0/2), round(len(scpectre)/2))
w1 = np.linspace(0, (fs1/2), round(len(spectre1)/2))

# PLOT String Section KSM
plt.style.use('seaborn')
fig, ((ax1, ax2), (ax3, ax4)) =\
plt.subplots(nrows=2, ncols=2, sharex='col', figsize=(16, 10))
if b0 == 1:
    fig.suptitle(r'$Karplus\ Strong\ Modified\ Synthesizing \ String$', fontsize=18)
else:
    fig.suptitle(r'$Karplus\ Strong\ Modified\ Synthesizing \ Drum$', fontsize=18)

ax1.plot(w0, 20*np.log10(spectre[0:round(len(spectre)/2)]),
         color='b', label=r'$Fs=$'+str(fs0)+r'$Samples$')
ax2.plot(t0, karplus0, color='black', label=r'$Fs=$'+str(fs0)+r'$Samples$')
ax3.plot(w1[0:round(len(spectre1)/2)], 20*np.log10(spectre1[0:round(len(spectre1)/2)])
         , color='b', label=r'$Fs=$'+str(fs1)+r'$Samples$')
ax4.plot(t1, karplus2, color='black', label=r'$Fs=$'+str(fs1)+r'$Samples$')

ax1.set_title(r'$ Signal \ Spectre $', fontsize=14)
ax1.set_ylabel(r'$Amplitude$', fontsize=14)
ax1.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax1.legend(loc='best')

ax2.set_title('Signal', fontsize=14)
ax2.set_ylabel(r'$Amplitude$', fontsize=14)
ax2.set_xlabel(r'$Time [S]$', fontsize=14)
ax2.legend(loc='best')

ax3.set_title(r'$Signal \ Spectre$', fontsize=14)
ax3.set_ylabel(r'$Amplitude$', fontsize=14)
ax3.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax3.legend(loc='best')

ax4.set_title('Signal', fontsize=14)
ax4.set_ylabel(r'$Amplitude$', fontsize=14)
ax4.set_xlabel(r'$Time [S]$', fontsize=14)
ax4.legend(loc='best')


plt.legend(fontsize=14)
plt.tight_layout()
plt.show()
