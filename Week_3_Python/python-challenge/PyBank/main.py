import os
import csv

# Create output text file
text_file = open("output.txt", "w")

# Create path for file
budgetdatacsv = os.path.join('.','Resource','homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

# Declare variables to store data in arrays
dates = []
average_net_change = []
monthAggregator = []

# Declare variables 
previousnumber = 0.0
monthsCounter = 0
TotalProfit = 0.0
# average_net_change = 0.0

# Read in the CSV file
with open(budgetdatacsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

     # first row is header
    header = next(csvreader)

# Loop through the data
    for row in csvreader:

        monthsCounter = int(monthsCounter + 1)

        TotalProfit = float(row[1]) + TotalProfit
       

        monthAggregator.append(row[1])

        dates.append(row[0])


        #difference.append(float(row[1])- previousnumber)
        average_net_change.append(float(row[1]) - previousnumber)
        
        previousnumber = float(row[1])
        

# Using pop to remove the first value of difference. - it is not valid becuase there is no value for calcultaion against first row
average_net_change.pop(0)


# Print results as text file
text_file.write("Financial Analysis\n------------------------\n")  
text_file.write(f"Total Months: {monthsCounter}\n")
text_file.write(f"Total: {TotalProfit}\n")
text_file.write(f"Average  Change: $ {sum(average_net_change)/len(average_net_change)}\n")


# Print results at terminal
print("Financial Analysis\n------------------------")
print(f"Total Months: {monthsCounter}")
print(f"Total: {TotalProfit}")
print(f"Average  Change: $ {sum(average_net_change)/len(average_net_change)}")



min_value = min(average_net_change)
max_value = max(average_net_change)
# 1 was added back because first row is removed (pop). This will give variance when calculating the average net change.
max_index = average_net_change.index(max_value) + 1
min_index = average_net_change.index(min_value) + 1

# Using min & max_index to find when (date) the greatest increase /decrease happend
max_date = dates[(max_index)]
min_date= dates[(min_index)]

text_file.write(f"Greatest Increase in Profits: {max_date} (${max_value})\n")
print(f"Greatest Increase in Profits: {max_date} (${max_value})")

text_file.write(f"Greatest Decrease in Profits: {min_date} (${min_value})\n")
print(f"Greatest Decrease in Profits: {min_date} (${min_value})")


#  Close output text file
text_file.close()