# Import CSV module   
import csv  
  
# Initialize variables  
highest_increment_day = 0     
highest_increment_amount = 0  
profit_deficit = 0  
  
# Open CSV file      
with open('profit_and_loss(2).csv') as file:  
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
            profit_deficit = previous_net_profit - current_net_profit  
            print(f"[PROFIT DEFICIT] DAY: {current_day}, AMOUNT: {profit_deficit} USD")  
              
        previous_net_profit = current_net_profit