import os 
import csv
csvpath = os.path.join("Resources", "election_data.csv")

total_votes = []
candidates = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    next(csvreader)

    for row in csvreader:
        total_votes.append(row[0])

        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

num_votes = len(total_votes)
num_candidates = len(candidates)

print("Election Results")
print()
print("-----------------------")
print()
print(f"Total Votes: {num_votes}")
print()
print("-----------------------")
print()

for candidate, votes in candidates.items():
        percentage = round(votes / num_votes*100,2)
        print(f"{candidate}: {percentage}% ({votes})")
        print()
print()
print("------------------------")
print()
winner = max(candidates, key=candidates.get)
print(f"Winner: {winner}")
print()
print("-----------------------")

output_file = os.path.join("Election_Results")

with open("election_Results.txt", "w") as file:
    file.write("Election Results\n")
    file.write("\n")
    file.write("-----------------------\n")
    file.write("\n")
    file.write(f"Total Votes: {num_votes}\n")
    file.write("------------------------\n")
    file.write("\n")
    for candidate, votes in candidates.items():
        percentage = round(votes / num_votes*100,2)
        file.write(f"{candidate}: {percentage}% ({votes})\n")
        file.write("\n")
    file.write("\n")
    file.write("------------------------\n")
    file.write("\n")
    winner = max(candidates, key=candidates.get)
    file.write(f"Winner: {winner}\n")
    file.write("\n")
    file.write("------------------------\n")
