import soundfile as sf
import numpy as np
from matplotlib import pyplot as plt

xn, fs1 = sf.read('IRS.wav')

hn, fs2 = sf.read('Srt.wav')
if fs1 == fs2:
    q = xn.shape
    w = hn.shape

    if q[1] & w[1] == 2:
        # Separacion de Canalaes
        xnL = xn[:, 0]
        xnR = xn[:, 1]
        hnL = hn[:, 0]
        hnR = hn[:, 1]
        # Convolucion
        yL = np.convolve(xnL, hnL)
        yR = np.convolve(xnL, hnL)
        yn = np.array([yL], [yR])
        sf.write('Ysalida.wav', yn, fs1)

    else:
        if q[1] & w[1] == []:
            yn = np.convolve(xn, hn)
        else:
            print('Estas intentando convolucionar un audio Stereo con uno Mono, lavate el orto')
else:
    print('Los audios no tienen la misma frecuencia de muestreo')
    