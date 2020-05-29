import numpy as np 
import scipy as sc 
from matplotlib import pyplot as plt 
from punto6 import fmmconv as fmmconv

#creo vector impulso 
fs=44100
impulse=np.zeros(fs-1)
impulse[0]=1

#filtrado del impulso
ir=fmmconv.fmmconv(impulse,2)
#funcion de transferencia
ir_frec=sc.fft.fft(ir)
frec_response=abs(ir_frec)
print(len(frec_response))
print(20*np.log10(frec_response[10000]))
w=np.linspace(0,np.pi,22050)
plt.plot(w,frec_response[0:round(fs/2)])
plt.show()