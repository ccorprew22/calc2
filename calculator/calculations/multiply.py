"""Multiply Class"""
from calculator.calculations.calculation import Calculation
class Multiply(Calculation):
    """ Multiply class """
    def get_result(self):
        """ Result """
        product_values = 1.0
        for arg in self.values:
            product_values = float(arg) * product_values
        return product_values