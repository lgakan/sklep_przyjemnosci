import algorithm

chance_list = [0, 0.1, 0.5, 0.85, 1]

report_list = []
algorithm.max_iters = 300
for i in range(len(chance_list)):
    algorithm.chance_to_crossover = chance_list[i]
    for _ in range(10):
        _, lowest_obj_func_value, iter_stop = algorithm.main()
        algorithm.create_report('reports_from_tests/chance_for_crossover.csv',
                                [iter_stop, str(int(100*chance_list[i])) + '%', '%.3f' % lowest_obj_func_value])

