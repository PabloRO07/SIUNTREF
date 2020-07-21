import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 

a = 0
v_anterior = 0
fs = 10000
f = 100
n = 44100
karplus = np.zeros(n)
p = fs // f
impulse = np.zeros(p)  # Set zero vector for impulse
impulse[0] = 1
wavetable = impulse
for i in range(n):
    wavetable[a] = 0.5 * (wavetable[a]+v_anterior)
    karplus[i] = wavetable[a]
    v_anterior = karplus[i]
    a += 1
    a = a % len(wavetable)

transfer = abs(sc.fft.fft(karplus))
transfer = transfer/abs(max(transfer))
w = np.linspace(0, (fs/2), round(len(transfer)/2))
real = np.real(sc.fft.fft(karplus))
imag = np.imag(sc.fft.fft(karplus))
phase = np.arctan((imag/real))
sf.write('karplus_hn.wav', karplus, fs)

# PLOT Frequency response karplus strong system
plt.style.use('seaborn')
fig, (ax1, ax2) =\
plt.subplots(nrows=2, ncols=1, figsize=(16, 10))
fig.suptitle(r'$ Transfer \ Function \ |H_3(e^{jw})| $', fontsize=18, y=0.991)

ax1.plot(w, 20*np.log10(transfer[0:round(n/2)]), color='b',label='Fs = '+str(int(fs/1000))+' K hz'+','+'f ='+str(f))
ax2.plot(w, phase[0:round(n/2)], color='b')


ax1.set_title(r'$ |H_3(e^{jw})| $', fontsize=14, y=0.999, x=0.025)
ax1.set_ylabel(r'$Amplitude$', fontsize=14)
ax1.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax1.legend(loc='best')


ax2.set_title(r'$Phase \ x[n] $', fontsize=14, y=0.999, x=0.035)
ax2.set_ylabel(r'$Amplitude\ [rad]$', fontsize=14)
ax2.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
ax2.legend(loc='best')


plt.legend(fontsize=12)
plt.savefig('sistema3_1d_1alfa.png')
plt.tight_layout()

plt.show()
