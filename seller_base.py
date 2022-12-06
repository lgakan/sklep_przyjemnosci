from file_reader import FileReader
from seller import Seller


class SellersBase:
    def __init__(self, inventory):
        self.file_reader = FileReader('unique_sellers.csv')
        self.sellers_list = []
        self.add_sellers_from_file(global_inventory=inventory)
        self.add_products_to_sellers()

    def add_sellers_from_file(self, global_inventory):
        for i in self.file_reader.get_file_records():
            self.sellers_list.append(Seller(id_seller=self.get_sellers_base_size(),
                                            store={},
                                            delivery_info=i['delivery'],
                                            discount_info=i['discount'],
                                            inventory=global_inventory))

    def get_seller_by_id(self, id_seller: int):
        if self.get_sellers_base_size() == 0:
            return 0
        else:
            for i in self.sellers_list:
                if str(i.id) == id_seller:
                    return i

    def add_products_to_sellers(self):
        file = FileReader('database.csv')
        for i in file.get_file_records():
            self.get_seller_by_id(i['id_seller']).store[i['id_item']] = (i['price'], i['count'])

    def get_sellers_base_size(self):
        return len(self.sellers_list)

    # TODO: Put '\n' here
    def __str__(self):
        return str(self.sellers_list)
