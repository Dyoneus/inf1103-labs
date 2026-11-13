# Write Prediction 1 before running this file.
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

supplier = Supplier("S001", "Campus Supplies", "sales@example.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.0, supplier)
course = DigitalProduct("D001", "Python Course", 30.0, 100, 500.0, supplier)

print("Products share one supplier:", laptop.get_supplier() is course.get_supplier())

del supplier

print("\nLaptop supplier after del supplier:")
laptop.get_supplier().display_information()
print("\nCourse supplier after del supplier:")
course.get_supplier().display_information()

independent_supplier = Supplier("S002", "Study Store", "info@example.com")
print("\nIndependent supplier:")
independent_supplier.display_information()
