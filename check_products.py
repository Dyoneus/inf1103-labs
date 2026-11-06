import physical_product as physical_module
import digital_product as digital_module

laptop = physical_module.PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.0)

course = digital_module.DigitalProduct("D001", "Python Course", 30.0, 100, 500.0)

laptop.display_information()
print()
course.display_information()

print("\nAfter updating laptop stock to 20:")
laptop.update_stock(20)
laptop.display_information()
