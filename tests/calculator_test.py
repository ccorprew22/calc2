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
    assert Calc.add_number(1,2) == 3.0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calc.subtract_number(1, 2) == -1.0

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calc.multiply_number(1,2) == 2.0

def test_remove_history():
    """ Tests remove history """
    lst = Calc.history[:]
    lst.pop(0)
    print(lst)
    Calc.remove_history(0)
    print(Calc.history)
    assert Calc.history == lst

def test_history_length():
    """ Tests history_length """
    assert Calc.history_length() == 2

def test_clear_history():
    """ Test clear function """
    Calc.clear_history()
    assert Calc.history == []

def test_get_calculation():
    """ Test get_calculation """
    Calc.subtract_number(1,22)
    Calc.add_number(4,4,4)
    Calc.multiply_number(3,4,2)
    print(Calc.history)
    print(Calc.get_calculation(0))
    print(Calc.get_calculation(1))
    print(Calc.get_calculation(2))
    assert Calc.get_calculation(0) == -21.0
    assert Calc.get_calculation(1) == 12.0
    assert Calc.get_calculation(2) == 24.0

def test_calculation_last():
    """ Test calculation last with populated history and empty history"""
    last = Calc.history[-1]
    assert Calc.get_calculation_last() == last
    Calc.clear_history()
    assert Calc.get_calculation_last() == "No history"
