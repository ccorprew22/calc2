""" Most recent controller """

from flask import render_template
from app.controllers.controller import ControllerBase
from calculator.csv_reader.CSVReader import CSVReader

class MostRecentController(ControllerBase):
    """ Index response controller """
    @staticmethod
    def get():
        """ Most Recent Route Response """
        csv = CSVReader.show_df()
        _d_ = {}
        try:
            last_row = csv.iloc[len(csv)-1]
            _d_["value1"] = last_row["Value1"]
            _d_["value2"] = last_row["Value2"]
            _d_["result"] = last_row["Result"]
            _d_["operation"] = last_row["Operation"]
        except IndexError:
            print("No values available yet")

        return render_template('most_recent.html', last=_d_)
