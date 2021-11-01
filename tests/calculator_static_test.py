"""Testing the Calculator Static Class"""
#from calculator.calculator import Calc
#pylint: disable=wrong-import-position
import sys
import os
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
#print(parent_dir)
path = os.path.dirname(parent_dir)
sys.path.append(path)

#Needed in order to get current dicectory

from calculator_static.calculator_static import CalcStatic
#pylint: enable=wrong-import-position

def test_calculator_add():
    """Testing the Add function of the calculator"""
    assert CalcStatic.add_number(1,2) == 3

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert CalcStatic.subtract_number(1, 2) == -1

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert CalcStatic.multiply_numbers(1,2) == 2
