import numpy as np
from matplotlib import pyplot as plt
import scipy as sc
import echo_infinito as ec
import delay4 as dl4
import soundfile as sf
import karplus as ks


circle = plt.Circle((0, 0), 1,)
fig, ax = plt.subplots()
ax.add_artist(circle)
plt.xlim(-2, 2)
plt.ylim(-2, 2)

plt.show()
