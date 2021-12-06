""" Result Table controller """

from flask import render_template
from app.controllers.controller import ControllerBase
from calculator.csv_reader.CSVReader import CSVReader

class ResultsTableController(ControllerBase):
    """ Result Table response controller """
    @staticmethod
    def get():
        """ Results Table Get Response """
        return render_template('results_table.html', data=CSVReader.csv_to_json())
