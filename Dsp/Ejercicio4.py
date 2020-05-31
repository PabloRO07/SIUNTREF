import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import singenerator as sg
from punto1 import desvio_str as ds
from punto1 import valor_medio as vm
from punto1 import desvio_medio as dm
from punto1 import RMS as rms

[xt,T]=sg.singenerator(44100, 10e3, 0.5, 1, 2)

N1=100 #define numero de ruidos a promediar 100
N2=1000  #define numero de ruidos a promediar 1000
matriz_ruido=np.zeros([N2,len(T)]) #matriz vacia para almacenar ruido.
valor_promedio=np.zeros(N2)   #vector vacio que acumula los valores a promediar de cada muestra
señal_promedio=np.zeros(len(T)) # vector vacio señal promedio 

valor_promedio_100=np.zeros(N1)   #vector vacio que acumula los valores a promediar de cada muestra para el promediado de 100 señales
señal_promedio_100=np.zeros(len(T)) # vector vacio señal promedio 100 señales

for i in range(N2):
    matriz_ruido[i]= np.random.normal(0,3,len(T)) + xt #Ruido media 0 , sigma3 + señal xt

for a in range(len(T)):
    
    for b in range(N1):
        valor_promedio_100[b]=matriz_ruido[b,a]
        

    señal_promedio_100[a]= np.sum(valor_promedio_100)/N1  # construcción del vector promedio.

        
################### PARA 1000 Ruidos ########################

for a in range(len(T)):
    
    for b in range(N2):
        valor_promedio[b]=matriz_ruido[b,a]
    señal_promedio[a]= np.sum(valor_promedio)/N2  # construcción del vector promedio.

print(len(valor_promedio_100))
print(len(valor_promedio))
snr_promedio= max(abs(señal_promedio)) / ds.desvio_str(señal_promedio)[0]
señal_promedio_snr_100 = (max(abs(señal_promedio_100)) / ds.desvio_str(señal_promedio_100)[0]) # SNR para 100 promediados
ruidito3 = np.random.normal(0,3,len(T)) #Creo la señal del punto 3 para compararla
x3= ruidito3+xt / max(ruidito3+xt)
snr3 = (max(abs(x3)) / ds.desvio_str(x3)[0])
print("la relación señal ruido sin promediar es:",snr3) # SNR de la señal del punto 3
print("la relación señal ruido promediada",N1,  "veces es:",señal_promedio_snr_100) # SNR de la señal promediada con 100 señales
print("la relación señal ruido  promediando",N2,"es:",snr_promedio) # SNR señal promediada con 1000 señales