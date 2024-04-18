import os
import csv

csvpath = os.path.join('PyPoll', 'election_data.csv')



with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)



    csv_header = next(csvreader)
    #print(f"CSV header: {csv_header}")
    print("Election Results")
    StockhamVotes = 0
    DeGetteVotes = 0
    DoaneVotes = 0
    TotalVotes = 0
    
    for row in csvreader:
        #print(row)
        
        TotalVotes = TotalVotes + 1
        
    
        #print(f"Total Votes: {count_rows(csvfile)}")

        candidate = row[2]
        
        if candidate == "Charles Casper Stockham":
            StockhamVotes = StockhamVotes + 1
        elif candidate == "Diana DeGette":
            DeGetteVotes = DeGetteVotes + 1
        else:
            DoaneVotes = DoaneVotes + 1
        StockhamPercent = (StockhamVotes / TotalVotes) * 100
        DeGettePercent = (DeGetteVotes / TotalVotes) * 100
        DoanePercent = (DoaneVotes / TotalVotes) * 100
    print("-"*30)
    print("Total Votes: ", TotalVotes)
    print("-"*30)
    print("Charles Casper Stockham: " , StockhamPercent , "% (" , StockhamVotes , ")")
    print("Diana DeGette: " , DeGettePercent , "% (" , DeGetteVotes , ")")
    print("Raymon Anthony Doane: " , DoanePercent , "% (" , DoaneVotes , ")")
    print("-"*30)
    if StockhamVotes > DeGetteVotes and StockhamVotes > DoaneVotes:
        print("Winner: Charles Casper Stockham")
    elif DeGetteVotes > StockhamVotes and DeGetteVotes > DoaneVotes:
        print("Winner: Diana DeGette")
    else:
        print("Winner: Raymon Anthony Doane")
    print("-"*30)
   