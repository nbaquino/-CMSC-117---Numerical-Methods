import numpy as np 

def NewtonLagrangeInterpolation(f,x):
    '''
    This function implements the Newton-Lagrange Interpolation method.
    
    Parameters:
    f (function): The function to be interpolated.
    x (array-like): The x-coordinates of the points used for interpolation.
    
    Returns:
    p (function): The interpolating polynomial function.
    
    The function first constructs a divided difference table, and then uses this table to construct the interpolating polynomial.
    '''
    n=len(x)
    d=np.zeros((n,n), dtype=float)
    d[:, 0] = f(x)
    
    for k in range (1,n):
        for l in range(k,n):
            d[l,k]= (d[l,k-1]- d[l-1, k-1]) / (x[l]- x[l-k])
    
    def p(z):
        v= d[n-1, n-1]
        for k in range(1,n):
            v= v * (z-x [n-1-k]) + d[n-1-k, n-1-k]
        return v
    
    return p