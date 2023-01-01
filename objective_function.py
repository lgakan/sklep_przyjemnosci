from seller_base import SellersBase
from general_inventory import GeneralInventory
from delivery_functionality import Delivery
from client import Client
# from individual import Individual


# TODO: Consider to change ObjFunction class into function
class ObjFunction:
    # TODO: Why objFunction class has individual (old solution) attribute?
    # edit: Teraz juz nie ma ale narazie tylko dla testow - zostal przerzucony do parametru metody get
    def __init__(self, seller_base: SellersBase, general_inventory: GeneralInventory):
        self.seller_base = seller_base
        self.general_inventory = general_inventory
        self.value = None

    def get_objective_func(self, individual_matrix):
        n, m = len(individual_matrix), len(individual_matrix[0])
        column_values = []
        for j in range(m):
            list_of_items = []
            for i in range(n):
                product = individual_matrix[i][j]
                if product > 0:
                    list_of_items.append((i, product))
            sj = self.seller_base.get_seller_by_id(str(j)).get_delivery_price(list_of_items)
            new_prices = self.seller_base.get_seller_by_id(str(j)).get_discounted_price(list_of_items)
            column_values.append(sj + sum(new_prices))

        return sum(column_values), column_values
