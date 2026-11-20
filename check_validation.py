from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order

supplier = Supplier("S001", "Campus Supplies", "sales@example.com")

print("Test 1 - Invalid price")

try:
    product = PhysicalProduct("P001", "Notebook", 0.0, 10, 2.0, supplier)

except ValueError as error:
    print(error)

print("\nTest 2 - Negative stock")
try:
    product = PhysicalProduct("P001", "Laptop", 100.0, -5, 2.0, supplier)

except ValueError as error:
    print(error)

print("\nTest 3 - Invalid order quantity")
product = PhysicalProduct("P001", "Laptop", 100.0, 10, 2.0, supplier)

order = Order("O001")

try:
    order.add_order_line(product, 0)
except ValueError as error:
    print(error)

print("\nTest 4 - Negative stock update")

try:
    product.update_stock(-5)    
except ValueError as error:
    print(error)