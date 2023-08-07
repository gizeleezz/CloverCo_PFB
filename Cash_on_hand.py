from pathlib import Path
import csv

# Open CSV file    
csv_folder_path=Path.cwd()/ "csv_reports"

file_path=csv_folder_path/"Cash_on_Hand.csv"

    # read the csv file to append profit and quantity from the csv.
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

    # create an empty lists to store the values for all 90 days
        cash_on_hand = []

        # append time sheet and sales record into the salesRecords list
        for row in reader:
            cash_on_hand.append([row[0], float(row[1])])

def analyse_cash_on_hand():
    """ This function reads cash on hand data from csv file and calculates cash deficits if cash on hand is lower on current day than previous day
        or, it will find the highest cash surplus if cash on hand is always increasing 

        Function return cash deficit or cash surplus day and amount
    """

    is_increasing=True # Flag to track if cash on each day is increasing
    cash_deficits = [] # List to store cash deficits for each day

    previous_cash = cash_on_hand[0][1]  # Cash-on-Hand on the first day
    highest_increment = 0  # Initialize the highest increment to 0

# Iterate through cash_on_hand starting from the second day
    for day, cash in cash_on_hand[1:]:  # Starting from the second day
        if cash > previous_cash:
            increment = cash - previous_cash # Calculate the cash increment from the previous day
            if increment > highest_increment:
                highest_increment = increment # Update the highest increment when necessary
        
        else:
            is_increasing = False # Cash on current day is not higher, it is FALSE

        deficit = previous_cash - cash   # Calculate the cash deficit
        cash_deficits.append([day, deficit])  # Store the day and deficit in the cash_deficits list
        previous_cash = cash  # Update previous_cash for the next iteration

    # Print the results based on the flag and stored data
    result = ""
    
    if is_increasing:
        result += "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        result += f"[HIGHEST CASH SURPLUS]: Day {day}, Amount: USD{round(highest_increment, 2)}\n"
    else:
    
        
        for day, deficit in cash_deficits:
            deficit_rounded = round(deficit, 2)
            result += f"[CASH DEFICIT] Day:{day}, AMOUNT: USD{deficit_rounded}\n"
    
    return result

# Call the analyse_cash_on_hand() function
cash_on_hand_output = analyse_cash_on_hand()
print(cash_on_hand_output)