# Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "budget_data.csv")

# Set variable 
count = 0
previous_month_amount = 0
profitlosses_amount = row[1]
date = row[0]
change = 0

max_value = None

#Set Lists
date = []
change = []
max_profit = []
max_loss = []
average_change_list = []

# # Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
       # Loop to add all months
    for row in csvreader:
        
        date.append(row[0])

        count = int(row[0]) + count

       
        if prevous_month_amount is not None:
            if profitlosses_amount > max_value:
                max_profit.append()
                else
                max_loss.append()
           
           change = profitlosses_amount - previous_month_amount
           change.append()



        


# Specify the file to write to
output_path = os.path.join("..", "Analysis")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(print)

    # Write the second row
    csvwriter.writerow(print)
