import numpy as np

def bisection (f,a,b,nmax,tol):
    """_summary_

    Args:
        f (_type_): callabale function
        a (_type_): float
        b (_type_): scalar
        nmax (_type_): int
                      maximum iteration
        tol (_type_): scalar
                      0 < tol < 1
                      tolerance

    Raises:
        RuntimeError: _description_
        RuntimeError: _description_

    Returns:
        _type_: _description_

    Outputs:
    c      : scalar
              root of function f
    k      : integer

    """

    err= b-a
    fa=f(a)
    fb=f(b)
    k=0
    if fa==0: # if abs(fa) < tol
        c=a
        err=0
    if fb==0:
        c=b
        err=0
    if fa* fb > 0:
        raise RuntimeError("Invalid")
    
    while err > tol and k < nmax:
        c= 0.5*(a+b)
        fc=f(c)
        if fc==0:
            return np.array([c,k,0])
        if fc*fa>0:
            a=c
            fa=fc
        else:
            b=c
        err= abs(b-a)
        k+=1
        
    if err> tol and k == nmax:
        raise RuntimeError("Invalid")
    return np.array([c,k,err])

def fun(x):
    return np.exp(x)-np.sin(x)

def main():
   a=-4
   b=4
   nmax=10e+3
   tol=10e-10
   root=bisection(fun,a,b,nmax,tol)
   
   print("root = ", root[0])
   print("iterate =" , root[1])
   print("error =" , root[2])
    
  
if __name__ == "__main__":
    main()