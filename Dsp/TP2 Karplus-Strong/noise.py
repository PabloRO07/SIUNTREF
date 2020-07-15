import numpy as np
from matplotlib import pyplot as plt 
import sounddevice as sd 
import soundfile as sf 

#Noise
def noise(amplitud,time):
    fs = 44100
    t=np.linspace(0,time,round(time*fs))
    rng = np.random.default_rng()  # generador de ruido
    ns= rng.normal(0, amplitud, len(t))
    return(ns)



