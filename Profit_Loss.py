# Import CSV module   
import csv  
from pathlib import Path
  
  
# Open CSV file    
csv_folder_path=Path.cwd()/ "csv_reports"

file_path=csv_folder_path/"profit_and_loss(2).csv"

def profit_and_loss(file_path):
    # Initialize variables  
    profit_deficit_days=[]
    highest_increment_day=0
    highest_increment_amount=0
    previous_net_profit=0
    previous_net_profit= None

    with open(file_path) as file:  
        reader = csv.reader(file)  
      
    # Skip header row  
        next(reader)

        
          
   
      
    # Iterate through rows  
        for row in reader:  
            current_day = int(row[0])   
            current_net_profit = int(row[4])   
            
            # Check if net profit decreased    
            if previous_net_profit: 
                if current_net_profit < previous_net_profit:  
                    deficit_amount = previous_net_profit - current_net_profit  
                    profit_deficit_days.append((current_day,deficit_amount))
                   
                    
                    
            else:
                if previous_net_profit is not None:
                    increment= current_net_profit - previous_net_profit
                    if increment > highest_increment_amount:
                        highest_increment_day=current_day
                        highest_increment_amount=increment
                        
            previous_net_profit=current_net_profit
        
        for day, amount, in profit_deficit_days:
            print(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: {amount} USD")
        if highest_increment_day != 0:
            print("[ NET PROFIT SURPLUS ] : Net profit each day is higher than previous day")
            print(f"[HIGHEST NET PROFIT SURPLUS]  Day: {highest_increment_day}, Amount: {highest_increment_amount} USD")    

profit_and_loss(file_path)

            