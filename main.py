""" Main.py """

from calculator.calculator import Calc
#from calculator_static.calculator_static import CalcStatic

print("Welcome!")
print("Type exit to end.")
symbols = ["+","-","*","/"]
calc = Calc()
while True:
    print("Enter another number and symbol.")
