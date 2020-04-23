import numpy  as np
from matplotlib import pyplot as plt

def blackmanf(x, m):
    a0 = .42
    a1 = .5
    a2 = .08
    n = np.arange(0, m-1)
    p = np.cos((2*np.pi*n)/m-1)
    q = np.cos((4*np.pi*n)/m-1)
    vn = a1 - a0*p + a2*q
    yn = np.convolve(x/abs(max(x)), vn/abs(max(vn)))
    return yn


fs = 44100
f = 10000
t = 0.5
# Vector tiempo
T = np.linspace(0, t, int(fs*t))
# Señal x(t)
xt = 2+np.sin(2*np.pi*f*T)
# Creo la señal del punto 3 para compararla
ruidito3 = np.random.normal(0, 3, len(T))
# sumo el ruido a la señal
x3 = ruidito3+xt

yn = blackmanf(x3, 51)


T1 = np.linspace(0, .5, len(yn))


# PLOT

plt.style.use('seaborn')

fig, ax1 = plt.subplots(nrows=1, ncols=1, sharex=True)

ax1.plot(T1, yn, color='r')
# ax2.plot(T, yn1, color='y')
# ax3.plot(T, yn2)

ax1.set_title('black man Filterl')
ax1.set_ylabel('Amplitude')
ax1.set_xlabel('Time[s]')

# ax2.set_title('FM FIlter')
# ax2.set_ylabel('Amplitude')
#
#
# ax3.set_title('RFMM FIlter')
# ax3.set_ylabel('Amplitude')
# ax3.set_xlabel('Time[s]')


plt.tight_layout()
plt.show()


