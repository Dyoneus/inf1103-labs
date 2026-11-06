#week 5
import json
import physical_product as physical_module
import digital_product as digital_module
import inventory as inventory_module

def load_inventory():
    inventory = inventory_module.Inventory()

    with open("inventory.json", "a") as file:
        file.write("")

    with open("inventory.json", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No saved inventory. Starting with an empty inventory.")
        return inventory

    with open("inventory.json", "r") as file:
        saved_products = json.load(file)

    for data in saved_products:
        if "type" not in data:
            print("Error")
            return None

        if data["type"] == "physical":
            product = physical_module.PhysicalProduct(
                data["id"],
                data["name"],
                data["price"],
                data["stock"],
                data["weight"]
            )
        elif data["type"] == "digital":
            product = digital_module.DigitalProduct(
                data["id"],
                data["name"],
                data["price"],
                data["stock"],
                data["download_size"]
            )
        else:
            print("Unknown product type.", data["type"])
            return None

        if not inventory.add_product(product):
            print("There is a duplicate product ID in file:", data["id"])
            return None

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


def get_number(prompt):
    while True:
        number_text = input(prompt)
        decimal_points = 0
        digits = 0
        valid = True

        #allow digits and at most one decimal point
        for character in number_text:
            if character in "0123456789":
                digits += 1
            elif character == ".":
                decimal_points += 1
            else:
                valid = False

        if valid and digits > 0 and decimal_points <= 1:
            return float(number_text)

        print("Error: Enter a non-negative number, such as 2 or 2.5.")


def add_product_from_input(inventory):
    print("\nAdd New Product")
    print("1. Physical Product")
    print("2. Digital Product")
    product_type = input("Enter product type: ")

    if product_type != "1" and product_type != "2":
        print("Invalid product type. Please enter 1 or 2.")
        return

    product_id = input("Enter Product ID: ")

    if product_id == "":
        print("Error: Product ID cannot be empty.")
        return

    if inventory.search_product(product_id) is not None:
        print("Error: Product ID already exists.")
        return

    name = input("Enter Product Name: ")
    if name == "":
        print("Error: Product Name cannot be empty.")
        return

    price = get_number("Price: ")
    stock = get_stock("Stock Quantity: ")

    if product_type == "1":
        weight = get_number("Weight (kg): ")
        product = physical_module.PhysicalProduct(product_id, name, price, stock, weight)
    else:
        download_size = get_number("Download Size (MB): ")
        product = digital_module.DigitalProduct(product_id, name, price, stock, download_size)

    if inventory.add_product(product):
        print("Product added successfully.")


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


def main():
    print("INVENTORY MANAGEMENT SYSTEM")
    inventory = load_inventory()

    if inventory is None:
        print("Program stopped. The saved file has not been changed.")
        return

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
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            break

        else:
            print("Invalid option. Please enter 1 to 6.")

main()