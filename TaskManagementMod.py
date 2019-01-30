from DatabaseManagement import DatabaseManagement
import utilities


class TaskManagementMod:
    def __init__(self):
        self.filename = 'tasks.json'
        database = DatabaseManagement(self.filename)
        print("Task Management constructor called")
