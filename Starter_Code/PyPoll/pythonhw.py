import os
import csv

input_path = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
output_path = os.path.join(os.path.dirname(__file__), "Analysis", "election_data.txt")

print(input_path)

# Establish dictionaries for votes and total votes
candidates = {}
total_votes = 0

# Open and read the CSV file
with open(input_path) as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row
    header = next(csv_reader)

    # Loop through the rows of the file
    for row in csv_reader:
        total_votes += 1

        # Get the candidate's name from the column
        candidate_name = row[2]

        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

output = 'Election Results\n'
output += '----------------------\n'
output += f' Total Votes: {total_votes}\n'
output += '-----------------------\n'

# # Print the total number of votes each candidate gets
# print('Election Results')
# print('----------------------')
# print(f'Total Votes: {total_votes}')
# print('-----------------------')

# Loop through the candidates to get the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage_of_votes = (votes / total_votes) * 100
    output += f'{candidate}: {percentage_of_votes:.3f}% ({votes})\n'

# Determine the winner
winner = max(candidates, key=candidates.get)

# print('----------------------')
# print(f'Winner: {winner}')
# print('----------------------')

output += '----------------------\n'
output += f'Winner: {winner}\n'
output += '----------------------\n'

print(output)

with open(output_path, "w") as file1:
    # Writing data to a file
    file1.write(output)