from Cash_on_hand import analyse_cash_on_hand
from overheads import highestOverheads
from Profit_Loss import profit_and_loss

def main():
    # Define file_path appropriately in your code
    subfolder_path = "csv_reports"  # Update if necessary
    file_path_cash_on_hand = subfolder_path + "/Cash_on_Hand.csv"
    file_path_profit_loss = subfolder_path + "/profit_and_loss(2).csv"

    # Call the functions directly with the defined file_path and other arguments
    highestOverheads(file_path_profit_loss)  # Update forex accordingly
    analyse_cash_on_hand(file_path_cash_on_hand)  # Update forex accordingly
    profit_and_loss(file_path_profit_loss)  # Update forex accordingly

    main()

