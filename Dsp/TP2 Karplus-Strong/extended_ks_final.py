import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 
import karplus_final as ks


def extended_ks(f, fs, n, b, bw, rho, beta):
    """
    :param f: Frecuency to synthesize
    :param fs: Sampling frequency
    :param n: Long time in second of the output signal
    :param b: Probabilistic parameter b>9 for string synthesizing  and 0>=b<9 for drum synthesizing
    :param bw: Cur Frequency Dynamic Low pass Filter
    :param rho: Pick direction Low pass filter From 0= no effect to 1
    :param beta: Pick position Comb filter from 0= no effect, to 0.5
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
    if rho != 0:
        for i in range(l):
            wavetable_pick[i] = wavetable[i] - rho*(wavetable[i]-acumulador)
            acumulador = wavetable_pick[i]
        wavetable = wavetable_pick
# Pick position Comb filter He
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


karplus = extended_ks(100, 12000, 1, 1, 0, 0, 0.5)
sf.write('prueba_dinamic_filter2.wav', karplus, 44100)
karplus2 = ks.karplus(100, 44100, 1, 1)
sf.write('prueba_dinamic_filter.wav', karplus2, 44100)
