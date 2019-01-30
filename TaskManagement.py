from TaskManagementMod import TaskManagementMod


class TaskManagement (TaskManagementMod):
    def __init__(self, userId):
        print("Task management constructed")
        super().__init__(userId)

    def add(self, date, content):
        print("Add called")
        super().insertTask(date, content)

    def list(self, options):
        print("List called")
        for task in self.userTasks:
            print(task)

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
