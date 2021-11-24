""" Main.py """

import os
import time
import pandas as pd
from calculator.calculator import Calc
from calculator.history.history import History

RECORD = 0
def main_calculator(name_file, operation):
    """ Makes log for calculations """
    global RECORD
    with open("log_file/log.txt", "a+") as _f_:
        result = History.get_calculation(RECORD)
        now = int(time.time())
        #print(now)
        log = "{}.\nTime:{}\nName of File: {}\nOperation: {}\nResult: {}\n\n".format(str(RECORD+1),
                                            now, name_file, operation, result)
        _f_.write(log)
    RECORD += 1

if not os.path.exists('log_file'):
    os.makedirs('log_file')

addition = pd.read_csv("math_data/add.csv")
subtraction = pd.read_csv("math_data/sub.csv")
division = pd.read_csv("math_data/div.csv")
multiply = pd.read_csv("math_data/mul.csv")

data_path = os.path.dirname(os.path.abspath(__file__))
for i in range(len(addition)):
    Calc.addition_number(addition.loc[i]["Value1"], addition.loc[i]["Value2"])
    main_calculator("add.csv", "Addition")
os.rename(data_path+"/math_data/add.csv", data_path+"/finished_data/add.csv")
for i in range(len(subtraction)):
    Calc.subtract_number(subtraction.loc[i]["Value1"], subtraction.loc[i]["Value2"])
    main_calculator("sub.csv", "Subtraction")
os.rename(data_path+"/math_data/sub.csv", data_path+"/finished_data/sub.csv")
for i in range(len(multiply)):
    Calc.multiply_number(multiply.loc[i]["Value1"], multiply.loc[i]["Value2"])
    main_calculator("mul.csv", "Multiply")
os.rename(data_path+"/math_data/mul.csv", data_path+"/finished_data/mul.csv")
for i in range(len(division)):
    Calc.divide_number(division.loc[i]["Value1"], division.loc[i]["Value2"])
    main_calculator("div.csv", "Division")
os.rename(data_path+"/math_data/div.csv", data_path+"/finished_data/div.csv")
