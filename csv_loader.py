import csv

from product_factory import ProductFactory
from inventory import Inventory
from supplier import Supplier

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")

    except FileNotFoundError:
        print("Products file ot found:", path)

    else:
        loaded = 0

        with file:
            reader = csv.reader(file)
            first_row = True

            for row in reader:
                if first_row:
                    first_row = False
                    continue

                try:
                    if len(row) != 5:
                        raise ValueError("Wrong number of fields.")

                    product = ProductFactory.create(row[0], row[1], row[2], float(row[3]), int(row[4]), supplier, 0.0)

                    if not inventory.add_product(product):
                        raise ValueError("Duplicate product ID.")

                    loaded += 1

                except ValueError:
                    print("Skipped row:", row)

        print("Products loaded:", loaded)
        
    finally:
        print("Load attempt finished.")