""" Main.py """

from calculator.calculator import Calc
#from calculator_static.calculator_static import CalcStatic

print("Welcome!")
print("Type exit to end.")
symbols = ["+","-","*","/"]
calc = Calc()
while True:
    print("Enter another symbol and list of numbers.")
    symbol = input("Symbol: ")
    numbers = input("Numbers: ")
    calc.get_symbol(symbol, numbers)
    if calc.get_calculation_last() == "Error":
        raise Exception("Can't divide by zero")
