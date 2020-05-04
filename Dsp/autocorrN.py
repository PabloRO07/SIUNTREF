import numpy as np
import energy


def autocorr(x):
    """
    Esta funcion calcula la autocorrelacion de una señal a partir de la funcion de NUMPY correlate' \
    Utilizando ademas la funcion energy, que calcula la energia
    """
    result = np.correlate(x, x, mode='full')
    t = energy(x)
    result = result/t
    return result