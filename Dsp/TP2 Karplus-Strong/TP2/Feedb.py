import numpy as np
import soundfile as sf


def fdb(xn, a, d, af, n, fs):
    """Entry Parameters
    This function recive a entry signal and creates "n" feedbacks
    xn = Signal Entry
    a = Amplitude delayed signal
    d = Delay time
    af = Amplitude feedback signal
    n = Quantity of feedbacks
    """
    l = len(xn)
    for i in range(n):
        if i == 0:
            delay = a*(np.hstack((np.zeros(d), xn)))
            delay2 = af * (np.hstack((np.zeros(d), delay)))
            delay = np.hstack((delay, np.zeros(d)))
            xn = np.hstack((xn, np.zeros(2*d)))
            fdb = xn+delay+delay2
        else:
            delay = a*(np.hstack((np.zeros(d), fdb)))
            delay2 = af*(np.hstack((np.zeros(d), delay)))
            delay = np.hstack((delay, np.zeros(d)))
            fdb = np.hstack((fdb, np.zeros(2*d)))
            fdb = fdb + delay + delay2
    return fdb


fs = 44100
xn, fs = sf.read('Midi69.wav')
'cantidad de repeticiones'
n = 1
'Muestas atrazadas'
d = round(4 * fs)
'Amplitud de los delays'
a = 0.5
'Amplitud de la realimentacion'
af = 0.5
synth = fdb(xn, a, d, af, n, fs)
sf.write('echo.wav', synth, fs)