from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory

supplier = Supplier("S001", "Campus Supplies", "sales@example.com")

laptop = ProductFactory.create("physical", "P001", "Laptop", 1200.0, 15, supplier, 2.0)

course = ProductFactory.create("digital", "D001", "Python Course", 30.0, 100, supplier, 500.0)

print("Physical product:")
laptop.display_information()

print("\nDigital product:")
course.display_information()