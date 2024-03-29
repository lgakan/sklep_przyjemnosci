# functions needed to work out the final solution based on the evolutionary algorithm
import csv
from solution import Solution
from random import randint
from random import sample
import numpy as np
from objective_function import ObjFunction
import random as rd
from client import Client
from seller_base import SellersBase
from general_inventory import GeneralInventory
from copy import deepcopy


new_population_created = False
population_size = 10
selection_method = 'ranking'
crossover_method = ('basic', 'rows_idx_and_number')
# Parent_count*(Parent_count - 1) < Population_size
parent_percentage = 0.2
chance_to_crossover = 0.5
mutation_type = 'singular'
max_iters = 100
iters_without_change = 15
budget = 1600
maxes = [[267, 199, 314, 376, 284, 293, 238, 352, 268, 214, 218, 274, 246, 200, 321, 224, 373, 330, 346, 311, 306, 321, 264, 266, 236, 195, 230, 203, 336, 286, 277, 252, 251, 244, 288, 225, 199, 249, 212, 224, 314, 290, 404, 388, 303, 322, 266, 292, 266, 340],
         [157, 193, 184, 104, 179, 203, 147, 170, 210, 153, 141, 189, 133, 153, 184, 184, 159, 233, 86, 198, 196, 155, 175, 179, 209, 109, 120, 216, 166, 154],
         [148, 183, 77, 91, 157, 136, 94, 175, 127, 126, 84, 162, 205, 125, 162, 106, 122, 162, 122, 77]]
path_to_inventory = 'small_unique_items_file.csv'
path_to_seller_base = 'small_unique_sellers.csv'
path_to_db = 'database_small.csv'
chosen_max = maxes[2]
main_inventory = GeneralInventory(path_to_inventory)
main_sellers_base = SellersBase(main_inventory, path_to_seller_base, path_to_db)

shopping_list = [('item_1', 7), ('item_2', 10), ('item_5', 2), ('item_6', 4), ('item_8', 6), ('item_9', 4), ('item_10', 1)]
main_client = Client(0, shopping_list, budget, main_inventory)
sol = Solution(main_sellers_base.sellers_list, main_inventory.product_list)
dict_of_sells = main_sellers_base.get_sellers_with_items(main_client.get_product_ids())
list_of_orders = main_client.get_oder_quantity()
general_population = []
for _ in range(population_size):
    sol.get_starting_solution(dict_of_sells,
                              list_of_orders,
                              'random')
    general_population.append(deepcopy(sol))
    sol.reset_solution()
# TODO: Delete if not necessary
sol_mat = deepcopy(sol.solution_matrix)
general_population_copy = deepcopy(general_population)


# Returns:
# 1. ObjFunction value for parents
# 2. Parents Solutions
# 3. ObjFunction value for worst members
# 4. Worst members Solutions
def selection_tournament(population: list, amount, budget):
    parents = []
    for matrix in population:
        parents.append((get_penalty_func(ObjFunction(matrix, main_sellers_base, main_inventory), budget), matrix))
    parents_amount = int(amount * population_size)
    parents.sort(key=lambda x: x[0])
    parents_sorted = parents[population_size - parents_amount * (parents_amount - 1):]
    while len(parents) > parents_amount:
        for i in range(0, len(parents)//2, 2):
            if parents[i][0] < parents[i+1][0]:
                parents.remove(parents[i+1])
            else:
                parents.remove(parents[i])
    return [i for i, _ in parents], \
           [i for _, i in parents], \
           [i for i, _ in parents_sorted], \
           [i for _, i in parents_sorted]


# Returns:
# 1. ObjFunction value for parents
# 2. Parents Solutions
# 3. ObjFunction value for worst members
# 4. Worst members Solutions
def selection_roulette(population: list, amount, budget):
    parents_amount = int(amount * population_size)
    parents = []
    for matrix in population:
        parents.append([get_penalty_func(ObjFunction(matrix, main_sellers_base, main_inventory), budget), matrix])
    parents.sort(key=lambda x: x[0])
    parents_sorted = parents[population_size - parents_amount * (parents_amount - 1):]
    for i in range(population_size):
        parents[i].append(population_size-i)
    new_list_of_solutions = []
    for i in range(population_size):
        for j in range(parents[i][2]):
            new_list_of_solutions.append((parents[i][0], parents[i][1]))
    rd.shuffle(new_list_of_solutions)
    parents.clear()
    for i in range(parents_amount):
        parents.append(new_list_of_solutions[0])
        new_list_of_solutions = list(filter((parents[-1]).__ne__, new_list_of_solutions))
    return [i for i, _ in parents], \
           [i for _, i in parents], \
           [i[0] for i in parents_sorted], \
           [i[1] for i in parents_sorted]


# Returns:
# 1. ObjFunction value for parents
# 2. Parents Solutions
# 3. ObjFunction value for worst members
# 4. Worst members Solutions
def selection_ranking(population: list, amount, budget):
    parents = []
    for matrix in population:
        parents.append((get_penalty_func(ObjFunction(matrix, main_sellers_base, main_inventory), budget), matrix))
    parents.sort(key=lambda x: x[0])
    parents_amount = int(amount * len(population))
    parents_sorted = parents[population_size - parents_amount * (parents_amount - 1):]
    parents = parents[:parents_amount]
    return [i for i, _ in parents], \
           [i for _, i in parents], \
           [i for i, _ in parents_sorted], \
           [i for _, i in parents_sorted]


def crossover_every_2nd(numpy_matrices_list: list, type_cross='rows'):
    m, n = np.shape(numpy_matrices_list[0])
    matrices_list = [i.tolist() for i in numpy_matrices_list]
    list_to_return = []
    for i in range(len(matrices_list)):
        for j in range(i, len(matrices_list)):
            if i != j:
                matrix1 = matrices_list[i]
                matrix2 = matrices_list[j]
                if type_cross == 'rows':
                    for x in range(0, m, 2):
                        for y in range(n):
                            matrix1[x][y], matrix2[x][y] = matrix2[x][y], matrix1[x][y]
                    list_to_return.append(matrix1)
                    list_to_return.append(matrix2)
                elif type_cross == 'columns':
                    for x in range(m):
                        for y in range(0, n, 2):
                            matrix1[x][y], matrix2[x][y] = matrix2[x][y], matrix1[x][y]
                    list_to_return.append(matrix1)
                    list_to_return.append(matrix2)
    return [np.array(i) for i in list_to_return]


# example of oder_list [('item_15', 7), ('item_16', 10)]
def crossover_basic(numpy_matrices_list: list, order_length: int, choice='random', mode="rows_idx_and_number"):
    m, n = np.shape(numpy_matrices_list[0])
    rows_idx_to_swap = None
    if order_length >= m:
        order_length = m-1
    if order_length == 1:
        order_length += 1
    if choice == 'random':
        if mode == 'rows_idx':
            rows_idx_to_swap = sample([i for i in range(m)],  order_length // 2)
        if mode == 'rows_number':
            rows_idx_to_swap = sample([i for i in range(0, m-1, 2)], randint(1, (order_length // 2) - 1))
        if mode == 'rows_idx_and_number':
            rows_idx_to_swap = sample([i for i in range(m)], randint(1, order_length - 1))
    elif choice == 'choice':
        if mode == 1:
            rows_idx_to_swap = input('Enter rows idx to swap in format: 0 2 4: ')
            rows_idx_to_swap = rows_idx_to_swap.split(' ')
            rows_idx_to_swap = [int(x) for x in rows_idx_to_swap]
            rows_idx_to_swap = list(set(rows_idx_to_swap))
            if len(rows_idx_to_swap) > m:
                rows_idx_to_swap = rows_idx_to_swap[0:m]
            for i in range(len(rows_idx_to_swap)):
                if rows_idx_to_swap[i] >= m:
                    rows_idx_to_swap[i] = m-1
            rows_idx_to_swap = list(set(rows_idx_to_swap))
    if rows_idx_to_swap is not None:
        if len(rows_idx_to_swap) == 0:
            return numpy_matrices_list
        else:
            list_to_return = []
            matrices_list = [i.tolist() for i in numpy_matrices_list]
            for i in range(len(matrices_list)):
                for j in range(i, len(matrices_list)):
                    if i != j:
                        m1 = matrices_list[i]
                        m2 = matrices_list[j]
                        for x in rows_idx_to_swap:
                            m1[x], m2[x] = m2[x], m1[x]
                        list_to_return.append(m1)
                        list_to_return.append(m2)
            return [np.array(i) for i in list_to_return]


def get_penalty_func(solution: ObjFunction, budget):
    obj_func = solution.get_objective_func()
    diff = obj_func[0] - budget
    if diff > 0:
        return obj_func[0] + 10*diff
    else:
        return obj_func[0]


def mutate_singular_product(sol_matrix: np.array, client):
    products_ordered = client.get_product_ids()
    candidates_for_mutation = []
    chosen_product = None
    chosen_seller_to_give_up = None
    while not len(candidates_for_mutation):
        chosen_product = rd.choice(products_ordered)
        # print('Chosen product')
        # print(chosen_product)
        dict_of_sellers = main_sellers_base.get_sellers_with_items(products_ordered)
        sellers_for_chosen_product = dict_of_sellers[chosen_product]
        row_of_chosen_product = deepcopy(sol_matrix[chosen_product])
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
    # print(candidates_for_mutation)
    chosen_seller_to_receive = rd.choice(candidates_for_mutation)
    # print('Chosen seller to receive')
    # print(chosen_seller_to_receive)
    sol_matrix[chosen_product][chosen_seller_to_give_up] -= 1
    sol_matrix[chosen_product][chosen_seller_to_receive] += 1
    return sol_matrix


def mutate_with_seller_elimination(sol_matrix: np.array, client):
    products_ordered = client.get_product_ids()
    chosen_product = rd.choice(products_ordered)
    # print('Chosen product')
    # print(chosen_product)
    dict_of_sellers = main_sellers_base.get_sellers_with_items(products_ordered)
    sellers_for_chosen_product = dict_of_sellers[chosen_product]
    row_of_chosen_product = deepcopy(sol_matrix[chosen_product])
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
    while sol_matrix[chosen_product][chosen_seller_to_give_up] and list_to_draw_from:
        # print('Changing row')
        # print(sol_matrix[chosen_product])
        sol_matrix[chosen_product][chosen_seller_to_give_up] -= 1
        chosen_seller_to_receive = rd.choice(list_to_draw_from)
        sol_matrix[chosen_product][chosen_seller_to_receive] += 1
        if sol_matrix[chosen_product][chosen_seller_to_receive] == list_with_max_quantities[chosen_seller_to_receive]:
            list_to_draw_from.remove(chosen_seller_to_receive)
    return sol_matrix


def create_report(csv_path: str, ordered_data: list):
    with open(csv_path, 'a', newline='') as file:
        # for clean view in Excel, you need to add , delimiter=';'
        writer_object = csv.writer(file, delimiter=';')
        writer_object.writerow(ordered_data)


def main():
    obj_functions_to_plot = []
    i_iter = 1
    iter_counter = 0
    starting_population = deepcopy(general_population)
    current_best_solution = None
    current_lowest_obj_func = np.inf
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
        if rd.random() > chance_to_crossover:
            if crossover_method == ('basic', 'rows_idx'):
                baby_matrices = crossover_basic([i.get_solution_matrix() for i in temp_pop],
                                                len(main_client.get_order()),
                                                mode='rows_idx')
            elif crossover_method == ('basic', 'rows_number'):
                baby_matrices = crossover_basic([i.get_solution_matrix() for i in temp_pop],
                                                len(main_client.get_order()),
                                                mode='rows_number')
            elif crossover_method == ('basic', 'rows_idx_and_number'):
                baby_matrices = crossover_basic([i.get_solution_matrix() for i in temp_pop],
                                                len(main_client.get_order()),
                                                mode='rows_idx_and_number')
            elif crossover_method == 'every_2nd':
                baby_matrices = crossover_every_2nd([i.get_solution_matrix() for i in temp_pop])
            else:
                baby_matrices = None
        else:
            baby_matrices = [i.get_solution_matrix() for i in temp_pop]
        if mutation_type == 'singular':
            baby_matrices = [mutate_singular_product(np.array(i), main_client) for i in baby_matrices]
        else:
            baby_matrices = [mutate_with_seller_elimination(np.array(i), main_client) for i in baby_matrices]
        offspring = []
        for baby in baby_matrices:
            sol.solution_matrix = deepcopy(baby)
            offspring.append((get_penalty_func(ObjFunction(sol, main_sellers_base, main_inventory), main_client.budget),
                              deepcopy(sol)))
            sol.reset_solution()
        offspring.sort(key=lambda x: x[0])
        k = 0
        offspring_count = len(offspring)
        for func_i, offspring_i in offspring:
            while func_i > worst_funcs[k]:
                k += 1
                if k == offspring_count:
                    break
            if k != offspring_count:
                starting_population.remove(comparison_pop[-1])
                worst_funcs.insert(k, func_i)
                worst_funcs.pop()
                comparison_pop.insert(k, offspring_i)
                comparison_pop.pop()
                starting_population.append(comparison_pop[k])

                if func_i < current_lowest_obj_func:
                    iter_counter = 0
                    current_lowest_obj_func = func_i
                    current_best_solution = offspring_i
            else:
                break
        i_iter += 1
        iter_counter += 1
        obj_functions_to_plot.append(current_lowest_obj_func)

    return current_best_solution, current_lowest_obj_func, i_iter, obj_functions_to_plot


if __name__ == '__main__':
    main()
