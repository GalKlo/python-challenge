# Vote-counting analysis

This Python script analyzes election results dataset. 
The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

The script loops through the dataset and returns the following values:
1. The total number of votes cast
2. A complete list of candidates with
    2.1. The percentage of votes each candidate won
    2.2. The total number of votes each candidate won
3. The winner of the election based on popular vote

The script prints result of the analysis to the terminal and export a text file with the results.

## Improvement opportunities
Sort dataset by Candidate before conducting the analysis to make sure part of the script with the calculation of the vote numbers for each candidate works correctly. 