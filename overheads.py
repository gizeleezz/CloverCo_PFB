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

      


def highestOverheads(Overhead_expenses):
    highest_overhead=0.0
    name_of_overhead=""

    for expense in Overhead_expenses:
        if expense[1]> highest_overhead:
            highest_overhead=expense[1]
            name_of_overhead=expense[0]
    return f"[HIGHEST OVERHEAD]: {name_of_overhead}, {highest_overhead}%"
result=highestOverheads(Overhead_expenses)
print(result)