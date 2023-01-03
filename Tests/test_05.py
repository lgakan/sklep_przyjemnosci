from algorithm import create_report
import algorithm


def main():
    create_report("Test_statistics/test_05.csv", 'Singular')
    algorithm.max_iters = 200
    algorithm.mutation_type = 'singular'
    for _ in range(30):
        create_report("Test_statistics/test_05.csv", algorithm.main()[1:])
    create_report("Test_statistics/test_05.csv", 'Elimination')
    algorithm.mutation_type = 'elimination'
    for _ in range(30):
        create_report("Test_statistics/test_05.csv", algorithm.main()[1:])


if __name__ == '__main__':
    main()
