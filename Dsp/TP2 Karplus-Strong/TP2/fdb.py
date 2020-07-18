import numpy as np
import soundfile as sf


def fdb(xn, a, d, af, n):
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
            xn = np.hstack((xn, np.zeros(2*d)))
            fdb = xn+ fdb + delay + delay2
            fdb=fdb/abs(max(fdb))
    return fdb
