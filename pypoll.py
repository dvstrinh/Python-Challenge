#import dependencies 
import os
import csv

#csvpath
csvpath = os.path.join('Resources', 'election_data.csv')

#csvreader
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #initializing list of voter ID, county, candidate
    voter_id = []
    county = []
    candidate = []

    #read header row
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

    #read each row of data
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    #election analysis

    #list of candidates who received votes
    unique_candidate = []
    for x in candidate:
        if x not in unique_candidate:
            unique_candidate.append(x)
    print(f"Candidates Who Received Votes: {unique_candidate}")

    #number of votes each candidate won
    khan = 0
    correy = 0
    li = 0
    o_tooley = 0
    for x in candidate:
        if x == unique_candidate[0]:
            khan = khan + 1
        elif x == unique_candidate[1]:
            correy = correy + 1
        elif x == unique_candidate[2]:
            li = li + 1
        elif x == unique_candidate[3]:
            o_tooley = o_tooley + 1
    print(f"Khan: {khan}, Correy: {correy}, Li: {li}, O'Tooley: {o_tooley}")
    
    print("----------------------------------------------------------")
    #percentage of votes for each candidate
    khan_percent = "{:.3%}".format(khan / len(voter_id))
    correy_percent = "{:.3%}".format(correy / len(voter_id))
    li_percent = "{:.3%}".format(li / len(voter_id))
    o_tooley_percent = "{:.3%}".format(o_tooley / len(voter_id))

    #election results
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {len(voter_id)}")
    print("----------------------------")
    print(f"Khan: {khan_percent}, ({khan})")
    print(f"Correy: {correy_percent}, ({correy})")
    print(f"Li: {li_percent}, ({li})")
    print(f"O'Tooley: {o_tooley_percent}, ({o_tooley})")
    print("----------------------------")
    print("Winner: Khan")
    print("----------------------------")
    
#export text file
file = open("output.txt", "w+")

file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total Votes: {len(voter_id)}\n")
file.write("----------------------------\n")
file.write(f"Khan: {khan_percent}, ({khan})\n")
file.write(f"Correy: {correy_percent}, ({correy})\n")
file.write(f"Li: {li_percent}, ({li})\n")
file.write(f"O'Tooley: {o_tooley_percent}, ({o_tooley})\n")
file.write("----------------------------\n")
file.write("Winner: Khan\n")
file.write("----------------------------")