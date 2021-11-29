"""Division Class"""

from calculator.calculations.calculation import Calculation

class Division(Calculation):
    """ Division Class """

    def get_result(self):
        """ Result """
        div_values = self.values[0]
        #print(type(float(div_values)))
        for arg in self.values[1:]:
            try:
                div_values = float(div_values) / float(arg)
            except ZeroDivisionError:
                return "Error"
        return div_values
