#import os and csv to run project
import csv
import os

#create list for the two columns
date = []
revenue = []

#Initialize csv files for read function
outputpath = os.path.join('..', 'PyBank', 'budget_data.csv')

#Start read command for csv file
with open(outputpath, 'r', newline='') as outputfile:
    outputreader = csv.reader(outputfile, delimiter=',')
    
#skip header row to read at row 2 
    next(outputreader)

#count number of months
    monthrow = 0
    for row in outputreader:
        date.append(row[0])
        revenue.append(row[1])
        monthrow += 1

#create greatest increase and decrease with corresponding
#dates for the entries
greatestinc = revenue[0]
greatestdec = revenue[0]
totalrev = 0
#total revenue
for h in revenue:
    totalrev += int(h)
#greatest inc/dec and months
for i in range(len(revenue)):
    if revenue[i] >= greatestinc:
        greatestinc = revenue[i]
        greatestincmonth = date[i]
    elif revenue[i] <= greatestdec:
        greatestdec = revenue[i]
        greatestdecmonth = date[i]
#average change
averagechange = round(totalrev / monthrow, 2)

#create text file 
textoutput = os.path.join('..', 'PyBank', 'budget_summary.txt')
with open (textoutput, 'w', newline='') as budget:
    write = csv.writer(budget)
    write.writerows([
            ["Financial Analysis for budget_data.csv"],
            ["-------------------------------------"],
            ["Total Revenue: $" + str(totalrev)],
            ["Total Months:" + str(monthrow)],
            ["Average Revenue Change:" + str(averagechange)],
            ["Greatest Increase in Profit:" + str(greatestincmonth) + "($ " + str(greatestinc) + ")"],
            ["Greatest Increase in Profit:" + str(greatestdecmonth) + "($ " + str(greatestdec) + ")"]
    ])

#print summary
print("Financial Analysis")
print("--------------------------------")
print("Total Months:" + str(monthrow))
print("Total Revenue:" + str(totalrev))
print("Average Revenue Change:" + str(averagechange))
print("Greatest Increase in Profit:" + str(greatestincmonth) + "($ " + str(greatestinc) + ")")
print("Greatest Decrease in Profit:" + str(greatestdecmonth) + "($ " + str(greatestdec) + ")")
