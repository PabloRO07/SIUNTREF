import numpy as np
from matplotlib import pyplot as plt
import RFMM as RMM
import FMM as FM

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

m = 0.01*t*fs
n = fs*t
m = int(m)
hn = (1/(m+1))*np.ones(m)

print(len(hn))
print(len(x3))


yn = np.convolve(hn, x3)
print(len(yn))
T1 = np.linspace(0, .5, len(yn))

yn1 = FM.FMM(x3, m)
yn2 = RMM.RFMM(x3, m)

# PLOT

plt.style.use('seaborn')

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)

ax1.plot(T1, yn, color='r')
ax2.plot(T, yn1, color='y')
ax3.plot(T, yn2)

ax1.set_title('Convolution FIlterl')
ax1.set_ylabel('Amplitude')

ax2.set_title('FM FIlter')
ax2.set_ylabel('Amplitude')


ax3.set_title('RFMM FIlter')
ax3.set_ylabel('Amplitude')
ax3.set_xlabel('Time[s]')


plt.tight_layout()
plt.show()
