import os
import csv

here = os.path.dirname(os.path.abspath(__file__))

csvpath = os.path.join(here,"Resources", 'budget_data.csv')
csvoutput = os.path.join("Budget_data_output.txt")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    print(csvreader)
    csvheaders = next(csvreader)
    print(csvheaders)