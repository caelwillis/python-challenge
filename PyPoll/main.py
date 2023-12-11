import os
import csv

os.getcwd()

budget_data = 'python-challenge/PyPoll/Resources/election_data.csv'

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    # print(f"Header: {csv_header}")

    total_votes = 0
    cand = []
    votes = []

    for row in csv_reader:
        #print(row)
        total_votes += 1
        if row[2] not in cand:
            cand.append(row[2])
            votes.append(1)
        else:
            votes[cand.index(row[2])] += 1

            
    text_file = open('python-challenge/PyPoll/election.rtf', 'w')

    text_file.write("Election Results" + "\n")
    text_file.write("Total Votes: " +str(total_votes) + "\n") #prints total number of votes
    text_file.write("Candidates: " + str(cand) + "\n") #prints list of candidates
    text_file.write("Votes for each Candidate: " +str(votes) + "\n") #prints votes each condidate received
    text_file.write("Winner: " + str(cand[votes.index(max(votes))])) #prints election winner

    text_file.close()

