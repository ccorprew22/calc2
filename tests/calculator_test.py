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
#from calculator.calculations.division import Division
#pylint: enable=wrong-import-position
#pylint: disable=redefined-outer-name
#pylint: disable=unused-argument
@pytest.fixture ##LOOK THIS UP
def clear_history_fixture():
    """ Will run and clear each time a test is passed """

    Calc.clear_history()
    return True

def test_calculator_add():
    """ Testing the Add function of the calculator"""
    assert Calc.add_number(*(1,2)) == 3.0

def test_calculator_subtract():
    """ Testing the subtract method of the calculator"""
    assert Calc.subtract_number(1, 2) == -1.0

def test_calculator_multiply():
    """ Tests multiplication of two numbers"""
    assert Calc.multiply_number(1,2) == 2.0

def test_calculator_divide():
    """ Tests multiplication of two numbers"""
    assert Calc.divide_number(8,4,2) == 1.0
    assert Calc.divide_number(4,0) == "Error"

#pylint: disable=redefined-outer-name
def test_remove_history(clear_history_fixture):

    """ Tests remove history """
    Calc.add_number(*(1,2))
    Calc.subtract_number(1, 2)
    Calc.multiply_number(1,2)
    lst = Calc.history[:]
    lst.pop(0)
    print(lst)
    Calc.remove_history(0)
    print(Calc.history)
    assert Calc.history == lst

def test_add_calculation_to_history():
    """ Test add calculation to history """
    repeat = Calc.history[0]
    Calc.add_calculation_to_history(repeat)
    assert Calc.history[-1] == repeat


def test_history_length(clear_history_fixture):
    """ Tests history_length """
    Calc.multiply_number(1,2)
    Calc.multiply_number(1,2)
    Calc.remove_history(0)
    Calc.multiply_number(1,2)
    Calc.remove_history(0)
    Calc.multiply_number(1,2)
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
    Calc.add_number(4,4,4)
    Calc.multiply_number(3,4,2)
    assert Calc.get_calculation_last() == 24.0
    Calc.clear_history()
    assert Calc.get_calculation_last() == "No history"

def test_get_symbol():
    """ Test get_symbol method """
    calc = Calc()
    assert calc.get_symbol("+", "3 3 3") == 9.0
    assert calc.get_symbol("*", "3 3 3") == 27.0
    assert calc.get_symbol("-", "9 4 1") == 4.0
    assert calc.get_symbol("/", "10 2") == 5.0
    assert calc.get_symbol("+", "3 b") == "Not a number"
    assert calc.get_symbol("@", "3 2") == "Invalid symbol"
