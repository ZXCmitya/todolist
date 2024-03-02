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
    db.execute("INSERT INTO todo (task) VALUES (?)", (task,))
    db.commit()

def delete_task(id):
    db.execute("DELETE FROM todo WHERE id=?", (id,))
    db.commit()

def complete_task(id):
    db.execute("UPDATE todo SET completed=1 WHERE id=?", (id,))

def uncomplete_task(id):
    db.execute("UPDATE todo SET completed=0 WHERE id=?", (id,))

def get_tasks():
    return db.execute("SELECT * FROM todo")

def get_completed_tasks():
    return db.execute("SELECT * FROM todo WHERE completed=1")

def get_uncompleted_tasks():
    return db.execute("SELECT * FROM todo WHERE completed=0")

def get_task(id):
    return db.execute("SELECT * FROM todo WHERE id=?", (id,))

def update_task(id, new_task):
    db.execute("UPDATE todo SET task=? WHERE id=?", (new_task, id))
    db.commit()

def close():
    db.close()

def main():
    create_table()
    add_task("test")
    print(get_tasks())
    close()

if __name__ == '__main__':
    main()