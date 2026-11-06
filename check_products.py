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

print("\nFulfilmen: ")
print(laptop.get_fulfilment_info())
print(course.get_fulfilment_info())

mouse = physical_module.PhysicalProduct("P002", "Mouse", 25.5, 40, 0.2)

print("\nShipping tests:")
print("2 kg, expected shipping cost: $10.0:", laptop.calculate_shipping_cost())
print("0.2 kg, expected shipping cost: $1.0:", mouse.calculate_shipping_cost())