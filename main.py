from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import sys
import api

class Todolist(QMainWindow):

    def __init__(self):
        super(Todolist, self).__init__()
        uic.loadUi("untitled.ui", self)
        self.show()

        self.setFixedSize(458, 569)

        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.model.itemChanged.connect(self.task_state_changed)
        self.addButton.clicked.connect(self.add_note)
        self.deleteButton.clicked.connect(self.delete_note)
        self.changeButton.clicked.connect(self.change_note)
        self.exitButton.clicked.connect(self.exit_note)


        self.load_tasks()

    def load_tasks(self):
        tasks = api.get_tasks()
        for task in tasks:
            item = QStandardItem(task[1])
            item.setCheckable(True)
            if task[2] == 1:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
            self.model.appendRow(item)

    def task_state_changed(self, item):
        index = self.model.indexFromItem(item)
        task_id = index.row() + 1
        if item.checkState() == Qt.Checked:
            api.complete_task(task_id)
        else:
            api.uncomplete_task(task_id)

    def add_note(self):
        new_task, confirmed = QInputDialog.getText(self, 'Add task', 'New task', QLineEdit.Normal, '')

        if confirmed and new_task:
            add_task = QStandardItem(new_task)
            add_task.setCheckable(True)
            add_task.setCheckState(Qt.Unchecked)
            self.model.appendRow(add_task)
            api.add_task(new_task)

    def delete_note(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index = indexes[0]
            self.model.removeRow(index.row())
            api.delete_task(index.row() + 1)

    def change_note(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index = indexes[0]
            new_task, confirmed = QInputDialog.getText(self, 'Change Task', 'Change Task', QLineEdit.Normal, '')
            if confirmed and new_task:
                item = self.model.itemFromIndex(index)
                item.setText(new_task)
                api.update_task(index.row() + 1, new_task)

    def exit_note(self):
        api.close()
        sys.exit()

app = QApplication([])
window = Todolist()
app.exec_()