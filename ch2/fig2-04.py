""" Figure 2.4: Exponentially decaying concentration profiles """

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
a1, a2, a3 = np.exp(-t), 2 * np.exp(-t), 3 * np.exp(-t)

plt.plot(t, a1, 'k', label='D=1', linewidth=3)
plt.plot(t, a2, 'k--', label='D=2', linewidth=3)
plt.plot(t, a3, 'k-.', label='D=3', linewidth=3)
plt.axis([0, 5, 0, 3.2])
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend(loc='best')