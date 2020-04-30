import numpy as np
from matplotlib import pyplot as plt


'Esta funcion calculad el valor medio de una señal'

def valor_medio(xn):
    n=len(xn)
    valor_medio=(1/n)*np.sum(xn)
    return valor_medio


'Esta funcion calcula el desvio medio de una señal utilizando la funcion valor_medio'

def desvio_medio(xn):
    n = len(xn)
    v_m = vm.valor_medio(xn)
    d = (1/n)*np.sum(abs(xn-v_m))
    return d


'Esta funcion calcula el desvio estandar de una señal a partir de la funcion valor_medio'

def desvio_str(xn):
    n = len(xn)
    v_m = vm.valor_medio(xn)
    sigma = np.sqrt((1/(n-1))*np.sum((np.square(abs(xn-v_m)))))
    sigma2 = sigma**2
    return sigma, sigma2


'Esta funcion calcula el RMS de una señal'


def RMS(xn):
    n=len(xn)
    rms=np.sqrt((1/n)*sum(np.square(abs(xn))))
    return rms
