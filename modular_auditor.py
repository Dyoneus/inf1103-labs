# Week 3 - Modular Auditor

# get_valid_input() handles the prompt, input validation and return a valid integer or a "quit" signal
# input none | output valid stock quantity, "quit" or invalid status

# process_delivery(current_total, new_value) calculates the new total and returns it
# input current inventory and new value | output updated inventory

# calculate_tax(amount) a new requirement, this function takes a delivery amount and returns the tax (10% of that specific delivery)
# input delivery amount | output 10% tax for that delivery

# generate report(total_units, failed_attempts) a dedicated function to print the final summarry
# input final inventory and failed attempts count | output the final report

# process delivery that returns updated inventory
def process_delivery(current_total, new_value):
    return current_total + new_value


# calculate tax for each delivery, return amount * 0.10%
def calculate_tax(amount):
    return amount * 0.10

# get_valid_input 
def get_valid_input():
    stock_input = input("Enter stock quantity or 'quit' to exit: ").strip()

    if stock_input.lower() == 'quit':
        return "quit"

    #negative number error message
    if stock_input.startswith("-") and stock_input[1:].isdigit():
        print("Error: Stock quantity cannot be negative.")
        return None

    #reject text and other invalid values
    if not stock_input.isdigit():
        print("Error: Please enter a valid integer.")
        return None

    return int(stock_input)


# generate report
def generate_report(total_units, failed_attempts):
    print("\nAudit Report")
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)