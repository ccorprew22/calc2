""" Main.py """

import sys
from calculator.calculator import Calc
#from calculator_static.calculator_static import CalcStatic

print("Welcome! Enter a math symbol(+,-,*,/), followed by a space and an integer.")
print("Type exit to end.")
symbols = ["+","-","*","/"]
calc = Calc()
while True:
    entry = input("").split()
    calc.get_symbol(entry)
    if calc.get_result() == "Error":
        raise Exception("Can't divide by zero")
    if calc.get_result() == "Exit":
        sys.exit()
    #print("Answer: {}".format(calc.get_result()))
    print("Enter another number and symbol.")
