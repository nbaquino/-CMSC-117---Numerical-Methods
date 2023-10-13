import numpy as np
import error2

x0s=np.single(13.0 + (168)**0.5)
x0d= np.double(13.0 + (168)**0.5)

print(x0s,x0d)
print(f"Relative Error of first root is {error2.relerr(x0d,x0s)}")