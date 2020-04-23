import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
from matplotlib import pyplot as plt
import scipy as sc
from scipy.fftpack import fft,fftfreq

m = 51
hn = np.repeat(1/m, m)
Hn = np.fft.rfft(hn)


HndB = 20*np.log10(abs(Hn+1))
f = np.fft.rfftfreq(len(hn), 1/m)
print(len(f), len(Hn))

# PLOT

plt.style.use('seaborn')

fig, ax1 = plt.subplots(nrows=1, ncols=1, sharex=True)

ax1.plot(f, abs(Hn), color='r')
# ax2.plot(T, yn1, color='y')
# ax3.plot(T, yn2)

ax1.set_title('Respuesta en Frecuencia')
ax1.set_ylabel('Amplitude')
ax1.set_xlabel('Frecuencia')

# ax2.set_title('FM FIlter')
# ax2.set_ylabel('Amplitude')
#
#
# ax3.set_title('RFMM FIlter')
# ax3.set_ylabel('Amplitude')
# ax3.set_xlabel('Time[s]')


plt.tight_layout()
plt.show()