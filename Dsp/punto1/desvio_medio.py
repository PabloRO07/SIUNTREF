import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import valor_medio as vm

'Esta funcion calcula el desvio medio de una señal utilizando la funcion valor_medio'


def desvio_medio(xn):
    n = len(xn)
    v_m = vm.valor_medio(xn)
    d = (1/n)*np.sum(abs(xn-v_m))
    return d
