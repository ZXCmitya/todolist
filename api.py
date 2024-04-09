import db_todolist


def get_tasks():
    print('Getting tasks')
    return db_todolist.get_tasks()


def add_task_and_set_complete_parameter(task):
    print(f'Adding task: {task}')
    db_todolist.add_task(task)


def delete_task(id):
    print(f'Deleting task with id: {id}')
    db_todolist.delete_task(id)


def complete_task(id):
    print(f'Completing task with id: {id}')
    db_todolist.complete_task(id)


def uncomplete_task(id):
    print(f'Uncompleting task with id: {id}')
    db_todolist.uncomplete_task(id)


def get_completed_tasks():
    print('Getting completed tasks')
    return db_todolist.get_completed_tasks()


def get_uncompleted_tasks():
    print('Getting uncompleted tasks')
    return db_todolist.get_uncompleted_tasks()


def update_task(id, new_task):
    print(f'Updating task with id: {id} to {new_task}')
    db_todolist.update_task(id, new_task)


def delete_all_tasks():
    print('Deleting all tasks')
    db_todolist.delete_all_tasks()


def close():
    print('Closing database')
    db_todolist.close()
