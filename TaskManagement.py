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
        return self.userTasks

    def update(self, id, field, content):
        print('Update Called')
        super().updateTask(id, field, content)

    def delete(self, option, value):
        print('Delete called')
        super().deleteTask(option, value)
