import algorithm

# zmienic, bo moze byc 101 iteracji (kosmetyka)

# blad general pop .remove(comparison_pop)
# znalezc dostep do zmiennych w funkcji main w algorithm.py
# wywolywac algorytm dla takiej samej starting pop, a nie dla caly czas aktualizowanej
# trzeba prawdopodobnie przerobić maina na funkcję, która będzie zwracać za każdym razem funkcję celu i liczbę iteracji
# aby móc to potem wykorzystać w testach
# po algorytmie podmienić general population na startowe, żeby się algorytm znowu wykonywał, ewentualnie funkcję tworzącą
# general population wstawić do maina, a nie robić tego globalnie, pytanie jak to będzie potem w gui

# a = [[1,2], [2,4], [3,5]]
# b = [2,4]
# print(b in a)
algorithm.selection_method = 'ranking'
list_of_funcs = []
list_of_best_sols = []
lst_iter = []
for _ in range(15):
    # algorithm.general_population = algorithm.general_population_copy
    sol, func, iters = algorithm.main()
    list_of_funcs.append(func)
    lst_iter.append(iters)
avg_ranking = sum(list_of_funcs)/len(list_of_funcs)
print(avg_ranking)
avg_iter = sum(lst_iter)/len(lst_iter)
print(avg_iter)

# algorithm.selection_method = 'tournament'
# list_of_funcs = []
# list_of_best_sols = []
# lst_iter = []
# for _ in range(15):
#     algorithm.general_population = algorithm.general_population_copy
#     sol, func, iters = algorithm.main()
#     list_of_funcs.append(func)
#     lst_iter.append(iters)
# avg_tour = sum(list_of_funcs)/len(list_of_funcs)
# print(avg_tour)
# avg_iter = sum(lst_iter)/len(lst_iter)
# print(avg_iter)
#
# algorithm.selection_method = 'roulette'
# list_of_funcs = []
# list_of_best_sols = []
# lst_iter = []
# for _ in range(15):
#     algorithm.general_population = algorithm.general_population_copy
#     sol, func, iters = algorithm.main()
#     list_of_funcs.append(func)
#     lst_iter.append(iters)
# avg_roulette = sum(list_of_funcs)/len(list_of_funcs)
# print(avg_roulette)
# avg_iter = sum(lst_iter)/len(lst_iter)
# print(avg_iter)

