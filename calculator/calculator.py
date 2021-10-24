""" Calculator class file """

class Calc:
    """ This is the Calculator class"""

    result = 0

    def get_symbol(self, entry):
        """
        Takes input and determines what action to take (math, invalid entry,
        or exit)
        """
        if len(entry) < 2 or entry[0] not in "+-*/":
            if len(entry) > 0 and entry[0] == "exit":
                self.result = "Exit"
                return
            print("Invalid entry.")
            return
        try:
            number = int(entry[1])
            symbol = entry[0]
        except ValueError:
            print("Invalid entry")
            return
        if symbol == "+":
            print(self.add_number(number))
        elif symbol == "-":
            print(self.subtract_number(number))
        elif symbol == "*":
            print(self.multiply_number(number))
        else:
            print(self.divide_number(number))


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
            self.result = "Error"
            return self.result
        self.result /= value_a
        return self.result

    def multiply_number(self, value_a):
        """ Multiply number from result"""
        self.result *= value_a
        return self.result
