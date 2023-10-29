import numpy as np
from linearsys import *

def create_matrix(n):
    a = [1 for i in range(n)]  
    b = [2 if i % 2 == 0 else 1 for i in range(n)]
    c = [(i % 3) + 3 for i in range(n)]
    d = [1 if i % 2 == 0 else 2 for i in range(n)]
    e = a 

    A = np.zeros((n, n))

    for i in range(n):
        A[i, i]   = c[i]
        if i >= 2:
            A[i, i-2] = a[i-2]
        if i >= 1:
            A[i, i-1] = b[i]
        if i < n - 1:
            A[i, i+1] = d[i]
        if i < n - 2:
            A[i, i+2] = e[i]
    return A

def block(n):
    for row in create_matrix(n):
        print(list(row))
        
def main():
    c = [(i % 3) + 3 for i in range(150)]
    d = [1 if i % 2 == 0 else 2 for i in range(100)]
    A=create_matrix(150)
    A2=create_matrix(100)
    
    
    x= LUSolve(A, c)
    y= LUSolve(A2, d)
    print("-"*200)
    print("Pentadiagonal Matrix n=150 M")
    # block(150)
    print(f"this is solution x: {np.array(x)}")
    print("Ax=", np.dot(A,x))
    nor_error=np.linalg.norm(np.dot(A,x) - c)/np.linalg.norm(c)
    print(f"Nor Error:" , nor_error)
    
    print("-"*200)
    print("Pentadiagonal Matrix n=100")
    # block(100)
    print(f"this is solution x: {np.array(y)}")
    print("Ay= ", np.dot(A2,y))
    nor_error2=np.linalg.norm(np.dot(A2,y) - d)/np.linalg.norm(d)
    print(f"Nor Error:" , nor_error2)
    
    
if __name__=="__main__":
   main()