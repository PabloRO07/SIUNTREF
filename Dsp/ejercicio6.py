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
muestras_tconv=len(señal_filtrada)
t_conv=np.linspace(0,0.5,muestras_tconv)
tfmm=np.linspace(0,0.5,muestras_tfmm)
tfrmm=np.linspace(0,0.5,muestras_tfrmm)

# Plot
plt.style.use('seaborn')

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)
ax1.plot(t_conv ,señal_filtrada, color='black')
ax2.plot(tfmm, señal_filtrada2, color='b')
ax3.plot(tfrmm, señal_filtrada3,color='orange')

ax1.set_title(r'$Filtrado \ por \ convolución$',fontsize=12)
ax1.set_ylabel(r'$Amplitud$',fontsize=10)


ax2.set_title(r'$Filtro \ de \ media \ movil$',fontsize=12)
ax2.set_ylabel(r'$Amplitud$',fontsize=10)


ax3.set_title(r'$Filtada \ con \ filtro \ de \ media \ movil \ recursivo$',fontsize=12)
ax3.set_ylabel(r'$Amplitud$',fontsize=10)
ax3.set_xlabel(r'$Time[s]$',fontsize=10)

plt.tight_layout()
plt.show()
