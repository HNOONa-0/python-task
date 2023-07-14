import pytest
import random
from data import *
from checkers import *
from my_utils import get_rand_function
# from our data import functions 
def test_valid_functions():
    # check that every function in the list is valid
    for f in valid_functions:
        r=is_funcx(f)
        # assert r==0
        if r!=0:
            pytest.fail(f"{f} is supposed to be VALID function of x, but its not" )
            # return False
    print("All functions inside valid_functions are indeed valid")
    return True
def test_invalid_functions():
    # check that every function in the list is valid
    for f in invalid_functions:
        r=is_funcx(f)
        # assert r==0
        if r==0:
            pytest.fail(f"{f} is supposed to be INVALID function of x, but its not" )
            # return False
    print("All functions inside invalid_functions are indeed invalid")
    return True
def test_invalid_comb():
    # check that every combination of invalid function and valid function is indeed invalid
    for i in range(TEST_COMB):
        # get a random invalid function
        ff=get_rand_function(valid_functions, invalid_functions)
        r=is_funcx(ff )
        if r==0:
            pytest.fail(f"{ff} is supposed to be INVALID function of x, but its not" )
            # return False
        # else:
        #     print(ff+" is safe")
    print("All combinations produced from both invalid_functions and valid_functions are indeed invalid")
    return True
def test_all():
    test_valid_functions()
    test_invalid_functions()
    test_invalid_comb()
def main():
    test_all()
if __name__ == "__main__":
    # Code for your main section here
    main()