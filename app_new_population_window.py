from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

class Ui_window_create_new_population(qtw.QWidget):
    signal_create_new_population_clicked = qtc.pyqtSignal(bool)

    def setupUi(self, window_create_new_population):
        window_create_new_population.setObjectName("window_create_new_population")
        window_create_new_population.resize(687, 568)
        self.centralwidget = QtWidgets.QWidget(window_create_new_population)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.layout_new_population_window = QtWidgets.QVBoxLayout()
        self.layout_new_population_window.setObjectName("layout_new_population_window")
        self.button_create_new_population = qtw.QPushButton(self.centralwidget)
        self.button_create_new_population.clicked.connect(self.create_new_population_fun)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_create_new_population.sizePolicy().hasHeightForWidth())
        self.button_create_new_population.setSizePolicy(sizePolicy)
        self.button_create_new_population.setObjectName("button_create_new_population")
        self.layout_new_population_window.addWidget(self.button_create_new_population)
        self.text_browser_population = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_browser_population.setObjectName("text_browser_population")
        self.layout_new_population_window.addWidget(self.text_browser_population)
        self.verticalLayout_4.addLayout(self.layout_new_population_window)
        window_create_new_population.setCentralWidget(self.centralwidget)

        self.retranslateUi(window_create_new_population)
        QtCore.QMetaObject.connectSlotsByName(window_create_new_population)

    def retranslateUi(self, window_create_new_population):
        _translate = QtCore.QCoreApplication.translate
        window_create_new_population.setWindowTitle(_translate("window_create_new_population", "MainWindow"))
        self.button_create_new_population.setText(_translate("window_create_new_population", "Create_new_population"))

    def create_new_population_fun(self):
        # new_population = 'new very big population :)'
        self.signal_create_new_population_clicked.emit(True)
        # self.text_browser_population.setText(new_population)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_create_new_population = QtWidgets.QMainWindow()
    ui = Ui_window_create_new_population()
    ui.setupUi(window_create_new_population)
    window_create_new_population.show()
    sys.exit(app.exec_())
