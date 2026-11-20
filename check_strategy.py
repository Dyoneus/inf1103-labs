from supplier import Supplier 
from physical_product import PhysicalProduct
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount

supplier = Supplier("S001", "Campus Supplies", "sales@example.com")

product = PhysicalProduct("P001", "Test Product", 250.0, 10, 2.0, supplier)

order = Order("O001")
order.add_order_line(product, 1)

print("No discount:", order.calculate_total())

order.set_discount(BulkDiscount(200, 20))
print("Bulk discount:", order.calculate_total())

order.set_discount(PercentageDiscount(10))
print("10% discount:", order.calculate_total())

order.set_discount(StudentDiscount())
print("Student discount:", order.calculate_total())