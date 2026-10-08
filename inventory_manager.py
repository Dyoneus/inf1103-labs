#week 5
import json
import os
def load_inventory():
    #missing file means this is a ne winventory.
    if not os.path.exists("inventory.json"):
        print("inventory.json not found. Starting with an empty inventory.")
        return []
    
    print("inventory.json found.")

    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    print("inventory loaded successfully.")
    return inventory

def display_all(inventory):
    print("\nCurrent Inventory")

    if len(inventory) == 0:
        print("No products in inventory.")
        return

    for product in inventory:
        print("ID:", product['id'], "| Name:", product['name'], 
              "| Price: $", product["price"], "| Stock:", product["stock"])

def search_product(inventory, product_id):
    #return matching dictionary so other func can use it
    for product in inventory:
        if product['id'] == product_id:
            return product
        
    return None

def get_stock(prompt):
    while True:
        stock_text = input(prompt)

        if stock_text.isdigit():
            return int(stock_text)

        print("Error: Stock must be a non-negative integer.")

def get_price():
    while True:
        price_text = input("Price: ")
        decimal_points = 0
        digits = 0
        valid = True

        #allow digits and at most one decimal point
        for character in price_text:
            if character in "0123456789":
                digits += 1
            elif character == ".":
                decimal_points += 1
            else:
                valid = False

        if valid and digits > 0 and decimal_points <= 1:
            return float(price_text)

        print("Error: Enter a non-negative price.")

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")

    if product_id == "":
        print("Error: Product ID cannot be empty.")
        return

    #duplicate ids would make searches and updates
    if search_product(inventory, product_id) is not None:
        print("Error: Product ID already exists.")
        return

    name = input("Product Name: ")

    if name == "":
        print("Error: Product Name cannot be empty.")
        return

    price = get_price()
    stock = get_stock("Stock Quantity: ")

    product = {"id": product_id, "name": name,
               "price": price, "stock": stock}

    #add only after all info has been accepted
    inventory.append(product)
    print("Product added successfully!")

def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = search_product(inventory, product_id)

    if product is None:
        print("Error: Product not found.")
        return

    print("Name:", product['name'])
    print("Current Stock:", product['stock'])

    new_stock = get_stock("New Stock Quantity: ")

    #replace old stock
    product['stock'] = new_stock
    print("Stock updated successfully!")

#main program
print("INVENTORY MANAGEMENT SYSTEM")
inventory = load_inventory()

while True:
    print("\nMenu:")
    print("1. Display All Products")
    print("2. Add New Product")
    print("3. Update Stock Quantity")
    print("4. Search Product by ID")
    print("5. Save Inventory")
    print("6. Exit")

    option = input("Enter option: ")

    if option == "1":
        display_all(inventory)

    elif option == "2":
        add_product(inventory)

    elif option == "3":
        update_stock(inventory)

    elif option == "4":
        product_id = input("Enter Product ID: ")
        product = search_product(inventory, product_id)

        if product is None:
            print("Error: Product not found.")
        else:
            display_all([product])

    elif option == "5":
        print("Saving inventory.")

    elif option == "6":
        print("Exiting program.")
        break

    else:
        print("Error: Invalid option. Please try again.")