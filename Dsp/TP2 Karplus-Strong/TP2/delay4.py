import numpy as np

# Delay 
def delay4(signal,d,y):
    """ Esta función genera una cantidad finita de echos a una señal, tiene 3 variables de entrada y solo una variable de salida.
    signal: señal de entrada
    d: retraso en muestras
    y: amplitud de los delay
    """
    l=len(signal) 
    d1= (y)*np.hstack((np.zeros(d),signal))  
    d2= (y**2)*np.hstack((np.zeros(2*d),signal))
    d3= (y**3)*np.hstack((np.zeros(3*d),signal))
    d4= (y**4)*np.hstack((np.zeros(4*d),signal))
    l2=len(d4)
    de1=np.hstack((d1,np.zeros(l2-len(d1))))
    de2=np.hstack((d2,np.zeros(l2-len(d2))))
    de3=np.hstack((d3,np.zeros(l2-len(d3))))
    signal=np.hstack((signal,np.zeros((l2-l))))
    synthesis=(signal+de1+de2+de3+d4)
    return synthesis


