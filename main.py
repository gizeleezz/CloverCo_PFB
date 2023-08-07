from pathlib import Path
from Cash_on_hand import analyse_cash_on_hand
from overheads import highestOverheads
from Profit_Loss import profit_and_loss

def main():
    # Set the file path for the summary report file
    file_path_write = Path.cwd() / "summary_report.txt"

    # Call the functions and capture the output
    overheads_output = highestOverheads()
    cash_on_hand_output = analyse_cash_on_hand()
    profit_loss_output = profit_and_loss()

    # Open the file for writing and generate the summary report
    with open(file_path_write, "w") as file:
        
        file.write(overheads_output)
        file.write("\n\n")

        
        file.write(cash_on_hand_output)
        file.write("\n\n")

        
        file.write(profit_loss_output)
        file.write("\n\n")

if __name__ == "__main__":
    main()




    
 





