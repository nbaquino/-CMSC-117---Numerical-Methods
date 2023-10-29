import numpy as np
from linearsys import *

def newton(f,Jf,x,tol,maxit):
    x = np.array(x,float)
    err_newton = tol + 1
    k_newton = 0
    while err_newton > tol and k_newton < maxit:
        dx = LUSolve(Jf(x),-f(x))
        x = x + dx
        err_newton = np.linalg.norm(f(x))
        k_newton += 1
    if err_newton > tol and k_newton == maxit:
        print("Error in tol and / or maxit.")
    return x, err_newton, k_newton


