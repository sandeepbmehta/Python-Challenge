import os
import csv

total_months = 0
total_amount = 0
change_amount = 0
total_change_amount = 0
prof_Date = ''
prof_amount = 0
prev_prof_amount = 0
loss_Date = ''
loss_amount = 0
prev_loss_amount = 0
csv_path = "../Resources/budget_data.csv"
with open (csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    # Bypassing the header record
    header=next(csv_reader)
    #print(header)
    for row in csv_reader:
        amount = int(row[1])
        total_months += 1
        total_amount += amount
        if total_months == 1:
            # This is valid only for the first data record
            prev_amount = amount
            average_amount = amount
            prof_Date = row[0]
            loss_Date = row[0]
            prof_amount = amount
            loss_amount = amount
        else:
            change_amount = amount - prev_amount
            prev_amount = amount
            
            if change_amount > prev_prof_amount:
                prev_prof_amount = change_amount
                prof_Date = row[0]
                prof_amount = amount
            else:
                if change_amount < prev_loss_amount:
                    prev_loss_amount = change_amount
                    loss_Date = row[0]
                    loss_amount = amount

            total_change_amount += change_amount


total_change_amount /= (total_months - 1)

# creating the display and write variables
Display_total = str("Total number of months: " + str(total_months))
Display_net_amount = str("Net amount Profilt/Loss: $ ") + str(total_amount)
Display_avg_chg = str("Average Change: $ ") + str(total_change_amount)
Display_grt_prof = str("Greatest Increase in profit: ") + str(prof_Date) + " " + str(prof_amount)
Display_grt_loss = str("Greatest Decerease in profit: ") + str(loss_Date) + " " + str(loss_amount)

# Displaying and writing the output file simultaneously
output_path = "../Resources/pybank_results.txt"
with open (output_path, 'w') as outfile:
    print(Display_total)
    outfile.write(Display_total)
    outfile.write('\n')
    print(Display_net_amount)
    outfile.write(Display_net_amount)
    outfile.write('\n')
    print(Display_avg_chg)
    outfile.write(Display_avg_chg)
    outfile.write('\n')
    print(Display_grt_prof)
    outfile.write(Display_grt_prof)
    outfile.write('\n')
    print(Display_grt_loss)
    outfile.write(Display_grt_loss)
