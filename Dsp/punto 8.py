import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
from matplotlib import pyplot as plt
import scipy as sc


xn, fs = sf.read('Midi69.wav')
hn, fs = sf.read('RIR.wav')


ync =
ynl = np.convolve(xn, hn)
T = np.linspace(0, len(ynl)/fs, len(ynl))

# PLOT

plt.style.use('seaborn')

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)

ax1.plot(T, ynl, color='r')
# ax2.plot(T, yn1, color='y')
# ax3.plot(T, yn2)

ax1.set_title('Convolution Lineal')
ax1.set_ylabel('Amplitude')
ax1.set_xlabel('Time[s]')

# ax2.set_title('FM FIlter')
# ax2.set_ylabel('Amplitude')
#
#
# ax3.set_title('RFMM FIlter')
# ax3.set_ylabel('Amplitude')
# ax3.set_xlabel('Time[s]')


plt.tight_layout()
plt.show()
