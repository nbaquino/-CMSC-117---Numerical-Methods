import numpy as np
from rootscalar import *

def funct (x):
    return np.exp(np.cos(x))-(3*np.sin(x))

def gfunct (x):
    return x*np.exp(np.cos(x))/ (3*np.sin(x))
    
def functprime (x) :
    return -np.exp(np.cos(x))*np.sin(x)-(3*np.cos(x))

n= newton_raphson(funct, functprime ,0 ,1000 ,1e-10 ,0.5 ,0.5)
n_forward = newton_raphson_inexact(funct ,1 ,0 ,1000 ,1e-10 ,0.5 ,0.5)
n_backward = newton_raphson_inexact(funct ,2 ,0 ,1000 ,1e-10 ,0.5 ,0.5)
n_central = newton_raphson_inexact(funct ,3 ,0 ,1000 ,1e-10 ,0.5 ,0.5)
f = steffensen (funct , 0 ,1000 ,1e-10 ,0.5 ,0.5)
fix = fixpoint (gfunct , 1 , 1000 , 1e-10)

print(f"{'Method':<30} {'Root x':<25} {'Iteration k':<20} {'Error':<25} {'Function Value f(x)':<20}")

def printformat(name, x, f):
    return print(f"{name:<30} {x[0]:<+25.16e} {str(int(x[1])):<20} {x[2]:<+25.15e} {f(x[0]):<+20.9e}")

printformat("Newton Raphson Method", n, funct)
printformat("(Forward) Newton-Raphson", n_forward , funct)
printformat("(Backward) Newton-Raphson", n_backward , funct)
printformat("(Central) Newton-Raphson", n_central , funct)
printformat("Steffensen", f, funct)
printformat("Picard Fix Point",fix, funct)  

