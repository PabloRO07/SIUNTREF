import numpy as np
from matplotlib import pyplot as plt
# RCE
x = [0, 8, 24]
y = [3.07, 2.05, 0]
# RCD 10k
x1 = [0, 8, 13.72]
y1 = [4.9, 2.05, 0]
# RCD inf
x2 = [0, 8, 15.99]
y2 = [4.1, 2.05, 0]
# RCD 1k
x3 = [0, 8, 9.63]
y3 = [12.11, 2.05, 0]
# Plot
plt.style.use('seaborn')

plt.plot(x, y, color='blue', label=r'$RCE$', marker='o', linestyle='-.')
plt.plot(x1, y1, color='orange', label=r'$RCD \ R_{L} \rightarrow \ 10k\Omega$', marker='o', linestyle=':')
plt.plot(x2, y2, color='red', label=r'$RCD \ R_{L} \rightarrow \ \infty \Omega$', marker='o', linestyle='-')
plt.plot(x3, y3, color='c', label=r'$RCD \ R_{L} \rightarrow \ 1k\Omega$', marker='o', linestyle='--')
plt.xticks(np.arange(25))
plt.yticks(np.arange(13))

plt.title(r'$Rectas \ de \ carga \ Dinámica \ y \ Estática$')
plt.xlabel(r'$V_{CEQ}[V]$', fontsize=12)
plt.ylabel(r'$I_{CQ}[mA]$', fontsize=12)
plt.xlim([-0.1, 24.1])
plt.ylim([-0.1, 13])
plt.legend()

plt.savefig('d.png')

plt.tight_layout()
plt.grid(True)
plt.legend()
plt.show()

