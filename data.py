MIN_PTS=50
MAX_DISTANCE=1e3
INIT_FUNC="1/((x-1)*(x-2))"
INIT_X1="-10"
INIT_X2="10"
TEST_COMB=20

is_funcx_err={
    1:"The string is not a valid function of x, please try again",
    # maybe deprecate this
    2:"The function must not contain other symbols/variables than x, please try again"
}
is_number_err={
    1:"Please enter a valid number"
}
is_validx_err={
    1:"Interval betweem x1, x2 is too large. The distance between x1,x2 must not exceed 1000,000"
}
operators=['+','-','*','/','^']
valid_functions=[
    "x**2 + 2*x + 1",
    "sin(x) + cos(x)",
    "tan(x)",
    "1/(1 + exp(-x))",
    "log(x)",
    "sqrt(x)",
    "exp(x)",
    "x**3 - 3*x**2 + 2*x",
    "2*sin(x) - cos(2*x)",
    "x**4 - 4*x**3 + 6*x**2 - 4*x + 1",
    "1/x",
    "1/(x**2 + 1)",
    "log(x**2 + 1)",
    "x*sin(x)",
    "x**2*sin(x)",
    "x**3 - 2*x**2 + x",
    "2*x**3 + 3*x**2 - 12*x + 1",
    "sqrt(x**2 + 1) - x",
    "cos(x)**2 - sin(x)**2",
    "sin(2*x)"
]
invalid_functions = [
    "y + x",
    "2 * x + ",
    "x**2,2",
    "tanx",
    "2 * (x + 1))",
    "x + 1 =",
    "sin x",
    "1/(x+y)",
    "sqrt(x**2 + 1) + 1,2",
    "1/2x",
    "cos(x y)",
    "sin(x, y)",
    "sin(x"
]