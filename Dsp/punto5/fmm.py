import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import singenerator as sg


def fmm(x, m):
    """
    This function calculate de  moving average filter
     for an entry signal

     Parameters:
     x = Entry signal
     m = Size of window
     """

    long = len(x)
    y = np.zeros(long)
    n = long-m
    for i in range(n):
        y[i] = np.sum(x[i:((m+1)+i)])/(m+1)
    return y



