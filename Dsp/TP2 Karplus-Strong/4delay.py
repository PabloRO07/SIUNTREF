import numpy as np
from matplotlib import pyplot as plt 
import sounddevice as sd 
import soundfile as sf 
import noise as ns
import scipy as sc 

#Karplus- Strong
def delay4(signal,d,y):
    l=len(signal) 
    d1= (y/2)*np.hstack((np.zeros(d),signal))  
    d2= (y/4)*np.hstack((np.zeros(2*d),signal))
    d3= (y/8)*np.hstack((np.zeros(3*d),signal))
    d4= (y/16)*np.hstack((np.zeros(4*d),signal))
    l2=len(d4)
    de1=np.hstack((d1,np.zeros(l2-len(d1))))
    de2=np.hstack((d2,np.zeros(l2-len(d2))))
    de3=np.hstack((d3,np.zeros(l2-len(d3))))
    signal=np.hstack((signal,np.zeros((l2-l))))
    synthesis=(signal+de1+de2+de3+d4)
    return synthesis


fs=44100
audio,fs = sf.read('Midi69.wav')
s=0.3
t_ret=round(s*fs)
impulse=np.zeros(44100)
impulse[0]=1

synt = delay4(impulse,t_ret,1)
transfer=sc.fft.fft(synt)
transfer=20*np.log10(abs(transfer))
sf.write('prueba_4echo.wav',synt,fs)


plt.plot(t,synt)
plt.show()
