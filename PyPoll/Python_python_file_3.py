import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")

# Initializing total count
total_count = 0 

candidatevotes = {}

# Open election_data file
with open(csvpath, newline='') as csvfile:
    # Specify delimiter for csv files
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_count += 1
        if row[2] not in candidatevotes:
            candidatevotes[row[2]] = 1
        else:
            candidatevotes[row[2]] += 1   

# Print results to terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_count))
print("-------------------------")

for candidate, votes in candidatevotes.items():
    print(candidate + ": " + "{:.3%}".format(votes / total_count) + "   (" + str(votes) + ")")

print("-------------------------") 

winner = max(candidatevotes, key=candidatevotes.get)
print(f"Winner: {winner}")

# Write to output file
output_path = os.path.join(".", "Resources", "election_results.txt")
with open(output_path, "w") as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write("Total Votes: " + str(total_count) + "\n")
    f.write("-------------------------\n")

    for candidate, votes in candidatevotes.items():
        f.write(candidate + ": " + "{:.3%}".format(votes / total_count) + "   (" + str(votes) + ")\n")
    
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")