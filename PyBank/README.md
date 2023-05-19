# Financial record analysis

This Python script analyzes a financial records of a company. 
Original data set is composed of two columns: "Date" and "Profit/Losses".

The script loops through the dataset and returns:
1. The total number of months included in the dataset.
2. The net total amount of "Profit/Losses" over the entire period.
3. The changes in "Profit/Losses" over the entire period, and then the average of those changes.
4. The greatest increase in profits (date and amount) over the entire period.
5. The greatest decrease in profits (date and amount) over the entire period.

The script prints result of the analysis to the terminal and export a text file with the results.

## Improvement opportunities
Sort dataset first to make sure months are in an ascending/descending order and confirm each line represents a differnt month record.