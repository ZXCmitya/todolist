from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5 import uic
import sys

class Todolist(QMainWindow):

    def __init__(self):
        super(Todolist, self).__init__()
        uic.loadUi("untitled.ui", self)
        self.show()

        self.setFixedSize(458, 569)

        self.model = QStandardItemModel()
        self.listView.setModel(self.model)

        self.addButton.clicked.connect(self.add_note)
        self.deleteButton.clicked.connect(self.delete_note)
        self.changeButton.clicked.connect(self.change_note)
        self.exitButton.clicked.connect(self.exit_note)

    def add_note(self):
        newtask, confirmed = QInputDialog.getText(self, 'Add Task', 'New Task', QLineEdit.Normal, '')

        if confirmed and newtask:
            addtask = QStandardItem(newtask)
            self.model.appendRow(addtask)
    def delete_note(self):
        selected = self.listView.selectedIndexes()[0]

        dialog_delete = QMessageBox()
        dialog_delete.setText(f"Delete the task '{selected.data()}'?")

        dialog_delete.addButton(QPushButton('yes'), QMessageBox.YesRole)
        dialog_delete.addButton(QPushButton('no'), QMessageBox.NoRole)

        if dialog_delete.exec_() == 0:
            self.model.removeRow(selected.row())

    def change_note(self):
        pass


    def exit_note(self):
        sys.exit(app.exec_())

app = QApplication([])
window = Todolist()
app.exec_()