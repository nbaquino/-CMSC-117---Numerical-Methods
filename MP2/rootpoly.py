import numpy as np

def horner(p, z):
    """
    Evaluates a polynomial at a specific value using Horner's method.

    This function applies Horner's method for polynomial evaluation, which reduces the number of multiplications and additions needed. It uses a backward iteration method to calculate the result, starting from the last coefficient of the polynomial.

    Args:
        p (array_like): The coefficients of the polynomial, where p[0] represents the highest degree term. 
        z (complex): The point at which to evaluate the polynomial.

    Returns:
        list: A list containing the first and remaining elements of the evaluated polynomial. The first element is the result of the polynomial evaluation, and the remaining elements represent the evaluated coefficients of the polynomial.

    References:
        - Horner's method for polynomial evaluation (https://www.geeksforgeeks.org/horners-method-polynomial-evaluation/)
    """
    lenp = len(p)
    b = np.zeros_like(p, dtype=complex)
    b[-1] = p[-1]
    for k in range(lenp - 2, -1, -1):
        b[k] = p[k] + b[k + 1] * z
    return [b[0], b[1:]]

def newtonhorner(p, z, maxit, refmax, tol, reftol, ref):
    """
    Finds the roots of a polynomial using the Newton-Raphson and Horner's methods.

    Args:
        p (list): Coefficients of the polynomial in decreasing order.
        z (complex): Initial guess for a root of the polynomial.
        maxit (int): Maximum number of iterations for the Newton-Raphson method.
        refmax (int): Maximum number of iterations for the refinement process.
        tol (float): Tolerance for the Newton-Raphson method.
        reftol (float): Tolerance for the refinement process.
        ref (bool): If True, refinement is performed on the roots.

    Returns:
        list: A list containing two lists. The first list contains the roots of the polynomial. 
        The second list contains the deflated polynomials at each step.
    """
    errref = tol * reftol
    n = len(p)
    zm = np.zeros(n - 1, dtype=complex)
    eps = np.finfo(float).eps
    pnm = [p]

    for m in range(n-1):
        k = 0
        z = complex(z, z)
        err = tol + 1

        if m == n - 2:
            k += 1
            b = pnm[m]
            z = -b[0] / b[1]
        else:
            while err > tol and k < maxit:
                k += 1
                zold = z
                pz, qnm = horner(pnm[m], z)
                qz = horner(qnm, z)[0]
                if abs(qz) > eps:
                    z = zold - pz / qz
                    err = max(abs(z-zold),abs(pz))
                else:
                    print("Division by a small number")
                    err = 0
                    z = zold
        #orignal function yung ginamit sa refinement
        if ref:
            kref = 0
            zref = z
            err = tol + 1
            while err > errref and kref < refmax:
                kref += 1
                pz, qn_1 = horner(p, zref)
                qz = horner(qn_1, zref)[0]
                if abs(qz) > eps:
                    zref2 = zref - pz / qz
                    err = max(abs(zref - zref2), abs(pz))
                    zref = zref2
                else:
                    print("Division by a small number")
                    err = 0
            z = zref
        zm[m] = z
        pnm.append(horner(pnm[m], z)[1])

    return [zm, pnm]
    