#import dependencies and set up data
import os
import csv
csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = csvfile.readline() #skip the header so that it does not impact later calculations 
    print("Financial Analysis")
    print("----------------------------")
    print(f"CSV: {csv_header}")
    # set variables before they are used in the loop and if statements
    #variables to calculate yearly change
    current_month = 0
    previous_month = 0
    #variables for calculating greatest increase and decrease in profits
    max_increase = 0
    max_month = [] #variable to display month of greatest increase and decrease in profits
    max_decrease = 0
    min_month = []
    delta_list = []
    row = () #index variable
    total = 0

    for row in csvreader :
        lineNum = csvreader.line_num #count rows to calculate average change formula
        dates = row[0]
        profit = row[1]
        total = int(total) + int(profit)
        current_month = row[1]
        delta = int(current_month) - int(previous_month) #equation to calculate yearly change, use int() to declare them as the integer type
        previous_month = int(current_month)
        delta_list.append(delta)
        #if statement to calculate greatest increase in profit and display corresponding month
        if delta > max_increase:
            max_increase = delta
            max_month = dates
        #if statement to calculate greatest decrease in profit and display corresponding month
        if delta < max_decrease:
            max_decrease = delta
            min_month = dates

    delta_list.pop(0) #delete the first value because "current - previous" will not be accurate if there is no previous value

    print("Average Change : $%.2f" %(sum(delta_list)/(lineNum-1))) #average change formula and formatting
    print(f"Total Months: {lineNum}")
    print(f"Total: ${total}")
    print(f"Greatest Increase in Profits: {max_month} ${max(delta_list)}")
    print(f"Greatest Decrease in Profits: {min_month} ${min(delta_list)}")