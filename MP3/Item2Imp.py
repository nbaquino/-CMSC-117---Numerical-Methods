from linearsys import *

import numpy as np

# Define the coefficients and constants
# A = [
#     [0, 0, 0, -1, 4, 2, 0, 0, 0, 0] # Equation (1)
#     [0, 0, 0, 0, 0, 0, 0, -1, 4, 2],  # Equation (2)
#     [0, -1, -1, 2, 0, 0, 0, 0, 0, 0],  # Equation (3)
#     [0, 0, 0, 0, 0, -1, 5, 2, 0, 0],  # Equation (4)
#     [4, 2, 0, 0, 0, 0, 0, 0, 0, 0],  # Equation (5)
#     [0, 0, 0, 0, -1, 4, 2, 0, 0, 0],  # Equation (6)
#     [0, 0, 0, 0, 0, 0, 0, 0, -1, 4],  # Equation (7)
#     [0, 0, 0, 0, 0, 0, -1, 4, 2, 0],  # Equation (8)
#     [-1, 4, 2, 0, 0, 0, 0, 0, 0, 0],  # Equation (9)
#     [0, 0, -1, 4, 2, 0, 0, 0, 0, 0]   # Equation (10)
# ]

# b = [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
#Coeffecients and constants after using pivoting method
    A =[
        [4, 2, 0, 0, 0, 0, 0, 0, 0, 0],   # Equation (5)
        [-1, 4, 2, 0, 0, 0, 0, 0, 0, 0],  # Equation (9)
        [0, -1, -1, 2, 0, 0, 0, 0, 0, 0], # Equation (3)
        [0, 0, -1, 4, 2, 0, 0, 0, 0, 0],  # Equation (10)
        [0, 0, 0, -1, 4, 2, 0, 0, 0, 0],  # Equation (1)
        [0, 0, 0, 0, -1, 4, 2, 0, 0, 0],  # Equation (6)
        [0, 0, 0, 0, 0, -1, 5, 2, 0, 0],  # Equation (4)
        [0, 0, 0, 0, 0, 0, -1, 4, 2, 0],  # Equation (8)
        [0, 0, 0, 0, 0, 0, 0, -1, 4, 2],  # Equation (2)
        [0, 0, 0, 0, 0, 0, 0, 0 , -1,4],  # Equation (7)
    ]

    b =[5,9,3,10,1,6,4,8,1,7]

    A1=np.array(A)
    b1=np.array(b)

    x1=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    maxit=1000
    tol=1e-15

    x,k,err= JacobiSolve(A1, b1, x1, tol, maxit)

    print(f"Solution {x}")
    print(f"Number of iterations {k}")
    print(f"relative error {err}")

if __name__ == "__main__":
    main()