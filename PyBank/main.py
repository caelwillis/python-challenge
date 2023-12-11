import os
import csv

os.getcwd()

budget_data = 'python-challenge/PyBank/Resources/budget_data.csv'

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    changes = []
    flag = True
    prev = 0
    dates = []
    
    for row in csv_reader:

        if flag: 
            prev = int(row[1])
            flag = False
            
        change = int(row[1]) - prev
        prev = int(row[1])
    
        changes.append(change)            
        dates.append(row[0])
              
dates.pop(0)
changes.pop(0)
average_change = sum(changes) / len(changes)

text_file = open('python-challenge/PyBank/budget.rtf', 'w')

text_file.write("Financial Analysis" + "\n")
text_file.write("Total Months: " +str(len(changes)+ 1) + "\n") #prints the total number of months for our data
text_file.write("Average Change: $" +str(average_change) + "\n") #prints the average change in "Profit/Losses"
text_file.write("Greatest Increase in Profits: $" +str(max(changes)) + "\n") #prints the greatest increase in "Profit/Losses"
text_file.write("Greatest Decrease in Profits: $" + str(min(changes))) #prints the greatest decrease in "Profit/Losses"

text_file.close()
