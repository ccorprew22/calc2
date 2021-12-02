"""Testing the CSV Reader Class"""
#from calculator.calculator import Calc
#pylint: disable=wrong-import-position
import sys
import os
import pandas as pd
from pandas._testing import assert_frame_equal

parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
#print(parent_dir)
path = os.path.dirname(parent_dir)
sys.path.append(path)

#Needed in order to get current dicectory
test_data = os.path.dirname(os.path.abspath(__file__)) + "/test_data/"

from calculator.CSV_Reader.CSVReader import CSVReader

#from calculator.calculations.division import Division
#pylint: enable=wrong-import-position
#pylint: disable=redefined-outer-name
#pylint: disable=unused-argument

def test_user_creation():
    """ Tests if csv file is accurately created """
    test_results = pd.read_csv(test_data + "test_results.csv")
    user = CSVReader("Chris")
    user.insert_row("Add", 1, 2, 3)
    user.insert_row("Add", 2, 2, 4)
    user.insert_row("Add", 5, 2, 7)
    assert_frame_equal(user.show_df(), test_results)
