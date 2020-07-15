import numpy as np
from matplotlib import pyplot as plt 
import sounddevice as sd 
import soundfile as sf 
import noise as ns

#Karplus- Strong
def Karplus(signal,d,y):
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

def Karplus_fb(signal,d,y,N):
    l=len(signal) 
    d1= np.hstack((np.zeros(d),signal))
    l2=len(d1)
    signal=np.hstack((signal,np.zeros((l2-l))))
    echo=(y/2)*d1
    synthesis2=np.zeros(len(echo))
    for i in range(N): 
        synthesis2=(1/(i*0.5+1))*echo+synthesis2
        echo=np.hstack((np.zeros(round((d*i)/(1+0.1*i)),synthesis2)))
        l3=len(echo)
        signal=np.hstack((signal,np.zeros((l3-len(signal)))))
        synthesis2=np.hstack((synthesis2,np.zeros((l3-len(synthesis2)))))
        l2=len(synthesis2)
    
    
    return synthesis2

fs=44100
noise = ns.noise(1,1)
audio,fs = sf.read('Midi69.wav')
s=0.5
t_ret=round(s*fs)
synt = Karplus(audio,t_ret,1)
synt2 = Karplus_fb(audio,t_ret,1,50)
sf.write('prueba_4echo.wav',synt,fs)
sf.write('prueba_fecho.wav',synt2,fs)
t=np.linspace(0,(len(synt)/fs),len(synt))
t2=np.linspace(0,(len(synt2)/fs),len(synt2))
t3=np.linspace(0,(len(audio)/fs),len(audio))
plt.plot(t,synt)
plt.show()
plt.plot(t2,synt2)

plt.show()
plt.plot(t3,audio)
plt.show()