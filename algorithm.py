# functions needed to work out the final solution based on the evolutionary algorithm
import copy

from solution import Solution
from random import randint, sample
import numpy as np


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
        pass

    # TODO: Implement later
    def crossover(self):
        pass

    # TODO: Implement later    def mutation(self):
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


def selection_tournament(population: list):
    pass


def selection_roulette(population: list):
    pass


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


def mutate_castling(matrix, type='row'):
    m, n = np.shape(matrix)
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
        rows_idx_to_swap = sample([i for i in range(m)], order_length-1)
    elif choice == 'choice':
        rows_idx_to_swap = input('Enter rows idx to swap in format: 0 2 4: ')
        rows_idx_to_swap = rows_idx_to_swap.split(' ')
        rows_idx_to_swap = [int(x) for x in rows_idx_to_swap]
    if rows_idx_to_swap is not None:
        if len(rows_idx_to_swap) == 0:
            return matrix1, matrix2
        else:
            m1 = copy.deepcopy(matrix1)
            m2 = copy.deepcopy(matrix2)
            for i in rows_idx_to_swap:
                # TODO: SOLVE IT BETTER (Tuples don't work)
                m1[i], m2[i] = matrix2[i], matrix1[i]
        return m1, m2


def crossover_e(matrix1, matrix2, number_of_rows, choice='random'):
    m,n = np.shape(matrix1)
    rows_idx_to_swap = None
    if choice == 'random':
        rows_idx_to_swap = sample([i for i in range(m)], number_of_rows-1)
    elif choice == 'choice':
        rows_idx_to_swap = input('Enter rows idx to swap in format: 0 2 4: ')
        rows_idx_to_swap = rows_idx_to_swap.split(' ')
        rows_idx_to_swap = [int(x) for x in rows_idx_to_swap]
    if rows_idx_to_swap is not None:
        if len(rows_idx_to_swap) == 0:
            return matrix1, matrix2
        else:
            m1 = copy.deepcopy(matrix1)
            m2 = copy.deepcopy(matrix2)
            for i in rows_idx_to_swap:
                # TODO: SOLVE IT BETTER (Tuples don't work)
                m1[i], m2[i] = sample(matrix2[i], len(matrix2)), sample(matrix1[i], len(matrix1))
        return m1, m2




matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix1 = np.array([[11,22,33],[44,55,66],[77,88,99]])
matrix_rect = [[1,2,3],[4,5,6]]
matrix_rect1 = [[11,22,33],[44,55,66]]
matrix_2 = [[1,2],[3,4]]
matrix_3 = [[5,6],[7,8]]

# crossover_basic(matrix, matrix1, 3, 1)
print(matrix)
print()
print(matrix1)
m1, m2 = crossover_basic(matrix, matrix1, 3, 'random')
print()
print(m1)
print()
print(m2)

# print(mutate_circle(matrix))
# print(crossover_halves(matrix, matrix1, 'columns'))

