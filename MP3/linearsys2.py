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

def LUKJI(A):
    n = len(A)
    A = np.array(A,dtype=float)
    for k in range(n):
        for j in range(k+1,n):
            A[j,k] = A[j,k]/A[k,k]
        for j in range(k+1,n):
            for i in range(k+1,n):
                A[i,j] = A[i,j] - A[i,k]*A[k,j]
    return A

def GetLU(A):
    n = len(A)
    A = LUKJI(A)
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
    y = ForwardSubRow(L,b)
    return BackwardSubRow(U,y)