""" Figure 3.3 Michaelis-Menten kinetics """
#%%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def rhs_full_mm(y, t, et, k1, km1, k2):
    """
    S + E <-> ES complex -> P + E
    """
    v1 = k1 * y[0] * (et - y[1]) - km1 * y[1]
    v2 = k2 * y[1]
    return [-v1, v1 - v2, v2]


def rhs_reduced_mm(y, t, et, k1, km1, k2):
    """
    QSSA of the ES complex
    """
    return - k1 * k2 * et * y / (km1 + k2 + k1 * y)

# Run full model
args = (et, k1, km1, k2) = (1, 30, 1, 10)
y0 = np.array([5, 0, 0])  # S, C, and P
solFull = solve_ivp(lambda t, y: rhs_full_mm(y, t, *args), (0, 1), y0)
t, y = solFull.t, solFull.y

# Plot full model
plt.figure(1)
plt.plot(t, y.T, t, et-y[1])
plt.legend(('s', 'c', 'p', 'e'))
plt.axis([0, 1, 0, 5])
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Concentration (arbitrary units)')

# Run reduced model
y0 = [5]
solReduced = solve_ivp(lambda t, y: rhs_reduced_mm(y, t, *args), (0, 1), y0)
t2, y2 = solReduced.t, solReduced.y
# Plot full and reduced model
plt.figure(2)
plt.plot(t, y[0], 'k', t, y[2], 'k:', t2, y2[0], 'r', t2, 5-y2[0], 'r:', linewidth=3)
plt.axis([0, 1, 0, 5])
plt.legend(('s (full model)', 'p (full model)', 's (reduced model)', 'p (reduced model)'))
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Concentration (arbitrary units)')
