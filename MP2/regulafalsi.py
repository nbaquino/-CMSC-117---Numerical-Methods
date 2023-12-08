import numpy as np

def regulafalsi(f,x0,x1,maxit,tol,wa,wf):
  err= tol + 1
  xi=np.empty(maxit, dtype=float)  
  fxi= np.empty(maxit, dtype=float)
  xi[0]=x0   #x**(0)=x0
  xi[1]=x1   #x**(1)=x1
  fxi[0]=f(x0)  #f**(0)=f(x0)
  fxi[1]=f(x1)  #f**(1)=f(x1)
  k=1
  while err> tol and k < maxit:
    xc=xi[k] 
    fc=fxi[k]
    k_old=k-1
    x_old=xi[k_old]
    f_old=fxi[k_old]
    while fc*f_old >= 0 and k_old > 1:
      k_old=k_old-1
      x_old=xi[k_old]
      f_old=fxi[k_old]
    q=(fc-f_old)/(xc-x_old)
    x=xc-fc/q
    xi[k+1]= x
    fxi[k+1]= f(x)
    err= wa*abs(x-xc)+ wf*abs(fxi[k+1])
    k= k + 1
  if err> tol and k==maxit:
    raise RuntimeError("Invalid")
  return np.array([x,k,err])


def f(x):
    return np.exp(np.cos(x))-(3*np.sin(x))

def main():
   maxit=1000
   tol=10e-10
   wa=0.5
   wf=0.5
   x=-3
   x1=1
   root=regulafalsi(f,x,x1,maxit,tol,wa,wf)

   print("root = ", root[0])
   print("iterate =" , root[1])
   print("error =" , root[2])


if __name__ == "__main__":
    main()