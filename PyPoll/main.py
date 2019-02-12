# Dependencies
import csv
import os

# Specify the file
election_csv = os.path.join("Resources", "election_data.csv")

#Lists to store data
voter_ID = []
county = []
candidate = []

#Open the CSV
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#Read the header row first
    csv_header = next(csvreader)
    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#Total votes cast
total_votes = len(voter_ID)

#List of candidates who received votes
unique_candidates = set(candidate)

#find the total number of votes each candidate won
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
for i in candidate:
    if i == 'Khan':
        khan_votes += 1
    elif i == 'Correy':
        correy_votes += 1
    elif i == 'Li':
        li_votes += 1
    elif i == "O'Tooley":
        otooley_votes += 1

#find the percentage of votes each candidate won
khan_perc = round(((khan_votes/total_votes) * 100), 3)
correy_perc = round(((correy_votes/total_votes) * 100), 3)
li_perc = round(((li_votes/total_votes) * 100), 3)
otooley_perc = round(((otooley_votes/total_votes) * 100), 3)

#set the dictionaries by candidate
khan_dict = {
    "name": "Khan",
    "votes": khan_votes,
    "percentage": khan_perc
    }

correy_dict = {
    "name": "Correy",
    "votes": correy_votes,
    "percentage": correy_perc
    }

li_dict = {
    "name": "Li",
    "votes": li_votes,
    "percentage": li_perc
    }

otooley_dict = {
    "name": "O'Tooley",
    "votes": otooley_votes,
    "percentage": otooley_perc
    }
#set a list of final vote tallies
vote_tally = [khan_votes,correy_votes, li_votes, otooley_votes]
#grab the winning number from the list
win_num = max(vote_tally)

#find the winning number in the four seperate dicts and set winning name
for name, votes in khan_dict.items():
    if votes == win_num:
        winner = "Khan"
for name, votes in correy_dict.items():
    if votes == win_num:
        winner = "Correy"
for name, votes in li_dict.items():
    if votes == win_num:
        winner = "Li"
for name, votes in otooley_dict.items():
    if votes == win_num:
        winner = "O'Tooley"

#Print to terminal
print("```")
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Khan: {khan_perc}% ({khan_votes})")
print(f"Correy: {correy_perc}% ({correy_votes})")
print(f"Li: {li_perc}% ({li_votes})")
print(f"O'Tooley: {otooley_perc}% ({otooley_votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")
print("```")

#Open the textfile, print results
with open('Results.txt', 'w') as txt:
    print("```", file=txt)
    print("Election Results", file=txt)
    print("----------------------------", file=txt)
    print(f"Total Votes: {total_votes}",file=txt)
    print("----------------------------", file=txt)
    print(f"Khan: {khan_perc}% ({khan_votes})", file=txt)
    print(f"Correy: {correy_perc}% ({correy_votes})", file=txt)
    print(f"Li: {li_perc}% ({li_votes})", file=txt)
    print(f"O'Tooley: {otooley_perc}% ({otooley_votes})", file=txt)
    print("----------------------------", file=txt)
    print(f"Winner: {winner}", file=txt)
    print("----------------------------", file=txt)
    print("```", file=txt)
