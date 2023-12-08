import numpy as np

def secant(f,x,x1,maxit,tol,wa,wf):
  err=tol + 1 
  f0=f(x)
  f1=f(x1)
  k=1
  while err > tol and k < maxit:
    q=(f1-f0)/(x1-x)
    xtemp=x1
    x1=x1-f1/q
    x=xtemp
    f0=f1
    f1=f(x1)
    err= wa*abs(x1-x)+ wf*abs(f1)
    k= k + 1
  if err> tol and k==maxit:
    raise RuntimeError("Invalid")
  return np.array([x,k,err])

def f(x):
    return np.exp(np.cos(x))-(3*np.sin(x))

def main():
   maxit=10e+3
   tol=10e-10
   wa=0.5
   wf=0.5
   x=-3
   x1=1
   root=secant(f,x,x1,maxit,tol,wa,wf)

   print("root = ", root[0])
   print("iterate =" , root[1])
   print("error =" , root[2])


if __name__ == "__main__":
    main()