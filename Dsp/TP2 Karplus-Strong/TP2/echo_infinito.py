import numpy as np


def echo_infinito(xn, a, d, c):
    """
    :param xn: Entry Signal
    :param a: Echoes Amplitude
    :param d: Delay time in samples
    :param c: Stop condition, Amplitude of delays
    :return: Entry signal with dealy until the echoes amplitude is under "c"
    """
    b = 1
    xn2 = xn
    while b > c:
        delay = a*np.hstack((np.zeros(d), xn))
        xn2 = np.hstack((xn2, np.zeros(d)))
        xn2 = xn2+delay
        xn = delay
        b = abs(max(delay))
    
    return xn2
