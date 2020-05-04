import numpy as np


def autocorr(x):
    """
    Esta funcion calcula la autocorrelacion de una señal a partir de la funcion de NUMPY correlate
    """
    result = np.correlate(x, x, mode='full')
    return result
