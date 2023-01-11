from file_reader import FileReader
from product import Product


class GeneralInventory:
    def __init__(self, path_to_inventory):
        self.file_reader = FileReader(path_to_inventory)
        self.product_list = []
        self.add_products_from_file()

    def add_products_from_file(self):
        for i in self.file_reader.get_file_records():
            self.product_list.append(Product(product_id=self.get_inventory_size(),
                                             product_weight=float(i['weight']),
                                             product_name=i['product_name']))

    def get_product_by_id(self, id_product: int):
        if self.get_inventory_size() == 0:
            return 0
        else:
            for i in self.product_list:
                if i.product_id == id_product:
                    return i

    def get_product_by_name(self, product_name: str):
        if self.get_inventory_size() == 0:
            return None
        else:
            for i in self.product_list:
                if i.product_name == product_name:
                    return i

    def get_inventory_size(self):
        return len(self.product_list)

    def __str__(self):
        product_list = ""
        for line in self.product_list:
            product_list += f'{line}\n'
        return product_list

