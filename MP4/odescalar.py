import numpy as np

import numpy as np

def runge_kutta4(f, y0, t0, tk, h):
    '''
    Solve an ordinary differential equation (ODE) using the Runge-Kutta method of order four (RK4).

    Parameters:
    - f: Function representing the ODE in the form f(t, y).
    - y0: Initial value of y at t0.
    - t0: Initial value of the independent variable.
    - tk: Final value of the independent variable.
    - h: Step size for numerical integration.

    Returns:
    - t_values: Array of time values.
    - y_values: Array of corresponding y values.
    '''

    num_steps = int((tk - t0) / h) + 1
    t_values = np.linspace(t0, tk, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0

    for i in range(1, num_steps):
        k1 = h * f(t_values[i-1], y_values[i-1])
        k2 = h * f(t_values[i-1] + h/2, y_values[i-1] + k1/2)
        k3 = h * f(t_values[i-1] + h/2, y_values[i-1] + k2/2)
        k4 = h * f(t_values[i-1] + h, y_values[i-1] + k3)

        y_values[i] = y_values[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6

    return t_values, y_values


import numpy as np

def runge_kutta3(f, y0, t0, tk, h):
    '''
    Solve an ordinary differential equation (ODE) using the Runge-Kutta-Heun method of order three (RKH3).

    Parameters:
    - f: Function representing the ODE in the form f(t, y).
    - y0: Initial value of y at t0.
    - t0: Initial value of the independent variable.
    - tk: Final value of the independent variable.
    - h: Step size for numerical integration.

    Returns:
    - t_values: Array of time values.
    - y_values: Array of corresponding y values.
    '''

    num_steps = int((tk - t0) / h) + 1
    t_values = np.linspace(t0, tk, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0

    for i in range(1, num_steps):
        k1 = f(t_values[i-1], y_values[i-1])
        k2 = f(t_values[i-1] + h/3, y_values[i-1] + (h/3)*k1)
        k3 = f(t_values[i-1] + 2*h/3, y_values[i-1] + (2*h/3)*k2)

        y_values[i] = y_values[i-1] + (h/4) * (k1 + 3*k3)

    return t_values, y_values



        
        