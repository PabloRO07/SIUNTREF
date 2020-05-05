import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import singenerator as sg
import scipy as sc 


def FMM(x, M):
    L = len(x)
    y = np.zeros(L)
    N = L-M
    for i in range(N):
        y[i] = np.sum(x[i:M+i])/M
    return y


[xt,T]=sg.singenerator(44100, 10e3, 0.5, 1, 2)

salida=FMM(xt,2)
fig, axs = plt.subplots(2)
fig.suptitle('Filtro de media movil')
axs[0].plot(T,xt)
axs[1].plot(T,salida)

plt.show()
