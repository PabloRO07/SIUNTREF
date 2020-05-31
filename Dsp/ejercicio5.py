import numpy as np
import scipy as sc
from matplotlib import pyplot as plt
from punto1 import singenerator as sg
from punto5 import fmm as fmm
from punto5 import frmm as frmm
from timeit import default_timer
from punto1 import RMS as rms
from punto6 import fmmconv as fmmconv

"""Se procede en este script a comparar el tiempo de ejecucion de:
        Filtro de media movil
        Filtro de media movil recursivo
    Para una señal de senoidal con los siguiente parametros
        Frecuencia de muestreo:44100
        Frecuencia de la señal:10kHz
        Duracion de la señal 0.5 seg
        Amplitud: 1
        Valor de continua/Centrado : 2
"""
# Definimos xt como la señal de entrada
[xt, T] = sg.singenerator(44100, 10000, 0.5, 1, 2)

##### Criterio para encontrar la frecuencia de corte del filtro en 10khz ################
fs = 44100
fc=10000 #Frecuencia de corte
m = 0 # Contador de ventana
frec_response=np.ones(fs-m) # este vector se sobreescribe cuando entra al while
while (frec_response[fc]>=0.707) : # condición para encontrar la frecuencia de corte
    m=m+1 #ventana inicial
    impulse = np.zeros(fs-m+1) # vector impulso
    impulse[0] = 1 # vector impulso
    
    # Filtrado del impulso
    ir = fmmconv.fmmconv(impulse, m)
    # Funcion de transferencia
    ir_frec = sc.fft.fft(ir)
    frec_response = abs(ir_frec)
    print("con una ventana de", m, " muestra, para el valor de 10khz", "que en proporcion de pi es", ((10e3*np.pi)/(fs/2)),
        ",la magnitud del filtro es de ", frec_response[fc], "o", 20*np.log10(frec_response[fc]), "dB")
  
i=(m-1) # por que se paso de la condicion de -3dB 

# Aplicamos los filtros y medimos los timepos
'Para filtro de media movil'
startfmm = default_timer()
filtro = fmm.fmm(xt, i)
finfmm = default_timer()
ejecucionfmm = finfmm - startfmm
'Para filtro recursivo de de media movil'
startfrmm = default_timer()
recursive = frmm.frmm(xt, i)
finfrmm = default_timer()
ejecucionfrmm = finfrmm - startfrmm


print('El tiempo de ejecucion para el filtro de media movil fue de: ', ejecucionfmm, 'Segundos')
print('El tiempo de ejecucion para el filtro Recursivo de media movil fue de: ', ejecucionfrmm, 'Segundos')


# Plot
plt.style.use('seaborn')

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)
ax1.plot(T, xt, color='black',label='x[n]')
ax2.plot(T, filtro, color='b',label='xfd[n]')
ax3.plot(T, recursive,color='orange',label='xfr[n]')


ax1.set_title(r'$Señal \ x[n] \ sin \ filtrar$')
ax1.set_ylabel(r'$Amplitud$')
ax1.set_ylim([0, 4])
ax1.legend(loc='best')

ax2.set_title(r'$Señal \ X_{fd}[n] \  filtrarada$')
ax2.set_ylabel(r'$Amplitud$')
ax2.set_ylim([0, 3])
ax2.legend(loc='best')

ax3.set_title(r'$Señal \ x_{fr}[n] \ filtrarada$')
ax3.set_xlabel(r'$Time[s]$')
ax3.set_ylabel(r'$Amplitud$')
ax3.set_ylim([0, 3])
ax3.legend(loc='best')


plt.tight_layout()
plt.legend()
plt.show()
