import numpy as np

'Esta funcion calcula la energia de una señal'
def energy(x):
    x = np.square(x)
    e = np.sum(x)
    return e
