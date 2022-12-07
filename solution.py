import numpy as np


class Solution:
    def __init__(self, sellers, items):
        self.solution_matrix = None
        self.create_solution_matrix(len(sellers), len(items))
        self.current_best = None

    def create_solution_matrix(self, size_s, size_i):
        self.solution_matrix = np.zeros((size_i, size_s), dtype=np.int)

    def get_starting_solution(self, list_of_ids: list, list_of_seller_ids: list, construct_type: str):
        pass

    def get_currently_best_solution(self):
        return self.current_best

    def get_solution_matrix_shape(self):
        return len(self.solution_matrix), len(self.solution_matrix[0])

    def __repr__(self):
        return self.solution_matrix.__str__()
