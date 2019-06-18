import os 
import csv

electionfile = os.path.join('..', 'PyPoll', 'election_data.csv')
#dictionary for candidate vote count
candidates = [] 
totalcandidates = [] 
candidatepercent = [] 
candidatetotal = []

#open csv file and read commands
with open(electionfile, 'r', newline = '') as infile:
    read = csv.reader(infile, delimiter = ',')
    #skip header rows 
    next(read)
    
    totalvote = 0
    
    for row in read:
        totalcandidates.append(row[2])
        totalvote += 1
        
sortcandidate = sorted(totalcandidates)
        
for h in range(totalvote):
    if sortcandidate[h-1] != sortcandidate[h]:
        candidates.append(sortcandidate[h])
for i in range (len(candidates)):
    candidatecount = 0 
      
    for j in range (len(sortcandidate)):
        if candidates[i] == sortcandidate[j]:
            candidatecount += 1
    candidatepercent.append(round(candidatecount / totalvote * 100, 1))
    candidatetotal.append(candidatecount) 

print("Election Results")
print("------------------------")
print("Total Votes: " + str(totalvote))
print("------------------------")  

zipcandidates = zip(candidates, candidatepercent, candidatetotal)  
for row in zipcandidates:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")

for k in range(len(candidatepercent)):
    if candidatetotal[k] > candidatetotal[k-1]:
        winnercandidate = candidates[k]
print("------------------------")  
print("Winner: ", str(winnercandidate))
print("------------------------") 
 
print("hello")
        
#create lists for candidates and vote numbers and percent

#combine candidate, number of votes, and vote percentage in zip


  
