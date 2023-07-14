import sympy
from data import *

def is_number(x):
    n="?"
    try:
        n=float(x)
    except ValueError:
        return 1
    return 0
def is_funcx(s):
    # Convert the string function to a SymPy expression
    s=py_expr(s)
    x=sympy.Symbol('x')
    try:
        # check if its a valid function of x
        expr = sympy.sympify(s)
        # ((x in expr.free_symbols and len(expr.free_symbols)==1) or
        #     isinstance(expr, sympy.Number)) and not isinstance(expr, bool)
        if isinstance(expr, tuple):
            return 1
        if len(expr.free_symbols)==0 or (len(expr.free_symbols)==1 and x in expr.free_symbols):
            return 0
        else:
            return 1
    except (sympy.SympifyError, TypeError):
        return 1
def is_validx(x1,x2):
    # x2>=x1 always
    if x1>x2:
        x1,x2=x2,x1
    if x2-x1<=MAX_DISTANCE:
        return 0
    return 1
def is_valid_GUI(x1,x2,s):
    r1,r2=is_number(x1),is_number(x2)
    if r1!=0:
        return is_number_err[r1]
    elif r2!=0:
        return is_number_err[r2]
    r3,r4=is_validx(float(x1),float(x2)),is_funcx(s)
    
    if r3!=0:
        return is_validx_err[r3]
    elif r4!=0:
        return is_funcx_err[r4]
    return 0
def py_expr(s):
    s=s.replace("^","**")
    return s
def math_expr(s):
    s=s.replace("**","^")
    return s
