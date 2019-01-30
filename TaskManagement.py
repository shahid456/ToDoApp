from TaskManagementMod import TaskManagementMod
import utilities


class TaskManagement (TaskManagementMod):
    def __init__(self, userId):
        print("Task management constructed")
        super().__init__(userId)

    def add(self, date, content):
        print("Add called")
        super().insertTask(date, content)

    def listByDate(self, date):
        print("List called By Date")
        for task in self.userTasks:
            if task['date'] == date:
                print(task)

    def listAsc(self):
        print("List called Ascending")
        tasks = utilities.myDateSort(self.userTasks.copy())
        for task in tasks:
            print(task)

    def listDesc(self):
        print("List called Descending")
        tasks = utilities.myDateSort(self.userTasks.copy())[::-1]
        for task in tasks:
            print(task)

    def count(self):
        print()

    def update(self, id, field, content):
        print('Update Called')
        super().updateTask(id, field, content)

    def delete(self, option, value):
        print('Delete called')
        super().deleteTask(option, value)


if __name__ == '__main__':
    task = TaskManagement('123')
    #task.add('12/13/14', 'Hello World')
    #task.add('13/01/14', 'Bye World')
    #task.add('14/02/14', 'Hello')
    #task.list('123')
