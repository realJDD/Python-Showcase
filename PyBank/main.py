# Dependencies
import csv
import os

# Specify the file
budget_csv = os.path.join("Resources", "budget_data.csv")

#Lists to store data
total_months = []
net_profit_loss = []
rate_of_change = []

#Open the CSV
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#Read the header row first
    csv_header = next(csvreader)
    for row in csvreader:
        total_months.append(row[0])
        net_profit_loss.append(row[1])

#Open the textfile
with open('Output.txt', 'w') as txt:

#Find total number of Months
    TM = len(total_months)
    print("```")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {TM}")
    print(f"Total Months: {TM}",file=txt)

#txt.write(f"Total Months: {TM}\n")

#Sum the net total amount of profit/lost:
    sum_NPL = 0
    for i in net_profit_loss:
        sum_NPL = sum_NPL + int(i)
        rate_of_change.append(sum_NPL)
    print(f"Total: ${sum_NPL}")
    print(f"Total: ${sum_NPL}",file=txt)

#txt.write(f"Total: ${sum_NPL}\n")

#Find first element in the list
    F = int(net_profit_loss[0])
#Find last element in the list
    L = int(net_profit_loss[-1])
#Get average of the changes value
    ROC = (L - F)/(len(net_profit_loss)-1)
    ROC = round(ROC, 2)
    print(f"Average Change: ${ROC}")
    print(f"Average Change: ${ROC}",file=txt)

    #txt.write(f"Average Change: ${ROC}\n")

#Find the difference in successive months
    x = 1
    y = 0
    diff = [0]
    for i in range(0, len(net_profit_loss) - 1):
        diff.append(int(net_profit_loss[x]) - int(net_profit_loss[y]))
        x += 1
        y += 1

#Find greatest increase in profits
    g_inc = 0
    for i in diff:
        if g_inc < i:
            g_inc = i

#Find greatest decrease in profits
    g_dec = 0
    for i in diff:
        if i < g_dec:
            g_dec = i

#Zip Lists
    zipped_inc = []
    zipped_dec = []
    zipped_inc = zip(total_months, net_profit_loss, diff)
    zipped_dec = zip(total_months, net_profit_loss, diff)

#date and time of greatest increase
    for row in zipped_inc:
        if (g_inc == row[2]):
            print(f"Greatest Increase in Profits: {row[0]} (${row[2]})")
            print(f"Greatest Increase in Profits: {row[0]} (${row[2]})",file=txt)

    #txt.write(f"Greatest Increase in Profits: {row[0]} (${row[2]})\n")

#date and time of greatest decrease
    for row in zipped_dec:
        if (g_dec == row[2]):
            print(f"Greatest Decrease in Profits: {row[0]} (${row[2]})")
            print(f"Greatest Decrease in Profits: {row[0]} (${row[2]})",file=txt)
    print("```")
