import numpy as np


def ks(f,fs,n,b):
    n=n*fs
    b=int(b*10)
    p= fs // f
    ### diseño de Wavetable ####
    wavetable = (2 * np.random.randint(0, 2, p) - 1).astype(np.float)  # generador de ruido (1;-1)
    
    v_anterior=0
    karplus=np.zeros(n)
    
    a=0

    for i in range(n):
        h=np.random.randint(0,9)
        if (h<=b):
            wavetable[a]= 0.5* (wavetable[a]+v_anterior)
        else:
            wavetable[a]= -0.5* (wavetable[a]+v_anterior)

        karplus[i]=wavetable[a]
        v_anterior=karplus[i]
        a+=1
        a= a % len(wavetable)
    return (karplus)