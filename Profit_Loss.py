# Import CSV module   
import csv  
from pathlib import Path
  
  
# Open CSV file    
csv_folder_path=Path.cwd()/ "csv_reports"

file_path=csv_folder_path/"profit_and_loss(2).csv"

def profit_and_loss():
    """ This function analyses profit and loss csv to find profit deficits if current day profit is less than previous day or
     find the highest net profit surplus and day if net prfit is always increasing 

     parameters: (file_path)= path to csv file that contains profit and loss data

     Function returns day and profit deficit if net profit on current day is less than previous day 
     if net profit is always increasing, function will return highest net profit increment and day 
    """
    # Initialize variables  
    profit_deficit_days=[] # store days with profit deficit
    highest_increment_day=0 # store day with highest net profit increment
    highest_increment_amount=0 # store the amount of the highest net profit increment
    previous_net_profit= None # initialise as none 

    # open csv file
    with open(file_path) as file:  
        reader = csv.reader(file)  
      
    # Skip header row  
        next(reader)

        
          
   
      
    # Iterate through rows of csv file
        for row in reader:  
            current_day = int(row[0])   
            current_net_profit = int(row[4])   
            
            # Check if net profit decreased    
            if previous_net_profit: 
                if current_net_profit < previous_net_profit:  
                    deficit_amount = previous_net_profit - current_net_profit  
                    profit_deficit_days.append((current_day,deficit_amount))
                   
                    
                 # check for highest net profit increment   
            else:
                if previous_net_profit is not None:
                    increment= current_net_profit - previous_net_profit
                    if increment > highest_increment_amount:
                        highest_increment_day=current_day
                        highest_increment_amount=increment
            # update previous_net_profit for the next iteration            
            previous_net_profit=current_net_profit
        result = ""
        for day, amount in profit_deficit_days:
            result += f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: {amount} USD\n"
        if highest_increment_day != 0:
            result += "[ NET PROFIT SURPLUS ] : Net profit each day is higher than previous day\n"
            result += f"[HIGHEST NET PROFIT SURPLUS]  Day: {highest_increment_day}, Amount: {highest_increment_amount} USD\n"
    return result

# Call function to analyse profit or loss
profit_loss_output = profit_and_loss()
print(profit_loss_output)
            