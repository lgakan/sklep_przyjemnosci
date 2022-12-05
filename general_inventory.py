from file_reader import FileReader
from product import Product


class GeneralInventory:
    def __init__(self):
        self.file_reader = FileReader('unique_items_file.csv')
        self.product_list = []

    def add_product(self, product: Product):
        self.product_list.append(product)

    def get_product_by_id(self, id_product: int):
        if self.get_inventory_size() == 0:
            return 0
        else:
            for i in self.product_list:
                if i.product_id == id_product:
                    return i

    def get_inventory_size(self):
        return len(self.product_list)


    # def get_all_unique_products(self):
    #     return self.file_reader.get_column_from_file('unique_product')


g = GeneralInventory()
print(g.get_product_by_id(1))
