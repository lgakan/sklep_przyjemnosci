from client import Client
from delivery_functionality import Delivery
from discount_functionality import Discount
from general_inventory import GeneralInventory
from solution import Solution
from seller_base import SellersBase


def main():
    print('START')
    my_inventory = GeneralInventory()
    my_sellers_base = SellersBase(my_inventory)
    print(my_sellers_base.get_sellers_base_size())
    my_own_self = Client(0, [(1, 5), (7, 3)], 300)
    my_solution = Solution(sellers=my_sellers_base.sellers_list, items=my_inventory.product_list)
    print(my_solution.solution_matrix)


if __name__ == '__main__':
    main()
