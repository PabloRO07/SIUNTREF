import numpy as np


def echo_infinito(xn,a,d,c):
    b=1
    xn2=xn
    while (b>c):
        delay=(a)*np.hstack((np.zeros(d),xn))
        xn2=np.hstack((xn2,np.zeros(d)))
        xn2=xn2+delay
        xn=delay
        b=abs(max(delay))
    
    return(xn2)
