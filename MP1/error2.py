import numpy as np

def main():
    x_values = [2, 4, 6, 9, 10, 12, 15, 18, 20, 25]
    n = [10, 20, 50, 75, 100, 125]

    print('Comparison of stored and computed values of e^x')
    print('n \t absolute error \t relative error')

    for i in n:
        mclaurin_exp=maclaurin_expansion(x_values, i)
        rel_error = relerr(x_values, mclaurin_exp)
        abs_error = abserr(x_values, mclaurin_exp)
    print(f"{i} \t {abs_error:.15e} \t {rel_error:.15e}")
        
def factorial(n):
    if n >= 1:
        return n * factorial(n - 1)
    else:
        return 1

def maclaurin_expansion(x1, n):
    result = 0
    for k in range(n+1):
        result += (x1**k) / factorial(k)
    return result

#note that x1 serves as np.exp and x2 serves as mclaurin_expansion
def abserr(x1, x2):
    norm = 0
    for x1e, x2e in zip(x1, x2):
        norm += (x1e - x2e)**2   # norm = norm + (x1e - x2e)^2
    return (norm)**0.5

def relerr(x1, x2):
    new_abserr = abserr(x1, x2) / abserr(x1, [0] * len(x2))
    return new_abserr
     
if __name__ == "__main__":
    main()