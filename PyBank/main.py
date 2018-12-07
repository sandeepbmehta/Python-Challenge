import os
import csv

def average(average_amount,change):
    #print(f'Inside the function1: {average_amount}, {change}')
    avg_amount = average_amount + change
    if avg_amount == 0:
        avg_amount = 0
    else:
        avg_amount /= 2
    
    #print(f'Inside the function2: {avg_amount}')
    return avg_amount

total_months = 0
total_amount = 0
change_amount = 0
total_change_amount = 0
prof_Date = ''
prof_amount = 0
loss_Date = ''
loss_amount = 0
csv_path = "../Resources/budget_data.csv"
with open (csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    #print(csvfile)
    #print(csv_reader)
    # Bypassing the header record
    header=next(csv_reader)
    print(header)
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
            total_change_amount += change_amount
            average_amount = average(average_amount,change_amount)
        #print (f'{row[0]}, {int(row[1])}, {change_amount}, {average_amount}', {total_change_amount})

total_change_amount /= (total_months - 1)
print(f'Total number of months: {total_months}')
print(f'Net amount "Profilt/Loss": $ {total_amount}')
print(f'Average Change: $ {total_change_amount}')