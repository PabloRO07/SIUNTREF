import numpy as np 
from matplotlib import pyplot as plt 


def fmm(x, m):
    """Return a filtered signal with a FMM

    Parameters:
    x : entry signal
    m : window

    """
    L = len(x)
    y = np.zeros(L)
    N = L-m
    p = round((m-1)/2)
    q = p+1

    for i in range(N):
        if i == 0:
            y[i] = np.sum(x[i:m+i])/m
        else:
            y[i] = y[i-1] + x[i+p] - x[i-q]
        
    return y


fs = 192000
f = 10000
t = 0.5
# Vector tiempo
T = np.linspace(0, t, int(fs*t))
# Señal x(t)
xt = 2+np.sin(2*np.pi*f*T)
# Creo la señal del punto 3 para compararla
ruidito3 = np.random.normal(0, 3, len(T))
# Normalizo y sumo el ruido a la señal
x3 = ruidito3+xt / max(ruidito3+xt)
# Aplico el filtro
salida = fmm(x3, 51)


# PLOT

plt.style.use('seaborn')

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(T, x3, label='Sin Filtro de Media Movil', color='r')
ax2.plot(T, salida, label='Con Filtro de Media Movil')

ax1.set_title('Sin Filtro de Media Movil')
ax1.set_ylabel('Amplitude')


ax2.set_title('Con Filtro de Media Movil')
ax2.set_ylabel('Amplitude')
ax2.set_xlabel('Time[s]')

plt.tight_layout()
plt.show()
