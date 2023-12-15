import numpy as np
from rootscalar import *
import matplotlib.pyplot as plt
from tabulate import tabulate

# Global variables
maxit = 100
tol = 1e-15
wa = 0.5
wf = 0.5

#t= x
#u= y

def scalartheta(f, u0, t0, tf, n, theta):
    global maxit, tol, wa, wf
    if 0 <= theta <= 1:
        pass
    else:
        raise ValueError("Theta must be between 0 and 1.")

    t, h = np.linspace(t0, tf, n+1, retstep=True)
    u = np.zeros(n + 1)
    u[0] = u0
    
    for k in range(n):
        def g(x):
            return u[k] + h * ((1 - theta) * f(t[k], u[k]) + theta * f(t[k + 1], x)) - x
        u[k+1] = secant(g, u[k], u[k]+ h, maxit, tol, wa, wf)[0]
    return t, u



