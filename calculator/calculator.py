""" This is the calculator function"""
from calculator.calculations.addition import Addition
from calculator.calculations.multiply import Multiply
from calculator.calculations.subtract import Subtract

class Calc:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def add_number(*argv):
        """ Adds number to result"""
        addition = Addition(argv)
        Calc.history.append(addition)
        result = addition.get_result()
        return result

    @staticmethod
    def subtract_number(*argv):
        """ Subtract number from result"""
        subtract = Subtract(argv)
        Calc.history.append(subtract)
        result = subtract.get_result()
        return result

    @staticmethod
    def multiply_number(*argv):
        """ Multiply two numbers and store the result"""
        multiply = Multiply(argv)
        Calc.history.append(multiply)
        result = multiply.get_result()
        return result

    @staticmethod
    def clear_history():
        """ Clear history """
        Calc.history.clear()

    @staticmethod
    def get_calculation(num):
        """ Get specific calculation """
        return Calc.history[num].get_result()

    @staticmethod
    def get_calculation_last():
        """ Get last calculation """
        if len(Calc.history) > 0:
            return Calc.history[-1]
        return "No history"
