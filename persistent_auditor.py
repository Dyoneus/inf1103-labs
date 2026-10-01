# Week 4 - Persistent Auditor

# get_valid_input() handles the prompt, input validation and return a valid integer or a "quit" signal
# input none | output valid stock quantity, "quit" or invalid status

# process_delivery(current_total, new_value) calculates the new total and returns it
# input current inventory and new value | output updated inventory

# calculate_tax(amount) a new requirement, this function takes a delivery amount and returns the tax (10% of that specific delivery)
# input delivery amount | output 10% tax for that delivery

# generate report(total_units, failed_attempts) a dedicated function to print the final summarry
# input final inventory and failed attempts count | output the final report

# load inventory saved from the previous run
def load_inventory():
    with open("inventory.txt", "a") as file:
        file.write("")

    with open("inventory.txt", "r") as file:
        data = file.readlines()

    # first run, create empty file
    if len(data) == 0:
        return 0, []

    total_units = int(data[0])
    transaction_history = []

    # if the first line is the total
    for line in data[1:]:
        transaction_history.append(int(line))

    return total_units, transaction_history

def get_valid_input():
    stock_input = input("Enter stock quantity or 'quit' to stop: ")

    if stock_input == "quit":
        return "quit"

    # reject negative amounts
    if not stock_input.isdigit():
        print("Error: Please enter a non-negative whole number.")
        return "invalid"

    return int(stock_input)

# process delivery that returns updated inventory
def process_delivery(current_total, new_value):
    return current_total + new_value


# calculate tax for each delivery, return amount * 0.10%
def calculate_tax(amount):
    return amount * 0.10


# generate report
def generate_report(total_units, failed_attempts):
    print("\nAudit Report")
    print("Total Units Processed: ", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

# start of main
inventory, transaction_history = load_inventory()
failed_entries = 0
deliveries_processed = 0

print("Starting inventory: ", inventory)
print("Loaded history: ", transaction_history)

while True:
    stock_value = get_valid_input()

    if stock_value == "quit":
        break

    if stock_value == "invalid":
        failed_entries += 1
        continue

    # Update inventory for each delivery
    inventory = process_delivery(inventory, stock_value)
    tax = calculate_tax(stock_value)
    deliveries_processed += 1

    print("Current inventory: ", inventory)
    print("Tax for this delivery: ", tax)

generate_report(inventory, failed_entries)
print("Total deliveries processed: ", deliveries_processed)