import numpy as np
from matplotlib import pyplot as plt 
import sounddevice as sd 
import soundfile as sf 
import noise as ns
import random

### diseño de Wavetable ####

fs=44100
N=2*fs
p= fs // 100
wavetable = (2 * np.random.randint(0, 2, p) - 1).astype(np.float)  # generador de ruido (1;-1)
wavetable_drum = (2 * np.random.randint(0, 2, p) - 1).astype(np.float)  # generador de ruido (1;-1)
v_anterior=0
karplus=np.zeros(N)
karplus_drum=np.zeros(N)
culo_rojo_de_mandril=np.zeros(N)
a=0

for i in range(N):
    wavetable[a]= 0.5* (wavetable[a]+v_anterior)
    
    karplus[i]=wavetable[a]
    v_anterior=karplus[i]
    a+=1
    a= a % len(wavetable)

for i in range(N):
    b=np.random.randint(0,9)
    if (b>=4):
        wavetable_drum[a]= 0.5* (wavetable_drum[a]+v_anterior)
    else:
        wavetable_drum[a]= -0.5* (wavetable_drum[a]+v_anterior)

    karplus_drum[i]=wavetable_drum[a]
    v_anterior=karplus_drum[i]
    a+=1
    a= a % len(wavetable_drum)



plt.plot(karplus)
plt.show()
sf.write('prueba_4echo.wav',karplus,fs)
sf.write('prueba_2echo.wav',karplus_drum,fs)

