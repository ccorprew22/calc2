"""A simple flask web app"""
import sys
import os
from flask import Flask, request

parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

#pylint: disable=wrong-import-position

from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.results_table_controller import ResultsTableController
from app.controllers.most_recent_controller import MostRecentController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    """index  Route Response"""
    return IndexController.get()

@app.route("/calculator", methods=['GET', 'POST'])
def basicform():
    """Basic Form Route"""
    if request.method == 'POST':
        return CalculatorController.post()
    return CalculatorController.get()

@app.route("/results_table")
def results_table():
    """ Results Table Route """
    return ResultsTableController.get()

@app.route("/most_recent")
def most_recent():
    """ Most recent result """
    return MostRecentController.get()
