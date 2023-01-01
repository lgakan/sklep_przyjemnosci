from client import Client
from general_inventory import GeneralInventory
from individual import Individual
from seller_base import SellersBase
from objective_function import ObjFunction
import matplotlib.pyplot as plt
import numpy as np
import random as rd


def main():
    # Generating products inventory from .csv file
    my_inventory = GeneralInventory()
    print(f'This is your Inventory!\n{my_inventory}')

    # Generating sellers from .csv file using generated inventory
    my_sellers_base = SellersBase(my_inventory)
    print(f'This is your Sellers Base!\n{my_sellers_base}')
    print(f'Sellers in total: {my_sellers_base.get_sellers_base_size()}\n')

    # Generating a client with the shopping list
    my_own_self = Client(0, [('item_15', 7),
                             ('item_16', 10)], 300, my_inventory)
    print(my_own_self)

    # Generating empty matrix based on amount of sellers and products in inventory
    my_solution = Individual(sellers=my_sellers_base.sellers_list, items=my_inventory.product_list)
    print(f'Solution matrix of zeros:\n{my_solution.individual_matrix}')

    # Plotting delivery functions
    # plt.figure()
    # ex_weight = np.linspace(380, 450, 150)
    # for weight in ex_weight:
    #     plt.plot(weight, my_sellers_base.get_seller_by_id('16').delivery.get_cost(weight), 'ko')
    #     plt.plot(weight, my_sellers_base.get_seller_by_id('17').delivery.get_cost(weight), 'ro')
    # plt.title('Delivery functions')
    # plt.xlabel('Weight of products [g]')
    # plt.ylabel('Function value [PLN]')
    # plt.legend(['Seller 16', 'Seller 17'])
    # plt.show()

    # Plotting discount functions
    # plt.figure()
    # ex_quantity = np.linspace(1, 10, 10)
    # for quant in ex_quantity:
    #     plt.plot(quant, my_sellers_base.get_seller_by_id('16').discount.get_disc()(quant), 'ko')
    #     plt.plot(quant, my_sellers_base.get_seller_by_id('17').discount.get_disc()(quant), 'r*')
    # plt.title('Discount functions')
    # plt.xlabel('Quantity of products [-]')
    # plt.ylabel('Overall discount [%]')
    # plt.legend(['Seller 16', 'Seller 17'])
    # plt.show()

    # Generating exemplary solution matrix
    # my_solution.solution_matrix = np.array([[0, 3, 0, 0],
    #                                         [1, 2, 0, 0],
    #                                         [0, 0, 0, 3],
    #                                         [0, 0, 1, 0]])
    # print(f'Your current solution:\n {my_solution}')
    #
    # # Generating target function
    # target_function = ObjFunction(solution=my_solution,
    #                               seller_base=my_sellers_base,
    #                               general_inventory=my_inventory)
    #
    # # Calculating value of the target function for the solution
    # total_cost, partial_costs = target_function.get_objective_func()
    # print(f'Total cost calculated for this solution: {total_cost}')
    # print(f'Total costs for each seller in corresponding order: {partial_costs}')

    my_solution.get_starting_individual(my_sellers_base.get_sellers_with_items(my_own_self.get_product_ids()),
                                        my_own_self.get_oder_quantity(),
                                      'random')
    print(my_solution)


if __name__ == '__main__':
    main()
