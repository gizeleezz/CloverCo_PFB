# Import CSV module  
import csv 
 
# Initialize variables 
highest_increment_day = 0    
highest_increment_amount = 0 
 
with open('Cash_on_Hand.csv') as file: 
    reader = csv.reader(file) 
    
# Skip header row 
    next(reader) 

    # create an empty lists to store the values for all 90 days
    cash_on_hand = []

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        cash_on_hand.append([row[0], float(row[1])])

cash_deficits = []

previous_cash = cash_on_hand[0][1]  # Cash-on-Hand on the first day
highest_increment = 0  # Initialize the highest increment to 0

for day, cash in cash_on_hand[1:]:  # Starting from the second day
    if cash > previous_cash:
        increment = cash - previous_cash # Calculates increment value
        if increment > highest_increment:
            highest_increment = increment
    else:
        deficit = previous_cash - cash  
        cash_deficits.append([day, deficit])
    previous_cash = cash

# Print the cash deficits and the days of cash deficits
print("Cash-on-Hand is not always increasing.")
print("Cash Deficits:")
for day, deficit in cash_deficits:
    deficit_rounded = round(deficit, 3)
    print(f"Day {day}, Cash Deficit AMOUNT: USD{deficit_rounded}") # Prints highest cash deficeit and day.  