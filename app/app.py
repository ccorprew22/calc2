"""A simple flask web app"""
import sys
import os
from flask import Flask, request, render_template

parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

#pylint: disable=wrong-import-position

from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    """index  Route Response"""
    return IndexController.get()

@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Basic Form Route"""
    if request.method == 'POST':
        return CalculatorController.post()
    return CalculatorController.get()

@app.route("/results_table")
def results_table():
    """ Results Table Route """
    # Read csv into dictionary
    #data = {}
    return render_template('results_table.html')
