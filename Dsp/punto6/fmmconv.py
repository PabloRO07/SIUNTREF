import numpy as np


def fmmconv(x, m):
    """This function aplly al moving average filter using convolution

    Parameters:
    x = Entry signal
    m = Window Size
    """
    kernel = (np.ones(m+1))/(m+1)
    salida = np.convolve(x, kernel)
    return salida
