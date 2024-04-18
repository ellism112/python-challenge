import os
import csv

csvpath = os.path.join('PyBank', 'budget_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV header: {csv_header}")
    
    TotalMonths = 0
    proloss = 0
    for row in csvreader:
        #print(row)
        TotalMonths =  TotalMonths + 1
        proloss += int(row[1])
        
print("Financial Analysis")
print("-"*30)
print("Total Months: ", TotalMonths)
print("Total: $", proloss)
        
    
        
        
        

       