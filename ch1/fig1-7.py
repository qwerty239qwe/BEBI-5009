"""
model of Collins toggle switch
from Gardiner et al. (2000) Nature 403, pp. 339-342
Figures 1.7, 7.13, 7.14, 7.15
"""

#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


"""Collins toggle switch function"""
def collin_toggleswitch_rhs(y, t, A1, A2, BETA, GAMMA, inducers):
    i1, i2 = inducers(t)
    dp1 = A1 / (1 + (y[1] / (1 + i2))**BETA) - y[0]
    dp2 = A2 / (1 + (y[0] / (1 + i1))**BETA) - y[1]
    return [dp1, dp2]


def get_inducers(t):
    if t < 10:
        return (0, 0)
    elif t < 20:
        return (0, 10)
    elif t < 30:
        return (0, 0)
    elif t < 40:
        return (10, 0)
    else:
        return (0, 0)


"""Initial conditions and parameters"""
N_POINTS = 500
T_START, T_END = 0, 50
y0 = np.array([0.075, 2.5])
t = np.linspace(0, T_END, N_POINTS)
A1, A2, BETA, GAMMA = 3, 2.5, 4, 4

args = (A1, A2, BETA, GAMMA, get_inducers)
solution = odeint(collin_toggleswitch_rhs, y0, t, args)

"""Plot the results"""
plt.plot(t, solution[:, 0], "b-", label="Protein 1", linewidth=3)
plt.plot(t, solution[:, 1], "r--", label="Protein 2", linewidth=3)
plt.axis([T_START, T_END, 0, 3.5])
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend(loc='best')
plt.show()