import os
import csv

Months = 0
Profit = 0
Monthly_Change = []
Avg_Change = 0.0
DateList = []
Greatest_Increase_Amt = 0
Greatest_Decrease_Amt = 0
Greatest_Increase_Date = ""
Greatest_Decrease_Date = ""

financial_csv = os.path.join("Resources", "budget_data.csv")

with open(financial_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Stores the header.
    header = next(csvreader)

    # Variable to store the value of the previous row's profit. Used to calculate monthly changes in profits.
    LastRow = 0

    for row in csvreader:
        Months += 1
        Profit += int(row[1])
        Monthly_Change.append(int(row[1]) - int(LastRow))
        DateList.append(row[0])

        # Updates LastRow value before moving onto next row in loop.
        LastRow = row[1]
    
    Avg_Change = round((sum(Monthly_Change) - Monthly_Change[0]) / (Months - 1),2)

    # Sets the greatest increase/decrease amounts and the accompanying months during which those records were set.
    Greatest_Increase_Amt = max(Monthly_Change)
    Greatest_Increase_Date = DateList[Monthly_Change.index(max(Monthly_Change))]
    Greatest_Decrease_Amt = min(Monthly_Change)
    Greatest_Decrease_Date = DateList[Monthly_Change.index(min(Monthly_Change))]

    output = f"Financial Analysis\n----------------------------\nTotal Months: {Months}\nTotal: ${Profit}\nAverage Change: ${Avg_Change}\nGreatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase_Amt})\nGreatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease_Amt})"

    # Prints results to the terminal.
    print(output)

    # Exports the results to a text file.
    with open('Analysis\Financial_Analysis.txt', 'w') as file:
        file.write(output)