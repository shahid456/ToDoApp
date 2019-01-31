from TaskManagementMod import TaskManagementMod
import utilities
import datetime


class TaskManagement (TaskManagementMod):
    def __init__(self, userId):
        super().__init__(userId)

    def add(self, date, content):
        super().insertTask(date, content)

    def list(self):
        for task in self.userTasks:
            print(task)

    def listByDate(self, date):
        for task in self.userTasks:
            if task['date'] == date:
                print(task)

    def listAsc(self):
        tasks = utilities.myDateSort(self.userTasks.copy())
        for task in tasks:
            print(task)

    def listDesc(self):
        tasks = utilities.myDateSort(self.userTasks.copy())[::-1]
        for task in tasks:
            print(task)

    def count(self):
        num = 0
        now = datetime.datetime.now()
        current = str(now).split(' ', 1)[0].replace('-', '')
        for task in self.userTasks:
            cmp = ''.join(task["date"].split('/')[::-1])
            if int(cmp) >= int(current):
                num += 1
        print(num)

    def update(self, id, field, content):
        super().updateTask(id, field, content)

    def delete(self, option, value):
        super().deleteTask(option, value)


