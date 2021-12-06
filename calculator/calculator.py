""" This is the calculator function"""
from calculator.calculations.addition import Addition
from calculator.calculations.multiply import Multiply
from calculator.calculations.subtract import Subtract
from calculator.calculations.division import Division
from calculator.history.history import History

class Calc:
    """ This is the Calculator class"""

    @staticmethod
    def addition(*argv):
        """ Adds number method"""
        addition = Addition(argv)
        History.add_calculation_to_history(addition)
        return True

    @staticmethod
    def subtraction(*argv):
        """ Subtract number method"""
        subtract = Subtract(argv)
        History.add_calculation_to_history(subtract)
        return True

    @staticmethod
    def multiplication(*argv):
        """ Multiply numbers method"""
        multiply = Multiply(argv)
        History.add_calculation_to_history(multiply)
        return True

    @staticmethod
    def division(*argv):
        """ Divide numbers method"""
        division = Division(argv)
        History.add_calculation_to_history(division)
        return True
