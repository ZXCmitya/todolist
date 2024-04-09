from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import sys
import api

class TaskManager:
    def __init__(self):
        self.task_data = []

    def add_task(self, task_id, index, completed=False):
        self.task_data.append((task_id, index, completed))

    def delete_task(self, index):
        for i, (_, task_index, _) in enumerate(self.task_data):
            if task_index == index:
                del self.task_data[i]
                return

    def update_indexes_after_deletion(self, deleted_index):
        for i, (task_id, index, completed) in enumerate(self.task_data):
            if index > deleted_index:
                self.task_data[i] = (task_id, index-1, completed)

    def get_id_by_index(self, index):
        for task_id, task_index, _ in self.task_data:
            if task_index == index:
                return task_id
        return None

    def clear(self):
        self.task_data.clear()

    def task_state_changed(self, task_id, completed):
        if completed:
            success = api.complete_task(task_id)
        else:
            success = api.uncomplete_task(task_id)

        if success:
            for i, (id, index, _) in enumerate(self.task_data):
                if id == task_id:
                    self.task_data[i] = (id, index, completed)
                    break

class Todolist(QMainWindow):
    def __init__(self):
        super(Todolist, self).__init__()
        uic.loadUi("untitled.ui", self)
        self.show()

        self.setFixedSize(458, 569)
        self.task_manager = TaskManager()

        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.model.itemChanged.connect(self.task_state_changed)
        self.addButton.clicked.connect(self.add_note)
        self.clearAllButton.clicked.connect(self.clear_all_notes)
        self.deleteButton.clicked.connect(self.delete_note)
        self.changeButton.clicked.connect(self.change_note)
        self.exitButton.clicked.connect(self.exit_note)

        self.load_tasks()

    def load_tasks(self):
        self.task_manager.clear()
        tasks = api.get_tasks()
        for index, task in enumerate(tasks):
            item = QStandardItem(task[1])
            item.setCheckable(True)
            item.setCheckState(Qt.Checked if task[2] == 1 else Qt.Unchecked)
            self.model.appendRow(item)
            self.task_manager.add_task(task[0], index, task[2] == 1)

    def task_state_changed(self, item):
        index = self.model.indexFromItem(item).row()
        task_id = self.task_manager.get_id_by_index(index)
        if task_id is not None:
            completed = item.checkState() == Qt.Checked
            if completed:
                success = api.complete_task(task_id)
            else:
                success = api.uncomplete_task(task_id)
            if success:
                self.task_manager.task_state_changed(task_id, completed)

    def add_note(self):
        new_task, confirmed = QInputDialog.getText(self, 'Add task', 'New task', QLineEdit.Normal, '')
        if confirmed and new_task:
            task_id = api.add_task_and_set_complete_parameter(new_task)
            item = QStandardItem(new_task)
            item.setCheckable(True)
            item.setCheckState(Qt.Unchecked)
            self.model.appendRow(item)
            self.task_manager.add_task(task_id, self.model.rowCount() - 1, False)

    def delete_note(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index = indexes[0].row()
            task_id = self.task_manager.get_id_by_index(index)
            api.delete_task(task_id)
            self.model.removeRow(index)
            self.task_manager.delete_task(index)
            self.task_manager.update_indexes_after_deletion(index)

    def clear_all_notes(self):
        confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to delete all notes?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.model.clear()
            self.task_manager.clear()
            api.delete_all_tasks()

    def change_note(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index = indexes[0].row()
            task_id = self.task_manager.get_id_by_index(index)
            new_task, confirmed = QInputDialog.getText(self, 'Change Task', 'Change Task', QLineEdit.Normal, '')
            if confirmed and new_task:
                item = self.model.itemFromIndex(indexes[0])
                item.setText(new_task)
                api.update_task(task_id, new_task)
    def exit_note(self):
        api.close()
        sys.exit()

app = QApplication([])
window = Todolist()
app.exec_()