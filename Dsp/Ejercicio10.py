import numpy as np 
import scipy as sc 
from matplotlib import pyplot as plt 
from punto6 import fmmconv as fmmconv
from punto7 import blackman as bm

#creo vector impulso 
fs=44100
impulse=np.zeros(fs-1)
impulse[0]=1

#filtrado del impulso
ir_rw=fmmconv.fmmconv(impulse,1000)
ir_blackman=bm.blackman(impulse,1000)

ir_rw_response=20*np.log10(abs(sc.fft.fft(ir_rw))/abs(max(abs(sc.fft.fft(ir_rw)))))
ir_bkw_response=20*np.log10(abs(sc.fft.fft(ir_blackman))/abs(max(abs(sc.fft.fft(ir_blackman)))))
w=np.linspace(0,np.pi,22050)


# Plot
plt.style.use('seaborn')

fig,ax1 = plt.subplots(nrows=1, ncols=1, sharex=True)
plt.plot(w,ir_bkw_response[0:round(fs/2)], color='black',label=(r'$|H_b(jw)|$'))
plt.plot(w,ir_rw_response[0:round(fs/2)] ,color='b',label=(r'$|H_r(jw)|$'))

ax1.set_title(r'$|H(jw)| \ Blackman \ y \ rectangular $',fontsize=16)
ax1.set_ylabel(r'$Amplitud \ [dB]$',fontsize=14)
ax1.set_xlabel(r'$ \frac{rad}{Hz}$',fontsize=16)

plt.legend(fontsize=14)
plt.tight_layout()
plt.show()