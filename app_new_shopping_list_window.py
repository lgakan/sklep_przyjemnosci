from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

class Ui_window_create_new_shopping_list(qtw.QWidget):
    signal_create_new_shopping_list = qtc.pyqtSignal(list)

    def setupUi(self, window_create_new_shopping_list):
        window_create_new_shopping_list.setObjectName("window_create_new_shopping_list")
        window_create_new_shopping_list.resize(692, 590)
        self.layout_new_shoppint_list_window = QtWidgets.QWidget(window_create_new_shopping_list)
        self.layout_new_shoppint_list_window.setObjectName("layout_new_shoppint_list_window")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layout_new_shoppint_list_window)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.layout_inner_new_shopping_list_window = QtWidgets.QHBoxLayout()
        self.layout_inner_new_shopping_list_window.setObjectName("layout_inner_new_shopping_list_window")
        self.table_widget_items = QtWidgets.QTableWidget(self.layout_new_shoppint_list_window)
        self.table_widget_items.setObjectName("table_widget_items")
        self.table_widget_items.setColumnCount(0)
        self.table_widget_items.setRowCount(0)
        self.layout_inner_new_shopping_list_window.addWidget(self.table_widget_items)
        self.layout_right = QtWidgets.QVBoxLayout()
        self.layout_right.setObjectName("layout_right")
        self.list_widget_shopping_list = QtWidgets.QListWidget(self.layout_new_shoppint_list_window)
        self.list_widget_shopping_list.setObjectName("list_widget_shopping_list")
        self.layout_right.addWidget(self.list_widget_shopping_list)
        self.layout_right_inputs = QtWidgets.QFormLayout()
        self.layout_right_inputs.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.layout_right_inputs.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.layout_right_inputs.setObjectName("layout_right_inputs")
        self.label = QtWidgets.QLabel(self.layout_new_shoppint_list_window)
        self.label.setObjectName("label")
        self.layout_right_inputs.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_item_name = QtWidgets.QLineEdit(self.layout_new_shoppint_list_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_item_name.sizePolicy().hasHeightForWidth())
        self.txt_item_name.setSizePolicy(sizePolicy)
        self.txt_item_name.setObjectName("txt_item_name")
        self.layout_right_inputs.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_item_name)
        self.label_2 = QtWidgets.QLabel(self.layout_new_shoppint_list_window)
        self.label_2.setObjectName("label_2")
        self.layout_right_inputs.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_item_quantity = QtWidgets.QLineEdit(self.layout_new_shoppint_list_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_item_quantity.sizePolicy().hasHeightForWidth())
        self.txt_item_quantity.setSizePolicy(sizePolicy)
        self.txt_item_quantity.setObjectName("txt_item_quantity")
        self.layout_right_inputs.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_item_quantity)
        self.layout_right.addLayout(self.layout_right_inputs)
        self.layout_right_buttons = QtWidgets.QHBoxLayout()
        self.layout_right_buttons.setObjectName("layout_right_buttons")
        self.button_add_item = QtWidgets.QPushButton(self.layout_new_shoppint_list_window, clicked=lambda: self.add_item())
        self.button_add_item.setObjectName("button_add_item")
        self.layout_right_buttons.addWidget(self.button_add_item)
        self.button_delete_item = QtWidgets.QPushButton(self.layout_new_shoppint_list_window, clicked=lambda: self.delete_item())
        self.button_delete_item.setObjectName("button_delete_item")
        self.layout_right_buttons.addWidget(self.button_delete_item)
        self.button_clear_shopping_list = QtWidgets.QPushButton(self.layout_new_shoppint_list_window,clicked=lambda: self.clear_shopping_list())
        self.button_clear_shopping_list.setObjectName("button_clear_shopping_list")
        self.layout_right_buttons.addWidget(self.button_clear_shopping_list)
        self.layout_right.addLayout(self.layout_right_buttons)
        self.button_submit_new_shopping_list = qtw.QPushButton(self.layout_new_shoppint_list_window, clicked=lambda: self.submit_shopping_list())
        self.button_submit_new_shopping_list.setObjectName("button_submit_new_shopping_list")
        self.layout_right.addWidget(self.button_submit_new_shopping_list)
        self.layout_inner_new_shopping_list_window.addLayout(self.layout_right)
        self.horizontalLayout_3.addLayout(self.layout_inner_new_shopping_list_window)
        window_create_new_shopping_list.setCentralWidget(self.layout_new_shoppint_list_window)

        self.retranslateUi(window_create_new_shopping_list)
        QtCore.QMetaObject.connectSlotsByName(window_create_new_shopping_list)

    def retranslateUi(self, window_create_new_shopping_list):
        _translate = QtCore.QCoreApplication.translate
        window_create_new_shopping_list.setWindowTitle(_translate("window_create_new_shopping_list", "BLS - Create new shopping list"))
        window_create_new_shopping_list.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label.setText(_translate("window_create_new_shopping_list", "Item name"))
        self.txt_item_name.setText(_translate("window_create_new_shopping_list", "item_1"))
        self.label_2.setText(_translate("window_create_new_shopping_list", "Item quantity"))
        self.txt_item_quantity.setText(_translate("window_create_new_shopping_list", "1"))
        self.button_add_item.setText(_translate("window_create_new_shopping_list", "Add item"))
        self.button_delete_item.setText(_translate("window_create_new_shopping_list", "Delete item"))
        self.button_clear_shopping_list.setText(_translate("window_create_new_shopping_list", "Clear shopping list"))
        self.button_submit_new_shopping_list.setText(_translate("window_create_new_shopping_list", "Submit new shopping list"))

    def add_item(self):
        item_name = self.txt_item_name.text()
        item_quantity = self.txt_item_quantity.text()
        self.list_widget_shopping_list.addItem(f'{item_name}: {item_quantity}')
        self.txt_item_name.setText('item_1')
        self.txt_item_quantity.setText('1')

    def delete_item(self):
        clicked_row = self.list_widget_shopping_list.currentRow()
        self.list_widget_shopping_list.takeItem(clicked_row)

    def clear_shopping_list(self):
        self.list_widget_shopping_list.clear()

    def submit_shopping_list(self):
        new_shopping_list = [str(self.list_widget_shopping_list.item(i).text()) for i in range(self.list_widget_shopping_list.count())]
        self.signal_create_new_shopping_list.emit(new_shopping_list)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_create_new_shopping_list = QtWidgets.QMainWindow()
    ui = Ui_window_create_new_shopping_list()
    ui.setupUi(window_create_new_shopping_list)
    window_create_new_shopping_list.show()
    sys.exit(app.exec_())
