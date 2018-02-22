"""Problem 2.4.6"""
#%%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def rhs(t, y, k):
    return k - k*y

y0 = [0]
K = 1
T_END = 10
sol = solve_ivp(lambda t, y: rhs(t, y, K), (0, T_END), y0)
t, y = sol.t, sol.y[0]

plt.plot(t, y, 'k', linewidth=3)
plt.xlabel('Time (arbitrary units)')