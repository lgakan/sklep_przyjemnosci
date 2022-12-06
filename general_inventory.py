from file_reader import FileReader
from product import Product


class GeneralInventory:
    def __init__(self):
        self.file_reader = FileReader('unique_items_file.csv')
        self.product_list = []
        self.add_products_from_file()

    def add_products_from_file(self):
        for i in self.file_reader.get_file_records():
            self.product_list.append(Product(product_id=self.get_inventory_size(),
                                             product_weight=i['weight'],
                                             product_name=i['product_name']))

    def get_product_by_id(self, id_product: int):
        if self.get_inventory_size() == 0:
            return 0
        else:
            for i in self.product_list:
                if i.product_id == id_product:
                    return i

    def get_inventory_size(self):
        return len(self.product_list)

    # TODO: Put "\n" here
    def __str__(self):
        return str(self.product_list)


    # def get_all_unique_products(self):
    #     return self.file_reader.get_column_from_file('unique_product')

g = GeneralInventory()
g.add_products_from_file()