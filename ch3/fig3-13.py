"""Figure 3.13: Comparions of GMA and Michaelis-Menten rate laws"""
#%%
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4)
plt.plot(t, 2 * t / (1 + t), 'k', linewidth=3, label='Michaelis-Menten')
plt.plot(t, t**0.4, 'k--', linewidth=2, label='GMA')
plt.xlabel('Substrate concentration (arbitrary units)')
plt.ylabel('Reaction rate (arbitrary units)')
plt.legend(loc='best')