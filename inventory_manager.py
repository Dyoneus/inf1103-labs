#week 5

def display_all(inventory):
    print("\nCurrent Inventory")

    if len(inventory) == 0:
        print("No products in inventory.")
        return

    for product in inventory:
        print("ID:", product['id'], "| Name:", product['name'], 
              "| Price: $", product["price"], "| Stock:", product["stock"])


#main program
inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
]

display_all(inventory)
