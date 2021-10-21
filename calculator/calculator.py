class Calculator:
    """ This is the Calculator class"""

    result = 0
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
        self.result /= value_a
        return self.result

    def multiply_number(self, value_a):
        """ Multiply number from result"""
        self.result *= value_a
        return self.result
