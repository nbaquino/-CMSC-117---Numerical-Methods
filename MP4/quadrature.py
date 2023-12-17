import numpy as np

def Simpsonseights(a, b, f, n):
    '''
    Simpson's 3/8 rule for numerical integration.

    Parameters:
    - a: Lower limit of integration.
    - b: Upper limit of integration.
    - f: Function to be integrated.
    - n: Number of subintervals (must be a multiple of 3).

    Returns:
    - Result of the integration.
    '''
    if n % 3 != 0:
        raise ValueError("Number of subintervals must be a multiple of 3")
    
    h = (b - a) / n
    sum_y = 0
    sum_y_3 = 0
    yn = 0  # Initialize yn outside the loop
    
    for i in range(n + 1):
        x = a + i * h
        y = f(x)
        
        if i == 0:
            y0 = y
        elif i == n:
            yn = y
        else:
            sum_y = sum_y + y
            if i % 3 == 0:
                sum_y_3 = sum_y_3 + y
    
    result = ((3 * h) / 8) * (y0 + 3 * sum_y - sum_y_3 + yn)
    return np.array(result)


def simpsonsthird(f, a, b, n):
    '''
    Simpson's 1/3 rule for numerical integration.

    Parameters:
    - f: Function to be integrated.
    - a: Lower limit of integration.
    - b: Upper limit of integration.
    - n: Number of subintervals.

    Returns:
    - Result of the integration.
    '''
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    
    result = h / 3
    fours = 4 * sum(f(x[i]) for i in range(1, n, 2))
    twos = 2 * sum(f(x[i]) for i in range(2, n - 1, 2))
    result *= f(x[0]) + fours + twos + f(x[n])
    
    return np.array(result)