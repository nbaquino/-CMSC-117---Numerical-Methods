import numpy as np

#Solving Triangular systems
def ForwardSubRow(L,b):
    n = len(L)
    L = np.array(L,dtype=float)
    x = np.zeros(n,dtype=float)
    for i in range(n):
        if L[i,i] == 0:
            raise RuntimeError("No Solution! The Triangular matrix is not singular.")
    x[0] = b[0]/L[0,0]
    for i in range(1,n):
        s = 0
        for j in range(i):
            s += L[i,j]*x[j]
        x[i] = (b[i]-s)/L[i,i]
    return x

def ForwardSubCol(L, b):
    n = len(L)
    L = np.array(L, dtype=float)
    b = np.array(b, dtype=float)
    for j in range(n-1):
        if L[j,j] == 0:
            raise RuntimeError("No Solution! The Triangular matrix is not singular.")
        b[j] = b[j] / L[j,j]
        for i in range(j+1, n):
            b[i] = b[i] - L[i,j] * b[j]
    b[n-1]= b[n-1]/L[n-1,n-1] 
    return b
            
def BackwardSubRow(U,b):
    n = len(U)
    U = np.array(U,dtype=float)
    x = np.zeros(n,dtype=float)
    for i in range(n):
        if U[i,i] == 0:
            raise RuntimeError("No Solution! The Triangular matrix is not singular.")
    x[n-1] = b[n-1]/U[n-1,n-1]
    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1, n):
            s = s + U[i,j]*x[j]   
        x[i] = (b[i]-s)/U[i,i]
    return x


def BackwardSubCol(U,b):
    n = len(U)     
    U = np.array(U, dtype=float)
    b = np.array(b, dtype=float)
    for j in range(n-1, 0, -1):
        if U[j,j] == 0:
            raise RuntimeError("No Solution! The Triangular matrix is not singular.")
        b[j] = b[j] / U[j,j]
        for i in range(j):
            b[i] = b[i] - U[i,j] * b[j]
    b[0]=b[0]/U[0,0]
    return b

def JacobiMethod(A,b,x,tol,maxit):
    A=np.array(A,dtype=float)
    x=np.array(x,dtype=float)
    b=np.array(b,dtype=float)
    k=0
    n=len(b)
    bnorm=np.linalg.norm(b)
    err=np.linalg.norm(np.dot(A,x)-b)/bnorm
    while err < tol and k < maxit:
        xold=x
        for i in range(n):
            x[i]= (b[i]-np.dot(A[i,:],xold)+A[i,i]*xold)/A[i,i]
        err=np.linalg.norm(np.dot(A,x)-b)/bnorm
        k+=1
    return x,k.err
         

            
def LUIJK(A):
    n = len(A)
    A = np.array(A, dtype=float)

    for j in range(n):
        A[j,0] = A[j,0] / A[0,0]
    for i in range(1, n):
        for j in range(i, n):
            s = 0
            for k in range(i):
                s = s + A[i,k] * A[k,j]
            A[i,j] = A[i,j] - s

        for j in range(i+1, n):
            s = 0
            for k in range(i):
                s = s + A[j,k] * A[k,i]
            A[j,i] = (A[j,i] - s) / A[i,i]

    return A

def GetLU(A):
    n = len(A)
    A = LUIJK(A)
    L = np.zeros((n,n),dtype=float)
    U = np.zeros((n,n),dtype=float)
    for i in range(n):
        L[i,i] = 1
        for j in range(i):
            L[i,j] = A[i,j]
        for j in range(i,n):
            U[i,j] = A[i,j]
    return L, U

def LUSolve(A,b):
    L , U = GetLU(A)
    y = ForwardSubCol(L,b)
    return BackwardSubCol(U,y)