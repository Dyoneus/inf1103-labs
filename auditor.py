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

    #reject text or other values that are not whole numbers
    if not stock_input.isdigit():
        print("Error: Please enter a valid integer.")
        failed_entries += 1
        continue

    #user input is safe to convert after it has pass the validation
    quantity = int(stock_input)

    #keep a total of all accepted stock
    inventory += quantity

    print(f"Current inventory:", inventory)

    #stop processing once t he storage limit has been exceeded
    if inventory > 500:
        print("Overstock Alert: Inventory exceeds 500 units.")
        break