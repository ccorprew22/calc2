from calculator import Calculator

power = "On"
print("Welcome! Enter a math symbol(+,-,*,/), followed by a space and an integer.")
print("Type exit to end.")
calc = Calculator()
while True:
    entry = input("").split()
    if entry[0] == "exit":
        break
    if len(entry) < 2:
        print("Invalid entry. Please enter a number and symbol.")
        continue
    number = int(entry[1])
    symbol = entry[0]
    if symbol == "+":
        calc.add_number(number)
    elif symbol == "-":
        calc.subtract_number(number)
    elif symbol == "*":
        calc.multiply_number(number)
    elif symbol == "/":
        calc.divide_number(number)
    else:
        "Print not a valid symbol"
    print("Answer: {}".format(calc.get_result()))
    print("Enter another number and symbol.")
