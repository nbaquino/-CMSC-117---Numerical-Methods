import numpy as np

def chord(f,a,b,x,maxit,tol,wa,wf):
  err= tol + 1 # para pumasok sa while loop yung tolerance
  q= f(b)*f(a)/(b-a)
  fx=f(x)
  k=0

  while err > tol and k < maxit:
    xold=x
    x=x-fx/q
    fx=f(x)
    err= wa*abs(x-xold)+wf*abs(fx)
    k+=1
  if err> tol and k==maxit:
    raise RuntimeError("Invalid")
  return np.array(  [x,k,err])

def fun(x):
    return np.exp(x)-np.sin(x)

def main():
   a=4
   b=-4
   nmax=10e+3
   tol=10e-10
   wa=0.5
   wf=0.5
   x=2
   root=chord(fun,a,b,x,nmax,tol,wa,wf)

   print("root = ", root[0])
   print("iterate =" , root[1])
   print("error =" , root[2])


if __name__ == "__main__":
    main()