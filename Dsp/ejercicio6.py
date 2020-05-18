import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import singenerator as sg
from punto5 import fmm as fmm
from punto5 import frmm as frmm
from punto6 import fmmconv as fmmconv
from timeit import default_timer


# Definimos xt como la señal de entrada
[x3, T] = sg.singenerator(44100, 10000, 0.5, 1, 2)

m=round(0.01*len(x3))
# Aplicamos los filtros y medimos los timepos
'Para filtro de media movil por convolución'
startFMM_conv = default_timer()
señal_filtrada= fmmconv.fmmconv(x3,m)
finFMM_conv = default_timer()
ejecucionFMM_conv = finFMM_conv - startFMM_conv

###################################
'Para filtro de media movil recursivo.'
startfrmm = default_timer()
señal_filtrada2=frmm.frmm(x3,m)
finfrmm=default_timer()
ejecucionfrmm= finfrmm - startfrmm
#################################
'Para filtro de media movil .'
startfmm=default_timer()
señal_filtrada3=fmm.fmm(x3,m)
finfmm=default_timer()
ejecucionfmm= finfmm - startfmm
####################################

print('El tiempo de ejecucion para el filtro de media movil por convolución fue: ', ejecucionFMM_conv, 'Segundos')
print('El tiempo de ejecucion para el filtro de media movil fue: ', ejecucionfmm, 'Segundos')
print('El tiempo de ejecucion para el filtro Recursivo de media movil fue: ', ejecucionfrmm, 'Segundos')
####################################
'Normalizado de los vectores.'
señal_filtrada= señal_filtrada/ abs(max(señal_filtrada))
señal_filtrada2= señal_filtrada2/ abs(max(señal_filtrada2))
señal_filtrada3= señal_filtrada3/ abs(max(señal_filtrada3))

muestras_tfmm=(len(señal_filtrada2))
muestras_tfrmm=(len(señal_filtrada3))
muestras_tconv=len(x3)+m-1
t_conv=np.linspace(0,0.5,muestras_tconv)
tfmm=np.linspace(0,0.5,muestras_tfmm)
tfrmm=np.linspace(0,0.5,muestras_tfrmm)

# Plot
plt.style.use('seaborn')

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)
ax1.plot(t_conv ,señal_filtrada, color='r')
ax2.plot(tfmm, señal_filtrada2, color='y')
ax3.plot(tfrmm, señal_filtrada3)

ax1.set_title('Filtrado por convolución')
ax1.set_ylabel('Amplitud')
ax1.set_xlabel('Time[s]')

ax2.set_title('Filtada con filtro de media movil recursivo')
ax2.set_ylabel('Amplitud')

ax3.set_title('Filtro de media movil')
ax3.set_xlabel('Time[s]')
ax3.set_ylabel('Amplitud')

plt.tight_layout()
plt.show()

#[m:muestras_tconv-m] ESTO ES POR SI QUIERO RECORTAR EL VECTOR POR LOS ZEROS que se forman al promediar las muestras d la señal.
#[0:muestras_tfmm]
#[0:muestras_tfrmm] PREGUNTAR AL PROFE SI EL PLOT TA BIEN O SI LO PUEDO DEJAR RECORTADO + lindo.
