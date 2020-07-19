import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 

a = 0
v_anterior = 0
fs=2000
f=20
n=44100
karplus = np.zeros(n)
p=fs // f
impulse = np.zeros(p)  # Set zero vector for impulse
impulse[0] = 1
wavetable=impulse
for i in range(n):

    wavetable[a] = 0.5 * (wavetable[a]+v_anterior)
    karplus[i] = wavetable[a]
    v_anterior = karplus[i]
    a += 1
    a = a % len(wavetable)

transfer = abs(sc.fft.fft(karplus))
transfer=transfer/abs(max(transfer))
w=np.linspace(0,(fs/2),round(len(transfer)/2))
sf.write('karplus_hn.wav', karplus, fs)
plt.plot(w,20*np.log10(transfer[0:round(n/2)]))
plt.show()