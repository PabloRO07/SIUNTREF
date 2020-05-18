import numpy as np 
from matplotlib import pyplot as plt 
import soundfile as sf 

[midi69,fs]=sf.read("midi69.wav")
[RIR,fs]=sf.read("RIR.wav")
conv_lineal=np.convolve(midi69,RIR)
L=len(midi69)
M=len(RIR)
midi69_1=np.append(midi69,np.zeros(M))

conv_circular=np.convolve(midi69_1,RIR,'same')
if len(midi69_1)==len(conv_circular):
    print("yeah")

fig, axs =plt.subplots(3)
axs[0].plot(midi69_1)
axs[1].plot(conv_circular)
axs[2].plot(conv_lineal)
plt.show()
