"""A simple flask web app"""
import sys
import os
from flask import Flask, request
from flask import render_template

parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

#pylint: disable=wrong-import-position
from calculator.calculator import Calc
from calculator.history.history import History
from calculator.CSV_Reader.CSVReader import CSVReader
app = Flask(__name__)

@app.route("/")
def index():
    """index  Route Response"""
    return render_template('index.html')

@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    if request.method == 'POST':
        #get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        symbol = None

        if operation == "addition":
            symbol = '+'
        elif operation == "subtraction":
            symbol = '-'
        elif operation == "multiplication":
            symbol = '*'
        else:
            symbol = '÷'
        getattr(Calc, operation)(value1, value2)
        result = str(History.get_calculation_last())

        CSVReader.insert_row(operation.capitalize(), value1, value2, result)

        return render_template('basicform.html',value1=value1,value2=value2,
                        operation=operation.capitalize(),result=result,symbol=symbol)
    # Displays the form because if it isn't a post it is a get request
    return render_template('basicform.html')

@app.route("/results_table")
def results_table():
    # Read csv into dictionary
    data = {}
    return render_template('results_table.html')
