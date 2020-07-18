import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc 
import delay4 as dl4
import echo_infinito as ec
import ks as ks

# Este es el Scrypt raiz de los 4 sistemas propuestos por el trabajo.

# Sistema 1 echos finitos

fs = 44100
d = 4  # Retraso en muestras , para gráfico de respuesta en frecuencia y fase.
s = 0.5  # tiempo en segundos , para señal de prueba
d2 = round(s*44100)  # retraso para audio de prueba
alfa = 0.5  # amplitud de los echos

audio, fs = sf.read('Midi69.wav')  # Audio de prueba
synt = dl4.delay4(audio, d2, alfa)

sf.write('Sistema_1.wav', synt, fs)  # archivo wav.

# Analisis del sistema #
impulse = np.zeros(fs-1)  # creo vector de ceros para el impulso
impulse[0] = 1
synt2 = dl4.delay4(impulse, d, alfa)  # respuesta al impulso del sistema
transfer = sc.fft.fft(synt2)  # FFT de la respuesta
imag = np.imag(transfer)
real = np.real(transfer)
frecuency_response = abs(transfer)  # respuesta en Frecuencia
phase = np.arctan((imag/real))
t1 = np.linspace(0, (len(audio)/fs), len(audio)) # Vector tiempo x[n]
t2 = np.linspace(0, (len(synt)/fs), len(synt))  # Vector tiempo para señal Y2[n]

plt.style.use('seaborn')  # ploteos del sistema 1
fig, ((ax1, ax2), (ax3, ax4)) = \
    plt.subplots(nrows=2, ncols=2, sharex='col', figsize=(16, 10))
fig.suptitle(r'$ Analisis \ del \ sistema \ 1 \ ecos \ finito $',
             fontsize=18, fontname="Times New Roman Bold")
ax1.plot(frecuency_response[0:round(fs/2)],
         color='b', label=r'$D=4$')
ax2.plot(t1, audio,
         color='black')
ax3.plot(phase[0:round(fs/2)],
         color='b', label=r'$D=4$')
ax4.plot(t2, synt,
         color='black', label=r'$ S= 500 ms $')


ax1.set_title(r'$ |H_1(e^{jw})| $', fontsize=14)
ax1.set_ylabel(r'$Amplitud$', fontsize=14)


ax2.set_title(r'$Señal \ Original \ x[n] $', fontsize=14)
ax2.set_ylabel(r'$Amplitud$', fontsize=14)


ax3.set_title(r'$Fase \ \angle \ H_1(e^{jw}) $', fontsize=14)
ax3.set_ylabel(r'$Amplitud$', fontsize=14)
ax3.set_xlabel(r'$Frecuencia [Hz]$', fontsize=14)


ax4.set_title(r'$Señal \ de \ salida \ y_1[n]  $', fontsize=14)
ax4.set_ylabel(r'$Amplitud$', fontsize=14)
ax4.set_xlabel(r'$Tiempo [s]$', fontsize=14)


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()


# Sistema 2 Feedback delay
fs = 44100
d = 4  # Retraso en muestras , para gráfico de respuesta en frecuencia y fase.
s = 0.5  # tiempo en segundos , para señal de prueba
d2 = round(s*44100) # retraso para audio de prueba
alfa = (0.5)  # amplitud de los echos
c=0.01
synth = ec.echo_infinito(audio,alfa,d2,c)

sf.write('Sistema_2.wav', synth, fs)


# Analisis del sistema 2 #
impulse = np.zeros(fs-1)  # creo vector de ceros para el impulso
impulse[0] = 1
synth2 = ec.echo_infinito(impulse,alfa,d,c)  # respuesta al impulso del sistema
transfer2 = sc.fft.fft(synth2)  # FFT de la respuesta
imag2 = np.imag(transfer2)
real2 = np.real(transfer2)
frecuency_response2 = abs(transfer2)  # respuesta en Frecuencia del sistema 2
phase2 = np.arctan((imag2/real2))  # Respuesta de fase del sistema 2
t1 = np.linspace(0, (len(audio)/fs), len(audio))  # Vector tiempo x[n]
t2 = np.linspace(0, (len(synth)/fs), len(synth))  # Vector tiempo para señal Y2[n]

plt.style.use('seaborn')  # ploteos del sistema 2
fig, ((ax1, ax2), (ax3, ax4)) =\
    plt.subplots(nrows=2, ncols=2, sharex='col')
fig.suptitle(r'$ Analisis \ del \ sistema \ 2 \ Feedback \ delay $', fontsize=18)
ax1.plot(frecuency_response2[0:round(fs/2)], color='b', label=(r'$D=4$'))
ax2.plot(t1, audio, color='black')
ax3.plot(phase2[0:round(fs/2)], color='b', label=r'$D=4$')
ax4.plot(t2, synth, color='black', label=r'$ S= 500 ms $')


ax1.set_title(r'$ |H_2(e^{jw})| $', fontsize=14)
ax1.set_ylabel(r'$Amplitud$', fontsize=14)


ax2.set_title(r'$Señal \ Original \ x[n] $', fontsize=14)
ax2.set_ylabel(r'$Amplitud$', fontsize=14)


ax3.set_title(r'$Fase \ \angle \ H_2(e^{jw}) $',fontsize=14)
ax3.set_ylabel(r'$Amplitud$', fontsize=14)
ax3.set_xlabel(r'$Frecuencia [Hz]$', fontsize=14)


ax4.set_title(r'$Señal \ de \ salida \ y_2[n] \ Normalizada  $', fontsize=14)
ax4.set_ylabel(r'$Amplitud$', fontsize=14)
ax4.set_xlabel(r'$Tiempo [s]$', fontsize=14)


plt.legend(fontsize=12)
plt.tight_layout()
plt.show()


# Analisis del sistema 3 #
fs = 8000
f = 50
ks = ks.ks(f, fs, 3, 1)
transfer = sc.fft.fft(ks)
transfer = abs(transfer)
transfer = transfer/abs(max(transfer))
w = np.linspace(0, (fs/2), round(len(transfer)/2))
plt.plot(w, transfer[0:round((fs*3)/2)])
plt.show()
sf.write('Sistema_5.wav', ks, fs)
