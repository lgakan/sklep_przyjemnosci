import algorithm

algorithm.max_iters = 300

algorithm.crossover_method = ('basic', 'rows_idx')
algorithm.create_report('reports_from_tests/crossovers.csv', ['basic', 'rows_idx'])
for _ in range(20):
    algorithm.create_report("reports_from_tests/crossovers.csv", algorithm.main()[1:])

algorithm.crossover_method = ('basic', 'rows_number')
algorithm.create_report('reports_from_tests/crossovers.csv', ['basic', 'rows_number'])
for _ in range(20):
    algorithm.create_report("reports_from_tests/crossovers.csv", algorithm.main()[1:])

algorithm.crossover_method = ('basic', 'rows_idx_and_number')
algorithm.create_report('reports_from_tests/crossovers.csv', ['basic', 'rows_idx_and_number'])
for _ in range(20):
    algorithm.create_report("reports_from_tests/crossovers.csv", algorithm.main()[1:])

algorithm.crossover_method = 'every_2nd'
algorithm.create_report('reports_from_tests/crossovers.csv', ['every_2nd'])
for _ in range(20):
    algorithm.create_report("reports_from_tests/crossovers.csv", algorithm.main()[1:])

