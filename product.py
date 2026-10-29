# product object represents one item in the inventory
class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        #reject negative stock value even when called outside menu
        if quantity < 0:
            print("Error: Stock cannot be negative.")
            return

        #the quantity replaces the old stock
        self.__stock = quantity

    def display_information(self):
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print("Price: $", self.__price)
        print("Stock:", self.__stock)

    def to_dict(self):
        #return a data copy for saving
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }