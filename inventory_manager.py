#week 5
import json
import os

import product as product_module
import inventory as inventory_module

def load_inventory():
    inventory = inventory_module.Inventory()

    #missing file means this is a ne winventory.
    if not os.path.exists("inventory.json"):
        print("No saved inventory. Starting with an empty inventory.")
        return inventory

    with open("inventory.json", "r") as file:
        saved_products = json.load(file)

    for data in saved_products:
        product = product_module.Product(data["id"], data["name"], data["price"], data["stock"])

        if not inventory.add_product(product):
            print("Duplicate ID skipped:", product.get_product_id())

    print("Inventory loaded successfully.")
    return inventory

def save_inventory(inventory):
    saved_products = []

    #perpare plain data before writing the complete list to JSON
    for product in inventory.get_products():
        saved_products.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(saved_products, file)

    print("Inventory saved successfully.")

def get_stock(prompt):
    while True:
        stock_text = input(prompt)
        valid = stock_text != ""

        #accept normal digits only, not signs or decimal points
        for character in stock_text:
            if character not in "0123456789":
                valid = False

        if valid:
            return int(stock_text)

        print("Error: Stock must be a non-negative number.")

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

        print("Error: Enter a non-negative price, such as 25.50")

def add_product_from_input(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")

    if product_id == "":
        print("Error: Product ID cannot be empty.")
        return

    #duplicate ids would make searches and updates
    if inventory.search_product(product_id) is not None:
        print("Error: Product ID already exists.")
        return

    name = input("Product Name: ")

    if name == "":
        print("Error: Product Name cannot be empty.")
        return

    price = get_price()
    stock = get_stock("Stock Quantity: ")

    product = product_module.Product(product_id, name, price, stock)

    #add only after all info has been accepted
    if inventory.add_product(product):
        print("Product added successfully!")

def update_stock_from_input(inventory):
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    product.display_information()
    quantity = get_stock("Enter new stock quantity: ")

    product.update_stock(quantity)
    print("Stock updated successfully!")

#main program
print("INVENTORY MANAGEMENT SYSTEM")
inventory = load_inventory()

while True:
    print("\n----------- Menu -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")

    option = input("Enter option: ")

    if option == "1":
        inventory.display_all()

    elif option == "2":
        add_product_from_input(inventory)

    elif option == "3":
        update_stock_from_input(inventory)

    elif option == "4":
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)

        if product is None:
            print("Product not found.")
        else:
            product.display_information()

    elif option == "5":
        save_inventory(inventory)

    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        break

    else:
        print("Invalid option. Please enter 1 to 6.")