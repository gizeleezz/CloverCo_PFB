from pathlib import Path
from cash_on_hand import analyse_cash_on_hand
from overheads import highestOverheads
from profit_loss import profit_and_loss

def main():
    """
     This function generates a summary report by calling various functions and writing their outputs to a text file.

     calls the highestOverheads, analyse_cash_on_hand, and profit_and_loss functions to capture their
    outputs. It then opens a file for writing and generates a summary report containing the outputs of the called
    functions.
    """
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




    
 





