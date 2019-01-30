from TaskManagementMod import TaskManagementMod


class TaskManagement (TaskManagementMod):
    def __init__(self, userId):
        super().__init__(userId)
        print("Task management constructed")

    def add(self, date, content):
        super().insertTask(date, content)
        print("Add called")

    def list(self, options):
        print("List called")
        return self.userTasks

    def update(self, id, field, content):
        print('Update Called')
        super().updateTask(id, field, content)

    def delete(self, option, value):
        print('Delete called')
