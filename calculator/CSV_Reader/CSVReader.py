#pylint: disable=invalid-name
""" CSV Reader Class """
import pandas as pd

class CSVReader:
    """ Takes user input and puts it into CSV """
    def __init__(self, name):
        self.name = name
        self.df = CSVReader.create_df(name)
        self.record = 1

    def insert_row(self, operation, value1, value2, result):
        """ Inserts new row in csv file """
        new_row_df = pd.DataFrame({'Record': [self.record],
                       'Operation': [operation],
                       'Value1': [value1],
                       'Value2': [value2],
                       'Result': [result]})
        new_row_df.to_csv('{}_results.csv'.format(self.name), mode='a', index=False, header=False)
        self.record += 1
        new_df = pd.read_csv('{}_results.csv'.format(self.name))
        self.df = new_df

    @staticmethod
    def create_df(name):
        """ Creates new table for user """
        df = pd.DataFrame({'Record': [],
                       'Operation': [],
                       'Value1': [],
                       'Value2': [],
                       'Result': []})
        df.to_csv('{}_results.csv'.format(name), index=False)
        return df

    def show_df(self):
        """ Shows df """
        return self.df
