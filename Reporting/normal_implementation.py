import numpy as np
from ode_scalar import *


def f(x,y):
    return y          #dy/dx= y

def y_equation(x):    #y=e^x
    return np.exp(x)


def main():
    u0=1
    t0=0
    tf=1
    n=10
    theta= 0.5
    
    x, y = scalartheta(f, u0, t0, tf, n, theta)
    error = max(np.abs(y - y_equation(x)))
    table = tabulate(zip(x, y), ["x", "y"], tablefmt="fancy_grid", floatfmt=".4f")
    print(table)
    print(f"Error: {error}\n")
    

if __name__ == '__main__':
    main()
