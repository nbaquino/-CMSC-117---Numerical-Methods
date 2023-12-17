import numpy as np
import matplotlib.pyplot as plt
from polyinterp import *

def supnorm(f, a, b, numnodes):
    x = np.linspace(a, b, numnodes)
    absfx = np.abs(f(x))
    return max(absfx)

def f(x):
    return x / ((1 - x**2 + x**4)**2)

[a, b] = [-2, 2]

subintervals = [[-2, -1], [-1, 1], [1, 2]]

max_norm = 0
max_norm_interval = None

fig, ax = plt.subplots(figsize=(10, 6))

for interval in subintervals:
    a_i, b_i = interval
    x_i = np.linspace(a_i, b_i, 11)
    p_i = NewtonLagrangeInterpolation(f, x_i)

    norm_i = supnorm(lambda x: f(x) - p_i(x), a_i, b_i, 3000)

    if norm_i > max_norm:
        max_norm = norm_i
        max_norm_interval = interval

    graph_i = np.linspace(a_i, b_i, 3000)

    ax.plot(graph_i, [p_i(z) for z in graph_i], label=f'Interpolated {interval}', linestyle='dashed')
    ax.scatter(x_i, f(x_i), label=f'Interpolation points {interval}')

    print(f"Subinterval {interval}: Function norm value: {norm_i}")

print("\nMaximum function norm:")
if max_norm_interval is not None:
    print(f"   Subinterval with the max norm: {max_norm_interval}")
    print(f"   Maximum function norm value  : {max_norm}")
    
    # Plot the subinterval with the maximum norm
    ax.set_title(f'Piecewise Interpolation - Max Norm Subinterval: {max_norm_interval}')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.tight_layout()
    plt.show()
else:
    print("   No maximum function norm found.")
