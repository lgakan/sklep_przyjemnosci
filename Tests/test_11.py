import algorithm
import numpy as np
import matplotlib.pyplot as plt


def main():
    algorithm.mutation_type = 'singular'
    algorithm.selection_method = 'ranking'
    algorithm.chance_to_crossover = 0.1
    algorithm.parent_percentage = 0.3
    algorithm.max_iters = 400
    algorithm.iters_without_change = 50
    algorithm.main_client = algorithm.Client(0, [('item_1', 7), ('item_2', 10),
                                                 ('item_5', 2), ('item_6', 4),
                                                 ('item_8', 6), ('item_9', 4),
                                                 ('item_10', 1)], 1200, algorithm.main_inventory)

    for i in range(30):
        score = algorithm.main()
        x_ax = np.arange(len(score[3]))
        plt.plot(x_ax, score[3], label=f'i={i}')
        print(i)
        print(score[:-1])
        algorithm.create_report('Test_statistics/test_11.csv', score[1:-1])
    plt.show()
    funs_start = []
    for mat in algorithm.general_population:
        funs_start.append(algorithm.get_penalty_func(
            algorithm.ObjFunction(mat, algorithm.main_sellers_base,
                                  algorithm.main_inventory), algorithm.main_client.budget))
    print(f'Mean: {np.mean(funs_start)}, Max: {np.max(funs_start)}, Min: {np.min(funs_start)}, Odch: {np.sqrt(np.var(funs_start))}')


if __name__ == '__main__':
    main()
