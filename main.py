from client import Client
from general_inventory import GeneralInventory
from solution import Solution
from seller_base import SellersBase
import matplotlib.pyplot as plt
import numpy as np


def main():
    print('START')
    my_inventory = GeneralInventory()
    my_sellers_base = SellersBase(my_inventory)
    print(my_sellers_base.get_sellers_base_size())
    my_own_self = Client(0, [(1, 5), (7, 3)], 300, my_inventory)
    my_solution = Solution(sellers=my_sellers_base.sellers_list, items=my_inventory.product_list)
    print(my_solution.solution_matrix)
    plt.figure()
    ex_weight = np.linspace(380, 450, 150)
    for weight in ex_weight:
        plt.plot(weight, my_sellers_base.get_seller_by_id('16').delivery.get_cost(weight), 'ko')
        plt.plot(weight, my_sellers_base.get_seller_by_id('17').delivery.get_cost(weight), 'ro')
    plt.title('Delivery functions')
    plt.xlabel('Weight of products [g]')
    plt.ylabel('Function value [PLN]')
    plt.legend(['Seller 16', 'Seller 17'])
    plt.show()

    plt.figure()
    ex_quantity = np.linspace(1, 10, 10)
    for quant in ex_quantity:
        plt.plot(quant, my_sellers_base.get_seller_by_id('16').discount.get_disc()(quant), 'ko')
        plt.plot(quant, my_sellers_base.get_seller_by_id('17').discount.get_disc()(quant), 'r*')
    plt.title('Discount functions')
    plt.xlabel('Quantity of products [-]')
    plt.ylabel('Overall discount [%]')
    plt.legend(['Seller 16', 'Seller 17'])
    plt.show()


if __name__ == '__main__':
    main()
