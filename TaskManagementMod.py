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

    def insertTask(self, date, content):
        taskId = utilities.generate_unique_id()
        task = {
            'taskid': taskId,
            'userid': self.userId,
            'date': date,
            'content': content
        }
        self.userTasks.append(task)
        self.tasks.append(task)
        self.__database.write(self.tasks)
        print("Task inserted")

    def deleteTask(self, taskId):
        for x in range(len(self.userTasks)):
            if self.userTasks[x]['taskid'] == taskId:
                self.userTasks[x].pop()
                break
        for x in range(len(self.tasks)):
            if self.tasks[x]['taskid'] == taskId:
                self.tasks.pop(x)
                break
        self.__database.write(self.tasks)


    def updateTask(self, taskId, field, content):
        for x in range(len(self.userTasks)):
            if self.userTasks[x]['taskid'] == taskId:
                self.userTasks[x][field] = content
                break

        for x in range(len(self.tasks)):
            if self.tasks[x]['taskid'] == taskId:
                self.tasks[x][field] = content
                break

        self.__database.write(self.tasks)


    def __fetchUserTasks(self):
        self.tasks = self.__database.read()
        for task in self.__tasks:
            if task['userid'] == self.userId:
                self.userTasks.append(task)
