import numpy as np
from matplotlib import pyplot as plt
from punto1 import singenerator as sg
from punto5 import fmm as fmm
from punto5 import frmm as frmm
from timeit import default_timer

"""Se procede en este scrip a comparar el tiempo de ejecucion de:
        Filtro de media movil
        Filtro de media movil recursivo
    Para una señal de senoidal con los siguiente parametros
        Frecuencia de muestreo:44100
        Frecuencia de la señal:1kHz
        Duracion de la señalÑ 0.5 seg
        Aplitud: 1
        Valor de continua/Centrado : 2
"""
# Definimos xt como la señal de entrada
[xt, T] = sg.singenerator(44100, 1000, 0.5, 1, 2)

# Aplicamos los filtros y medimos lso timepos
'Para filtro de media movil'
startfmm = default_timer()
filtro = fmm.fmm(xt, 3)
finfmm = default_timer()
ejecucionfmm = finfmm - startfmm
'Para filtro recursivo de de media movil'
startfrmm = default_timer()
recursive = frmm.frmm(xt, 3)
finfrmm = default_timer()
ejecucionfrmm = finfrmm - startfrmm

print('El tiempo de ejecucion para el filto de media movil fue: ', ejecucionfmm, 'Segundos')
print('El tiempo de ejecucion para el filto Recursivo de media movil fue: ', ejecucionfrmm, 'Segundos')

# Plot
plt.style.use('seaborn')

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)

ax1.plot(T, xt, color='r')
ax2.plot(T, filtro, color='y')
ax3.plot(T, recursive)

ax1.set_title('Señal senoidal sin filtro')
ax1.set_ylabel('Amplitud')
ax1.set_xlabel('Time[s]')

ax2.set_title('Filtada con filtro de media movil')
ax2.set_ylabel('Amplitude')

ax3.set_title('RFMM FIlter')
ax3.set_xlabel('Time[s]')

plt.tight_layout()
plt.show()
