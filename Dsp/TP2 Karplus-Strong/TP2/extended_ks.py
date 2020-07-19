import numpy as np
import soundfile as sf
import karplus as ks


def extended_ks(f, fs, n, b, R):
    """
    :param f: Frecuency to synthesize
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
    
# Dinamic Filter   
    y = 0
    l = len(wavetable)
    a = 0
    for i in range(l):
        wavetable[i] = (1-R)*wavetable[i] + R*y
        y = wavetable[i]

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


karplus = extended_ks(50, 44100, 1, 1, 0.9)
sf.write('prueba_dinamic_filter2.wav', karplus, 44100)
karplus2 = ks.karplus(50, 44100, 1, 1)
sf.write('prueba_dinamic_filter.wav', karplus2, 44100)