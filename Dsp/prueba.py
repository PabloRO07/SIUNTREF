import numpy as np 
from matplotlib import pyplot as plt 
import desvio_medio as dm
import desvio_str as ds
import RMS as rms
import valor_medio as vm


fs=44100
f=10000
t=0.5
t=np.linspace(0,t,int(fs*t))
xt=2+np.sin(2*np.pi*f*t)


valor_medio=vm.valor_medio(xt)
d=dm.desvio_medio(xt)
sigma=ds.desvio_str(xt)
rms=rms.RMS(xt)
 
ruidito=np.random.normal(0,1,10)

print(ruidito)
print(valor_medio)
print(d)
print(sigma)
print(rms)
