import numpy as np


'Esta funcion calcula la autocorrelacion de una señal a partir de la funcion de NUMPY correlate'


def autocorr(x):
    result = np.correlate(x, x, mode='full')
    return result
