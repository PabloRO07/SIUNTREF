import numpy as np 
from matplotlib import pyplot as plt 
from punto1 import singenerator as sg
from punto5 import fmm as fmm
from punto5 import frmm as frmm
from timeit import default_timer
from Ejercicio6 import FMM_conv
def black_w(xt,m):
    a0 = 0.42
    a1 = 0.5
    a2 = 0.08
    kernel=np.zeros(m)
    
    i=np.arange(m-1)
    kernel = a0 - a1*np.cos((2*np.pi*i)/(m-1))+a2*np.cos((4*np.pi*i)/(m-1))
    y=np.convolve(xt,kernel)
    return(y)


# Definimos xt como la señal de entrada
[xt, t] = sg.singenerator(44100, 10000, 0.5, 1, 2)

ruidito3 = np.random.normal(0,3,len(t)) #Creo la señal del punto 3 para compararla
x3= (ruidito3+xt)
m=round(0.01*len(x3)) # ventana del 1%




# Aplicamos los filtros y medimos los timepos
'Para filtro de media movil por convolución'
startFMM_conv = default_timer()
señal_filtrada=FMM_conv(x3,m)
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
'Para filtro de media movil con ventana Blackman .'
startblack=default_timer()
señal_filtrada4=black_w(x3,m) 
finblack=default_timer()
ejecucionblack = finblack - startblack

print('El tiempo de ejecucion para el filtro de media movil por convolución fue: ', ejecucionFMM_conv, 'Segundos')
print('El tiempo de ejecucion para el filtro de media movil fue: ', ejecucionfmm, 'Segundos')
print('El tiempo de ejecucion para el filtro Recursivo de media movil fue: ', ejecucionfrmm, 'Segundos')
print('El tiempo de ejecucion para el filtro Recursivo de media movil con ventana blackman fue: ', ejecucionblack, 'Segundos')
####################################
'Normalizado de los vectores.'
señal_filtrada= señal_filtrada/ abs(max(señal_filtrada))
señal_filtrada2= señal_filtrada2/ abs(max(señal_filtrada2))
señal_filtrada3= señal_filtrada3/ abs(max(señal_filtrada3))
señal_filtrada4= señal_filtrada4/ abs(max(señal_filtrada4))

#####################
'Vectores tiempo para el plot'
muestras_tfmm=(len(señal_filtrada2))
muestras_tfrmm=(len(señal_filtrada3))
muestras_tconv=len(x3)+m-1
muestras_tblack=len(señal_filtrada4)
t_conv=np.linspace(0,0.5,muestras_tconv)
tfmm=np.linspace(0,0.5,muestras_tfmm)
tfrmm=np.linspace(0,0.5,muestras_tfrmm)
tblack=np.linspace(0,0.5,muestras_tblack)
# Plot
plt.style.use('seaborn')

fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, sharex=True)
ax1.plot(t_conv ,señal_filtrada, color='r')
ax2.plot(tfmm, señal_filtrada2, color='y')
ax3.plot(tfrmm, señal_filtrada3)
ax4.plot(tblack, señal_filtrada4, color='g')

ax1.set_title('Filtrado por convolución')
ax1.set_ylabel('Amplitud')
ax1.set_xlabel('Time[s]')

ax2.set_title('Filtada con filtro de media movil recursivo')
ax2.set_ylabel('Amplitud')

ax3.set_title('Filtro de media movil')
ax3.set_xlabel('Time[s]')
ax3.set_ylabel('Amplitud')

ax4.set_title('Filtro de media movil con ventana blackman')
ax4.set_xlabel('Time[s]')
ax4.set_ylabel('Amplitud')

plt.tight_layout()
plt.show()

