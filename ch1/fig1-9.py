"""
Hodgkin-Huxley model of excitable barnacle muscle fiber
reviewed in Rinzel (1990) Bulletin of Mathematical Biology 52 pp. 5-23.
Figure 1.9 and problem 8.6.4
"""


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import exp, expm1


def hh_rhs(y, t, iStim):
    # Constants
    E_N = 55  # Reversal potential of Na
    E_K = -72  # Reversal potential of K
    E_LEAK = -49.0  # Reversal potential of leaky channels
    G_N_BAR = 120.0  # Max. Na channel conductance
    G_K_BAR = 36.0  # Max. K channel conductance
    G_LEAK = 0.30  # Max. leak channel conductance
    C_M = 1.0  # membrane capacitance

    # Equations
    v, m, h, n = y

    mAlfaV = -0.10 * (v + 35)
    mAlfa = mAlfaV / expm1(mAlfaV)
    mBeta = 4.0 * exp(-(v + 60) / 18.0)
    dmdt = -(mAlfa + mBeta) * m + mAlfa
    hAlfa = 0.07 * exp(-(v+60)/20)
    hBeta = 1 / (exp(-(v+30)/10) + 1)
    dhdt  = -(hAlfa + hBeta) * h + hAlfa
    iNa = G_N_BAR * (v-E_N) * (m**3) * h

    nAlfaV = -0.1 * (v+50)
    nAlfa = 0.1 * nAlfaV / expm1(nAlfaV)
    nBeta = 0.125 * exp( -(v+60) / 80)
    dndt  = -(nAlfa + nBeta) * n + nAlfa
    iK = G_K_BAR * (v - E_K) * (n**4)

    iLeak = G_LEAK * (v - E_LEAK)
    iSt = iStim(t)
    dVdt = -(iNa + iK + iLeak + iSt) / C_M
    return [dVdt, dmdt, dhdt, dndt]

# Initial conditions
v, m, h, n = -59.8977, 0.0536, 0.5925, 0.3192
y0 = np.array([v, m, h, n])
tStart, tEnd = 0, 100
N_POINTS = 1000
t = np.linspace(tStart, tEnd, N_POINTS)
def get_iStim(t):
    if 20 < t <= 21:
        return -6.65
    elif 60 < t <= 61:
        return -6.87
    else:
        return 0

solution = odeint(hh_rhs, y0, t, args=(get_iStim, ))
plt.plot(t, solution[:, 0], 'k-', linewidth=2)
plt.xlabel("Time (ms)")
plt.ylabel("Membrane voltage (mV)")
plt.axis([tStart, tEnd, -80, 50])