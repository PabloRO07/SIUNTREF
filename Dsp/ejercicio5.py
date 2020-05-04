import numpy as np
from matplotlib import pyplot as plt
from punto5 import fmm as fm
from punto5 import frmm as rfm

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
[xt, T] = sg.singenerator(44100, 10e3, 0.5, 1, 2)
# Aplicamos los filtros
fmm = fm.fmm(xt, 3)
frmm = rfm.frmm(xt, 3)
# Plot
plt.style.use('seaborn')

fig, ax1 = plt.subplots(nrows=3, ncols=1, sharex=True)

ax1.plot(T, xt, color='r')
ax2.plot(T, fmm, color='y')
ax3.plot(T, frmm)

ax1.set_title('Señal senoidal sin filtro')
ax1.set_ylabel('Amplitud')
ax1.set_xlabel('Time[s]')

ax2.set_title('Filtada con filtro de media movil')
ax2.set_ylabel('Amplitude')


ax3.set_title('RFMM FIlter')
x3.set_ylabel('Amplitude')
ax3.set_xlabel('Time[s]')


plt.tight_layout()
plt.show()
