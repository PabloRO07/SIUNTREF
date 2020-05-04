import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import valor_medio as vm


def desvio_str(xn):
    """'
    Esta funcion calcula el desvio estandar de una señal a partir de la funcion valor_medio
    '"""
    n = len(xn)
    v_m = vm.valor_medio(xn)
    sigma = np.sqrt((1/(n-1))*np.sum((np.square(abs(xn-v_m)))))
    sigma2 = sigma**2
    return sigma, sigma2
