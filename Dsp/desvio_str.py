import numpy as np 
from matplotlib import pyplot as plt 
import valor_medio as vm
def desvio_str(xn):
    n=len(xn)
    v_m=vm.valor_medio(xn)
    sigma=np.sqrt((1/(n-1))*np.sum((np.square(abs(xn-v_m)))))
    sigma2=sigma**2
    return(sigma,sigma2)