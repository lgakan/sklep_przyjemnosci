from typing import List, Tuple
from general_inventory import GeneralInventory


class Client:
    def __init__(self, client_id: int, order: List[Tuple[str, int]], budget: int, inventory: GeneralInventory):
        self.client_id = client_id
        self.order = order
        self.budget = budget
        self.inventory = inventory

    def get_order(self) -> List[Tuple[str, int]]:
        return self.order

    def get_oder_quantity(self):
        quants = []
        for quant in self.get_order():
            quants.append(quant[1])
        return quants

    def get_product_ids(self):
        list_of_ids = []
        for item_name, item_count in self.get_order():
            list_of_ids.append(self.inventory.get_product_by_name(item_name).get_product_id())
        return list_of_ids

    def __repr__(self):
        orders = ""
        for i, order in enumerate(self.order):
            if i == 0:
                orders += f'{order[1]}x {order[0]}\n'
            else:
                orders += 20*f' ' + f'{order[1]}x {order[0]}\n'

        return f"+++++ Customer's information +++++\n" \
               f'Your ID: {self.client_id}\n' \
               f'Your shopping list: {orders}' \
               f'Your max budget: {self.budget} PLN\n'
