#pylint: disable=invalid-name
""" CSV Reader Class """
import pandas as pd
import os

class CSVReader:
    """ Takes user input and puts it into CSV """
    #record = 1
    # def __init__(self, name):
    #     self.name = name
    #     self.df = CSVReader.create_df(name)
    #     self.record = 1

    @staticmethod
    def insert_row(operation, value1, value2, result):
        """ Inserts new row in csv file """
        new_row_df = pd.DataFrame({
                       'Operation': [operation],
                       'Value1': [value1],
                       'Value2': [value2],
                       'Result': [result]})
        script_dir = os.path.dirname(os.path.abspath(__file__)) #directory name of path to file

        with open(script_dir+'/results.csv', 'a') as f:
            if f.tell() == 0:
                new_row_df.index += 1
                new_row_df.to_csv(f, header=True)
            else:
                curr = pd.read_csv(script_dir+'/results.csv')
                new_row_df.index += len(curr.index) + 1
                new_row_df.to_csv(f, mode='a', header=False)

    # @staticmethod
    # def create_df(name):
    #     """ Creates new table for user """
    #     df = pd.DataFrame({'Record': [],
    #                    'Operation': [],
    #                    'Value1': [],
    #                    'Value2': [],
    #                    'Result': []})
    #     df.to_csv('{}_results.csv', index=False)
    #     return df

    @staticmethod
    def show_df():
        """ Shows df """
        return pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + "/results.csv")

    @staticmethod
    def clear_csv():
        """ Clear csv """
        f = open(os.path.dirname(os.path.abspath(__file__))+"/results.csv", "w+")
        f.close()
        return True

    @staticmethod
    def csv_to_json(file):
        """ Converts csv to dictionary """
        csv = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + "/results.csv")
        dict = {}
        #for row in csv:

        return dict
