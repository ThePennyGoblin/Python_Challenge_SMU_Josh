import os
import csv

csvpath = os.path.join("budget_data.csv")
csvoutput = os.path.join("Budget_data_output.txt")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    print (csvreader)