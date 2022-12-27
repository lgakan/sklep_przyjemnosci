# functions needed to work out the final solution based on the evolutionary algorithm
from solution import Solution
from random import randint
import numpy as np
from objective_function import ObjFunction
import random as rd
from client import Client
from seller_base import SellersBase
from general_inventory import GeneralInventory
from copy import deepcopy

main_inventory = GeneralInventory()
main_sellers_base = SellersBase(main_inventory)
main_client = Client(0, [('item_1', 7),
                         ('item_2', 10),
                         ('item_5', 2),
                         ('item_6', 4),
                         ('item_8', 6),
                         ('item_9', 4),
                         ('item_10', 1)], 800, main_inventory)
sol = Solution(main_sellers_base.sellers_list, main_inventory.product_list)
sol.get_starting_solution(main_sellers_base.get_sellers_with_items(main_client.get_product_ids()),
                          main_client.get_oder_quantity(), 'random')
sol_mat = deepcopy(sol.solution_matrix)


class EvolutionaryAlgorithm:

    def __init__(self, first_solution: Solution, stop_condition: callable, mutation_prob: float = 0.05):
        self.first_solution = first_solution
        self.stop_condition = stop_condition
        self.mutation_prob = mutation_prob

    # TODO: Implement later
    # population - lista macierzy rozwiązań, możemy startowo przyjąć, że będzie ich 10
    def evolution(self, population: list):
        t = 0

        while True:
        # teraz niby w algorytmie jest, by ocenić populację. I jest pytanie czy chcemy oceniać od razu każdą z macierzy,
        # bo wsm nie wiem jak inaczej moglibyśmy to zrobić.
        # Ja bym ocenił wszystkich i wybrał 2 najlepszych na rodziców
            pass

    # TODO: Implement later
    def mutation(self):
        pass

    # TODO: Implement later
    def crossover(self):
        pass

    # TODO: Implement later
    def selection(self):
        pass

    # TODO: Implement later
    def generate_population(self, solution: Solution, dict_of_items_with_sellers, order_list):
        population = []
        for i in range(10):
            if i == 1:
                individual = solution.get_starting_solution(dict_of_items_with_sellers, order_list, 'left')
            else:
                individual = solution.get_starting_solution(dict_of_items_with_sellers, order_list, 'random')
            population.append(individual)
        return population


def mutate_castling(matrix, type='row'):
    m = len(matrix)
    n = len(matrix[0])
    if type == 'row':
        pivot = m // 2
        index_1 = randint(0, pivot-1)
        index_2 = randint(pivot, m-1)
        matrix[index_1], matrix[index_2] = matrix[index_2], matrix[index_1]
        return matrix
    if type == 'col':
        pivot = n // 2
        index_1 = randint(0, pivot-1)
        index_2 = randint(pivot, m-1)
        for i in range(m):
            matrix[i][index_1], matrix[i][index_2] = matrix[i][index_2], matrix[i][index_1]
        return matrix

# population - lista macierzy solution
# amount - ile rodziców chcemy
def selection_tournament(population: list, amount, budget):
    parents = []
    for matrix in population:
        parents.append((get_penalty_func(matrix, budget), matrix))
    parents_amount = amount * len(population)
    while len(parents) > parents_amount:
        for i in range(0, len(parents)//2, 2):
            if parents[i][0] < parents[i+1][0]:
                parents.remove(parents[i+1])
            else:
                parents.remove(parents[i])
    for i in range(len(parents)):
        parents[i] = parents[i][1]
    return parents

def selection_roulette(population: list, amount, budget):
    parents_amount = amount * len(population)
    parents = []
    for matrix in population:
        parents.append([get_penalty_func(matrix, budget), matrix])
    parents = sorted(parents)
    length = len(parents)
    for i in range(length):
        parents[i].append(length-i)
    new_list_of_solutions = []
    for i in range(length):
        for j in range(parents[i][2]):
            new_list_of_solutions.append(parents[i][1])
    rd.shuffle(new_list_of_solutions)
    parents_chosen = new_list_of_solutions[:parents_amount]
    return parents_chosen



# amount - procent rodziców
def selection_ranking(population: list, amount, budget):
    parents = []
    for matrix in population:
        parents.append((get_penalty_func(matrix, budget), matrix))
    parents = sorted(parents)
    parents_amount = amount * len(population)
    parents = parents[:parents_amount+1]
    for i in range(parents_amount):
        parents[i] = parents[i][1]
    return parents



def crossover_chess(matrix1, matrix2):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if (i + j) % 2 != 0:
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
    return matrix1, matrix2


def mutate_circle(matrix: np.array):
    # m = len(matrix)   # ilość wierszy
    # n = len(matrix[0])   # ilość kolumn
    m, n = np.shape(matrix)
    for i in range(m):
        for j in range(n):
            if j+1 >= n or i+1 >= m:
                break
            elem = matrix[i][j+1]
            matrix[i][j+1] = matrix[i][j]
            elem1 = matrix[i+1][j+1]
            matrix[i+1][j+1] = elem
            elem2 = matrix[i+1][j]
            matrix[i+1][j] = elem1
            matrix[i][j] = elem2
    return matrix


def crossover_halves(matrix1: np.array, matrix2: np.array, type='rows'):
    # m1 = len(matrix1)   # ilość wierszy
    # n1 = len(matrix1[0])   # ilość kolumn
    # m2 = len(matrix2)   # ilość wierszy
    # n2 = len(matrix2[0])   # ilość kolumn
    # if m1 != m2 or n1 != n2:
    #     return None
    # m = len(matrix1)
    # n = len(matrix1[0])
    m, n = np.shape(matrix)
    if type == 'rows':
        for i in range(m):
            if i == m//2:
                break
            for j in range(n):
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
        return matrix1, matrix2
    elif type == 'columns':
        for i in range(m):
            for j in range(n):
                if j == n//2:
                    break
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
        return matrix1, matrix2


def crossover_every_2nd(matrix1: np.array, matrix2: np.array, type='rows'):
    # m = len(matrix1)
    # n = len(matrix1[0])
    m, n = np.shape(matrix)
    if type == 'rows':
        for i in range(0, m, 2):
            for j in range(n):
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
        return matrix1, matrix2
    elif type == 'columns':
        for i in range(m):
            for j in range(0, n, 2):
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
        return matrix1, matrix2


def get_penalty_func(solution: ObjFunction, budget):
    obj_func = solution.get_objective_func()
    diff = obj_func - budget
    if diff > 0:
        return obj_func + 10*diff
    else:
        return obj_func


def mutate_singular_product(sol_matrix: np.array):
    products_ordered = main_client.get_product_ids()
    chosen_product = rd.choice(products_ordered)
    print('Chosen product')
    print(chosen_product)
    dict_of_sellers = main_sellers_base.get_sellers_with_items(products_ordered)
    sellers_for_chosen_product = dict_of_sellers[chosen_product]
    row_of_chosen_product = deepcopy(sol_matrix[chosen_product])
    print('Row of chosen products')
    print(row_of_chosen_product)
    calculations_for_mutation = {seller_id: quantity - row_of_chosen_product[seller_id]
                                 for seller_id, quantity in sellers_for_chosen_product
                                 if row_of_chosen_product[seller_id]}
    print('Calculations for mutation')
    print(calculations_for_mutation)
    chosen_seller_to_give_up = rd.choice(list(calculations_for_mutation.keys()))
    ready_for_mutation = {seller_id: quantity - row_of_chosen_product[seller_id]
                          for seller_id, quantity in sellers_for_chosen_product
                          if seller_id != chosen_seller_to_give_up}
    print('Chosen seller to give up')
    print(chosen_seller_to_give_up)
    print('Ready for mutation')
    print(ready_for_mutation)
    candidates_for_mutation = [k for _, (k, v) in enumerate(ready_for_mutation.items())
                               if v != 0 and k != chosen_seller_to_give_up]
    print('Candidates for mutation')
    print(candidates_for_mutation)
    chosen_seller_to_receive = rd.choice(candidates_for_mutation)
    print('Chosen seller to receive')
    print(chosen_seller_to_receive)
    sol_matrix[chosen_product][chosen_seller_to_give_up] -= 1
    sol_matrix[chosen_product][chosen_seller_to_receive] += 1
    return sol_matrix


def mutate_with_seller_elimination(sol_matrix: np.array):
    products_ordered = main_client.get_product_ids()
    chosen_product = rd.choice(products_ordered)
    print('Chosen product')
    print(chosen_product)
    dict_of_sellers = main_sellers_base.get_sellers_with_items(products_ordered)
    sellers_for_chosen_product = dict_of_sellers[chosen_product]
    row_of_chosen_product = deepcopy(sol_matrix[chosen_product])
    print('Row of chosen products')
    print(row_of_chosen_product)
    calculation_for_mutation = {seller_id: amount for seller_id, amount in enumerate(row_of_chosen_product) if amount}
    print('Calculation for mutation')
    print(calculation_for_mutation)
    chosen_seller_to_give_up = rd.choice(list(calculation_for_mutation.keys()))
    print('Chosen to give')
    print(chosen_seller_to_give_up)
    list_with_max_quantities = [0 for _ in row_of_chosen_product]
    for idx, amount in sellers_for_chosen_product:
        if idx != chosen_seller_to_give_up:
            list_with_max_quantities[idx] = amount
    list_to_draw_from = [idx for (idx, amount) in sellers_for_chosen_product
                         if idx != chosen_seller_to_give_up and amount != row_of_chosen_product[idx]]
    while sol_matrix[chosen_product][chosen_seller_to_give_up] and list_to_draw_from:
        print('Changing row')
        print(sol_matrix[chosen_product])
        sol_matrix[chosen_product][chosen_seller_to_give_up] -= 1
        chosen_seller_to_receive = rd.choice(list_to_draw_from)
        sol_matrix[chosen_product][chosen_seller_to_receive] += 1
        if sol_matrix[chosen_product][chosen_seller_to_receive] == list_with_max_quantities[chosen_seller_to_receive]:
            list_to_draw_from.remove(chosen_seller_to_receive)
    return sol_matrix


matrix = [[[1,2,3],[4,5,6],[7,8,9]], [[11,22,33],[44,55,66],[77,88,99]], [[1,22,3],[4,55,6],[47,18,9]]]
matrix1 = np.array([[11,22,33],[44,55,66],[77,88,99]])
# matrix_rect = [[1,2,3],[4,5,6]]
# matrix_rect1 = [[11,22,33],[44,55,66]]
# matrix_2 = [[1,2],[3,4]]
# matrix_3 = [[5,6],[7,8]]

# print(selection_ranking(matrix, 0.5, 200))
# print(crossover_halves(matrix, matrix1, 'columns'))
print(sol)
print(mutate_with_seller_elimination(sol_mat))
