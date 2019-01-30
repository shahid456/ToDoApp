from User_Management import User_Man
from TaskManagement import TaskManagement
import datetime


class Interface:
    def __init__(self):
        print("Constructor called")

    def register(self,command):
        if len(command) != 3:
            print("Invalid Expression")
            return
        user_man = User_Man()
        user_man.register(command[1], command[2])

    def login(self):
        user_man = User_Man()
        val = user_man.login()
        self.TM = TaskManagement(val)
        while True:
            log_commands_allowed = ["add", "list", "update", "delete", "logout"]
            log_enter = input("Task Manager > ")
            log_command = list(log_enter.split(" "))
            first_part_of_log_command = log_command[0]
            if first_part_of_log_command not in log_commands_allowed:
                print("Command not found")
                continue
            if first_part_of_log_command == log_commands_allowed[0]:
                if len(log_command) != 2:
                    print("Input date is not valid.")
                    continue
                inputDate, content = list(log_command[1].split(";"))
                day, month, year = inputDate.split('/')
                isValidDate = True
                try :
                    datetime.datetime(int(year),int(month),int(day))
                    self.TM.add(inputDate, content)
                except ValueError :
                    print("Date is not correct")
            elif first_part_of_log_command == log_commands_allowed[1]:
                if len(log_command) != 2:
                    print("Input date is not valid.")
                    continue
                options=["asc", "desc", "count"]
                if log_command[1] not in options:
                    inputDate = log_command[1]
                    day, month, year = inputDate.split('/')
                    try:
                        datetime.datetime(int(year), int(month), int(day))
                        self.TM.listByDate(log_command[1])
                    except ValueError:
                        print("Date is not correct")
                        continue
                else:
                    if log_command[1] == "asc":
                        self.TM.listAsc()
                    elif options == "desc":
                        self.TM.listDesc()
                    else:
                        self.TM.count()
            elif first_part_of_log_command == log_commands_allowed[2]:
                if len(log_command) != 3:
                    print("Input date is not valid.")
                    continue
                fields = list(log_command[2].split("="))
                if fields[0] == "date":
                    inputDate = fields[1]
                    day, month, year = inputDate.split('/')
                    try:
                        datetime.datetime(int(year), int(month), int(day))
                    except ValueError :
                        print("Input date is not valid..")
                        continue
                self.TM.update(val, fields[0], fields[1])
            elif first_part_of_log_command == log_commands_allowed[3]:
                if len(log_command) != 2:
                    print("Input data is not valid..")
                    continue
                try:
                    inputDate = log_command[1]
                    day, month, year = inputDate.split('/')
                    datetime.datetime(int(year), int(month), int(day))
                    self.TM.delete('date', log_command[1])
                except ValueError:
                    self.TM.delete('taskid', log_command[1])
                    continue
            elif first_part_of_log_command == log_commands_allowed[4]:
                    return




    def deleteuser(self,command):
        if len(command) == 2:
            user_man = User_Man()
            user_man.deleteuser(command[1])
        else:
            print("Invalid Expression")
    def listusers(self):
         user_man = User_Man()
         user_man.listusers()
    def updateuser(self,command):
        if len(command)==3:
            user_man = User_Man()
            user_man.userupdate(command[1],command[2])








if __name__ == '__main__':

    print("App started")
    interface = Interface()
    while(1):

        user_enter = input()
        command = list(user_enter.split(" "))
        commands_allowed = ["register", "login", "deleteuser", "listusers", "updateuser"]
        first_part_of_command = command[0]
        if first_part_of_command in commands_allowed:
            if first_part_of_command == commands_allowed[0]:
                interface.register(command)
            elif first_part_of_command == commands_allowed[1]:
                interface.login()
            elif first_part_of_command == commands_allowed[2]:
                interface.deleteuser(command)
            elif first_part_of_command == commands_allowed[3]:
                interface.listusers()
            elif first_part_of_command == commands_allowed[4]:
                interface.updateuser(command)
            print("Invalid Expression")
