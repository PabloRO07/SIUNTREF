import numpy as np
from matplotlib import pyplot as plt


def blackmanf(x, m):
    a0 = .42
    a1 = .5
    a2 = .08
    n = np.arange(0, m-1)
    p = np.cos((2*np.pi*n)/m-1)
    q = np.cos((4*np.pi*n)/m-1)
    vn = a1 - a0*p + a2*q
    yn = np.convolve(x/abs(max(x)), vn/abs(max(vn)))
    return yn
