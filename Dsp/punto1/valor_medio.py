import numpy as np 
from matplotlib import pyplot as plt 


def valor_medio(xn):
    """'
    Esta funcion calcula el valor medio de una señal entrante
    """
    n = len(xn)
    vm = (1/n)*np.sum(xn)
    return vm
