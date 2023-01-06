from client import Client
from general_inventory import GeneralInventory
from solution import Solution
from seller_base import SellersBase
from objective_function import ObjFunction
import matplotlib.pyplot as plt
import numpy as np
import random as rd

# jak dużo kosztuje to dużo waży
# cena w tym samym przedziale dla danego produktu
def generate_database(sellers_count, products_count, count_max):
    print('id_seller;id_item;count;price')
    id_items_p = {}
    for i in range(sellers_count):
        list_of_id_items = []
        seller_different_products = rd.randint(int(0.15*products_count), products_count)  # tu zależnie ile chcemy by seller miał unikalnych produktow w ofercie
        for j in range(seller_different_products):
            while True:
                id_item = rd.randint(0, products_count-1)
                if id_item not in list_of_id_items:
                    list_of_id_items.append(id_item)
                    break
            count = rd.randint(1, count_max)
            # p = rd.randint(0, 10)  # prawdopodobienstwo cen
            if list_of_id_items[j] in id_items_p.keys():
                p = id_items_p[list_of_id_items[j]]
                if p <= 5:
                    price = rd.randint(0, 5)
                elif 6 <= p <= 8:
                    price = rd.randint(20, 50)
                elif p >= 9:
                    price = rd.randint(200, 500)
            else:
                p = rd.randint(0, 10)
                id_items_p[list_of_id_items[j]] = p
                if p <= 5:
                    price = rd.randint(0, 5)
                elif 6 <= p <= 8:
                    price = rd.randint(20, 50)
                elif p >= 9:
                    price = rd.randint(200, 500)
            print(f"{i};{list_of_id_items[j]};{count};{price}")
def main():
    # # Generating products inventory from .csv file
    # my_inventory = GeneralInventory()
    # print(f'This is your Inventory!\n{my_inventory}')
    #
    # # Generating sellers from .csv file using generated inventory
    # my_sellers_base = SellersBase(my_inventory)
    # print(f'This is your Sellers Base!\n{my_sellers_base}')
    # print(f'Sellers in total: {my_sellers_base.get_sellers_base_size()}\n')

    # Generating a client with the shopping list
    # my_own_self = Client(0, [('item_15', 7),
    #                          ('item_16', 10)], 300, my_inventory)
    # print(my_own_self)

    # Generating empty matrix based on amount of sellers and products in inventory
    # my_solution = Solution(sellers=my_sellers_base.sellers_list, items=my_inventory.product_list)
    # print(f'Solution matrix of zeros:\n{my_solution.solution_matrix}')

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

    # my_solution.get_starting_solution(my_sellers_base.get_sellers_with_items(my_own_self.get_product_ids()),
    #                                   my_own_self.get_oder_quantity(),
    #                                   'random')
    # print(my_solution)
    # a = [2, 1, 1, 3]
    # print(sorted(a))
    print(generate_database(20, 30, 30))

if __name__ == '__main__':
    main()
