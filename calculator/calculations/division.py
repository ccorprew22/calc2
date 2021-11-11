"""Division Class"""

from calculator.calculations.calculation import Calculation

class Division(Calculation):
    """ Division Class """

    def get_result(self):
        """ Result """
        div_values = self.values[0]
        for arg in self.values[1:]:
            try:
                div_values = float(div_values) / arg
            except ZeroDivisionError:
                return "Error"
        return div_values
