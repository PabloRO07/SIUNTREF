import numpy as np


def fmm_conv(x, m):
    """This function aplly al moving average filter using convolution

    Parameters:
    x = Entry signal
    m = Window Size
    """
    kernel = np.ones(m)/(m+1)
    salida = np.convolve(x, kernel)
    return salida
