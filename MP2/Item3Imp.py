import numpy as np
import matplotlib.pyplot as plt
from rootpoly import *

plt.style.use('seaborn-v0_8-whitegrid')

    
def poly(n):
    #pn-1(x) = sum of k=1 to n (k^k ( mod 7))x^k-1 for n=20,40,50
    p=[]
    for k in range(1,n+1):
        p.append(np.mod(k**k,7))        
    return p

def findmax(n,a):
    p = poly(n)
    max_fv = max(np.linalg.norm(horner(p, ak)[0]) for ak in a)
    return max_fv

n_values=[20,40,50]

for n in n_values:
    a, b = newtonhorner(poly(n), complex(1, 1), 100, 100, 1e-3, 1e-3, True)
    plt.figure(figsize=(10, 6)) 
    plt.plot(a.real, a.imag, '.', markersize=5)  
    plt.axis("equal")
    plt.show()
    max_fv = findmax(n,a)
    print(f"Maximum function value of approximate roots for n={n}: {max_fv:.15e}")
