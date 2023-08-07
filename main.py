from pathlib import Path

# Import your functions
from Cash_on_hand import analyse_cash_on_hand
from overheads import highestOverheads
from Profit_Loss import profit_and_loss

def main():
    # Set the file path for the summary report file
    file_path_write = Path.cwd() / "summary_report.txt"

    # Open the file for writing and generate the summary report
    with open(file_path_write, "w") as file:

        file.write
        highestOverheads("\Users\gisel\CloverCo_PFB\CloverCo_PFB-8\overheads.py")  # Update forex accordingly
        file.write("\n")

        file.write
        analyse_cash_on_hand(z)  # Update forex accordingly
        file.write("\n")

        file.write
        profit_and_loss()  # Update forex accordingly

if __name__ == "__main__":
    main()




    
 





