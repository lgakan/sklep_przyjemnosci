from algorithm import create_report
import algorithm
import numpy as np


def main():
    algorithm.mutation_type = 'singular'
    algorithm.selection_method = 'roulette'
    algorithm.chance_to_crossover = 0.2
    algorithm.max_iters = 300
    algorithm.iters_without_change = 50
    algorithm.main_client = algorithm.Client(0, [('item_1', 2), ('item_2', 1),
                                                 ('item_5', 2), ('item_6', 2),
                                                 ('item_8', 2), ('item_9', 1),
                                                 ('item_10', 1)], 1000, algorithm.main_inventory)
    create_report("Test_statistics/test_09.csv", ['Singular_many'])
    for _ in range(30):
        create_report("Test_statistics/test_09.csv", algorithm.main()[1:-1])
    create_report("Test_statistics/test_09.csv", ['Elimination_many'])
    algorithm.mutation_type = 'elimination'
    for _ in range(30):
        create_report("Test_statistics/test_09.csv", algorithm.main()[1:-1])

    funs_start = []
    for mat in algorithm.general_population:
        funs_start.append(algorithm.get_penalty_func(
            algorithm.ObjFunction(mat, algorithm.main_sellers_base,
                                  algorithm.main_inventory), algorithm.main_client.budget))
    print(
        f'Mean: {np.mean(funs_start)}, Max: {np.max(funs_start)}, Min: {np.min(funs_start)}, Odch: {np.sqrt(np.var(funs_start))}')

    algorithm.main_client = algorithm.Client(0, [('item_1', 7), ('item_2', 10),
                                                 ('item_5', 3)], 1000, algorithm.main_inventory)
    create_report("Test_statistics/test_09.csv", ['Singular_less'])
    algorithm.mutation_type = 'singular'
    for _ in range(30):
        create_report("Test_statistics/test_09.csv", algorithm.main()[1:-1])
    create_report("Test_statistics/test_09.csv", ['Elimination_less'])
    algorithm.mutation_type = 'elimination'
    for _ in range(30):
        create_report("Test_statistics/test_09.csv", algorithm.main()[1:-1])

    funs_start = []
    for mat in algorithm.general_population:
        funs_start.append(algorithm.get_penalty_func(
            algorithm.ObjFunction(mat, algorithm.main_sellers_base,
                                  algorithm.main_inventory), algorithm.main_client.budget))
    print(
        f'Mean: {np.mean(funs_start)}, Max: {np.max(funs_start)}, Min: {np.min(funs_start)}, Odch: {np.sqrt(np.var(funs_start))}')


if __name__ == '__main__':
    main()
