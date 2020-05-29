import numpy as np 
from matplotlib import pyplot as plt


def frmm(x, m):
    """
    Return a filtered signal with a FMM

    Parameters:
    x : entry signal
    m : window
    """
    long = len(x)
    y = np.zeros(long)
    n = long-m

    for i in range(n):
        if i == 0:
            y[i] = np.sum(x[i:(m+1)+i])/(m+1)
        else:
            y[i] = y[i-1] + (x[i+(m+1)-1] - x[i-1])/(m+1)
        
    return y
