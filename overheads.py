import csv
from pathlib import Path

# Specify the path to the "csv report" subfolder
subfolder_path = Path.cwd() / "csv_reports"

# Combine the subfolder path with the filename to get the complete file path
file_path = subfolder_path / "Overheads.csv"

# Read the csv file to append profit and quantity from the csv.
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    # Create an empty list to store overhead records
    Overhead_expenses = []

    # Append overhead category and overhead percentage into the Overhead_expense list
    for row in reader:
        Overhead_expenses.append([row[0], float(row[1])])

      

# Create a function to find the highest overhead 
def highestOverheads():
    """ This function finds and returns the highest overhead expense and the corresponding percentage 
        parameters : overhead_expenses:a list that consists of overhead expenses, that contains name of overhead and corresponding percentage
        The function will return the name of overhead and percentageof highest overhead expense
    """
    highest_overhead=0.0
    name_of_overhead=""
    # Iterate through the overhead expenses to find the highest
    for expense in Overhead_expenses:
    # Check to see if the current expense percentage is higher than the highest amount previously discovered
        if expense[1]> highest_overhead:
        # Updating the highest overhead and the overhead category name that corresponds
            highest_overhead=expense[1]
            name_of_overhead=expense[0]
    # Return function indicating the name of highest overhead and the percentage
    return f"[HIGHEST OVERHEAD]: {name_of_overhead}, {highest_overhead}%"
# Run the highestOverheads function, then save the outcome
result=highestOverheads()
print(result)