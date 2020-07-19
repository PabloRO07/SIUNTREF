import numpy as np
from matplotlib import pyplot as plt
import scipy as sc
import echo_infinito as ec
import delay4 as dl4
import soundfile as sf
import karplus as ks


f = 50
fs = 44100
n = 1
b = 1
c = 0.5
ks_0 = ks.karplus(f, fs, n, b, c)
transfer = abs(sc.fft.fft(ks_0))
transfer = transfer / abs(max(transfer))
w = np.linspace(0, (fs / 2), round(len(transfer) / 2))
# sf.write('pruebapolC=1.wav', ks_0, fs)
c = 1
ks_1 = ks.karplus(f, fs, n, b, c)
transfer1 = abs(sc.fft.fft(ks_1))
transfer1 = transfer / abs(max(transfer1))

# d = 100
# audio, fs = sf.read('Midi69.wav')  # Test Audio
# delay = np.zeros(len(audio+d))
# out = audio
# for i in range(2):
#     print(i)
#     delay = 0.8995*0.1087*np.hstack((np.zeros(d), out))
#     audio = np.hstack((audio, np.zeros(len(delay)-len(audio))))
#     delay = audio + delay
#     out = -0.0136*np.hstack((np.zeros(d), delay)) + np.hstack((delay, np.zeros(d)))
#     # out2 = 0.0136*np.hstack((np.zeros(d), delay)) + np.hstack((delay, np.zeros(d)))
#
#
# transfer = sc.fft.fft(out)
# # transfer2 = sc.fft.fft(out2)
# frequency_response = abs(transfer)
# # frequency_response2 = abs(transfer2)
#
plt.style.use('seaborn')
fig, ((ax1, ax2), (ax3, ax4)) = \
    plt.subplots(nrows=2, ncols=2, sharex='col', figsize=(16, 10))
fig.suptitle(r'$ System\ 1\ Analysis\ 1\ Finite\ Echoes  $',
             fontsize=18)
ax1.plot(frequency_response[0:round(fs/2)],
         color='b', label=r'$D=4$')
# ax2.plot(frequency_response2[0:round(fs/2)],
#          color='black')
# ax3.plot(phase[0:round(fs/2)],
#          color='b', label=r'$D=4$')
# ax4.plot(t2, synt,
#          color='black', label=r'$ S= 500 ms $')


ax1.set_title(r'$ |H_1(e^{jw})| $', fontsize=14)
ax1.set_ylabel(r'$Amplitude$', fontsize=14)
ax1.legend(loc='best')

ax2.set_title(r'$Original \ Signal \ x[n] $', fontsize=14)
ax2.set_ylabel(r'$Amplitude$', fontsize=14)
ax2.legend(loc='best')

# ax3.set_title(r'$Fase \ \angle \ H_1(e^{jw}) $', fontsize=14)
# ax3.set_ylabel(r'$Amplitude$', fontsize=14)
# ax3.set_xlabel(r'$Frequency [Hz]$', fontsize=14)
# ax3.legend(loc='best')
#
# ax4.set_title(r'$Ouput \ Signal \ y_1[n]  $', fontsize=14)
# ax4.set_ylabel(r'$Amplitude$', fontsize=14)
# ax4.set_xlabel(r'$Time [s]$', fontsize=14)
# ax4.legend(loc='best')

plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

