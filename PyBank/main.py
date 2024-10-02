# Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources","budget_data.csv")
output_csv_path = os.path.join(".","analysis","output.txt")

#Set Lists
date = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",9999999999999]
net_total = 0
average_change_list = []
total_months = 1

# # Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    first_row = next(csvreader)
    prev_net = int(first_row[1])
    net_total = int(first_row[1])
    
       # Loop to add all months
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])


        net_change = int(row[1])- prev_net
        prev_net = int(row[1])
        net_change_list  += [net_change]
        date += [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
       
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

avg_monthly_change = sum(net_change_list)/len(net_change_list)

final_output = (f"Financial Analysis\n"
                f"---------------------------\n"
                f"Total Months: {total_months}\n"
                f"Total:${net_total}\n"
                f"Average Change: {avg_monthly_change}\n"
                f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
                f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
print(final_output)
 
with open(output_csv_path, "w") as txt_file:
    txt_file.write(final_output)

