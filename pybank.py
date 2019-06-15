#import module(s)
import os 
import csv

#csvpath
csvpath = os.path.join('Resources', 'budget_data.csv')

#read with csv module 
with open(csvpath, newline='') as csvfile:
    
    #csvreader
    csvreader = csv.reader(csvfile, delimiter=',')

    #initializing list of date and pnl
    date = []
    change_date = []
    pnl = []
    rows = []
    #read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #read each row of data after the header
    for row in csvreader:
        date.append(row[0])
        change_date.append(row[0])
        pnl.append(int(row[1]))
        rows.append(row)

    change_date.remove("Jan-2010")

    
    print('Financial Analysis')
    print('------------------------------------------')
    #total months
    print(f"Total Months: {len(date)}")
    

    #total profit and losses
    total = sum(pnl)
    print(f"Total: ${total}")

    #average change
    change = [int(pnl[i+1]-pnl[i]) for i in range(len(pnl)-1)]
    change_sum = sum(change)
    average_change = round(int(change_sum) / int(len(change)), 2)
    print(f"Average Change: ${average_change}")
    
    #greatest increase in profit
    increase = 0 
    for i in change:
        if i > increase:
            increase = i
    #index of element
    index = change.index(increase)
    date_increase = change_date[index]
    print(f"Greatest Increase in Profits: {date_increase}, ${increase}")

    #greatest decrease in profit
    decrease = 0
    for i in change:
        if i < decrease:
            decrease = i 
    #index of element
    index_2 = change.index(decrease)
    date_decrease = change_date[index_2]
    print(f"Greatest Decrease in Profits: {date_decrease}, ${decrease}")


#export text file 
file = open("output.txt", "w+")

file.write("Financial Analysis\n")
file.write("---------------------\n")
file.write(f"Total Months: {len(date)}\n")
file.write(f"Total: ${total}\n")
file.write(f"Average Change: ${average_change}\n")
file.write(f"Greatest Increase in Profits: {date_increase}, ${increase}\n")
file.write(f"Greatest Decrease in Profits: {date_decrease}, ${decrease}\n")

