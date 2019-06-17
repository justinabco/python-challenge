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
    
    for row in outputreader:
        date.append(row[0])
        revenue.append(row[1])
monthrow = len(date)

#create greatest increase and decrease with corresponding
#dates for the entries


#print summary
print("Financial Analysis")
print("--------------------------------")
print("Total Months :", monthrow)

