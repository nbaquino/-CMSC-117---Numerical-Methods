import numpy as np
from rootscalar import *

def fun(x):
    return x**3-24

def fprime(x):
    return 3*x**2

x=3
maxit=100
tol=10e-9
wa=0.5
wf=0.5

#comment to commit and push
root=newton_raphson(fun,fprime,x,maxit,tol,wa,wf)
actual= 2**(1/2)*3**(1/3)*4**(1/4)

print(f"{'Approximate':<25} {'Actual x':<25} {'Iteration k':<15}")
print(f"{root[0]:<+25.9e} {actual:<+25.9e} {root[1]:<15}")



