import os
import csv

input_path = os.path.join(os.path.dirname(__file__),"Resources","budget_data.csv")
output_path = os.path.join(os.path.dirname(__file__), "Analysis", "budget_data.txt")

print(input_path)

# Open and read the CSV file
with open(input_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

# Skip the header row
    next(csv_reader)

# Establish variables for profit and months to separate the columns
    months = []
    profits = []

    for row in csv_reader:
        months.append(row[0])
        profits.append(int(row[1]))

# Find the total months included in the dataset
total_months = len(months)

# Find the net total amount of "Profit/Losses" over the entire period
net_profit = sum(profits)

# Find the changes in "Profit/Losses" over the entire period
month_changes = [profits[i] - profits[i - 1] for i in range(1, total_months)]

# Find the average of the changes over the entire period (adding the -1 to avoid any 0's)
average_change = sum(month_changes) / (total_months - 1)

# Find the greatest increase in profits (date and amount) over the entire period
greatest_increase_index = month_changes.index(max(month_changes)) + 1
greatest_increase_date = months[greatest_increase_index]
greatest_increase_amount = max(month_changes)

# Find the greatest decrease in profits (date and amount) over the entire period
greatest_decrease_index = month_changes.index(min(month_changes)) + 1
greatest_decrease_date = months[greatest_decrease_index]
greatest_decrease_amount = min(month_changes)

# Creating the report
output = "Financial Analysis\n"
output += "------------------------\n"
output += f"Total Months:, {total_months}\n"
output += f"Total: {net_profit}\n"
output += f"Average Change: ${average_change}\n"
output += f"Greatest Increase in Profits:" f"{greatest_increase_date}: (${greatest_increase_amount})\n"
output += f"Greatest Decrease in Profits:" f"{greatest_decrease_date}: (${greatest_decrease_amount})\n"



print(output)

with open(output_path, "w") as file1:
    # Writing data to a file
    file1.write(output)
