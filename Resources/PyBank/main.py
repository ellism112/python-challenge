import os
import csv

csvpath = os.path.join('PyBank', 'budget_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    TotalMonths = 0
    ProLossTotal = 0
    change = 0
    months = []
    profit = []
    
    FirstRow = next(csvreader)
    TotalMonths += 1
    ProLossTotal += int(FirstRow[1])
    ProLoss = int(FirstRow[1])

    for row in csvreader:
        months.append(row[0])
        change = int(row[1]) - ProLoss
        profit.append(change)
        ProLoss = int(row[1])
        TotalMonths += 1
        ProLossTotal = ProLossTotal +int(row[1])

    Increase = max(profit)
    GreatIndex = profit.index(Increase)
    GreatMonth = months[GreatIndex]

    Decrease = min(profit)
    LeastIndex = profit.index(Decrease)
    LeastMonth = months[LeastIndex]

    average = sum(profit)/len(profit)

with open("bank.txt", "a") as f:       
    print("Financial Analysis", file = f)
    print("-"*30, file = f)
    print("Total Months: ", TotalMonths, file = f)
    print("Total: $", ProLossTotal, file = f)
    print("Average Change: $", round(average,2), file = f)
    print("Greatest Increase in Profits: ", GreatMonth, "($", Increase, ")", file = f)
    print("Greatest Descrease in Profits: ", LeastMonth, "($", Decrease, ")", file = f)
        
    
        
        
        

       