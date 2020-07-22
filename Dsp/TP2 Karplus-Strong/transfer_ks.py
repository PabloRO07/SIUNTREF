import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
import scipy as sc

a = 0
v_anterior = 0
fs = 10000
f = 100
n = 44100
karplus = np.zeros(n)
p = fs // f
impulse = np.zeros(p)  # Set zero vector for impulse
impulse[0] = 1
wavetable = impulse

for i in range(n):
    wavetable[a] = 0.5 * (wavetable[a] + v_anterior)
    karplus[i] = wavetable[a]
    v_anterior = karplus[i]
    a += 1
    a = a % len(wavetable)
# Para segunda señal en plot
a1 = 0
v_anterior1 = 0
fs1 = 10000
f1 = 100
n1 = 44100
karplus1 = np.zeros(n1)
p1 = fs1 // f1
impulse1 = np.zeros(p1)  # Set zero vector for impulse
impulse1[0] = 1
wavetable1 = impulse1
for i in range(n1):
    wavetable1[a1] = 0.5 * (wavetable1[a1] + v_anterior1)
    karplus1[i] = wavetable1[a1]
    v_anterior1 = karplus1[i]
    a1 += 1
    a1 = a1 % len(wavetable1)
# # Para tercera señal en plot
# a2 = 0
# v_anterior2 = 0
# fs2 = 10000
# f2 = 100
# n2 = 44100
# karplus2 = np.zeros(n2)
# p2 = fs2 // f2
# impulse2 = np.zeros(p2)  # Set zero vector for impulse
# impulse2[0] = 1
# wavetable2 = impulse2
# for i in range(n2):
#     wavetable2[a2] = 0.5 * (wavetable2[a2] + v_anterior2)
#     karplus2[i] = wavetable2[a1]
#     v_anterior2 = karplus2[i]
#     a2 += 1
#     a2 = a2 % len(wavetable2)
# # Para 4 señal en plot
# a3 = 0
# v_anterior3 = 0
# fs3 = 10000
# f3 = 100
# n3 = 44100
# karplus3 = np.zeros(n3)
# p3 = fs3 // f3
# impulse3 = np.zeros(p3)  # Set zero vector for impulse
# impulse3[0] = 1
# wavetable3 = impulse3
# for i in range(n3):
#     wavetable3[a3] = 0.5 * (wavetable3[a3] + v_anterior3)
#     karplus3[i] = wavetable3[a1]
#     v_anterior3 = karplus3[i]
#     a3 += 1
#     a3 = a3 % len(wavetable3)
# Primera señal
transfer = abs(sc.fft.fft(karplus))
transfer = transfer / abs(max(transfer))
w = np.linspace(0, (fs / 2), round(len(transfer) / 2))
real = np.real(sc.fft.fft(karplus))
imag = np.imag(sc.fft.fft(karplus))
phase = np.arctan((imag / real))
sf.write('karplus_hn.wav', karplus, fs)
# Segunda Señal
transfer1 = abs(sc.fft.fft(karplus1))
transfer1 = transfer1 / abs(max(transfer1))
w1 = np.linspace(0, (fs1 / 2), round(len(transfer1) / 2))
real1 = np.real(sc.fft.fft(karplus1))
imag1 = np.imag(sc.fft.fft(karplus1))
phase1 = np.arctan((imag1 / real1))
sf.write('karplus1_hn.wav', karplus1, fs1)
# # Tercera Señal
# transfer2 = abs(sc.fft.fft(karplus2))
# transfer2 = transfer2/abs(max(transfer2))
# w2 = np.linspace(0, (fs2/2), round(len(transfer2)/2))
# real2 = np.real(sc.fft.fft(karplus2))
# imag2 = np.imag(sc.fft.fft(karplus2))
# phase2 = np.arctan((imag2/real2))
# sf.write('karplus1_hn.wav', karplus2, fs2)
# # 4 Señal
# transfer3 = abs(sc.fft.fft(karplus3))
# transfer3 = transfer3/abs(max(transfer3))
# w3 = np.linspace(0, (fs3/2), round(len(transfer3)/2))
# real3 = np.real(sc.fft.fft(karplus3))
# imag3 = np.imag(sc.fft.fft(karplus3))
# phase3 = np.arctan((imag3/real3))
# sf.write('karplus1_hn.wav', karplus3, fs3)

# PLOT Frequency response karplus strong system
plt.style.use('seaborn')
fig, (ax1, ax2) = \
    plt.subplots(nrows=2, ncols=1, figsize=(16, 10))
fig.suptitle(r'$ Transfer \ Function \ |H_3(e^{jw})| $', fontsize=18, y=0.991)

ax1.plot(w, 20 * np.log10(transfer[0:round(n / 2)]), color='b',
         label='Fs = ' + str(int(fs / 1000)) + ' K hz' + ',' + 'f =' + str(f))
ax1.plot(w1, 20 * np.log10(transfer1[0:round(n1 / 2)]), color='orange',
         label='Fs = ' + str(int(fs1 / 1000)) + ' K hz' + ',' + 'f =' + str(f1))
# ax1.plot(w2, 20*np.log10(transfer2[0:round(n2/2)]), color='g',
#          label='Fs = '+str(int(fs2/1000))+' K hz'+','+'f ='+str(f2))
# ax1.plot(w3, 20*np.log10(transfer3[0:round(n3/2)]), color='r',
#          label='Fs = '+str(int(fs3/1000))+' K hz'+','+'f ='+str(f3))
ax2.plot(w, phase[0:round(n / 2)], color='b')

ax1.set_title(r'$ |H_3(e^{jw})| $', fontsize=14, y=0.999, x=0.025)
ax1.set_ylabel(r'$Amplitude$', fontsize=14)
ax1.set_xlabel(r'$Frequency [Hz]$', fontsize=14)

ax2.set_title(r'$Phase \ x[n] $', fontsize=14, y=0.999, x=0.035)
ax2.set_ylabel(r'$Amplitude\ [rad]$', fontsize=14)
ax2.set_xlabel(r'$Frequency [Hz]$', fontsize=14)

plt.legend(fontsize=12)
plt.savefig('sistema3_1d_1alfa.png')
plt.tight_layout()

plt.show()
