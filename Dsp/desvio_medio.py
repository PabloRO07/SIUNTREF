import numpy as np 
from matplotlib import pyplot as plt 
import valor_medio as vm
def desvio_medio(xn):
    n=len(xn)
    v_m= vm.valor_medio(xn)
    d=(1/n)*np.sum(abs(xn-v_m))
    return(d)