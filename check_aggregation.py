from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory

supplier = Supplier("S001", "Campus Supplies", "sales@example.com")

#create prouct before adding it to inventory
laptop = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.0, supplier)

inventory_a = Inventory()
inventory_b = Inventory()

print("Adding product to Inventory A:")
print(inventory_a.add_product(laptop))

print("\nIs laptop in Inventory A?")
print(inventory_a.find_product("P001") is laptop)

print("\nRemoving laptop from Inventory A:")
print(inventory_a.remove_product("P001"))

print("\nSearching inventory A again:")
print(inventory_a.find_product("P001"))

print("\nCan laptop still display information?")
laptop.display_information()

print("\nAdding laptop to Inventory B:")
print(inventory_b.add_product(laptop))

print("\nIs it the same laptop object?")
print(inventory_b.find_product("P001") is laptop)