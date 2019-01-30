from User_Management import User_Man

class Interface:

    def __init__(self):
        print("Constructor called")
    def register(self,command):
        if len(command) == 3:
            user_man = User_Man()
            user_man.register(command[1],command[2])
        else:
            print("Invalid Expression")
    def login(self):
        user_man = User_Man()
        val = user_man.login()
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
            field=command[2]
            field_split=list(field.split("="))
            user_man = User_Man()
            user_man.userupdate(command[1],field_split[0],field_split[1])
    def logout(self):
        user_man=User_Man()
        user_man.logout()








if __name__ == '__main__':
    print("App started")
    interface = Interface()
    user_enter = input()
    command = list(user_enter.split(" "))
    commands_allowed = ["register", "login", "deleteuser", "listusers", "updateuser", "logout"]
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
        elif first_part_of_command == commands_allowed[5]:
            interface.logout()
    else:
        print("Invalid Expression")
