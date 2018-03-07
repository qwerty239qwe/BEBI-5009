"""
Model of asymmetric network from Figure 4.1. This code generates phase plane in Figures 4.2, 4.3, 4.4A, 4.5 and 
continuation diagram in Figure 4.18
"""


#%%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def rhs(t, y, k1, k2, k3, k4, k5, n):
    s1, s2 = y
    v1 = k1 / (1 + s2**n)
    v2 = k2
    v3 = k3 * s1
    v4 = k4 * s2
    v5 = k5 * s1
    return [v1 - v3 - v5, v2 + v5 - v4]


T_START, T_END = 0, 1.5
t = np.linspace(T_START, T_END, 100)
k1, k2, k3, k4, k5, n = 20, 5, 5, 5, 2, 4 
y0s = [[0, 0], [0.5, 0.6], [0.17, 1.1], [0.25, 1.9], [1.85, 1.7]]
sols = [solve_ivp(lambda t, y: rhs(t, y, k1, k2, k3, k4, k5, n),
            (T_START, T_END), y0, t_eval=t, rtol=1e-6, atol=1e-6)
            for y0 in y0s ]

# Fig. 4.2A
plt.figure()
t1, s1 = sols[0].t, sols[0].y.T
plt.plot(t1, s1, linewidth=3)
plt.legend(('S1', 'S2'))
plt.xlabel('Time')
plt.ylabel('Concentration')

# Fig. 4.2B
plt.figure()
plt.plot(s1[:,0], s1[:,1], 'k', linewidth=3)
plt.axis([0, 2, 0, 2])
plt.xlabel(r'Concentration of $S_1$')
plt.ylabel(r'Concentration of $S_2$')

# Fig. 4.3A
plt.figure()
plt.axis([0, 1.5, 0, 2])
plt.xlabel('Time')
plt.ylabel('Concentration')
for sol, color in zip(sols, 'rgbyk'):
    plt.plot(sol.t, sol.y[0], color, linewidth=3)
    plt.plot(sol.t, sol.y[1], color + '.', linewidth=3)

# Fig. 4.3B
plt.figure()
plt.axis([0, 2, 0, 2])
plt.xlabel(r'Concentration of $S_1$')
plt.ylabel(r'Concentration of $S_2$')
for sol, color in zip(sols, 'rgbyk'):
    plt.plot(sol.y[0], sol.y[1], color, linewidth=3)

# Figure 4.4A
plt.figure()
plt.axis([0, 2, 0, 2])
plt.xlabel(r'Concentration of $S_1$')
plt.ylabel(r'Concentration of $S_2$')
for sol, color in zip(sols, 'rgbyk'):
    plt.plot(sol.y[0], sol.y[1], color, linewidth=3)

yy, xx = np.mgrid[0:2:20j, 0:2:20j]
xdot = k1/(1+yy**n) - k3*xx - k5*xx
ydot = k2 - k4*yy + k5*xx
plt.quiver(xx, yy, xdot, ydot, np.hypot(xdot, ydot))

# Figure 4.5A
plt.figure()
plt.axis([0, 2, 0, 2])
plt.xlabel(r'Concentration of $S_1$')
plt.ylabel(r'Concentration of $S_2$')
for sol, color in zip(sols, 'kkkkk'):
    plt.plot(sol.y[0], sol.y[1], color, linewidth=1)
# nullclines (ds/dt = 0)
ns12 = np.linspace(0, 2, 100)
ns11 = k1 / ((k3 + k5) * (1 + ns12**n))
ns21 = np.linspace(0, 2, 100)
ns22 = (k2 + k5 * ns21) / k4
plt.plot(ns11, ns12, 'k--', ns21, ns22, 'k:', linewidth=2)

# Figure 4.5B
plt.figure()
plt.axis([0, 2, 0, 2])
plt.xlabel(r'Concentration of $S_1$')
plt.ylabel(r'Concentration of $S_2$')
plt.quiver(xx, yy, xdot, ydot, np.hypot(xdot, ydot))
plt.plot(ns11, ns12, 'k--', ns21, ns22, 'k:', linewidth=2)

# Figure 4.18
# Run N simulations to steady state for different values of k_1
sols = [solve_ivp(lambda t, y: rhs(t, y, k1, k2, k3, k4, k5, n),
                (0, 100), [0, 0]) for k1 in range(40)]
s1s = [sol.y[0, -1] for sol in sols]
plt.figure()
plt.plot(np.arange(40), s1s)
plt.xlabel(r'$k_1$')
plt.ylabel(r'Steady state $S_1$ concentration')