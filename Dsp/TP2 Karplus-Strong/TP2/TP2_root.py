import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 
import delay4 as dl4

#####################################################

#Sistema 1 echos finitos

fs=44100 
d=4 # Retraso en muestras , para gráfico de respuesta en frecuencia y fase.
s= 0.5 # tiempo en segundos , para señal de prueba 
d2=round(s*44100) # retraso para audio de prueba
alfa=(0.5) # amplitud de los echos

audio,fs = sf.read('Midi69.wav') # Audio de prueba
synt = dl4.delay4(audio,d2,alfa) 

sf.write('prueba_4echo.wav',synt,fs) # archivo wav.

### Analisis del sistema ###
impulse=np.zeros(fs-1) # creo vector de ceros para el impulso
impulse[0]=1
synt2 = dl4.delay4(impulse,d,alfa) # respuesta al impulso del sistema
transfer=sc.fft.fft(synt2) #FFT de la respuesta
imag=np.imag(transfer)
real=np.real(transfer)
frecuency_response=abs(transfer) # respuesta en Frecuencia 
phase= np.arctan((imag/real))
t1=np.linspace(0,(len(audio)/fs),len(audio))
t2=np.linspace(0,(len(synt)/fs),len(synt))

plt.style.use('seaborn') # ploteos del sistema 1
fig, ((ax1,ax2 ),(ax3,ax4)) = plt.subplots(nrows=2, ncols=2,sharex='col')
ax1.plot(frecuency_response[0:round(fs/2)], color='b',label=(r'$D=4$'))
ax2.plot(t1,audio, color='black')
ax3.plot(phase[0:round(fs/2)], color='b',label=(r'$D=4$'))
ax4.plot(t2,synt, color='black',label=(r'$ S= 500 ms $'))


ax1.set_title(r'$ |H_1(e^{jw})| \ Sistema 1 $',fontsize=14)
ax1.set_ylabel(r'$Amplitud$',fontsize=14)


ax2.set_title(r'$Señal \ Original \ x[n] $',fontsize=14)
ax2.set_ylabel(r'$Amplitud$',fontsize=14)


ax3.set_title(r'$Fase \ \angle \ H_1(e^{jw}) $',fontsize=14)
ax3.set_ylabel(r'$Amplitud$',fontsize=14)
ax3.set_xlabel(r'$Frecuencia [Hz]$',fontsize=14)


ax4.set_title(r'$Señal \ de \ salida \ y[n]  $',fontsize=14)
ax4.set_ylabel(r'$Amplitud$',fontsize=14)
ax4.set_xlabel(r'$Tiempo [s]$',fontsize=14)


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

########################################################################


#Sistema 2 Feedback delay