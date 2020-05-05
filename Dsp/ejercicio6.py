import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import singenerator as sg
from punto5 import fmm as fmm
from punto5 import frmm as frmm
from timeit import default_timer
def FMM_conv(x,m):
    kernel= np.ones(m)/(m+1)
    salida=np.convolve(x,kernel)
    return(salida)

# Definimos xt como la señal de entrada
[xt, T] = sg.singenerator(44100, 10000, 0.5, 1, 2)

ruidito3 = np.random.normal(0,3,len(T)) #Creo la señal del punto 3 para compararla
x3= (ruidito3+xt) 
m=round(0.01*len(x3))
# Aplicamos los filtros y medimos los timepos
'Para filtro de media movil por convolución'
startFMM_conv = default_timer()
señal_filtrada=FMM_conv(x3,m)
finFMM_conv = default_timer()
ejecucionFMM_conv = finFMM_conv - startFMM_conv
###################################
'Para filtro de media movil.'
startfmm = default_timer()
señal_filtrada2=frmm.frmm(x3,m)
finfmm=default_timer()
ejecucionfmm= finfmm - startfmm
#################################
'Para filtro de media movil recursivo.'
startfrmm=default_timer()
señal_filtrada3=fmm.fmm(x3,m)
finfrmm=default_timer()
ejecucionfrmm= finfrmm - startfrmm
####################################

print('El tiempo de ejecucion para el filto de media movil fue: ', ejecucionFMM_conv, 'Segundos')
print('El tiempo de ejecucion para el filto Recursivo de media movil fue: ', ejecucionfmm, 'Segundos')
print('El tiempo de ejecucion para el filto Recursivo de media movil fue: ', ejecucionfrmm, 'Segundos')
####################################
'Normalizado de los vectores.'
señal_filtrada= señal_filtrada/ abs(max(señal_filtrada))
señal_filtrada2= señal_filtrada2/ abs(max(señal_filtrada2))
señal_filtrada3= señal_filtrada3/ abs(max(señal_filtrada3))


t2=np.linspace(0,0.5,len(señal_filtrada))


fig, axs = plt.subplots(4)
fig.suptitle('Filtro de media movil')
axs[0].plot(T,x3)
axs[1].plot(t2,señal_filtrada)
axs[2].plot(T,señal_filtrada2)
axs[3].plot(T,señal_filtrada3)
plt.show()