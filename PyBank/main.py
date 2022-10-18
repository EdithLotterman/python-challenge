#create variables
#list of months
months = []
#list of profit/loss amounts by month
profit_loss = []
#variable to calculate cumuative profit/loss
total_profit_loss = 0
#list of cumulative profit loss
list_total_pandl = []
#variable to track previous p&l in order to calculate change in p&l. Set to row index to calculate row1, then reset every loop
previous = 0    
#variable to calculate change in profits/losses
change_pandl = 0
#list to track change in profit/loss
list_change_pandl = []


#import modules
from calendar import month
import os
import csv
from pickletools import int4

##store filepath as variable
filepath = os.path.join("..", "Resources", "budget_data.csv")

#open file
with open(filepath, newline = '', encoding='utf-8') as budget_file:

    #CSV reader specifying variable and delimiter
    reader = csv.reader(budget_file, delimiter = ',')

    #skip first row of csv file
    next(reader)

    #Loop through rows 
    for row in (reader):

        #update months list
        months.append(row[0])

        #update profits/losses list
        profit_loss.append(float(row[1]))

        #update cumulative profit/loss amount
        total_profit_loss +=float(row[1])

        #update cumulative profit/loss list
        list_total_pandl.append(total_profit_loss)

        #calculate change in profit/loss
        change_pandl = float(row[1])  - previous
        
        #update change in profit/loss list
        list_change_pandl.append(float(change_pandl))

        #update previous variable
        previous = float(row[1])

#update first month's change in profit/losses to null
list_change_pandl[0] = int()

#calculate average change in profit/loss
sum = sum(list_change_pandl)
ave = sum/(len(list_change_pandl)-1)

# Create dictionary
keys = list_change_pandl
values = months
dictionary = dict(zip(keys, values))

#Max profit loss
max = max(list_change_pandl)

#min profit loss
min = min(list_change_pandl)

#Print results to terminal
print(f"Total months: {len(months)}")
print(f"Total: {list_total_pandl[-1]}")
print(f"Average Change: {ave}")
print(f"Greatest increase in profit: {dictionary[max]} (${max})")
print(f"Greatest decrease in profit: {dictionary[min]} (${min})")

#print to csv
#specify output path file
output_path = os.path.join("..", "Analysis",'PyBankAnalysis.csv')

#open the file
with open(output_path, 'w', newline="") as csvfile:

    #initialize csv writer
    writer = csv.writer(csvfile)

    #write rows
    writer.writerow([f"Total months: {len(months)}"])
    writer.writerow([f"Total: {list_total_pandl[-1]}"])
    writer.writerow([f"Average Change: {ave}"])
    writer.writerow([f"Greatest increase in profit: {dictionary[max]} (${max})"])
    writer.writerow([f"Greatest decrease in profit: {dictionary[min]} (${min})"])
