import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 

#def extended_ks(f, fs, n, b,bw,rho):
f=100 
fs=12000 
n=1 
b=100
b2=500
bw=0
rho=0
n = n*fs
b = int(b*10)
p = fs // f
# Wave Table Desing #
wavetable = (2 * np.random.randint(0, 2, p) - 1).astype(np.float)  # Noise Generator (1;-1)
v_anterior = 0
karplus = np.zeros(n)
karplus2 = np.zeros(n)  
# Pick direction Low pass filter 
l=len(wavetable) 
y=0
acumulador=0
wavetable_pick = np.zeros(l)
if (rho!=0):
    for i in range(l):
        wavetable_pick[i]= wavetable[i] -rho*( wavetable[i]-acumulador)
        acumulador=wavetable_pick[i]
    wavetable=wavetable_pick
# Pick position Comb filter
beta=0.5
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

# Pick position Comb filter
#beta=0.5
#wavetable_d=np.hstack((np.zeros(round(l*beta)),wavetable))
#wavetable_comb_pick=np.zeros(l)
#a1=0
#for i in range(l):
#    wavetable_comb_pick[i]=wavetable[a1]-wavetable_d[i]
#    a1+=1
#    a1= a1 % len(wavetable) 
        
    
a = 0
for i in range(n):
    h = np.random.randint(0, 9)
    if h <= b:
        wavetable[a] = 0.5 * (wavetable[a]+v_anterior)
    else:
        wavetable[a] = -0.5 * (wavetable[a]+v_anterior)
        
    karplus2[i] = wavetable[a]
    v_anterior = karplus[i]
    a += 1
    a = a % len(wavetable)
    
    #Dynamic Low pass Filter  Butterworth first order
    if bw!=0:
        r=np.exp(-np.pi*bw*(2/fs))
        for i in range(n):
            karplus[i]= (1-r)*karplus[i] +r*y
            y=karplus[i]


    #return karplus,wavetable


#karplus,wavetable=extended_ks()
sf.write('prueba_beta05.wav',karplus,12000)
#karplus2=ks.karplus(100, 44100, 1, 1)
sf.write('prueba_sinbeta.wav',karplus2,12000)