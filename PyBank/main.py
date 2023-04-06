import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
profit = []
total = []
previous_profit = None
total_change = 0
num_changes = 0
max_month = []
min_month = []
max_increase = 0
max_decrease = float('inf')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        current_month = row[0]
        current_profit = int(row[1])
        
        months.append(row[0])
        total.append(float(row[1]))
        
        if previous_profit is not None:
            change = current_profit - previous_profit
            total_change += change
            num_changes += 1

            if change > max_increase:
                max_increase = change
                max_month = current_month
            
            if change < max_decrease:
                max_decrease = change
                min_month = current_month

        previous_profit = current_profit

if num_changes > 0:
    average_change = total_change / num_changes
else:
    average_change = 0

num_months = len(months)
total_pl = sum(total)

print("Financial Analysis")
print()
print("--------------------------")
print()
print(f"Total Months: {num_months}")
print()
print(f"Total: ${total_pl:.0f}")
print()
print(f"Average Change: {average_change:.2f}")
print()
print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
print()
print(f"Greatest Decrease in Profits: {min_month} (${max_decrease})")

output_file = os.path.join("financial_analysis.csv")

with open("financial_analysis.txt", "w") as file:
    
    file.write("Financial Analysis\n")
    file.write("\n")
    file.write("--------------------------\n")
    file.write("\n")
    file.write(f"Total Months: {num_months}\n")
    file.write("\n")
    file.write(f"Total: ${total_pl:.0f}\n")
    file.write("\n")
    file.write(f"Average Change: {average_change:.2f}\n")
    file.write("\n")
    file.write(f'Greatest Increase in Profits: {max_month} (${max_increase})\n')
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {min_month} (${max_decrease})\n")