from supplier import Supplier
from inventory import Inventory
from csv_loader import load_products

supplier = Supplier("S001", "Campus Supplies", "sales@example.com")
inventory = Inventory()

load_products("products.csv", inventory, supplier)

print("\nProducts in inventory:")
inventory.display_all()