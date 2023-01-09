import numpy as np
import random as rd


class Solution:
    def __init__(self, sellers, items):
        self.solution_matrix = None
        self.create_solution_matrix(len(sellers), len(items))

    def create_solution_matrix(self, size_s, size_i):
        self.solution_matrix = np.zeros((size_i, size_s), dtype=np.int)

    def get_starting_solution(self, dict_of_items_with_sellers, order_list, construct_type: str):
        if construct_type == 'left':
            for i, (product_row, values) in enumerate(dict_of_items_with_sellers.items()):
                quantity_from_buyer = order_list[i]
                j = 0
                while quantity_from_buyer > 0:
                    seller_id, quantity_from_seller = values[j]
                    slots = min(quantity_from_buyer, quantity_from_seller)
                    self.solution_matrix[product_row][seller_id] = slots
                    quantity_from_buyer -= slots
                    j += 1
        # TODO: 2
        elif construct_type == 'random':
            for i, (product_row, values) in enumerate(dict_of_items_with_sellers.items()):
                input_list_of_sellers = np.array(self.solution_matrix[product_row])
                for j, (seller_id, quantity_from_seller) in enumerate(values):
                    input_list_of_sellers[seller_id] = quantity_from_seller
                concatenated_sellers = list(np.concatenate(np.array([a_i * [i] for i, a_i in
                                                                     enumerate(input_list_of_sellers)
                                                                     if a_i != 0], dtype=object)))
                rd.shuffle(concatenated_sellers)
                quantity_from_buyer = order_list[i]
                sellers_chosen = concatenated_sellers[:quantity_from_buyer]
                for seller in sellers_chosen:
                    self.solution_matrix[product_row][seller] += 1

    def get_solution_matrix_shape(self):
        return len(self.solution_matrix), len(self.solution_matrix[0])

    def reset_solution(self):
        for i, _ in enumerate(self.solution_matrix):
            self.solution_matrix[i].fill(0)

    def get_solution_matrix(self):
        return self.solution_matrix

    def __repr__(self):
        return self.solution_matrix.__str__()
