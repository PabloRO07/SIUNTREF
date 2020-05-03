import numpy as np 
from matplotlib import pyplot as plt
from punto1 import desvio_str as ds

"Generacion de los ruidos aleatorios con varianza 1"

ruidito5 = np.random.normal(0, 1, 5)
ruidito10 = np.random.normal(0, 1, 10)
ruidito100 = np.random.normal(0, 1, 100)
ruidito1k = np.random.normal(0, 1, 1000)
ruidito10k = np.random.normal(0, 1, 10000)
ruidito100k = np.random.normal(0, 1, 100000)

"Calculo del Desvio Estandar para cada uno delos ruidos generados"
desvio5 = ds.desvio_str(ruidito5)[0]
desvio10 = ds.desvio_str(ruidito10)[0]
desvio100 = ds.desvio_str(ruidito100)[0]
desvio1k = ds.desvio_str(ruidito1k)[0]
desvio10k = ds.desvio_str(ruidito10k)[0]
desvio100k = ds.desvio_str(ruidito100k)[0]

"Vector con lso devios"
des = np.array([desvio5, desvio10, desvio100, desvio1k, desvio10k, desvio100k])

desv = abs(1-des)
desv = (desv/des)*100

t = [des, desv]

# "Creacion de Tabla"
# fig, ax = plt.subplots()
# # hide axes
# fig.patch.set_visible(False)
# ax.axis('off')
# ax.axis('tight')
#
# colLabels = ("Varianza", "%")
# rowLabels = ("5", "10", "100", "1k", "10k", "100k")
# data = t
#
# ax.table(cellText=data, colLabels=colLabels, loc='center', rowLabels=rowLabels)
# fig.tight_layout()
# plt.show()
