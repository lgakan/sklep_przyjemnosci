from file_reader import FileReader
from seller import Seller


class SellersBase:
    def __init__(self):
        self.file_reader = FileReader('unique_sellers.csv')
        self.sellers_list = []
        self.add_sellers_from_file()

    def add_sellers_from_file(self):
        for i in self.file_reader.get_file_records():
            self.sellers_list.append(Seller(id=self.get_seller_base_size(),
                                            store='Implement me right :(',
                                            delivery_info=i['delivery'],
                                            discount_info=i['discount']))

    def get_seller_by_id(self, id_seller: int):
        if self.get_seller_base_size() == 0:
            return 0
        else:
            for i in self.sellers_list:
                if i.id == id_seller:
                    return i

    def get_seller_base_size(self):
        return len(self.sellers_list)