"""Subtract Class"""
from calculator.calculations.calculation import Calculation

class Subtract(Calculation):
    """ Subtract class """

    def get_result(self):
        """ Result """
        diff_values = self.values[0]
        for arg in self.values[1:]:
            diff_values = float(diff_values) - float(arg)
        return diff_values
