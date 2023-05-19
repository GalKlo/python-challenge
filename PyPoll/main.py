# Import OS library to create a path to the file
import os

# Import CSV library to read dataset stored in csv format
import csv

# Define path to the file with the dataset
election_path = os.path.join("PyPoll","Resources", "election_data.csv")

# Open and read CSV file
with open(election_path,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
     # Read/Skip the header row
    csv_header = next(csv_file)

    # Set initial value for number of rows (headear row excluded)
    rowcount = 0

    # Create a list to hold candidates name
    candidate_names = []

    # Create a dictionary to hold candidate names and respective number of votes
    candidate_votes = {}

    # Loop through the dataset
    for row in csv_reader:
        # Count number of records on the data set (number of votes)
        rowcount += 1

        # Set first candidate name
        candidate = row[2]

        # Check if candidate name is already in the list
        if candidate not in candidate_names:

            # If not, add it to the list 
            candidate_names.append(candidate)

            # Reset the number of votes for newly added candidate to 0
            candidate_votes[candidate] = 0

        # Calculate the number of votes for a candidate as looping through the list
        candidate_votes[candidate] += 1

    # Create a dictionary to hold % of total number of votes for each candidate
    percent_votes = {} 
    
    # Calculate % of total number of votes for each candidate
    for candidate in candidate_votes:
        percentage = round(candidate_votes[candidate]/rowcount*100,3)
        percent_votes[candidate] = percentage 
    
    # Identify the winner
    winner = max(percent_votes, key=percent_votes.get)

# Print report header
print("Election Results\n----------------------------")

# Print total number of votes in the dataset
print(f"Total Votes:{rowcount}\n----------------------------")

# Print list of candidates with number of votes
for candidate in candidate_names:
    print(f"{candidate}:{percent_votes[candidate]}% ({candidate_votes[candidate]})")

print("----------------------------")

# Print a winner name
print(f"Winner:{winner}\n----------------------------")

# Define path to a file with the results
results_path = os.path.join("PyPoll","analysis", "results.txt")

# Export analysis results into a text file
with open(results_path, 'w') as txt_file:
        txt_file.write("Election Results\n----------------------------\n")
        txt_file.write(f"Total Votes:{rowcount}\n----------------------------\n")
        for candidate in candidate_names:
            txt_file.write(f"{candidate}:{percent_votes[candidate]}% ({candidate_votes[candidate]})\n")
        txt_file.write("----------------------------\n")
        txt_file.write(f"Winner:{winner}\n----------------------------")