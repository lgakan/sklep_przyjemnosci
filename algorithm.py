# functions needed to work out the final solution based on the evolutionary algorithm
from solution import Solution
from random import randint

class EvolutionaryAlgorithm:

    def __init__(self, first_solution: Solution, stop_condition: callable, mutation_prob: float = 0.05):
        self.first_solution = first_solution
        self.stop_condition = stop_condition
        self.mutation_prob = mutation_prob

    # TODO: Implement later
    def evolution(self):
        t = 0
        while True:
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
    def generate_population(self):
        pass


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


def crossover_chess(matrix1, matrix2):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if (i + j) % 2 != 0:
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
    return matrix1, matrix2


def mutate_circle(matrix):
    m = len(matrix)   # ilość wierszy
    n = len(matrix[0])   # ilość kolumn
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


def crossover_halves(matrix1, matrix2, type='rows'):
    # m1 = len(matrix1)   # ilość wierszy
    # n1 = len(matrix1[0])   # ilość kolumn
    # m2 = len(matrix2)   # ilość wierszy
    # n2 = len(matrix2[0])   # ilość kolumn
    # if m1 != m2 or n1 != n2:
    #     return None
    m = len(matrix1)
    n = len(matrix1[0])
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


def crossover_every_2nd(matrix1, matrix2, type='rows'):
    m = len(matrix1)
    n = len(matrix1[0])
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


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix1 = [[11,22,33],[44,55,66],[77,88,99]]
matrix_rect = [[1,2,3],[4,5,6]]
matrix_rect1 = [[11,22,33],[44,55,66]]
matrix_2 = [[1,2],[3,4]]
matrix_3 = [[5,6],[7,8]]

# print(mutate_circle(matrix))
print(crossover_every_2nd(matrix, matrix1, 'columns'))

