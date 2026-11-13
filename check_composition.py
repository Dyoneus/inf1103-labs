from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order

supplier = Supplier("S001", "Campus Supplies", "sales@example.com")

laptop = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.0, supplier)
course = DigitalProduct("D001", "Python Course", 30.0, 100, 500.0, supplier)

order_a = Order("O001")
order_b = Order("O002")

#both orders use the same laptop object
order_a.add_order_line(laptop, 1)
order_b.add_order_line(laptop, 2)

line_a = order_a.get_order_lines()[0]
line_b = order_b.get_order_lines()[0]

print("Are two of the OrderLines the same object?")
print(line_a is line_b) 

print("\nDo both of the OrderLines refer to the sae Product?")
print(line_a.get_product() is line_b.get_product())

#adds digital product to the first order
order_a.add_order_line(course, 2)

print("\nOrder A:")
order_a.display_order()

print("\nOrder B:")
order_b.display_order()

print("\nRemove the first line from Order A:")
print(order_a.remove_order_line(1))

print("\nOrder A after removal:")
order_a.display_order()

print("\nOrder B is unchanged:")
order_b.display_order()