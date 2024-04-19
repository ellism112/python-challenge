import os
import csv

csvpath = os.path.join('Resources', 'PyPoll', 'election_data.csv')



with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    StockhamVotes = 0
    DeGetteVotes = 0
    DoaneVotes = 0
    TotalVotes = 0
    
    for row in csvreader:

        TotalVotes = TotalVotes + 1

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

    with open("votes.txt", "a") as f:
        print("Election Results", file = f)
        print("-"*30, file = f)
        print("Total Votes: ", TotalVotes, file = f)
        print("-"*30, file = f)
        print("Charles Casper Stockham: " , StockhamPercent , "% (" , StockhamVotes , ")", file = f)
        print("Diana DeGette: " , DeGettePercent , "% (" , DeGetteVotes , ")", file = f)
        print("Raymon Anthony Doane: " , DoanePercent , "% (" , DoaneVotes , ")", file = f)
        print("-"*30, file = f)
        if StockhamVotes > DeGetteVotes and StockhamVotes > DoaneVotes:
            print("Winner: Charles Casper Stockham", file = f)
        elif DeGetteVotes > StockhamVotes and DeGetteVotes > DoaneVotes:
            print("Winner: Diana DeGette", file = f)
        else:
            print("Winner: Raymon Anthony Doane", file = f)
        print("-"*30, file = f)
   