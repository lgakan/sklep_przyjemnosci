import algorithm
from time import time


client_to_test = [algorithm.Client(0, [('item_1', 1), ('item_8', 1)], 2000, algorithm.main_inventory),
                  algorithm.Client(1, [('item_1', 1), ('item_2', 1),
                                       ('item_5', 1), ('item_6', 1),
                                       ('item_8', 1), ('item_9', 1)], 2000, algorithm.main_inventory),
                  algorithm.Client(2, [('item_1', 10), ('item_2', 10),
                                       ('item_5', 10), ('item_6', 10),
                                       ('item_8', 10), ('item_9', 10)], 2000, algorithm.main_inventory),
                  algorithm.Client(3, [('item_1', 20), ('item_8', 20)], 2000, algorithm.main_inventory)]

report_list = []
algorithm.max_iters = 300
for i in range(len(client_to_test)):
    algorithm.main_client = client_to_test[i]
    for _ in range(10):
        test_start = time()
        _, lowest_obj_func_value, iter_stop = algorithm.main()
        test_end = time()
        run_time = test_end - test_start
        algorithm.create_report('reports_from_tests/time_complexity.csv',
                                [iter_stop, client_to_test[i].client_id, '%.3f' % run_time, '%.3f' % lowest_obj_func_value])

