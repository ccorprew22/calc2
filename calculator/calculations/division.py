"""Division Class"""

from calculator.calculations.calculation import Calculation

class Division(Calculation):
    """ Division Class """

    def get_result(self):
        """ Result """
        tup_values = self.values[0]
        div_values = tup_values[0]
        for arg in tup_values[1:]:
            try:
                div_values = float(div_values) / arg
            except ZeroDivisionError:
                return "Error"
        return div_values
