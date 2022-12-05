from file_reader import FileReader


class GeneralInventory:
    def __init__(self):
        self.file_reader = FileReader('unique_items_file.csv')
        self.unique_products_list = self._get_all_unique_products()

    def _get_all_unique_products(self):
        return self.file_reader.get_column_from_file('unique_product')

    # TODO Here, we should return object from Product class
    def get_product_by_id(self, id_product: int):
        return self.file_reader.get_record_by_id_column('id_product', id_product)

    def get_inventory_size(self):
        return len(self._get_all_unique_products())

