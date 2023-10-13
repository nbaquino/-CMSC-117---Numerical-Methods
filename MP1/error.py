import numpy as np

def main():
    x_values = [2, 4, 6, 9, 10, 12, 15, 18, 20, 25] 
    n_values = [10, 20, 50, 75, 100, 125]

    print('Comparison of stored and computed values of e^x')
    print(55 * "-")
    print('n \t Absolute error \t Relative error')

    for n in n_values:
        np_exp = []
        mclaurin_exp = []
        for x in x_values:
            #so all the data in the x values will be added to the np_exp array to compute for np_exp
            #To compute for the mclaurin expansion, we need to use all the x values and n values. Add it into mclaurin_exp array
            np_exp.append(np.exp(x))
            mclaurin_exp.append(maclaurin_expansion(x, n))
            #To solve for the relative error and absolute error, we need to compare all the np_exp values and mclaurin_exp values
        rel_error = relerr(np_exp, mclaurin_exp)
        abs_error = abserr(np_exp, mclaurin_exp)
        print(f"{n} \t {abs_error:.15e} \t {rel_error:.15e}")

def factorial(n):
    if n >= 1:
        return n * factorial(n - 1)
    else:
        return 1

def maclaurin_expansion(x, n):
    result = 0
    for k in range(n+1):
        result += (x**k) / factorial(k)
    return result

def abserr(x1, x2):
    return  np.linalg.norm(np.array(x1) - np.array(x2))

def relerr(x1 ,x2):
    return abserr(x1, x2) / np.linalg.norm(np.array(x1))

if __name__ == "__main__":
    main()