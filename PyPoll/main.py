import os
import csv

Votes = 0
Candidates = []
Vote_Total_Charles = 0
Vote_Total_Diana = 0
Vote_Total_Raymon = 0
Winner = ""

electoral_csv = os.path.join("Resources", "election_data.csv")

with open(electoral_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        Votes += 1

        if row[2] not in Candidates:
            Candidates.append(row[2])
        
        if row[2] == "Charles Casper Stockham":
            Vote_Total_Charles += 1
        elif row[2] == "Diana DeGette":
            Vote_Total_Diana += 1
        elif row[2] == "Raymon Anthony Doane":
            Vote_Total_Raymon += 1
    
    if Vote_Total_Charles > Vote_Total_Diana and Vote_Total_Charles > Vote_Total_Raymon:
        Winner = "Charles Casper Stockham"
    elif Vote_Total_Diana > Vote_Total_Charles and Vote_Total_Diana > Vote_Total_Raymon:
        Winner = "Diana DeGette"
    else:
        Winner = "Raymon Anthony Doane"

    output = f"Election Results\n-------------------------\nTotal Votes: {Votes}\n-------------------------\nCharles Casper Stockham: {round(Vote_Total_Charles/Votes*100,3)}% ({Vote_Total_Charles})\nDiana DeGette: {round(Vote_Total_Diana/Votes*100,3)}% ({Vote_Total_Diana})\nRaymon Anthony Doane: {round(Vote_Total_Raymon/Votes*100,3)}% ({Vote_Total_Raymon})\n-------------------------\nWinner: {Winner}\n-------------------------"

    print(output)

    with open('Analysis\Electoral_Analysis.txt', 'w') as file:
        file.write(output)