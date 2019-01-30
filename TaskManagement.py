from TaskManagementMod import TaskManagementMod


class TaskManagement (TaskManagementMod):
    def __init__(self):
        super().__init__()
        print("Task management constructed")

    def add(self, date, content):
        print("Add called")

    def list(self, options):
        print("List called")
        return []

    def update(self, id, field, content):
        print('Update Called')

    def delete(self, option, value):
        print('Delete called')
