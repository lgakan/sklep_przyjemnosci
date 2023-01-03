import algorithm
from time import time


client_to_test = [algorithm.Client(0, [('item_1', 1), ('item_2', 1),
                                       ('item_5', 1), ('item_6', 1),
                                       ('item_8', 1), ('item_9', 1),
                                       ('item_10', 1)], 1600, algorithm.main_inventory),
                  algorithm.Client(1, [('item_1', 7), ('item_2', 10),
                                       ('item_5', 2), ('item_6', 4),
                                       ('item_8', 6), ('item_9', 4),
                                       ('item_10', 1)], 1600, algorithm.main_inventory)]

report_list = []
for i in range(len(client_to_test)):
    algorithm.main_client = client_to_test[i]
    for _ in range(10):
        test_start = time()
        _, lowest_obj_func_value, iter_stop = algorithm.main()
        test_end = time()
        run_time = test_end - test_start
        algorithm.create_report('reports_from_tests/time_complexity.csv',
                                [iter_stop, client_to_test[i].client_id, '%.3f' % run_time, lowest_obj_func_value])

