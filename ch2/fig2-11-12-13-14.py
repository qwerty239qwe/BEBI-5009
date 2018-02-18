"""
Figure 2.11 (Fig 1) & Figure 2.12 (Fig 2) 
Simulation and rapid equilibrium approximation
As well as figure 2.13 Rapid equilibrium approximation
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def original_rhs(y, t, k0, k1, km1, k2):
    a, b = y
    vf = k1 * a
    vb = km1 * b
    dA = k0 - vf + vb
    dB = vf - vb - k2 * b
    return [dA, dB]


def approx_rhs(y, t, k0, k1, km1, k2):
    bApprox = k1 / (km1 + k1) * y
    return k0 - k2 * bApprox


def qssa_rhs(y, t, k0, k1, km1, k2):
    return k0 - k2 * y


T_START, T_END = 0, 3
N_POINTS = 100
t = np.linspace(T_START, T_END, N_POINTS)

# Figure 2.11 (Fig 1)
args = (k0, k1, km1, k2) = (0, 9, 12, 2)
y0 = [0, 10]
y = odeint(original_rhs, y0, t, args)
plt.figure(1)
plt.plot(t, y[:, 0], 'k-', linewidth=3, label='a')
plt.plot(t, y[:, 1], 'k--', linewidth=3, label='b')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Concentration (arbitrary units)')
plt.legend(loc='best')

# Figure 2.12 (Fig 2)
y0 = 10
yApprox = odeint(approx_rhs, y0, t, args)
plt.figure(2)
plt.plot(t, y[:, 0], 'k-', linewidth=2, label='a (original)')
plt.plot(t, y[:, 1], 'k--', linewidth=2, label='b (original)')
(aApprox, bApprox) = (km1 / (km1 + k1) * yApprox, k1 / (km1 + k1) * yApprox)
plt.plot(t, aApprox, 'r-', linewidth=2, label='a (reduced)')
plt.plot(t, bApprox, 'r--', linewidth=2, label='b (reduced)')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Concentration (arbitrary units)')
plt.legend(loc='best')

# Figure 2.13
args = (k0, k1, km1, k2) = (9, 20, 12, 2)
y = odeint(original_rhs, [8, 4], t, args)
yApprox = odeint(approx_rhs, 12, t, args)
plt.figure(3)
plt.plot(t, y[:, 0], 'k-', linewidth=2, label='a (original)')
plt.plot(t, y[:, 1], 'k--', linewidth=2, label='b (original)')
(aApprox, bApprox) = (km1 / (km1 + k1) * yApprox, k1 / (km1 + k1) * yApprox)
plt.plot(t, aApprox, 'r-', linewidth=2, label='a (reduced)')
plt.plot(t, bApprox, 'r--', linewidth=2, label='b (reduced)')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Concentration (arbitrary units)')
plt.legend(loc='best')

# Figure 2.14
T_START, T_END = 0, 4
N_POINTS = 100
t = np.linspace(T_START, T_END, N_POINTS)
args = (k0, k1, km1, k2) = (5, 20, 12, 2)
y = odeint(original_rhs, [8, 4], t, args)
bApprox = odeint(qssa_rhs, 235/32, t, args)
aApprox = (k0 + km1 * bApprox) / k1

plt.figure(4)
plt.plot(t, y[:, 0], 'k-', linewidth=2, label='a (original)')
plt.plot(t, y[:, 1], 'k--', linewidth=2, label='b (original)')
plt.plot(t, aApprox, 'r-', linewidth=2, label='a (reduced)')
plt.plot(t, bApprox, 'r--', linewidth=2, label='b (reduced)')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Concentration (arbitrary units)')
plt.legend(loc='best')

plt.show()