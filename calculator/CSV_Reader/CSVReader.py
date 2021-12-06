#pylint: disable=invalid-name
""" CSV Reader Class """
import os
import pandas as pd

class CSVReader:
    """ Takes user input and puts it into CSV """

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
            if f.tell() <= 31:
                new_row_df.index += 1
                new_row_df.to_csv(f, header=True)
            else:
                curr = pd.read_csv(script_dir+'/results.csv')
                new_row_df.index += len(curr.index) + 1
                new_row_df.to_csv(f, mode='a', header=False)

    @staticmethod
    def show_df():
        """ Shows df """
        return pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + "/results.csv")

    @staticmethod
    def clear_csv():
        """ Clear csv """
        with open(os.path.dirname(os.path.abspath(__file__))+"/results.csv", "w+") as f:
            f.write(",Operation,Value1,Value2,Result\n")
            f.close()
        return True

    @staticmethod
    def csv_to_json():
        """ Converts csv to dictionary """
        csv = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + "/results.csv")
        d = {"record" : [],
                "operation": [],
                "value1": [],
                "value2": [],
                "result": []
                }
        for i in range(len(csv)):
            d["record"].append(csv.iloc[i]["Unnamed: 0"])
            d["operation"].append(csv.iloc[i]["Operation"])
            d["value1"].append(csv.iloc[i]["Value1"])
            d["value2"].append(csv.iloc[i]["Value2"])
            d["result"].append(csv.iloc[i]["Result"])

        return d

CSVReader.clear_csv()
