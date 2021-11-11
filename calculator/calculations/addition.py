"""Addition Class"""

from calculator.calculations.calculation import Calculation

class Addition(Calculation):
    """ Addition Class """

    def get_result(self):
        """ Result """
        sum_values = 0.0
        for arg in self.values:
            sum_values = float(arg) + sum_values
        return sum_values
