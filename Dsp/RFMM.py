import numpy as np 
from matplotlib import pyplot as plt 


def fmm(x, M):
    L = len(x)
    y = np.zeros(L)
    N = L-M
    p = round((M-1)/2)
    q = p+1

    for i in range(N):
        if i == 0:
            y[i] = np.sum(x[i:M+i])/M
            print("aca entro")
        else:
            y[i] = y[i-1] + x[i+p] - x[i-q]
        
    return y


fs = 192000
f = 10000
t = 0.5
T = np.linspace(0, t, int(fs*t))    # Vector tiempo
xt = 2+np.sin(2*np.pi*f*T)        # Señal x(t)
ruidito3 = np.random.normal(0, 3, len(T)) # Creo la señal del punto 3 para compararla
x3 = ruidito3+xt / max(ruidito3+xt)
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
