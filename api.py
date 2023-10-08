import sqlite3

from task import Task
from user import User
from datetime import datetime

class DBProvider:

    def __init__(self):
        self.conn = sqlite3.connect('famcs.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, tg_id TEXT, course INTEGER, group INTEGER, type TEXT, admin INTEGER)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, type TEXT, description TEXT, deadline TEXT, persons TEXT, notify INTEGER, completed INTEGER)')

    def add_admin(self, tg_id):
        self.cursor.execute('UPDATE users SET admin = ? WHERE tg_id = ?', (1, tg_id))
        

    def if_admin(self, id):
        pass
    
    def create_user(self, user: User):
        self.cursor.execute('INSERT INTO users (name, surname, tg_id, course, group, type, admin) VALUES(?, ?, ?, ?, ?, ?)', (user.name, user.surname, user.tg_id, user.course, user.group, user.type, user.admin))
        self.conn.commit()

    def update_user(self, id, name):
        pass
    
    def remove_user(self, tg_id):
        self.cursor.execute('DELETE FROM users WHERE tg_id = ?', (tg_id))
        self.conn.commit()

    def add_task(self, task: Task):
        self.cursor.execute('INSERT INTO tasks (name, type, description, deadline, persons, creator_id, notify, completed) VALUES (?, ?, ?, ?, json(?), ?, ?, ?)', (task.name, task.type, task.description, task.deadline, task.persons, task.creator_id, task.notify, task.completed))

    def remove_task(self, task_id):
        pass

    def update_task(self, task_id, name, type, description, deadline, persons, notify):
        pass

    def get_task(self, task_id):
        return Task("1", "test_name", "test_type", "test_desc", datetime.now(), ["test_person_1", "test_person_2"], "test_creator", False, False)
    
    def __del__(self):
        self.conn.close()
    
db_provider = DBProvider()
def get_db_provider():
    return db_provider