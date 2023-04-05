import csv
import os
file_path = os.path.join('Resources', 'election_data.csv')

printStmts = "Election Results\n\n-------------------------\n\n"

# with open(file_path, newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#        print(row)
#Total number of votes cast
# Initialize variables
total_votes = 0
# Open file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Loop through rows in file
    for row in csvreader:
        total_votes += 1
printStmts += (f"Total Votes {total_votes}\n\n")
printStmts += "-------------------------\n\n"
#A complete list of candidates who received votes
# Initialize variables
candidates = []
# Open file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Loop through rows in file
    for row in csvreader:
        candidate = row[2]
        candidates.append(candidate)
#The percentage of votes each candidate won

# Initialize variables
total_votes = 0
candidate_votes = {}

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Loop through rows in file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        # Add candidate to dictionary if not already present
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        # Increment candidate's vote count
        candidate_votes[candidate] += 1

# Calculate percentage of votes for each candidate
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    printStmts += (f"{candidate}: {vote_percentage:.3f}% ({votes})\n\n")

printStmts += "-------------------------\n\n"
# Find winner of election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)
printStmts += (f"Winner: {winner}\n\n")
printStmts += "-------------------------\n"
print(printStmts)

pathName = os.path.join('analysis', 'results.txt')
outputFile = open(pathName, 'w')
outputFile.writelines(printStmts)