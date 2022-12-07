from seller_base import SellersBase
from general_inventory import GeneralInventory
from delivery_functionality import Delivery
from client import Client
from solution import Solution


class ObjFunction:

    def __init__(self, solution: Solution, seller_base: SellersBase, general_inventory: GeneralInventory):
        self.solution = solution
        self.seller_base = seller_base
        self.general_inventory = general_inventory
        self.value = None

    def get_objective_func(self):
        n, m = self.solution.get_solution_matrix_shape()
        column_values = []
        for j in m:
            list_of_items = []
            list_of_prices = []
            for i in n:
                product = self.solution.solution_matrix[i][j]
                if isinstance(product, tuple):
                    list_of_items.append((i, product[1]))
                    list_of_prices.append((i, product[0]))
            sj = self.seller_base.get_seller_by_id(str(j)).get_delivery_price(list_of_items)
            new_prices = self.seller_base.get_seller_by_id(str(j)).get_discounted_price(list_of_prices)
            column_values.append(sj + sum(new_prices))

        return sum(column_values)
