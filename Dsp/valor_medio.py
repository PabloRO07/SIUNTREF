import numpy as np 
from matplotlib import pyplot as plt 


def valor_medio(xn):
    n=len(xn)
    valor_medio=(1/n)*np.sum(xn)
    return(valor_medio)
