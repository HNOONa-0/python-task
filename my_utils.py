from checkers import *
from data import *
import numpy as np
from sympy.calculus.util import continuous_domain
import random

def to_number(x):
    return float(x)
def get_2x_intm():
    x1,x2="?","?"
    # force user to give valid x1
    while is_number(x1)!=0:
        x1=input("Enter x1: ")
        if is_number(x1)!=0:
            print(is_number_err[is_number(x1) ] )
    # force user to give valid x2
    while is_number(x2)!=0:
        x2=input("Enter x2: ")
        if is_number(x2)!=0:
            print(is_number_err[is_number(x2) ] )
    # convert to numbers
    return [x1,x2 ]
def get_2x():
    while True:
        x1,x2=get_2x_intm()
        x1=to_number(x1)
        x2=to_number(x2)
        # make sure that X1 is minimal x
        r=is_validx(x1,x2)
        if r!=0:
            print(is_validx_err[r] )
        else:
            break
    if x1>x2:
        x1,x2=x2,x1
    return [x1,x2]
def get_funcx():
    s="?"
    # force user to input a valid function
    while is_funcx(s)!=0:
        s=input("Please enter a valid function:")
        if is_funcx(s)!=0:
            print(is_funcx_err[is_funcx(s)] )
    # always return a valid function
    return py_expr(s)
def get_pts_new(x1,x2,s):
    # Define the function and the range to plot
    # maybe make it a large constant to get a nice looking graph
    if x1>x2:
        x1,x2=x2,x1
    n_pts=int(MAX_DISTANCE)
    # n_pts=int(max(x2-x1,MIN_PTS) )
    x = sympy.Symbol('x')
    # define range that will be used later
    x_range = (x1,x2)
    # Convert the function expression to a numpy-aware function
    # cant properly check for presence of asymptote, can only detect some of them

    f=sympy.sympify(s)
    vas=sympy.solve(sympy.denom(f), x)
    # print(vas)
    # 2d arrays to hold all subplots
    x_vals,y_vals=[],[]
    cur_x,cur_y,j=[],[],0

    # calculate x,y pts for each subplot, Iterate over the intervals in order
    # needs more work to detect discontiouities
    for xi in np.linspace(x_range[0], x_range[1], num=n_pts):
        # check if its function is defined at point x defined
        try:
            res=f.subs(x,xi)
            # check if it doesnt evaluate to a complex
            if sympy.simplify(res).is_real==False:
                continue
            if j<len(vas) and xi>=vas[j]:
                x_vals.append(cur_x)
                y_vals.append(cur_y ) 
                cur_x=[]
                cur_y=[]
                j+=1
            cur_x.append(xi)
            cur_y.append(res)
            
        except Exception:
            continue
    if len(cur_x)>0:
        x_vals.append(cur_x)
        y_vals.append(cur_y )

    return [x_vals,y_vals]
def get_pts_old(x1,x2,s):
    # number of pts is atleast MIN_PTS
    n_pts=int(max(x2-x1,MIN_PTS) )
    # step size
    h=(x2-x1)/n_pts
    # points to plot
    x_pts,y_pts=[0]*(n_pts+1),[0]*(n_pts+1)
    # initial x is x1
    x=x1
    for i in range(n_pts):
        # add cur point to x_pts
        x_pts[i]=x
        # eval function at cur x
        y_pts[i]=eval(s)
        x+=h
    x_pts[n_pts]=x
    y_pts[n_pts]=eval(s)
    return [x_pts,y_pts]
def py_expr(s):
    s=s.replace("^","**")
    return s
def math_expr(s):
    s=s.replace("**","^")
    return s
def get_rand_function(a,b,no_exp=1):
    f1=a[random.randint(0,len(a)-1) ]
    f2=b[random.randint(0,len(b)-1) ]
    op=operators[random.randint(0,len(operators)-1-no_exp) ]
    return f1+op+f2
def get_rand_2x():
    x1=random.randint(0,MAX_DISTANCE)
    x2=random.randint(0,MAX_DISTANCE)
    return [x1-MAX_DISTANCE/2,x2-MAX_DISTANCE/2]