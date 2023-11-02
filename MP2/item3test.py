import numpy as np
from rootpoly import *

def poly(n):
    pol=[]
    for k in range(1,n+1):
        print(np.mod(k**k,7),"x^" , k-1 , " + ", end="", sep="")
        pol.append(np.mod(k**k,7))
    print("\n \n")
    return pol
        

[a, b] = newtonhorner(poly(20), complex(1, 1), 100, 100, 1e-3, 1e-3, True)
[c, d] = newtonhorner(poly(40), complex(1, 1), 100, 100,  1e-3, 1e-3, True)
[e, f] = newtonhorner(poly(50), complex(1, 1), 100, 100,  1e-3, 1e-3, True)


print("Roots when n=20 True")
for k in a:
    print(k)
print("__"*30)

    
    
print("Roots when n=40")
for i in c:
    print(i)  
print("__"*30)
  
  
print("Roots when n=50")  
for j in e:
    print(j)
    
print("__"*30)


