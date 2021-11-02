"""Testing the Calculator Class"""
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

from calculator.calculator import Calc
#pylint: enable=wrong-import-position

def test_calculator_add():
    """Testing the Add function of the calculator"""
    calc_add = Calc()
    assert calc_add.add_number(1,2) == 3.0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc_sub = Calc()
    assert calc_sub.subtract_number(1, 2) == -1.0

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc_mul = Calc()
    assert calc_mul.multiply_number(1,2) == 2.0

def test_clear_history():
    """ Test clear function """
    calc_clear = Calc()
    calc_clear.clear_history()
    assert calc_clear.history == []

def test_get_calculation():
    """ Test get_calculation """
    calc2 = Calc()
    calc2.subtract_number(1,22)
    calc2.add_number(4,4,4)
    calc2.multiply_number(3,4,2)
    print(calc2.history)
    print(calc2.get_calculation(0))
    print(calc2.get_calculation(1))
    print(calc2.get_calculation(2))
    assert calc2.get_calculation(0) == -21.0
    assert calc2.get_calculation(1) == 12.0
    assert calc2.get_calculation(2) == 24.0
