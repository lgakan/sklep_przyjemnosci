# functions needed to work out the final solution based on the evolutionary algorithm
from individual import Individual
from random import randint
from random import sample
import numpy as np
import random as rd
from client import Client
from seller_base import SellersBase
from general_inventory import GeneralInventory
from copy import deepcopy
import matplotlib.pyplot as plt


# population - lista obiektow individuals
# amount - ile rodziców chcemy
# Returns:
# 1. ObjFunction value for parents
# 2. Parents Individuals
# 3. ObjFunction value for worst members
# 4. Worst Individuals
def selection_tournament(population: list, amount, budget):
    parents = []
    for matrix in population:
        parents.append((get_penalty_func(get_obj_func(main_sellers_base, matrix), budget), matrix))
    parents_sorted = deepcopy(sorted(parents))
    parents_amount = int(amount * population_size)
    parents_sorted = parents_sorted[population_size - parents_amount * (parents_amount - 1):]
    while len(parents) > parents_amount:
        for i in range(0, len(parents) // 2, 2):
            if parents[i][0] < parents[i + 1][0]:
                parents.remove(parents[i + 1])
            else:
                parents.remove(parents[i])
    return [i for i, _ in parents], \
           [i for _, i in parents], \
           [i for i, _ in parents_sorted], \
           [i for _, i in parents_sorted]


# Returns:
# 1. ObjFunction value for parents
# 2. Parents Individuals
# 3. ObjFunction value for worst members
# 4. Worst Individuals
def selection_roulette(population: list, amount, budget):
    parents_amount = int(amount * population_size)
    parents = []
    for matrix in population:
        parents.append([get_penalty_func(get_obj_func(main_sellers_base, matrix), budget), matrix])
    parents = sorted(parents)
    parents_sorted = deepcopy(parents)
    parents_sorted = parents_sorted[population_size - parents_amount * (parents_amount - 1):]
    length = population_size
    for i in range(length):
        parents[i].append(length - i)
    new_list_of_individuals = []
    for i in range(length):
        for j in range(parents[i][2]):
            new_list_of_individuals.append((parents[i][0], parents[i][1]))
    rd.shuffle(new_list_of_individuals)
    parents.clear()
    for i in range(parents_amount):
        parents.append(new_list_of_individuals[0])
        new_list_of_individuals = list(filter((parents[-1]).__ne__, new_list_of_individuals))
    return [i for i, _ in parents], \
           [i for _, i in parents], \
           [i for i, _ in parents_sorted], \
           [i for _, i in parents_sorted]


# amount - procent rodziców
# Returns:
# 1. ObjFunction value for parents
# 2. Parents Individuals
# 3. ObjFunction value for worst members
# 4. Worst Individuals
def selection_ranking(population: list, amount, budget):
    parents = []
    penalty_func_val = None
    for matrix in population:
        try:
            penalty_func_val = get_penalty_func(get_obj_func(main_sellers_base, matrix.get_individual_matrix()), budget)
        except:
            print('Penalty function failed')
        parents.append((penalty_func_val, matrix))
    parents = sorted(parents)
    parents_amount = int(amount * len(population))
    parents_sorted = parents[population_size - parents_amount * (parents_amount - 1):]
    parents = parents[:parents_amount]
    return [i for i, _ in parents], \
           [i for _, i in parents], \
           [i for i, _ in parents_sorted], \
           [i for _, i in parents_sorted]


# def mutate_circle(matrix: np.array):
#     m, n = np.shape(matrix)
#     for i in range(m):
#         for j in range(n):
#             if j+1 >= n or i+1 >= m:
#                 break
#             elem = matrix[i][j+1]
#             matrix[i][j+1] = matrix[i][j]
#             elem1 = matrix[i+1][j+1]
#             matrix[i+1][j+1] = elem
#             elem2 = matrix[i+1][j]
#             matrix[i+1][j] = elem1
#             matrix[i][j] = elem2
#     return matrix


# def mutate_castling(matrix, type_mut='row'):
#     m, n = np.shape(matrix)
#     if type_mut == 'row':
#         pivot = m // 2
#         index_1 = randint(0, pivot-1)
#         index_2 = randint(pivot, m-1)
#         matrix[index_1], matrix[index_2] = matrix[index_2], matrix[index_1]
#         return matrix
#     if type_mut == 'col':
#         pivot = n // 2
#         index_1 = randint(0, pivot-1)
#         index_2 = randint(pivot, m-1)
#         for i in range(m):
#             matrix[i][index_1], matrix[i][index_2] = matrix[i][index_2], matrix[i][index_1]
#         return matrix


def crossover_halves(matrix1: np.array, matrix2: np.array, type_cross='rows'):
    m, n = np.shape(matrix1)
    if type_cross == 'rows':
        for i in range(m):
            if i == m // 2:
                break
            for j in range(n):
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
        return matrix1, matrix2
    elif type_cross == 'columns':
        for i in range(m):
            for j in range(n):
                if j == n // 2:
                    break
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
        return matrix1, matrix2


def crossover_every_2nd(matrix1: np.array, matrix2: np.array, creation_type='rows'):
    m, n = np.shape(matrix1)
    if creation_type == 'rows':
        for i in range(0, m, 2):
            for j in range(n):
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
        return matrix1, matrix2
    elif creation_type == 'columns':
        for i in range(m):
            for j in range(0, n, 2):
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
        return matrix1, matrix2


def crossover_chess(matrix1, matrix2):
    m, n = np.shape(matrix1)
    for i in range(m):
        for j in range(n):
            if (i + j) % 2 != 0:
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
    return matrix1, matrix2


# example of oder_list [('item_15', 7), ('item_16', 10)]
def crossover_basic(matrix1, matrix2, order_length, choice='random'):
    m, n = np.shape(matrix1)
    rows_idx_to_swap = None
    if choice == 'random':
        rows_idx_to_swap = sample([i for i in range(m)], randint(0, order_length-1))
    elif choice == 'choice':
        rows_idx_to_swap = input('Enter rows idx to swap in format: 0 2 4: ')
        rows_idx_to_swap = rows_idx_to_swap.split(' ')
        rows_idx_to_swap = [int(x) for x in rows_idx_to_swap]
    if rows_idx_to_swap is not None:
        if len(rows_idx_to_swap) == 0:
            return matrix1, matrix2
        else:
            m1 = deepcopy(matrix1)
            m2 = deepcopy(matrix2)
            for i in rows_idx_to_swap:
                m1[i], m2[i] = matrix2[i], matrix1[i]
        return m1, m2


def get_obj_func(seller_base: SellersBase, individual_matrix: np.array):
    n, m = individual_matrix.shape
    column_values = []
    for j in range(m):
        list_of_items = []
        for i in range(n):
            product = individual_matrix[i][j]
            if product > 0:
                list_of_items.append((i, product))
        sj = seller_base.get_seller_by_id(str(j)).get_delivery_price(list_of_items)
        new_prices = seller_base.get_seller_by_id(str(j)).get_discounted_price(list_of_items)
        column_values.append(sj + sum(new_prices))

    return sum(column_values), column_values


def get_penalty_func(obj_function_value, budget: int):
    diff = obj_function_value[0] - budget
    if diff > 0:
        return obj_function_value[0] + 10 * diff
    else:
        return obj_function_value[0]


def mutate_singular_product(individual_matrix: np.array):
    products_ordered = main_client.get_product_ids()
    chosen_product = rd.choice(products_ordered)
    # print('Chosen product')
    # print(chosen_product)
    dict_of_sellers = main_sellers_base.get_sellers_with_items(products_ordered)
    sellers_for_chosen_product = dict_of_sellers[chosen_product]
    row_of_chosen_product = deepcopy(individual_matrix[chosen_product])
    # print('Row of chosen products')
    # print(row_of_chosen_product)
    calculations_for_mutation = {seller_id: quantity - row_of_chosen_product[seller_id]
                                 for seller_id, quantity in sellers_for_chosen_product
                                 if row_of_chosen_product[seller_id]}
    # print('Calculations for mutation')
    # print(calculations_for_mutation)
    chosen_seller_to_give_up = rd.choice(list(calculations_for_mutation.keys()))
    ready_for_mutation = {seller_id: quantity - row_of_chosen_product[seller_id]
                          for seller_id, quantity in sellers_for_chosen_product
                          if seller_id != chosen_seller_to_give_up}
    # print('Chosen seller to give up')
    # print(chosen_seller_to_give_up)
    # print('Ready for mutation')
    # print(ready_for_mutation)
    candidates_for_mutation = [k for _, (k, v) in enumerate(ready_for_mutation.items())
                               if v != 0 and k != chosen_seller_to_give_up]
    # print('Candidates for mutation')
    # print("THIS, ", candidates_for_mutation)
    try:
        chosen_seller_to_receive = rd.choice(candidates_for_mutation)
    except:
        return individual_matrix
    # print('Chosen seller to receive')
    # print(chosen_seller_to_receive)
    individual_matrix[chosen_product][chosen_seller_to_give_up] -= 1
    individual_matrix[chosen_product][chosen_seller_to_receive] += 1
    return individual_matrix


def mutate_with_seller_elimination(individual_matrix: np.array):
    products_ordered = main_client.get_product_ids()
    chosen_product = rd.choice(products_ordered)
    # print('Chosen product')
    # print(chosen_product)
    dict_of_sellers = main_sellers_base.get_sellers_with_items(products_ordered)
    sellers_for_chosen_product = dict_of_sellers[chosen_product]
    row_of_chosen_product = deepcopy(individual_matrix[chosen_product])
    # print('Row of chosen products')
    # print(row_of_chosen_product)
    calculation_for_mutation = {seller_id: amount for seller_id, amount in enumerate(row_of_chosen_product) if amount}
    # print('Calculation for mutation')
    # print(calculation_for_mutation)
    chosen_seller_to_give_up = rd.choice(list(calculation_for_mutation.keys()))
    # print('Chosen to give')
    # print(chosen_seller_to_give_up)
    list_with_max_quantities = [0 for _ in row_of_chosen_product]
    for idx, amount in sellers_for_chosen_product:
        if idx != chosen_seller_to_give_up:
            list_with_max_quantities[idx] = amount
    list_to_draw_from = [idx for (idx, amount) in sellers_for_chosen_product
                         if idx != chosen_seller_to_give_up and amount != row_of_chosen_product[idx]]
    while individual_matrix[chosen_product][chosen_seller_to_give_up] and list_to_draw_from:
        # print('Changing row')
        # print(individual_matrix[chosen_product])
        individual_matrix[chosen_product][chosen_seller_to_give_up] -= 1
        chosen_seller_to_receive = rd.choice(list_to_draw_from)
        individual_matrix[chosen_product][chosen_seller_to_receive] += 1
        if individual_matrix[chosen_product][chosen_seller_to_receive] == list_with_max_quantities[chosen_seller_to_receive]:
            list_to_draw_from.remove(chosen_seller_to_receive)
    return individual_matrix


population_size = 10
selection_method = 'ranking'
parent_percentage = 0.2
chance_to_crossover = 0.5
mutation_type = 'singular'
max_iters = 100
iters_without_change = 15
main_inventory = GeneralInventory()
main_sellers_base = SellersBase(main_inventory)
main_client = Client(0, [('item_1', 7), ('item_2', 10), ('item_5', 2), ('item_6', 4), ('item_8', 6), ('item_9', 4),
                         ('item_10', 1)], 1600, main_inventory)
dict_of_sells = main_sellers_base.get_sellers_with_items(main_client.get_product_ids())
list_of_orders = main_client.get_oder_quantity()
general_population = []
for _ in range(population_size):
    individual = Individual(main_sellers_base.sellers_list, main_inventory.product_list)
    individual.get_starting_individual(dict_of_sells, list_of_orders, 'random')
    individual.set_individual_fitness_func_val(get_obj_func(main_sellers_base, individual.get_individual_matrix()))
    general_population.append(individual)


def main():
    obj_functions_to_plot = []
    i_iter = 1
    iter_counter = 0
    starting_population = general_population
    current_lowest_obj_func = np.inf
    current_best_solution = None
    potential_individual = Individual(main_sellers_base.sellers_list, main_inventory.product_list)
    while i_iter <= max_iters and iter_counter <= iters_without_change:
        if selection_method == 'tournament':
            obj_funcs, temp_pop, worst_funcs, comparison_pop = selection_tournament(starting_population,
                                                                                    parent_percentage,
                                                                                    main_client.budget)
            if i_iter == 1:
                current_lowest_obj_func = min(obj_funcs)
                current_best_solution = temp_pop[obj_funcs.index(current_lowest_obj_func)]
        elif selection_method == 'roulette':
            obj_funcs, temp_pop, worst_funcs, comparison_pop = selection_roulette(starting_population,
                                                                                  parent_percentage,
                                                                                  main_client.budget)
            if i_iter == 1:
                current_lowest_obj_func = min(obj_funcs)
                current_best_solution = temp_pop[obj_funcs.index(current_lowest_obj_func)]
        elif selection_method == 'ranking':
            obj_funcs, temp_pop, worst_funcs, comparison_pop = selection_ranking(starting_population,
                                                                                 parent_percentage,
                                                                                 main_client.budget)
            if i_iter == 1:
                current_lowest_obj_func = obj_funcs[0]
                current_best_solution = temp_pop[0]
        else:
            obj_funcs, temp_pop, worst_funcs, comparison_pop = [None] * 4
            return obj_funcs, temp_pop, worst_funcs, comparison_pop

        if rd.random() > chance_to_crossover:
            baby1, baby2 = crossover_basic(temp_pop[0].get_individual_matrix(),
                                           temp_pop[1].get_individual_matrix(),
                                           len(main_client.get_order()))
        else:
            baby1, baby2 = temp_pop[0].get_individual_matrix(), temp_pop[1].get_individual_matrix()
        if mutation_type == 'singular':
            baby1, baby2 = mutate_singular_product(np.array(baby1)), mutate_singular_product(np.array(baby2))
        else:
            baby1, baby2 = mutate_with_seller_elimination(np.array(baby1)), \
                           mutate_with_seller_elimination(np.array(baby2))
        potential_individual.set_individual_matrix(baby1)
        potential_individual.set_individual_fitness_func_val(get_obj_func(main_sellers_base,
                                                                          potential_individual.get_individual_matrix()))
        offspring = [(get_penalty_func(get_obj_func(main_sellers_base, potential_individual.get_individual_matrix()),
                                       main_client.budget), deepcopy(potential_individual))]

        potential_individual.set_individual_matrix(baby2)
        potential_individual.set_individual_fitness_func_val(get_obj_func(main_sellers_base,
                                                                          potential_individual.get_individual_matrix()))
        offspring.append((
                         get_penalty_func(get_obj_func(main_sellers_base, potential_individual.get_individual_matrix()),
                                          main_client.budget), deepcopy(potential_individual)))
        offspring = sorted(offspring)
        k = 0
        offspring_count = len(offspring)
        for func_i, offspring_i in offspring:
            while func_i > worst_funcs[k]:
                k += 1
                if k == offspring_count:
                    break
            if k != offspring_count:
                general_population.remove(comparison_pop[-1])
                worst_funcs.insert(k, func_i)
                worst_funcs.pop()
                comparison_pop.insert(k, offspring_i)
                comparison_pop.pop()
                general_population.append(comparison_pop[k])

                if func_i < current_lowest_obj_func:
                    iter_counter = 0
                    current_lowest_obj_func = func_i
                    current_best_solution = offspring_i
            else:
                break
        i_iter += 1
        iter_counter += 1
        obj_functions_to_plot.append(current_lowest_obj_func)
        print(i_iter)
    plt.figure()
    plt.plot(np.arange(1, i_iter), obj_functions_to_plot)
    plt.show()


if __name__ == '__main__':
    main()
