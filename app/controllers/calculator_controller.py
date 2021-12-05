""" Calculator controller """

from flask import render_template, flash, request
from app.controllers.controller import ControllerBase
from calculator.calculator import Calc
from calculator.history.history import History
from calculator.csv_reader.CSVReader import CSVReader


class CalculatorController(ControllerBase):
    """ Calculator form response controller """
    @staticmethod
    def post():
        """ Calculator Controller post method """
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        symbol = None

        if len(value1) == 0 or len(value2) == 0:
            flash("Enter number values into text boxes")
            return render_template('basicform.html',value1=value1,value2=value2)

        try:
            value1 = float(value1)
            value2 = float(value2)
        except ValueError:
            flash("Must enter number!!!")
            return render_template('basicform.html',value1=value1,value2=value2)

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

    @staticmethod
    def get():
        """ Calculator Controller get method """
        return render_template('basicform.html')
