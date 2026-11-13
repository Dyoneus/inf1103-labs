from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

def show_product_details(product: Product) -> None:
    product.display_information()
    print("Fulfilment:", product.get_fulfilment_info())

supplier = Supplier("S001", "Campus Supplies", "sales@example.com")

laptop = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.0, supplier)
course = DigitalProduct("D001", "Python Course", 30.0, 100, 500.0, supplier)

inventory = Inventory()

inventory.add_product(laptop)
inventory.add_product(course)

print("Testing both product types:")

for product in inventory.get_products():
    show_product_details(product)

    print("Updating stock to 20:")
    product.update_stock(20)
    product.display_information()

    print("Trying an invalid stock update:")
    product.update_stock(-5)
    product.display_information()

    print()