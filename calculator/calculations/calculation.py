""" Calculation class """

class Calculation:
    """ Calculation class """

    def __init__(self, *argv):
        self.values = Calculation.args_to_tuple(argv)

    @staticmethod
    def args_to_tuple(values):
        """ Converts args to tuple """
        value_tup = values[0]
        return value_tup
