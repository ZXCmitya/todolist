import sqlite3

db = sqlite3.connect('todo.db')


def create_table():
    db.execute("""
        CREATE TABLE "todo" (
            "id" INTEGER NOT NULL UNIQUE,
            "task" TEXT,
            "completed" NUMERIC,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
    """)


def add_task(task):
    db.execute("INSERT INTO todo (task) VALUES (?)", [task])
    db.commit()


def delete_task(id):
    db.execute("DELETE FROM todo WHERE id=?", [id])
    db.commit()


def complete_task(id):
    db.execute("UPDATE todo SET completed=1 WHERE id=?", [id])


def uncomplete_task(id):
    db.execute("UPDATE todo SET completed=0 WHERE id=?", [id])


def get_tasks():
    result = []
    tasks = db.execute("SELECT * FROM todo")
    for task in tasks:
        result.append(task)
    return result


def get_completed_tasks():
    list_of_completed_tasks = []
    tasks = db.execute("SELECT * FROM todo WHERE completed=1")
    for task in tasks:
        list_of_completed_tasks.append(task)

    return list_of_completed_tasks


def get_uncompleted_tasks():
    list_of_uncompleted_tasks = []
    tasks = db.execute("SELECT * FROM todo WHERE completed=0")
    for task in tasks:
        list_of_uncompleted_tasks.append(task)
    return list_of_uncompleted_tasks


def get_task(id):
    needed_task = []
    task = db.execute("SELECT * FROM todo WHERE id=?", [id])
    for t in task:
        needed_task.append(t)
    return needed_task


def update_task(id, new_task):
    db.execute("UPDATE todo SET task=? WHERE id=?", [new_task, id])
    db.commit()


def close():
    db.close()


def main():
    create_table()
    # add_task('test task')
    # delete_task(1)
    # complete_task(1)
    # uncomplete_task(1)
    # print(get_tasks())
    # print(get_completed_tasks())
    # print(get_uncompleted_tasks())
    # print(get_task(1))
    # update_task(1, 'new test task')
    # print(get_tasks())
    close()


if __name__ == '__main__':
    main()
