# Import OS library to create a path to the file
import os

# Import CSV library to read dataset stored in csv format
import csv

# Define path to the file with the dataset
budget_path = os.path.join("PyBank","Resources", "budget_data.csv")

# Open and read CSV file
with open(budget_path,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read/Skip the header row
    csv_header = next(csv_file)
    
    # Set initial value for number of rows (headear row excluded)
    rowcount = 0

    # Set initial value net profit_loss
    net_profit_loss = 0

    # Set initial value for the changes in "Profit/Losses" over entire period
    sum_change = 0

    # Set initial value for a previous period profit_loss
    last_month_profit = 0

    # Set initial value for greatest increase in profit
    great_profit_incr = 0

    # Set initial value for greatest decrease in profit
    great_profit_decr = 0

    # Loop through the dataset
    for row in csv_reader:
        # Count number of records on the data set (number of months)
        rowcount += 1

        # Calculate net total amount of "Profit/Losses"
        profit_loss = float (row[1])
        net_profit_loss += profit_loss
        round_net_profit_loss = round(net_profit_loss)

        # Calculate total change for "Profit/Losses" over entire period           
        if rowcount >1 :
            profit_dif = profit_loss - last_month_profit
            sum_change += profit_dif 

            # Find greatest profit increase
            if profit_dif > great_profit_incr :
                great_profit_incr = profit_dif
                incr_month = row [0]

             # Find greatest profit decrease
            if profit_dif < great_profit_decr :
                great_profit_decr = profit_dif
                decr_month = row[0]
            
         # Adjust previous month "Profit/Losses" value
        last_month_profit = profit_loss   

    # Calculate average profit change over entire period
    avg_profit_change = sum_change/(rowcount-1)
    round_avg_profit_change = round(avg_profit_change,2)

# Print report header
print("Financial Analysis\n----------------------------")

# Print total number of months in the dataset
print(f"Total Months:{rowcount}")

# Print net total amount of "Profit/Losses"
print(f"Total: $ {round_net_profit_loss}")
    
# Print average for "Profit/Losses"
print(f"Average Change: $ {round_avg_profit_change}")

# Print greatest increase in profit
print(f"Greatest Increase in Profits: {incr_month} (${great_profit_incr})")

# Print greatest decrease in profit
print(f"Greatest Decrease in Profits: {decr_month} (${great_profit_decr})")

# Define path to a file with the results
results_path = os.path.join("PyBank","analysis", "results.txt")

# Export analysis results into a text file
with open(results_path, 'w') as txt_file:
        txt_file.write("Financial Analysis\n----------------------------\n")
        txt_file.write(f"Total Months:{rowcount}\n")
        txt_file.write(f"Total: $ {round_net_profit_loss}\n")
        txt_file.write(f"Average Change: $ {round_avg_profit_change}\n")
        txt_file.write(f"Greatest Increase in Profits: {incr_month} (${great_profit_incr})\n")
        txt_file.write(f"Greatest Decrease in Profits: {decr_month} (${great_profit_decr})\n")