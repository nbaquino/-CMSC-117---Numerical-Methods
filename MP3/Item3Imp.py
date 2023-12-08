import numpy as np
from linearsys import *

# For letter a
def f(x):
    a, b, c, d = np.array(x, float)  
    f0 = 20*a*c - 8*a*b + 16*c**3 - 4*b*d - 39
    f1 = 12*a + 6*b + 2*c - 2*d - 11
    f2 = 4*a**2 + 2*b*c - 10*c + 2*a*d**2 + 7
    f3 = -3*a*d - 2*b**2 + 7*c*d - 16
    
    return np.array([f0, f1, f2, f3])
    
def Jf(x):
    a, b, c, d = np.array(x, float)
    f0 = [20*c - 8*b, -8*a - 4*d, 20*a + 48*c**2, -4*b]
    f1 = [12, 6, 2, -2]
    f2 = [8*a + 2*d**2, 2*c, 2*b - 10, 4*a*d]
    f3 = [-3*d, -4*b, 7*d, -3*a + 7*c]
    
    return np.array([f0, f1, f2, f3])

# For letter b
def f1(x):
    a, b, c = np.array(x, float)
    f0 = 3*a - np.cos(b*c) - 0.5
    f1 = a**2 - 81*(b + 0.1)**2 + np.sin(c) + 1.06
    f2 = np.exp(-a*b) + 20*c - ((3 - 10*np.pi) / 3)
    
    return np.array([f0, f1, f2])


def Jf1(x):
    a, b, c = np.array(x, float)
    f0 = [3, c*np.sin(b*c), b*np.sin(b*c)]
    f1 = [2*a, -162*b-16.2, np.cos(c)]
    f2 = [-b*np.exp(-a*b), -a*np.exp(-a*b), 20]

    return np.array([f0, f1, f2])


def main():
    x = [1, 1, 1, 1]
    x1 = np.array([1, 1, 1])
    b1 = np.array([39, 11, -7, 16])
    b2 = [0.5, -1.06, (3 - 10*np.pi)/3]
    tol = 1e-14
    maxit = 100
        
    x, err_newton, k_newton = newton(f, Jf, x, tol, maxit)
    rel_error= err_newton/np.linalg.norm(b1)
    print("Answer for letter a")
    print(f"Solution: {x}")
    print(f"Number of Iterations: {k_newton}") 
    print(f"Newton Error: {err_newton}")
    print(f"Relative Error: {rel_error}")
    
    
    x1, err_newton1, k_newton1 = newton(f1, Jf1, x1, tol, maxit)
    print("_" * 50)
    print("Answer for letter b")
    print(f"Solution: {x1}")
    print(f"Number of iterations: {k_newton1}")
    print(f"Error: {err_newton1}")
    rel_error_b = err_newton1 / np.linalg.norm(b2)
    print(f"Relative error for letter b: {rel_error_b}")
    
if __name__ == "__main__":
    main()
