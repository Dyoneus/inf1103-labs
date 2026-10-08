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


#main program
inventory = load_inventory()
display_all(inventory)
