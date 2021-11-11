"""Testing the Calculator Class"""
#from calculator.calculator import Calc
#pylint: disable=wrong-import-position
import sys
import os
import pytest
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
#print(parent_dir)
path = os.path.dirname(parent_dir)
sys.path.append(path)

#Needed in order to get current dicectory

from calculator.calculator import Calc
from calculator.history.history import History
#from calculator.calculations.division import Division
#pylint: enable=wrong-import-position
#pylint: disable=redefined-outer-name
#pylint: disable=unused-argument
@pytest.fixture
def clear_history_fixture():
    """ Will run and clear each time a test is passed """

    History.clear_history()
    return True

def test_calculator_add():
    """ Testing the Add function of the calculator"""
    Calc.add_number(1,2)
    assert History.get_calculation_last() == 3.0

def test_calculator_subtract():
    """ Testing the subtract method of the calculator"""
    Calc.subtract_number(1, 2)
    assert History.get_calculation_last() == -1.0

def test_calculator_multiply():
    """ Tests multiplication of two numbers"""
    Calc.multiply_number(1,2)
    assert History.get_calculation_last() == 2.0

def test_calculator_divide():
    """ Tests multiplication of two numbers"""
    Calc.divide_number(8,4,2)
    assert History.get_calculation_last() == 1.0
    Calc.divide_number(4,0)
    assert History.get_calculation_last() == "Error"

#pylint: disable=redefined-outer-name
def test_remove_history(clear_history_fixture):

    """ Tests remove history """
    Calc.add_number(1,2)
    Calc.subtract_number(1, 2)
    Calc.multiply_number(1,2)
    lst = History.history[:]
    lst.pop(0)
    print(lst)
    History.remove_history(0)
    print(History.history)
    assert History.history == lst

def test_add_calculation_to_history():
    """ Test add calculation to history """
    repeat = History.history[0]
    History.add_calculation_to_history(repeat)
    assert History.history[-1] == repeat


def test_history_length(clear_history_fixture):
    """ Tests history_length """
    Calc.multiply_number(1,2)
    Calc.multiply_number(1,2)
    History.remove_history(0)
    Calc.multiply_number(1,2)
    History.remove_history(0)
    Calc.multiply_number(1,2)
    assert History.history_length() == 2

def test_clear_history():
    """ Test clear function """
    History.clear_history()
    assert History.history == []

def test_get_calculation():
    """ Test get_calculation """
    Calc.subtract_number(1,22)
    Calc.add_number(4,4,4)
    Calc.multiply_number(3,4,2)
    print(History.history)
    print(History.get_calculation(0))
    print(History.get_calculation(1))
    print(History.get_calculation(2))
    assert History.get_calculation(0) == -21.0
    assert History.get_calculation(1) == 12.0
    assert History.get_calculation(2) == 24.0

def test_calculation_last():
    """ Test calculation last with populated history and empty history"""
    Calc.add_number(4,4,4)
    Calc.multiply_number(3,4,2)
    assert History.get_calculation_last() == 24.0
