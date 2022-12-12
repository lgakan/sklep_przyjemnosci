# functions needed to work out the final solution based on the evolutionary algorithm
from solution import Solution


class EvolutionaryAlgorithm:

    def __init__(self, first_solution: Solution, stop_condition, mutation_prob: float = 0.05):
        self.first_solution = first_solution
        self.stop_condition = stop_condition
        self.mutation_prob = mutation_prob

    def evolution(self):
        t = 0
        while True:
            pass
