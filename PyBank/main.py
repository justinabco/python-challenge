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
greatesetdec = revenue[0]
greatesetincmonth = date[0]
greatestdecmonth = date[0]
totalrev = 0

#create loop for the revenue column to determine greatest
#increase and decrease and determine total revenue
for i in range(len(revenue)):
    if revenue[i] >= greatestinc:
        greatestinc = revenue[i]
        greatestincmonth = date[i]
    elif revenue[i] <= greatestdec:
        greatestdec = revenue[i]
        greatestdecmonth = date[i]
        

#print summary
print("Financial Analysis")
print("--------------------------------")
print("Total Months :", monthrow)

