import numpy as np
from nonlinearsys import *

def f (x):
    a,b,c,d=x
    return [20*a*c-8*a*b+16*c**3-4*b*d-39,
            12*a+6*b+2*c-2*d-11,
            4*a**2+2*b*c-10*c+2*a*d**2+7,
            -3*a*d-2*b**2+7*c*d-16]


