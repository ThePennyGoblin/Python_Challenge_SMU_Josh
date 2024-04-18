import os
import csv

here = os.path.dirname(os.path.abspath(__file__))

csvpath = os.path.join(here,"Resources", 'budget_data.csv') # Selects the CSV file
csvoutput = os.path.join(here,"analysis","Budget_data_output.txt")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")   # opens the CSV file and reads it
    next(csvreader) 
    revenue = []
    date = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in csvreader:

        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])

    #prints the average along with the greatest and least change
    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")
   

# This Writes all the outputs into the .txt file 
with open(csvoutput,"w") as writefile:
    writefile.write(f"Total Months:{len(date)}\n")
    writefile.write(f"Total Revenue: ${sum(revenue)}\n")
    writefile.write(f"Avereage Revenue Change: ${round(avg_rev_change)}\n")
    writefile.write(f"Greatest Increase in Revenue: {max_rev_change_date} ${max_rev_change}\n")
    writefile.write(f"Greatest Decrease in Revenue:{min_rev_change_date} ${min_rev_change}")