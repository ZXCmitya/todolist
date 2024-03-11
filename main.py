from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
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
        new_task, confirmed = QInputDialog.getText(self, 'Add Task', 'New Task', QLineEdit.Normal, '')

        if confirmed and new_task:
            add_task = QStandardItem(new_task)
            add_task.setCheckable(True)
            add_task.setCheckState(Qt.Unchecked)
            self.model.appendRow(add_task)

    def delete_note(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index = indexes[0]
            self.model.removeRow(index.row())

    def change_note(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index = indexes[0]
            new_task, confirmed = QInputDialog.getText(self, 'Edit Task', 'Edit Task', QLineEdit.Normal, '')
            if confirmed and new_task:
                item = self.model.itemFromIndex(index)
                item.setText(new_task)

    def exit_note(self):
        sys.exit()

app = QApplication([])
window = Todolist()
app.exec_()