""" Calculator class file """
import sys

class Calc:
    """ This is the Calculator class"""

    result = 0

    def get_symbol(self, entry):
        if entry[0] == "exit":
            sys.exit()
        elif len(entry) < 2 or entry[0] not in "+-*/" or isinstance(entry[1], int):
            print("Invalid entry.")
            return
        number = int(entry[1])
        symbol = entry[0]
        if symbol == "+":
            print(self.add_number(number))
        elif symbol == "-":
            print(self.subtract_number(number))
        elif symbol == "*":
            print(self.multiply_number(number))
        elif symbol == "/":
            print(self.divide_number(number))
        else:
            print("Print not a valid symbol")

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result += value_a
        return self.result

    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result -= value_a
        return self.result

    def divide_number(self, value_a):
        """ Divide number from result"""
        if value_a == 0:
            raise Exception("Can't divide by zero")
        self.result /= value_a
        return self.result

    def multiply_number(self, value_a):
        """ Multiply number from result"""
        self.result *= value_a
        return self.result
