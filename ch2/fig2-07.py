"""Figure 2.7 Numerical Simulation by Euler's Method"""


import math
import numpy as np
import matplotlib.pyplot as plt


def integrate_fe(rhs, y0, t, args=()):
    # Simulates odeint() in the scipy package

    def forward_euler(rhs, y, t, dt, args=()):
        return y + dt * rhs(y, t, *args)
    
    dts = np.diff(t)
    y = np.empty(np.shape(t) + np.shape(y0))
    y[0] = y0
    for idx, dt in np.ndenumerate(dts):
        idx = idx[0]  # idx: tuple -> integer
        y[idx+1] = forward_euler(rhs, y[idx], t[idx], dt)
    return y

    
def rhs(y, t):
    # RHS: dy/dt = -y => y = exp(-t)
    return -y


T_START, T_END = 0, 2
# Exact solution
t = np.linspace(T_START, T_END, 100)
ref = np.exp(-t)

# Step-size h = 2/3 and h= 1/3

h = 2/3
b0 = [1]
nSteps = int(1 + (T_END - T_START) / h)
tMesh1 = np.linspace(T_START, T_END, nSteps)
y1 = integrate_fe(rhs, b0, tMesh1)

# Step-size h = 1/3
h = 1/3
c0 = [1]
nSteps = int(1 + (T_END - T_START) / h)
tMesh2 = np.linspace(T_START, T_END, nSteps)
y2 = integrate_fe(rhs, c0, tMesh2)

plt.plot(t, ref, 'k-', linewidth=3, label='True value')
plt.plot(tMesh1, y1, 'go--', linewidth=2, markersize=10, label=r'$h=2/3$')
plt.plot(tMesh2, y2, 'bs:', linewidth=2, markersize=10, label=r'$h=1/3$')
plt.axis([T_START, T_END, 0, 1])
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Concentration (arbitrary units)')
plt.legend(loc='best')