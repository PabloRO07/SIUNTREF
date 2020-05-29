import numpy as np


def blackman(x, m):
    """This function apply moving avergae filter using the Black Man Window

    Parameters:
    x = Entry Signal
    m = Window Size
    """
    a0 = 0.42
    a1 = 0.5
    a2 = 0.08
    kernel = np.zeros(m)
    n = np.arange(m-1)
    kernel = a0 - a1 * np.cos((2 * np.pi * n) / (m - 1)) + a2 * np.cos((4 * np.pi * n) / (m - 1))
    y = np.convolve(x, kernel)
    return y



