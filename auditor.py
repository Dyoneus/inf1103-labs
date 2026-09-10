#Smart Inventory Auditor

#keeps track of the current amount of stock
inventory = 0

#counts inputs that the program rejects
failed_entries = 0

#keep asking for stock until te program is told to stop
while True:
    stock_input = input("Enter the amount of stock to add or type 'quit' to stop): ").strip()

    #stop when the operator has finished entering stock
    if stock_input.lower() == 'quit':
        break

    #negative stock should not be added to inventory
    if stock_input.startswith('-') and stock_input[1:].isdigit():
        print("Error: Stock quantity cannot be negative.")
        failed_entries += 1
        continue