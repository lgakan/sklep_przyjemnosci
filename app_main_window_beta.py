from PyQt5 import QtCore, QtWidgets
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QTableWidgetItem, QStyledItemDelegate
from PyQt5 import QtWidgets as qtw
from app_new_population_window import Ui_window_create_new_population
from app_new_shopping_list_window import Ui_window_create_new_shopping_list
import algorithm


class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return


class Ui_MainWindow(qtw.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 110, 172, 152))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layout_parameters = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layout_parameters.setContentsMargins(0, 0, 0, 0)
        self.layout_parameters.setObjectName("layout_parameters")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.layout_parameters.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_population_size = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_population_size.setEnabled(True)
        self.txt_population_size.setObjectName("txt_population_size")
        self.layout_parameters.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_population_size)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.layout_parameters.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_parents_percentage = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_parents_percentage.setObjectName("txt_parents_percentage")
        self.layout_parameters.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_parents_percentage)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.layout_parameters.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_crossover_chance = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_crossover_chance.setObjectName("txt_crossover_chance")
        self.layout_parameters.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_crossover_chance)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.layout_parameters.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txt_generation_number = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_generation_number.setObjectName("txt_generation_number")
        self.layout_parameters.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_generation_number)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.layout_parameters.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txt_solution_accuracy = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_solution_accuracy.setObjectName("txt_solution_accuracy")
        self.layout_parameters.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_solution_accuracy)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.layout_parameters.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txt_budget = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_budget.setObjectName("txt_budget")
        self.layout_parameters.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_budget)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 500, 91, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_cross = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_cross.setContentsMargins(0, 0, 0, 0)
        self.layout_cross.setObjectName("layout_cross")
        self.radio_cro_every_2nd = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_cro_every_2nd.setChecked(True)
        self.radio_cro_every_2nd.setObjectName("radio_cro_every_2nd")
        self.layout_cross.addWidget(self.radio_cro_every_2nd)
        self.radio_cro_basic_rows_idx = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_cro_basic_rows_idx.setObjectName("radio_cro_basic_rows_idx")
        self.layout_cross.addWidget(self.radio_cro_basic_rows_idx)
        self.radio_cro_basic_rows_number = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_cro_basic_rows_number.setObjectName("radio_cro_basic_rows_number")
        self.layout_cross.addWidget(self.radio_cro_basic_rows_number)
        self.radio_cro_basic_rows_idx_and_number = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_cro_basic_rows_idx_and_number.setChecked(False)
        self.radio_cro_basic_rows_idx_and_number.setObjectName("radio_cro_basic_rows_idx_and_number")
        self.layout_cross.addWidget(self.radio_cro_basic_rows_idx_and_number)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(44, 400, 81, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layout_mutation = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_mutation.setContentsMargins(0, 0, 0, 0)
        self.layout_mutation.setObjectName("layout_mutation")
        self.radio_mut_singular = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radio_mut_singular.setChecked(True)
        self.radio_mut_singular.setObjectName("radio_mut_singular")
        self.layout_mutation.addWidget(self.radio_mut_singular)
        self.radio_mut_elimination = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radio_mut_elimination.setObjectName("radio_mut_elimination")
        self.layout_mutation.addWidget(self.radio_mut_elimination)
        # USER
        self.button_start = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.gui_main_fun())
        self.button_start.setGeometry(QtCore.QRect(50, 30, 75, 23))
        self.button_start.setObjectName("button_start")
        self.button_restart = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.restart_parameters())
        self.button_restart.setGeometry(QtCore.QRect(40, 820, 75, 23))
        self.button_restart.setObjectName("button_restart")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(180, 10, 921, 881))
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.widget_charts = QtWidgets.QWidget()
        self.widget_charts.setObjectName("widget_charts")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.widget_charts)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 911, 851))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.layout_charts = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.layout_charts.setContentsMargins(0, 0, 0, 0)
        self.layout_charts.setObjectName("layout_charts")
        self.frame_discount = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.frame_discount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_discount.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_discount.setObjectName("frame_discount")
        self.layout_charts.addWidget(self.frame_discount)

        # DISCOUNT CHART
        self.layout_horizontal_discount_chart = QtWidgets.QHBoxLayout(self.frame_discount)
        self.layout_horizontal_discount_chart.setObjectName("layout_horizontal_discount_chart")
        self.figure_charts = plt.figure()
        self.canvas_discount = FigureCanvas(self.figure_charts)
        self.layout_horizontal_discount_chart.addWidget(self.canvas_discount)

        self.frame_delivery = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.frame_delivery.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_delivery.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_delivery.setObjectName("frame_delivery")
        self.layout_charts.addWidget(self.frame_delivery)

        # DELIVERY CHART
        self.layout_horizontal_delivery_chart = QtWidgets.QHBoxLayout(self.frame_delivery)
        self.layout_horizontal_delivery_chart.setObjectName("layout_horizontal_delivery_chart")
        self.canvas_delivery = FigureCanvas(self.figure_charts)
        self.layout_horizontal_delivery_chart.addWidget(self.canvas_delivery)

        self.tabWidget.addTab(self.widget_charts, "")
        self.widget_algorithm = QtWidgets.QWidget()
        self.widget_algorithm.setObjectName("widget_algorithm")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.widget_algorithm)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 911, 851))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.layout_algorithm = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.layout_algorithm.setContentsMargins(0, 0, 0, 0)
        self.layout_algorithm.setObjectName("layout_algorithm")
        self.frame_algorithm = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.frame_algorithm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_algorithm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_algorithm.setObjectName("frame_algorithm")
        self.layout_algorithm.addWidget(self.frame_algorithm)

        # ALGORITHM CHART
        self.layout_horizontal_algorithm_chart = QtWidgets.QHBoxLayout(self.frame_algorithm)
        self.layout_horizontal_algorithm_chart.setObjectName("layout_horizontal_algorithm_chart")
        self.figure_algorithm = plt.figure(1)
        self.canvas_algorithm = FigureCanvas(self.figure_algorithm)
        self.layout_horizontal_algorithm_chart.addWidget(self.canvas_algorithm)

        self.tabWidget.addTab(self.widget_algorithm, "")
        self.widget_solution_matrix = QtWidgets.QWidget()
        self.widget_solution_matrix.setObjectName("widget_solution_matrix")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.widget_solution_matrix)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 911, 851))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.layout_solution_matrix = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.layout_solution_matrix.setContentsMargins(0, 0, 0, 0)
        self.layout_solution_matrix.setObjectName("layout_solution_matrix")
        self.table_widget_solution_matrix = QtWidgets.QTableWidget(self.verticalLayoutWidget_7)
        self.table_widget_solution_matrix.setObjectName("table_widget_solution_matrix")
        self.table_widget_solution_matrix.setColumnCount(0)
        self.table_widget_solution_matrix.setRowCount(0)
        self.layout_solution_matrix.addWidget(self.table_widget_solution_matrix)
        self.tabWidget.addTab(self.widget_solution_matrix, "")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 101, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 480, 101, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 380, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 650, 61, 16))
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 670, 83, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.layout_mutation_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.layout_mutation_3.setContentsMargins(0, 0, 0, 0)
        self.layout_mutation_3.setObjectName("layout_mutation_3")
        self.radio_sel_tournament = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radio_sel_tournament.setChecked(True)
        self.radio_sel_tournament.setObjectName("radio_sel_tournament")
        self.layout_mutation_3.addWidget(self.radio_sel_tournament)
        self.radio_sel_roulette = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radio_sel_roulette.setObjectName("radio_sel_roulette")
        self.layout_mutation_3.addWidget(self.radio_sel_roulette)
        self.radio_sel_ranking = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radio_sel_ranking.setObjectName("radio_sel_ranking")
        self.layout_mutation_3.addWidget(self.radio_sel_ranking)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 270, 91, 16))
        self.label_13.setObjectName("label_13")
        # User
        self.button_create_population = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.open_new_population_window())
        self.button_create_population.setEnabled(True)
        self.button_create_population.setGeometry(QtCore.QRect(20, 290, 131, 31))
        self.button_create_population.setCheckable(False)
        self.button_create_population.setObjectName("button_create_population")
        self.button_create_shopping_list = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.open_new_shopping_list_window())
        self.button_create_shopping_list.setEnabled(True)
        self.button_create_shopping_list.setGeometry(QtCore.QRect(20, 330, 131, 31))
        self.button_create_shopping_list.setCheckable(False)
        self.button_create_shopping_list.setObjectName("button_create_shopping_list")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Population size"))
        self.txt_population_size.setText(_translate("MainWindow", "10"))
        self.label_2.setText(_translate("MainWindow", "Parents [%]"))
        self.txt_parents_percentage.setText(_translate("MainWindow", "20"))
        self.label_3.setText(_translate("MainWindow", "Crossover chance [%]"))
        self.txt_crossover_chance.setText(_translate("MainWindow", "10"))
        self.label_4.setText(_translate("MainWindow", "Number of generations"))
        self.txt_generation_number.setText(_translate("MainWindow", "100"))
        self.label_5.setText(_translate("MainWindow", "Solution accuracy"))
        self.txt_solution_accuracy.setText(_translate("MainWindow", "15"))
        self.label_6.setText(_translate("MainWindow", "Budget"))
        self.txt_budget.setText(_translate("MainWindow", "2000"))
        self.radio_cro_every_2nd.setText(_translate("MainWindow", "Every 2nd"))
        self.radio_cro_basic_rows_idx.setText(_translate("MainWindow", "Basic idx"))
        self.radio_cro_basic_rows_number.setText(_translate("MainWindow", "Basic number"))
        self.radio_cro_basic_rows_idx_and_number.setText(_translate("MainWindow", "Basic both"))
        self.radio_mut_singular.setText(_translate("MainWindow", "Singular"))
        self.radio_mut_elimination.setText(_translate("MainWindow", "Elimination"))
        self.button_start.setText(_translate("MainWindow", "START"))
        self.button_restart.setText(_translate("MainWindow", "RESTART"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_charts), _translate("MainWindow", "Charts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_algorithm), _translate("MainWindow", "Algorithm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_solution_matrix), _translate("MainWindow", "Solution Matrix"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Parameters</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Crossover</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Mutate</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Selection</span></p></body></html>"))
        self.radio_sel_tournament.setText(_translate("MainWindow", "Tournament"))
        self.radio_sel_roulette.setText(_translate("MainWindow", "Roulette"))
        self.radio_sel_ranking.setText(_translate("MainWindow", "Ranking"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Construction<br/></span></p><p align=\"center\"><br/></p></body></html>"))
        self.button_create_population.setText(_translate("MainWindow", "Create population"))
        self.button_create_shopping_list.setText(_translate("MainWindow", "Create shopping list"))

    def restart_parameters(self):
        print("Current algorithm.general_population")
        print(algorithm.general_population)
        print("Current algorithm.shopping_list")
        print(algorithm.shopping_list)

    def print_population(self):
        string_to_print = ''
        for i in range(len(algorithm.general_population)):
            string_to_print = string_to_print + f'Matrix_{i}:\n'
            string_to_print = string_to_print + str(algorithm.general_population[i].solution_matrix) + '\n\n'
        return string_to_print

    def open_new_population_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_window_create_new_population()
        self.ui.setupUi(self.window)
        self.ui.text_browser_population.setText(self.print_population())
        self.ui.signal_create_new_population_clicked.connect(self.new_population_signal_handler)
        self.window.show()

    def new_population_signal_handler(self, new_population_signal):
        new_general_population = []
        for _ in range(int(self.txt_population_size.text())):
            algorithm.sol.get_starting_solution(algorithm.dict_of_sells,
                                                algorithm.list_of_orders,
                                                'random')
            new_general_population.append(algorithm.deepcopy(algorithm.sol))
            algorithm.sol.reset_solution()
        algorithm.general_population = new_general_population
        self.ui.text_browser_population.setText(self.print_population())


    def open_new_shopping_list_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_window_create_new_shopping_list()
        self.ui.setupUi(self.window)
        columns = ['max amount']
        rows = [f'item_{i}' for i in range(len(algorithm.maxes[2]))]
        self.ui.table_widget_items.setRowCount(len(rows))
        self.ui.table_widget_items.setColumnCount(len(columns))
        self.ui.table_widget_items.setVerticalHeaderLabels(rows)
        self.ui.table_widget_items.setHorizontalHeaderLabels(['Max Amount'])
        for i in range(len(rows)):
            self.ui.table_widget_items.setItem(i, 0, QTableWidgetItem(str(algorithm.maxes[2][i])))
        self.ui.table_widget_items.setItemDelegateForColumn(0, ReadOnlyDelegate())
        self.ui.signal_create_new_shopping_list.connect(self.new_shopping_list_signal_handler)
        self.window.show()

    def new_shopping_list_signal_handler(self, new_shopping_list):
        shopping_list = []
        for i in range(len(new_shopping_list)):
            split_i = new_shopping_list[i].split(': ')
            shopping_list.append((split_i[0], int(split_i[1])))
        algorithm.shopping_list = shopping_list
        algorithm.main_client = algorithm.Client(0,
                                                 algorithm.shopping_list,
                                                 algorithm.budget,
                                                 algorithm.main_inventory)
        algorithm.dict_of_sells = algorithm.main_sellers_base.get_sellers_with_items(algorithm.main_client.get_product_ids())
        algorithm.list_of_orders = algorithm.main_client.get_oder_quantity()


    def prepare_gui_parameters(self):
        # PARAMETERS
        algorithm.population_size = int(self.txt_population_size.text())
        algorithm.parent_percentage = int(self.txt_parents_percentage.text()) / 100
        algorithm.chance_to_crossover = int(int(self.txt_crossover_chance.text()) / 100)
        algorithm.max_iters = int(self.txt_generation_number.text())
        algorithm.iters_without_change = int(self.txt_solution_accuracy.text())
        algorithm.budget = int(self.txt_budget.text())
        # Mutate
        if self.radio_mut_singular.isChecked():
            algorithm.mutation_type = 'singular'
        elif self.radio_mut_elimination.isChecked():
            algorithm.mutation_type = 'elimination'
        # Crossover
        if self.radio_cro_every_2nd.isChecked():
            algorithm.crossover_method = 'every_2nd'
        elif self.radio_cro_basic_rows_idx.isChecked():
            algorithm.crossover_method = ('basic', 'rows_idx')
        elif self.radio_cro_basic_rows_number.isChecked():
            algorithm.crossover_method = ('basic', 'rows_number')
        elif self.radio_cro_basic_rows_idx_and_number.isChecked():
            algorithm.crossover_method = ('basic', 'rows_idx_and_number')
        # Selection
        if self.radio_sel_tournament.isChecked():
            algorithm.selection_method = 'tournament'
        elif self.radio_sel_roulette.isChecked():
            algorithm.selection_method = 'roulette'
        elif self.radio_sel_ranking.isChecked():
            algorithm.selection_method = 'ranking'
        print('Chosen parameters:')
        print(f'population_size: {algorithm.population_size}')
        print(f'parent_percentage: {algorithm.parent_percentage}')
        print(f'chance_to_crossover: {algorithm.chance_to_crossover}')
        print(f'max_iters: {algorithm.max_iters}')
        print(f'iters_without_change: {algorithm.iters_without_change}')
        print(f'budget: {algorithm.budget}')
        print(f'mutation_type: {algorithm.mutation_type}')
        print(f'crossover_method: {algorithm.crossover_method}')
        print(f'selection_method: {algorithm.selection_method}')

    def create_solution_matrix_tab(self, solution_matrix):
        self.table_widget_solution_matrix.setRowCount(len(solution_matrix))
        self.table_widget_solution_matrix.setColumnCount(len(solution_matrix[0]))
        for i in range(len(solution_matrix)):
            for j in range(len(solution_matrix[0])):
                self.table_widget_solution_matrix.setItem(i, j, QTableWidgetItem(str(solution_matrix[i, j])))
        self.table_widget_solution_matrix.setEnabled(False)

    def create_algorithm_chart_tab(self, iterations, obj_function_values):
        self.figure_algorithm.clear()
        # plt.plot(algorithm.np.arange(iterations - 1), obj_function_values)
        # plt.xlabel('iterations')
        # plt.ylabel('Function values')
        # plt.title('Objective function')
        oranges = ['9', '10', '11', '12']
        oranges_values = [90, 100, 110, 120]
        plt.bar(oranges, oranges_values, color='purple', width=0.4)
        plt.xlabel('orangesx')
        plt.ylabel('orangesy')
        plt.title('oranges')
        self.canvas_algorithm.draw()

    def create_charts_tab(self):
        self.figure_charts.clear()
        apples = ['1', '2', '3', '4']
        bananas = ['5', '6', '7', '8']
        apples_values = [10, 20, 30, 40]
        bananas_values = [50, 60, 70, 80]
        plt.bar(apples, apples_values, color='red', width=0.4)
        plt.xlabel('applesx')
        plt.ylabel('applesy')
        plt.title('apples')
        self.canvas_discount.draw()
        self.figure_charts.clear()
        plt.xlabel('bananasx')
        plt.ylabel('bananasy')
        plt.title('bananas')
        plt.bar(bananas, bananas_values, color='blue', width=0.4)
        self.canvas_delivery.draw()

    def gui_main_fun(self):
        self.prepare_gui_parameters()
        print(algorithm.shopping_list)
        current_best_solution, current_lowest_obj_func, i_iter, obj_functions_to_plot = algorithm.main()

        self.create_solution_matrix_tab(current_best_solution.solution_matrix)
        self.create_algorithm_chart_tab(i_iter, obj_functions_to_plot)
        self.create_charts_tab()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
