import numpy as np 
from matplotlib import pyplot as plt

'Esta funcion calcula el RMS de una señal'


def RMS(xn):
    n=len(xn)
    rms=np.sqrt((1/n)*sum(np.square(abs(xn))))
    return(rms)
