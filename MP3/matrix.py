import numpy as np
from judeacode import *

def block(n):
    a = [1 for i in range(n)]  
    b = [2 if i % 2 == 0 else 1 for i in range(n)]
    c = [(i % 3) + 3 for i in range(n)]
    d = [1 if i % 2 == 0 else 2 for i in range(n)]
    e = a 

    A = np.zeros((n, n), dtype=float)

    for i in range(n):
        A[i, i] = c[i]
        if i >= 1:
            A[i, i - 1] = b[i - 2]
        if i >= 2:
            A[i, i - 2] = a[i - 1]
        if i < n - 1:
            A[i, i + 1] = d[i]
        if i < n - 2:
            A[i, i + 2] = e[i]
    return A


def main():
    n1=150
    A1 = block(n1)
    c = [(i % 3) + 3 for i in range(n1)]
    print(A1)
    x = LUSolve(A1, c)
    nor_error=np.linalg.norm(A1 @ x - c)/np.linalg.norm(c)

    # n2 = 150
    # A2 = block(n2)
    # d = np.array([1, 2] in range(n2))
    # y = LUSolve(A2, d)
    # error_d = np.linalg.norm(np.dot(A2, y) - d) / np.linalg.norm(d)

    print(np.array(x))
    print(f"Relative Error for c:", nor_error)

    # print(f"Solution for n = {n2} and d:\n", y)
    # print(f"Relative Error for d: {error_d}")
    
if __name__=="__main__":
    main()