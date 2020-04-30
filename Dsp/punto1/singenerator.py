import numpy as np 


def singenerator(fs, f, t, a, c):
    """Esta funcion genera una funcion seno con los siguientes parametros
    fs = frecuencia de muestreo
    f = frecuecnia de la señal
    t = tiempo de duracion de la señal
    a = amplitud
    c = Valor medio"""
    t = np.linspace(0, t, int(fs*t))
    xt = 2+np.sin(2*np.pi*f*t)
    return xt, t
