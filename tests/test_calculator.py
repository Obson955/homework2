'''My Calculator Test'''
from calculator import add, subtract,multiply

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_multiply():
    '''Test that multiplication function works ''' 
    assert multiply(2,2) == 4
