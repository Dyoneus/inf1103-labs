import product as product_module
import can_be_shipped as shipping_module

class PhysicalProduct(product_module.Product, shipping_module.CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information() #reuses the display_information method from the parent class
        print("Weight (kg):", self.__weight)
        print("Fulfilment:", self.get_fulfilment_info())
        print("Shipping Cost: $", self.calculate_shipping_cost())

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5.0 # shipping costs $5 per kg

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data