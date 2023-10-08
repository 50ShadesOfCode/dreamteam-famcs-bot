import sqlite3

from task import Task
from datetime import datetime

class DBProvider:

    def __init__(self):
        pass

    def if_admin(self, id):
        pass
    
    def create_person(self, id, name):
        pass

    def update_person(self, id, name):
        pass
    
    def remove_person(self, id, name):
        pass

    def add_task(self, name, type, description, deadline, persons, creator_id, notify):
        pass

    def remove_task(self, task_id):
        pass

    def update_task(self, task_id, name, type, description, deadline, persons, notify):
        pass

    def get_task(self, task_id):
        return Task("1", "test_name", "test_type", "test_desc", datetime.now(), ["test_person_1", "test_person_2"], "test_creator", False)