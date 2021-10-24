""" Main.py """

from calculator.calculator import Calc

print("Welcome! Enter a math symbol(+,-,*,/), followed by a space and an integer.")
print("Type exit to end.")
symbols = ["+","-","*","/"]
calc = Calc()
while True:
    entry = input("").split()
    calc.get_symbol(entry)
    #print("Answer: {}".format(calc.get_result()))
    print("Enter another number and symbol.")
