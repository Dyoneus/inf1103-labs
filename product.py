from abc import ABC, abstractmethod
from supplier import Supplier

# product object represents one item in the inventory
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock

        # keep the supplied object rather than making a new Supplier.
        self.__supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def get_supplier(self) -> Supplier:
        return self.__supplier

    @property
    def price(self) -> float:
        return self.__price

    def update_stock(self, quantity: int) -> None:
        #reject negative stock value even when called outside menu
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        #the quantity replaces the old stock
        self.__stock = quantity

    def display_information(self) -> None:
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print("Price: $", self.__price)
        print("Stock:", self.__stock)
        self.__supplier.display_information()

    def to_dict(self) -> dict:
        #return a data copy for saving
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
