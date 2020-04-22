import numpy as np
import FMM
import fmm

fs = 44100
f = 10000
t = 0.5
# Vector tiempo
T = np.linspace(0, t, int(fs*t))
# Señal x(t)
xt = 2+np.sin(2*np.pi*f*T)
# Creo la señal del punto 3 para compararla
ruidito3 = np.random.normal(0, 3, len(T))
# sumo el ruido a la señal
x3 = ruidito3+xt
# Aplico el filtro

salida1 = fmm(x3, 51)
salida2 = FMM(x3, 51)


# PLOT

plt.style.use('seaborn')

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(T, salida2, color='r')
ax2.plot(T, salida1)

ax1.set_title('Recurisvo')
ax1.set_ylabel('Amplitude')


ax2.set_title('No recursivo')
ax2.set_ylabel('Amplitude')
ax2.set_xlabel('Time[s]')

plt.tight_layout()
plt.show()