import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import singenerator as sg
from punto1 import desvio_str as ds
from punto1 import valor_medio as vm
from punto1 import desvio_medio as dm
from punto1 import RMS as rms

[xt,T]=sg.singenerator(44100, 10e3, 0.5, 1, 2)

N=1000 #define numero de ruidos a promediar
matriz_ruido=np.zeros([N,len(T)]) #matriz vacia para almacenar ruido.
valor_promedio=np.zeros(N)   #vector vacio que acumula los valores a promediar de cada muestra
señal_promedio=np.zeros(len(T)) # vector vacio señal promedio 

for i in range(N):
    matriz_ruido[i]= np.random.normal(0,3,len(T)) + xt #Ruido media 0 , sigma3 + señal xt

for a in range(len(T)):
    
    for b in range(N):
        valor_promedio[b]=matriz_ruido[b,a]

    señal_promedio[a]= np.sum(valor_promedio)/N  # construcción del vector promedio.



snr_promedio= max(abs(señal_promedio)) / ds.desvio_str(señal_promedio)[0]

ruidito3 = np.random.normal(0,3,len(T)) #Creo la señal del punto 3 para compararla
x3= ruidito3+xt / max(ruidito3+xt)
snr3 = (max(abs(x3)) / ds.desvio_str(x3)[0])
print("la relación señal ruido  promediando",N,"es:",snr_promedio) # SNR señal promediada
print("la relación señal ruido sin promediar es:",snr3) # SNR de la señal del punnto 3
