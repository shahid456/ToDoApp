from DatabaseManagement import DatabaseManagement
import utilities


class TaskManagementMod:
    def __init__(self, userId):
        print("Task Management constructor called")
        self.filename = 'tasks.json'
        self.userId = userId
        self.__tasks = []
        self.userTasks = []

        self.__database = DatabaseManagement(self.filename)
        self.__fetchUserTasks()

    def __fetchUserTasks(self):
        self.tasks = self.__database.read()
        for task in self.__tasks:
            if task['userid'] == self.userId:
                self.userTasks.append(task)

    def insertTask(self, date, content):
        task_id = utilities.generate_unique_id()
        task = {
            'taskid': task_id,
            'userid': self.userId,
            'date': date,
            'content': content
        }
        self.userTasks.append(task)
        self.tasks.append(task)
        self.__database.write(self.tasks)
        print("Task inserted")
