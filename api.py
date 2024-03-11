import db_todolist


def get_tasks():
    return db_todolist.get_tasks()


def add_task(task):
    db_todolist.add_task(task)


def delete_task(id):
    db_todolist.delete_task(id)


def complete_task(id):
    db_todolist.complete_task(id)


def uncomplete_task(id):
    db_todolist.uncomplete_task(id)


def get_completed_tasks():
    return db_todolist.get_completed_tasks()


def get_uncompleted_tasks():
    return db_todolist.get_uncompleted_tasks()


def update_task(id, new_task):
    db_todolist.update_task(id, new_task)


def close():
    db_todolist.close()
