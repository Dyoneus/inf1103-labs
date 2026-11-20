import unittest

from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory
from order import Order
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount
from inventory import Inventory
from csv_loader import load_products

class TestLab9(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S001", "Campus Supplies", "sales@example.com")

    def test_order_discounts(self):
        product = ProductFactory.create("physical","P001", "Lamp", 250.0, 10, self.supplier, 2.0)

        order = Order("O001")
        order.add_order_line(product, 1)

        self.assertEqual(order.calculate_total(), 250.0)

        order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 230.0)

        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225.0)

        order.set_discount(StudentDiscount())
        self.assertEqual(order.calculate_total(), 237.5)

    def test_factory_types(self):
        physical = ProductFactory.create("physical", "P001", "Lamp", 25.0, 10, self.supplier, 2.0)
        digital = ProductFactory.create("digital", "D001", "Photo Editor", 49.90, 100, self.supplier, 500.0)

        self.assertIsInstance(physical, PhysicalProduct)
        self.assertIsInstance(digital, DigitalProduct)

        with self.assertRaises(ValueError):
            ProductFactory.create("service", "S001", "Installation", 30.0, 5, self.supplier, 0.0)

    def test_invali_values(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P009", "Bad price", 0.0, 10, self.supplier, 1.0)

        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P010", "Bad stock", 10.0, -1, self.supplier, 1.0)

        product = ProductFactory.create("digital", "D009", "Test Product", 20.0, 1, self.supplier, 5.0)

        order = Order("O002")

        with self.assertRaises(ValueError):
            order.add_order_line(product, 0)

        with self.assertRaises(ValueError):
            product.update_stock(-5)

    def test_csv_loading(self):
        inventory = Inventory()

        load_products("products.csv", inventory, self.supplier)

        self.assertEqual(len(inventory.get_products()), 3)
        self.assertIsNotNone(inventory.find_product("P001"))
        self.assertIsNone(inventory.find_product("P002"))
        self.assertIsNone(inventory.find_product("S001"))