import numpy as np

def energy(x):
    x = np.square(x)
    e = np.sum(x)
    return e
