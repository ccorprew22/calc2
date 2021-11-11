""" History class file """

class History:
    """ History class that handles list of calculations """
    history = []

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Add calculation to history """
        History.history.append(calculation)
        return True

    @staticmethod
    def history_length():
        """ Checks history length """
        return len(History.history)

    @staticmethod
    def remove_history(num):
        """ Removes specific item from history """
        History.history.pop(num)
        return True

    @staticmethod
    def clear_history():
        """ Clear history """
        History.history.clear()
        return True

    @staticmethod
    def get_calculation(num):
        """ Get specific calculation """
        return History.history[num].get_result()

    @staticmethod
    def get_calculation_last():
        """ Get last calculation """
        return History.history[-1].get_result()
