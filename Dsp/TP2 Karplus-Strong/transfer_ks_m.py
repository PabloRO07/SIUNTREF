import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 

a = 0
v_anterior = 0
fs=10000
f=100
n=44100
karplus = np.zeros(n)
p=fs // f
impulse = np.zeros(p)  # Set zero vector for impulse
impulse[0] = 1
wavetable=impulse
b=1
beta=0
bw=44100
b = int(b*10)
rho=0.9

    
# Pick direction Low pass filter  Hf
l=len(wavetable) 
y=0
acumulador=0
wavetable_pick = np.zeros(l)
if (rho!=0):
    for i in range(l):
        wavetable_pick[i]= wavetable[i] -rho*( wavetable[i]-acumulador)
        acumulador=wavetable_pick[i]
    wavetable=wavetable_pick
# Pick position Comb filter He

wavetable_d=np.hstack((np.zeros(round(l*beta)),wavetable))
wavetable_comb_pick=np.zeros(l)
a1=0
for i in range(l):
    wavetable_comb_pick[i]=wavetable[a1]-wavetable_d[i]
    a1+=1
    a1= a1 % len(wavetable) 
    
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
    
    #Dynamic Low pass Filter  Butterworth first order Hd
if bw!=0:
    r=np.exp(-np.pi*bw*(2/fs))
    for i in range(n):
        karplus[i]= (1-r)*karplus[i] +r*y
        y=karplus[i]





transfer = abs(sc.fft.fft(karplus))
transfer=transfer/abs(max(transfer))
w=np.linspace(0,(fs/2),round(len(transfer)/2))
sf.write('karplus_hn.wav', karplus, fs)
plt.plot(w,20*np.log10(transfer[0:round(n/2)]))
plt.show()