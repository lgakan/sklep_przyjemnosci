from general_inventory import GeneralInventory
from delivery_functionality import Delivery
from discount_functionality import Discount


class Seller:
    def __init__(self,
                 id_seller: int,
                 store: dict,
                 delivery_info: list,
                 discount_info: list,
                 inventory: GeneralInventory):
        self.id = id_seller
        self.store = store
        self.delivery = Delivery(list_of_conditions=delivery_info)
        self.discount = Discount(list_of_conditions=discount_info)
        self.inventory = inventory

    def get_delivery_price(self, list_of_items):
        weight = 0
        for item_id, item_amount in list_of_items:
            weight += item_amount * self.inventory.get_product_by_id(item_id).get_product_weight()
        return self.delivery.get_cost(weight=weight)

    def get_discounted_price(self, list_of_items):
        prices = []
        amount = 0
        for item_id, item_amount in list_of_items:
            price, quantity = self.get_products()[item_id]
            prices.append(price*quantity)
            amount += quantity
        return self.discount.get_new_cost(old_cost=prices, amount=amount)

    def get_products(self):  #zwraca asortyment sprzedawcy
        return self.store
