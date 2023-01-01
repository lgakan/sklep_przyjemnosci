import numpy as np
import random as rd


class Individual:
    def __init__(self, sellers, items):
        self.individual_matrix = np.zeros((len(sellers), len(items)), dtype=np.int)
        self.fitness_func_value = None

    def get_starting_individual(self, dict_of_items_with_sellers, order_list, construct_type: str):
        if construct_type == 'left':
            for i, (product_row, values) in enumerate(dict_of_items_with_sellers.items()):
                quantity_from_buyer = order_list[i]
                j = 0
                while quantity_from_buyer > 0:
                    seller_id, quantity_from_seller = values[j]
                    slots = min(quantity_from_buyer, quantity_from_seller)
                    self.individual_matrix[product_row][seller_id] = slots
                    quantity_from_buyer -= slots
                    j += 1
        elif construct_type == 'random':
            for i, (product_row, values) in enumerate(dict_of_items_with_sellers.items()):
                input_list_of_sellers = np.array(self.individual_matrix[product_row])
                for j, (seller_id, quantity_from_seller) in enumerate(values):
                    input_list_of_sellers[seller_id] = quantity_from_seller
                concatenated_sellers = list(np.concatenate(np.array([a_i * [i] for i, a_i in
                                                                     enumerate(input_list_of_sellers)
                                                                     if a_i != 0], dtype=object)))
                rd.shuffle(concatenated_sellers)
                quantity_from_buyer = order_list[i]
                sellers_chosen = concatenated_sellers[:quantity_from_buyer]
                for seller in sellers_chosen:
                    self.individual_matrix[product_row][seller] += 1

    def get_individual_matrix_shape(self):
        return len(self.individual_matrix), len(self.individual_matrix[0])

    def reset_individual(self):
        for i, _ in enumerate(self.individual_matrix):
            self.individual_matrix[i].fill(0)

    def get_individual_matrix(self):
        return self.individual_matrix

    def get_individual_fitness_func(self):
        return self.fitness_func_value

    def set_individual_matrix(self, matrix):
        self.individual_matrix = matrix

    def set_individual_fitness_func_val(self, individual_fitness_func_val):
        self.fitness_func_value = individual_fitness_func_val

    def __gt__(self, other):
        return self.fitness_func_value > other.fitness_func_value

    def __lt__(self, other):
        return self.fitness_func_value < other.fitness_func_value

    def __repr__(self):
        return self.individual_matrix.__str__()
