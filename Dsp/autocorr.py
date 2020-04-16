import numpy as np


def autocorr(x):
    result = np.correlate(x, x, mode='full')
    return result
