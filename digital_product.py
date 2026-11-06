import product as product_module

class DigitalProduct(product_module.Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information() #reuses the display_information method from the parent class
        print("Download Size (MB):", self.__download_size)
        print("Fulfilment:", self.get_fulfilment_info())

    def get_fulfilment_info(self):
        return "Delivered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data