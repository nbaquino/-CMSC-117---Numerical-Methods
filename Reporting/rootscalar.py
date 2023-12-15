import numpy as np

def newton_raphson(f,fprime,x,maxit,tol,wa,wf):  
  err= tol +1
  fx=f(x)
  k=0
  while err> tol and k < maxit:
    xold=x
    x= x-(fx/fprime(x))
    fx=f(x)
    err= wa*abs(x-xold) + wf*abs(fx)
    k+=1
  if err > tol and k == maxit:
    raise RuntimeError("Error in maximum iterate and / or tolerance!")
  return np.array([x,k,err])

def newton_raphson_inexact(f,i,x,maxit,tol,wa,wf):
  err = tol + 1
  fx = f(x)
  k = 0
  h = np.sqrt(np.finfo(float).eps)
  while err > tol and k < maxit:
    xold = x
    if i == 1: #forward finite difference
      fprime = (f(x+h)-f(x))/h
    elif i == 2: # backward finite difference
      fprime = (f(x)-f(x-h))/h
    elif i == 3: # central finite differenc
      fprime = (f(x+h)-f(x-h))/(2*h)
    x = x - fx/fprime
    fx = f(x)
    err = wa*abs(x-xold) + wf*abs(fx)
    k += 1
    if err > tol and k == maxit:
      raise RuntimeError("Error in maximum iterate and / or tolerance!")
  return np.array([x, k, err])

def steffensen(f,x,maxit,tol,wa,wf):
  err= tol +1
  fx=f(x)
  k=0
  while err> tol and k < maxit:
    xold=x
    fx=f(x)
    q=(f(x+fx)-fx)/fx
    x=x-(fx/q)
    err= wa*abs(x-xold) + wf*abs(fx)
    k+=1
  if err > tol and k == maxit:
    raise RuntimeError("Error in maximum iterate and / or tolerance!")
  return np.array([x,k,err])
  
def fixpoint(g,x,maxit,tol):
    err = tol + 1
    k = 0
    while err> tol and k < maxit:
      xold = x
      x = g(x)
      err = abs(x-xold)
      k += 1
    if err > tol and k == maxit:
      raise RuntimeError("Error in maximum iterate and / or tolerance!")
    return np.array([x, k, err])
  
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
  
  
