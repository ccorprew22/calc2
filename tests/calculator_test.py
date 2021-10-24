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
from calculator.calculator import Calc
#pylint: enable=wrong-import-position

def test_get_symbol():
    """ Testing get_symbol function """
    calc = Calc()
    calc.get_symbol("+ 9".split())
    assert calc.result == 9
    calc.get_symbol("* 3".split())
    assert calc.result == 27
    calc.get_symbol("- 2".split())
    assert calc.result == 25

def test_calculator_result():
    """Testing calculator result is 0"""
    calc = Calc()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calc()
    #Act by calling the method to be tested
    calc.add_number(1)
    #Assert that the results are correct
    assert calc.result == 1

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calc()
    calc.subtract_number(1)
    assert calc.get_result() == -1

def test_calculator_multiply():
    """Testing the subtract method of the calculator"""
    calc = Calc()
    calc.multiply_number(5)
    assert calc.get_result() == 0

def test_calculator_divide():
    """Testing the subtract method of the calculator"""
    calc = Calc()
    calc.add_number(6)
    calc.divide_number(2)
    assert calc.get_result() == 3

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calc()
    calc.add_number(1)
    assert calc.get_result() == 1
