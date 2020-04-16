import numpy as np 
from matplotlib import pyplot as plt 
import desvio_medio as dm
import desvio_str as ds
import RMS as rms
import valor_medio as vm

ruidito5=np.random.normal(0,1,5) #genera ruido con distribucion gaussiana . (0 para tipo de distribucion gaussiana,1 para desviacion standard unitaria,Numero de muestras)
ruidito10=np.random.normal(0,1,10)
ruidito100=np.random.normal(0,1,100)
ruidito1k=np.random.normal(0,1,1000)
ruidito10k=np.random.normal(0,1,10000)
ruidito100k=np.random.normal(0,1,100000)

desvio5=ds.desvio_str(ruidito5)
desvio10=ds.desvio_str(ruidito10)
desvio100=ds.desvio_str(ruidito100)
desvio1k=ds.desvio_str(ruidito1k)
desvio10k=ds.desvio_str(ruidito10k)
desvio100k=ds.desvio_str(ruidito100k)

print(desvio5[0])
print(desvio10[0])
print(desvio100[0])
print(desvio1k[0])
print(desvio10k[0])
print(desvio100k[0])