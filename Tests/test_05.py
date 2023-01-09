from algorithm import create_report
import numpy as np
import algorithm


def main():
    create_report("Test_statistics/test_05.csv", ['Singular'])
    algorithm.selection_method = 'roulette'
    algorithm.max_iters = 300
    algorithm.chance_to_crossover = 0.2
    algorithm.mutation_type = 'singular'
    for _ in range(30):
        create_report("Test_statistics/test_05.csv", algorithm.main()[1:-1])
    create_report("Test_statistics/test_05.csv", ['Elimination'])
    algorithm.mutation_type = 'elimination'
    for _ in range(30):
        create_report("Test_statistics/test_05.csv", algorithm.main()[1:-1])
    funs_start = []
    for mat in algorithm.general_population:
        funs_start.append(algorithm.get_penalty_func(
            algorithm.ObjFunction(mat, algorithm.main_sellers_base,
                                  algorithm.main_inventory), algorithm.main_client.budget))
    print(
        f'Mean: {np.mean(funs_start)}, Max: {np.max(funs_start)}, Min: {np.min(funs_start)}, Odch: {np.sqrt(np.var(funs_start))}')


if __name__ == '__main__':
    main()
