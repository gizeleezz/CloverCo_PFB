# Import CSV module   
import csv  
from pathlib import Path
  
# Initialize variables  
profit_deficit_day = 0     
profit_deficit_amount = 0  

  
# Open CSV file    
csv_folder_path=Path.cwd()/ "csv_reports"

file_path=csv_folder_path/"profit_and_loss(2).csv"

with open(file_path) as file:  
    reader = csv.reader(file)  
      
    # Skip header row  
    next(reader)  
          
    # Read first row           
    row = next(reader)         
    previous_net_profit = int(row[4])   
      
    # Iterate through rows  
    for row in reader:  
        current_day = int(row[0])   
        current_net_profit = int(row[4])   
          
        # Check if net profit decreased     
        if current_net_profit < previous_net_profit:  
            profit_deficit_amount = previous_net_profit - current_net_profit  
            #Update highest deficit 
            if profit_deficit_amount>profit_deficit_amount:
                profit_deficit_day= current_day
                profit_deficit_amount=current_net_profit
        previous_net_profit = current_net_profit
    print(f"[PROFIT DEFICIT] DAY: {current_day}, AMOUNT: {profit_deficit_amount} USD")  