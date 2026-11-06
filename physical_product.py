import product as product_module

class PhysicalProduct(product_module.Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information() #reuses the display_information method from the parent class
        print("Weight (kg):", self.__weight)

    def get_fulfilment_info(self):
        return "Requires physical shipping."