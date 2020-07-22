import numpy as np
from matplotlib import pyplot as plt 
import soundfile as sf 
import scipy as sc

# Function Run KSM
f0 = 100
fs0 = 44100
n0 = 1
b0 = 1
bw0 = 0  # So is not filtering
rho0 = 0.5
beta0 = 0.5
impulse=np.zeros(50)
impulse[0]=1
wavetable=impulse
l=len(wavetable)
y=0
# Pick direction Low pass filter  Hf
    
y = 0
acumulador = 0
wavetable_pick = np.zeros(l)
if rho0 != 0:
    for i in range(l):
        wavetable_pick[i] = wavetable[i] - rho0*(wavetable[i]-acumulador)
        acumulador = wavetable_pick[i]
    wavetable = wavetable_pick
# Data Process KSM
karplus0=wavetable
scpectre = sc.fft.fft(karplus0)  # Output FFT
spectre = abs(scpectre)/max(abs(scpectre))  # Frequency response
w=np.linspace(0,np.pi,round(len(spectre)/2))


# PLOT String Section KSM
plt.style.use('seaborn')
fig, ax1 =\
plt.subplots(nrows=1, ncols=1, sharex='col', figsize=(16, 10))

ax1.plot(w,20*np.log10(spectre[0:round(len(spectre)/2)]),color='b', label=r'$ \rho \ = $'+str(rho0))
ax1.set_title(r'$ Pick \ Direction \ Comb \ filter $', fontsize=30)
ax1.set_ylabel(r'$Amplitude  \ [dB]$', fontsize=26)
ax1.set_xlabel(r'$  [rad/Hz]$', fontsize=26)
ax1.legend(loc='upper right', fontsize=20  )
ax1.xaxis.set_tick_params(labelsize=22)
ax1.yaxis.set_tick_params(labelsize=22)
plt.show()
