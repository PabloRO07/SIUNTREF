import numpy as np
import energy


def autocorr(x):
    result = np.correlate(x, x, mode='full')
    t = energy(x)
    result = result/t
    return result