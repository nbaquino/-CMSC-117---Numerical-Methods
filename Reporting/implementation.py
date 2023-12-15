import numpy as np
import rootscalar as rs
import matplotlib.pyplot as plt
from tabulate import tabulate
from ode_scalar import *

#dy/dx= x-y
# y = x- 1 + 2e^-x

def f(x,y):
    return y          #dy/dx= y

def y_equation(x):    #y=e^x
    return np.exp(x)


methods = [("Explicit Euler Method (Forward Euler)", 0),
               ("Trapezoidal Method", 0.5),
               ("Implicit Euler Method (Backward Euler)", 1)]

for method, theta in methods:
    u0=1
    t0=0
    tf=1
    n=10
    x, y = scalartheta(f, u0, t0, tf, n, theta)
    error = max(np.abs(y - y_equation(x)))
    table = tabulate(zip(x, y), ["x", "y"], tablefmt="fancy_grid", floatfmt=".4f")
    print(f"{method}")
    print(table)
    print(f"Error: {error}\n")
    plt.plot(x, y, label=f'{method} (θ = {theta})')

#linspace(start, stop, n,)
t = np.linspace(0, 1, 10 + 1)
sol_values = np.exp(x)

plt.plot(t, sol_values, label='True Solution', linestyle='--')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
plt.show()

