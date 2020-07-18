import numpy as np


def ks(f, fs, n, b):
    """
    :param f: Frecuency to synthesize
    :param fs: Sampling frequency
    :param n: Long time in second of the output signal
    :param b: Probabilistic parameter b>9 for string synthesizing  and 0>=b<9 for drum synthesizing
    :return: Signal of "f" frecuency, drum or string, of time "n"
    """
    n = n*fs
    b = int(b*10)
    p = fs // f
# Diseño de Wavetable #
    wavetable = (2 * np.random.randint(0, 2, p) - 1).astype(np.float)  # generador de ruido (1;-1)

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
