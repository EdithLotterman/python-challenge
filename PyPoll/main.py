#create variables
#list of candidates
candidates = []
total_votes = 0
percent_votes = []
cand_names = []
cand_votes = []
winner = ""

#import modules
import os
import csv
from collections import Counter

#store filepath as variable
filepath = os.path.join("..", "Resources", "election_data.csv")

#open file with encoding variable (remove encoding variable if not needed)
with open(filepath, newline = '', encoding='utf-8') as file:

    #CSV reader specifying variable and delimiter
    reader = csv.reader(file, delimiter = ',')

    #skip first row of csv file
    next(reader)
    
    #Loop through 
    for row in reader:
        #create list of candidates
        candidates.append(row[2])

#count total number of votes
total_votes = len(candidates)

#count unique candidates as key in dictionary and put in list
cand_names = list(Counter(candidates).keys())

#count votes for each candidate in dictionary
cand_votes = list(Counter(candidates).values())

#calculate percent votes
for vote in cand_votes:
    percent = round(int(vote)/int(total_votes)*100, 3)
    percent_votes.append(percent)

#zip into one list
data = zip(cand_names, percent_votes, cand_votes)
data2 = zip(cand_names, percent_votes, cand_votes)

#find max number of votes in candidate votes
max = max(cand_votes)

# Create dictionary
keys = cand_votes
values = cand_names
dictionary = dict(zip(keys, values))

#Return winner
winner = dictionary[max]

#print to terminal
print("")
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")
for row in data:
    print(f"{row[0]}: {row[1]}%  ({row[2]})")
print("------------------------")
print(f"Winner: {winner}")

#print to csv
#specify output path file
output_path = os.path.join("..", "Analysis",'PyPollAnalysis.csv')

#open the file
with open(output_path, 'w', newline="") as csvfile:

    #initialize csv writer
    writer = csv.writer(csvfile)

    #write rows
    writer.writerow(["Election Results"])
    writer.writerow([f"Total Votes: {total_votes}"])
    for row in data2:
        writer.writerow([f"{row[0]}: {row[1]}%  ({row[2]})"])
    writer.writerow([f"Winner: {winner}"])