""" This is the calculator function"""
from calculator.calculations.addition import Addition
from calculator.calculations.multiply import Multiply
from calculator.calculations.subtract import Subtract
from calculator.calculations.division import Division

class Calc:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def get_symbol(symbol, numbers):
        """
        Takes input and determines what action to take (math, invalid entry,
        or exit)
        """

        lst = numbers.split()
        lst_numbers = []
        math = None
        for num in lst:
            if num.isdigit():
                lst_numbers.append(int(num))
            else:
                math = "Not a number"
                return math
        tup_numbers = tuple(lst_numbers)

        if symbol == "+":
            math =  Calc.add_number(*tup_numbers)
        elif symbol == "-":
            math = Calc.subtract_number(*tup_numbers)
        elif symbol == "*":
            math = Calc.multiply_number(*tup_numbers)
        elif symbol == "/":
            math = Calc.divide_number(*tup_numbers)
        else:
            math = "Invalid symbol"
        return math

    @staticmethod
    def add_number(*argv):
        """ Adds number meothod"""
        addition = Addition(argv)
        Calc.history.append(addition)
        result = addition.get_result()
        print("Answer: " + str(result))
        return result

    @staticmethod
    def subtract_number(*argv):
        """ Subtract number method"""
        subtract = Subtract(argv)
        Calc.history.append(subtract)
        result = subtract.get_result()
        return result

    @staticmethod
    def multiply_number(*argv):
        """ Multiply numbers method"""
        multiply = Multiply(argv)
        Calc.history.append(multiply)
        result = multiply.get_result()
        return result

    @staticmethod
    def divide_number(*argv):
        """ Divide numbers method"""
        division = Division(argv)
        Calc.history.append(division)
        result = division.get_result()
        return result

    @staticmethod
    def history_length():
        """ Checks history length """
        return len(Calc.history)

    @staticmethod
    def remove_history(num):
        """ Removes specific item from history """
        Calc.history.pop(num)

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
            return Calc.history[-1].get_result()
        return "No history"
