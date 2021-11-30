"""A simple flask web app"""
from flask import Flask, request
from flask import render_template
from calculator.calculator import Calc
from calculator.history.history import History
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
        #make the tuple
        my_tuple = (value1, value2)
        #this will call the correct operation
        getattr(Calc, operation)(my_tuple)
        result = str(History.get_calculation_last())
        return render_template('result.html',value1=value1,value2=value2,
                        operation=operation,result=result)
    # Displays the form because if it isn't a post it is a get request
    return render_template('basicform.html')


@app.route("/bad/<value1>/<value2>")
def bad_calc(value1,value2):
    """bad calc Route Response"""
    result = value1 + value2
    response = "The result of the calculation is: " + result + '<a href="/"> back</a>'
    return response

# @app.route("/good/<float:value1>/<float:value2>")
# def good_calc(value1,value2):
#     """good calc Route Response"""
#     #my_tuple = (value1,value2)
#     #Calc.add_numbers(my_tuple)
#     #Put addition here
#     response = "The result of the calculation is: {} <a href="/"> back</a>".format(
#     str(History.get_calculation_last()))
#     return response
