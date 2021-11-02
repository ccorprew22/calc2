"""Subtract Class"""
from calculator.calculations.calculation import Calculation

class Subtract(Calculation):
    """ Subtract class """

    def get_result(self):
        """ Result """
        tup_values = self.values[0]
        diff_values = tup_values[0]
        for arg in tup_values[1:]:
            diff_values = diff_values - float(arg)
        return diff_values
