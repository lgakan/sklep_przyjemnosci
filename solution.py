import numpy as np


class Solution:
    def __int__(self, sellers, items):
        self.solution_matrix = None
        self.create_solution_matrix(len(sellers), len(items))
        self.current_best = None

    def create_solution_matrix(self, size_s, size_i):
        self.solution_matrix = np.zeros((size_s + 1, size_i))

    def get_starting_solution(self):
        pass

    def get_currently_best_solution(self):
        return self.current_best
