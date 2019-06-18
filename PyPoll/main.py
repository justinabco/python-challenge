import os 
import csv

electionfile = os.path.join('..', 'PyPoll', 'election_data.csv')
#dictionary for candidate vote count
poll = {}

totalvote = 0


#open csv file and read commands
with open(electionfile, 'r', newline = '') as infile:
    read = csv.reader(infile, delimiter = ',')
    #skip header rows 
    next(read)
    
    for row in read:
        totalvote += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1


#create lists for candidates and vote numbers and percent
candidate = []
numvotes = []
voteper = []



print("Election Results")
print("------------------------")
print("Total Votes: " + str(totalvote))
print("------------------------")       