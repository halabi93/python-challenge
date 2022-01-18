import os
import csv

#initializing variables
total_number_of_months = 0
total_net = 0
first_PL = 0
second_PL = 0
total_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

#opening and reading file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #reading first line of file alone since it is the header
    first_row = next(csvreader)
    #loop thru the file
    for row in csvreader:
        total_number_of_months = total_number_of_months + 1
        total_net = total_net + int(row[1])
        #enter here to store the first profit/loss value
        if total_number_of_months == 1:
            first_PL = int(row[1])
        #get the second profit/loss value, calculate the change, increment the total change, 
        # and then assign the first_PL to be the second_PL in order to use it in our next calculation 
        else:
            second_PL = int(row[1])
            change = second_PL - first_PL
            total_change = total_change + change
            first_PL = second_PL
            #looking for the greatest increase and greatest decrease in the profit/loss
            if greatest_increase < change:
                greatest_increase = change
                greatest_increase_date = row[0]
            if greatest_decrease > change:
                greatest_decrease = change
                greatest_decrease_date = row[0]

#create the results text file, print the results in it, and print the results in the terminal
output_file = os.path.join("analysis", "results.txt")

with open(output_file, "w", encoding="utf-8") as datafile:
    writer = csv.writer(datafile) 
    writer.writerow([str("Financial Analysis")])
    print("Financial Analysis")
    writer.writerow([str("----------------------------")])
    print("----------------------------")
    x = "Total Months: " + str(total_number_of_months)
    writer.writerow([str(x)])
    print(x)
    x = "Total: $" + str(total_net)
    writer.writerow([str(x)])
    print(x)
    x = "Average Change: $" + str(round(total_change/(total_number_of_months - 1),2))
    writer.writerow([str(x)])
    print(x)
    x = "Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase)  + ")"
    writer.writerow([str(x)])
    print(x)
    x = "Greatest Decrease in Profits: "+ greatest_decrease_date + " ($" + str(greatest_decrease) + ")"
    writer.writerow([str(x)])
    print(x)