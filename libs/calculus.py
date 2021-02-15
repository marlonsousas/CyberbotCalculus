import numpy as np
from sympy import *
from sympy.integrals.transforms import *
import IPython.display as disp
from sympy.abc import t, s, a




def derivate(function):
    x = Symbol('x')
    y = eval(function)
    yprime = y.diff(x)
    return yprime

def integral(function):
    
    x, y = symbols('x y') 
    gfg = Integral(sqrt(1 / x), x) 
    
    print(gfg) 
    x = Symbol('x')
    y = eval(function)
    yintegral = integrate(y)
    return yintegral




