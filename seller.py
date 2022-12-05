from typing import List, Tuple, Dict, Union, Function
from delivery_functionality import Delivery
from discount_functionality import Discount


class Seller:
    def __init__(self, id: int, store: Dict[int:Tuple[float, int]], delivery_info, discount_info):
        self.id = id
        self.store = store
        self.delivery = Delivery(delivery_info)
        self.discount = Discount(discount_info)

    def get_delivery_price(self, weight: int):
        return self.delivery.get_cost(weight)

    def get_discounted_price(self):
        prices = []
        amount = 0
        for k, v in self.get_products().items():
            prices.append(v[0])
            amount += v[1]
        return self.discount.get_new_cost(prices, amount)

    def get_products(self):  #zwraca asortyment sprzedawcy
        return self.store
