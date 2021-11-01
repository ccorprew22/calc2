"""Testing the Calculator"""
#from calculator.calculator import Calc
import sys
import os
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
#print(parent_dir)
path = os.path.dirname(parent_dir)
sys.path.append(path)

#Needed in order to get current dicectory
#pylint: disable=wrong-import-position
from calculator.calculator_static import Calc
#pylint: enable=wrong-import-position

def test_calculator_add():
    """Testing the Add function of the calculator"""
    assert Calc.add_number(1,2) == 3

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calc.subtract_number(1, 2) == -1

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calc.multiply_numbers(1,2) == 2
