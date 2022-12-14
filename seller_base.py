from file_reader import FileReader
from seller import Seller


def function_from_string(function_string, func_type: str):
    strings_list, last_el = function_string.split('],')[:-1], function_string.split('],')[-1]
    for i in range(len(strings_list)):
        strings_list[i] = strings_list[i][1:].split(',')
        strings_list[i][1] = float(strings_list[i][1])
    if func_type == 'discount':
        strings_list.append([float(last_el[1:-1])])
    elif func_type == 'delivery':
        strings_list.append([last_el[1:-1]])
    return strings_list


class SellersBase:
    def __init__(self, inventory, path_to_seller_base, path_to_db):
        self.file_reader = FileReader(path_to_seller_base)
        self.sellers_list = []
        self.add_sellers_from_file(global_inventory=inventory)
        self.add_products_to_sellers(path_to_db)

    def add_sellers_from_file(self, global_inventory):
        for i in self.file_reader.get_file_records():
            self.sellers_list.append(Seller(id_seller=self.get_sellers_base_size(),
                                            store={},
                                            delivery_info=function_from_string(function_string=i['delivery'],
                                                                               func_type='delivery'),
                                            discount_info=function_from_string(function_string=i['discount'],
                                                                               func_type='discount'),
                                            inventory=global_inventory))

    def get_seller_by_id(self, id_seller: str):
        if self.get_sellers_base_size() == 0:
            return 0
        else:
            for i in self.sellers_list:
                if str(i.id) == id_seller:
                    return i

    def add_products_to_sellers(self, path_to_db):
        file = FileReader(path_to_db)
        for i in file.get_file_records():
            self.get_seller_by_id(i['id_seller']).store[i['id_item']] = (i['price'], i['count'])

    def get_sellers_base_size(self):
        return len(self.sellers_list)

    def get_sellers_with_items(self, item_ids):
        dict_of_sellers = {}
        list_of_sellers = []
        for i, item_id in enumerate(item_ids):
            list_of_sellers.append([])
            for seller in self.sellers_list:
                potential_seller = seller.item_in_stock(item_id)
                if potential_seller:
                    list_of_sellers[-1].append((potential_seller, seller.get_quantity_of_item(item_id)))
            if list_of_sellers[-1]:
                dict_of_sellers[item_id] = (list_of_sellers[-1])
        return dict_of_sellers

    def __str__(self):
        list_of_sth = ""
        for line in self.sellers_list:
            list_of_sth += f'{line}\n'
        return list_of_sth
