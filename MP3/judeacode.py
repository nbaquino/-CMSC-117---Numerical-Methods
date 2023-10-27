import numpy as np

# Column-wise Forward Substitution
def ForwardSubCol(L, b):
    n = len(L)
    L = np.array(L,dtype=float)
    x = np.zeros(n,dtype=float)
    for i in range(n - 1, -1, -1):
        if L[i,i] == 0:
            raise RuntimeError("No Solution! The Triangular matrix is not singular.")
    for j in range(n):
        x[j] = b[j] / L[j, j]
        for i in range(j + 1, n):
            b[i] -= L[i, j] * x[j]
    x[n-1] = b[n-1] / L[n-1, n-1]
    return x

# Column-wise Backward Substitution
def BackwardSubCol(U, b):
   n = len(U)
   U = np.array(U,dtype=float)
   x = np.zeros(n,dtype=float)
   for i in range(n - 1, -1, -1):
    if U[i,i] == 0:
        raise RuntimeError("No Solution! The Triangular matrix is not singular.")
    for j in range(n - 1, 0, -1):
        x[j] = b[j] / U[j, j]
        for i in range(j):
            b[i] -= U[i, j] * x[j]
    x[0] = b[0] / U[0, 0]
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
    y = ForwardSubCol(L,b)
    return BackwardSubCol(U,y)