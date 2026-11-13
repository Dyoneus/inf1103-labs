from product import Product

#inventory manages a collection of product objects
class Inventory:
    def __init__(self):
        #each inventory object gets its own lists.
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        #keep ids unique so a search can identify just one product
        if self.search_product(product.get_product_id()) is not None:
            return False

        self.__products.append(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
            
        return None

    def display_all(self):
        print("\nCurrent Inventory")

        if len(self.__products) == 0:
            print("No products in inventory.")
            return

        for product in self.__products:
            product.display_information()
            print()

    def get_products(self):
        #copy list so the caller cannot append to the original list
        return self.__products.copy()

    def find_product(self, product_id: str) -> Product | None:
        # reuse the search func from previous lab
        return self.search_product(product_id)

    def remove_product(self, product_id: str) -> bool:
        product = self.search_product(product_id)

        if product is None:
            return False

        #remove the reference from this inventory
        self.__products.remove(product)
        return True