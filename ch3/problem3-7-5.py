"""Problem 3.7.5 part (a)"""

#%%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def rhs_chain(t, y, v0, vm, km):
    vs = vm * y / (km + y)
    v1, v2, v3 = vs
    return [v0 - v1, v1 - v2, v2 - v3]

v0 = 2
vm = np.array([9, 12, 15])
km = np.array([1, 0.4, 3])
y0 = np.array([0.3, 0.2, 0.1])
sol = solve_ivp(lambda t, y: rhs_chain(t, y, v0, vm, km), (0, 2), y0)

plt.plot(sol.t, sol.y.T, linewidth=3)
plt.legend(('s1', 's2', 's3'))
plt.axis([0, 2, 0, 0.8])
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Concentration (arbitrary units)')