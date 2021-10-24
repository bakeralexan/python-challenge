import os
import csv
csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = csvfile.readline()
    print("Financial Analysis")
    print("----------------------------")

    print(f"CSV: {csv_header}")

    
    current_month = 0
    previous_month = 0
    max_increase = 0
    max_month = []
    max_decrease = 0
    min_month = []
    delta_list = []
    budget_data = []

    row = ()
    total = 0

    for row in csvreader :
        lineNum = csvreader.line_num
        budget_data.append(row)
        
        dates = row[0]
        profit = row[1]
        total = int(total) + int(profit)
        current_month = row[1]
        delta = int(current_month) - int(previous_month)

        previous_month = int(current_month)
        delta_list.append(delta)

        
        if delta > max_increase:
            max_increase = delta
            max_month = dates
        
        if delta < max_decrease:
            max_decrease = delta
            min_month = dates


    delta_list.pop(0)

    print(f"Average Change : $", "{:.2f}".format(sum(delta_list)/(lineNum-1)))
    
    print(f"Total Months: {lineNum}")
    print(f"Total: ${total}")
    print(f"Greatest Increase in Profits: {max_month} ${max(delta_list)}")
    print(f"Greatest Decrease in Profits: {min_month} ${min(delta_list)}")