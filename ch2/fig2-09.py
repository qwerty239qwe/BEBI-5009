"""Figure 2.9 Numerical Simulation of network"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def rhs(y, t):
    a, b, c, d = y
    v1, v2 = 2 * a, 2.5 * a * b
    dA = 3 - v1 - v2
    dB = v1 - v2
    dC = v2 - 3 * c
    dD = v2 - 4 * d
    return [dA, dB, dC, dD]


def jac(y, t):
    # Jacobian of the rhs is optional
    a, b, _, _ = y
    return np.array([[-2-2.5*b, -2.5*a, 0, 0],
                     [2-2.5*b, -2.5*a, 0, 0],
                     [2.5*b, 2.5*a, -3, 0],
                     [2.5*b, 2.5*a, 0, -4]])


T_START, T_END = 0, 10
N_STEPS = 100
t = np.linspace(T_START, T_END, N_STEPS)
y0 = [0] * 4
y = odeint(rhs, y0, t, Dfun=jac)

lineStyles = ('k-', 'r--', 'g:', 'b-.')
legends = ('A', 'B', 'C', 'D')
for i, (style, leg) in enumerate(zip(lineStyles, legends)):
    plt.plot(t, y[:, i], style, label=leg)
plt.axis([0, 4, 0, 1])
plt.legend(loc='best')
plt.xlabel('Time (sec)')
plt.ylabel('Concentration (mM)')