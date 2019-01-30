from User_Management import User_Man
from TaskManagement import TaskManagement
import datetime


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

        self.TM=TaskManagement(val)
        while(1):
            log_commands_allowed = ["add", "list", "update", "delete", "logout"]

            log_enter=input()
            log_command=list(log_enter.split(" "))
            first_part_of_log_command=log_command[0]
            if first_part_of_log_command in log_commands_allowed:
                if first_part_of_log_command == log_commands_allowed[0]:
                    if len(log_command)==2:
                        fields=list(log_command[1].split(";"))
                        inputDate = fields[0]
                        content = fields[1]
                        day,month,year = inputDate.split('/')
                        isValidDate = True
                        try :
                            datetime.datetime(int(year),int(month),int(day))
                        except ValueError :
                            isValidDate = False
                        if(isValidDate) :
                            self.TM.add(inputDate, content)
                        else :
                            print ("Input date is not valid..")

                elif first_part_of_log_command == log_commands_allowed[1]:
                    if len(log_command)==2:
                        options=["asc", "desc", "date","update"]
                        if log_command[1] in options:
                            if log_command[1] != options[0] and log_command[1] != options[1] and log_command[1] != options[3]:
                                inputDate = log_command[1]

                                day,month,year = inputDate.split('/')
                                isValidDate = True
                                try :
                                    datetime.datetime(int(year),int(month),int(day))
                                except ValueError :
                                    isValidDate = False
                                if(isValidDate) :
                                    self.TM.list(log_command[1])
                                else :
                                    print ("Input date is not valid..")
                            elif log_command[1] == options[0] or log_command[1] == options[1] or log_command[1] == options[3]:
                                    self.TM.list(log_command[1])

                elif first_part_of_log_command == log_commands_allowed[2]:
                    if len(log_command)==3:
                        fields=list(log_command[2].split("="))
                        if fields[0]=="date":
                            inputDate = fields[1]

                            day,month,year = inputDate.split('/')
                            isValidDate = True
                            try :
                                datetime.datetime(int(year),int(month),int(day))
                            except ValueError :
                                isValidDate = False
                            if(isValidDate) :
                                self.TM.update(val,fields[0],fields[1])
                            else :
                                print ("Input date is not valid..")
                        else:
                            self.TM.update(val,fields[0],fields[1])


                elif first_part_of_log_command == log_commands_allowed[3]:
                     if len(log_command)==2:
                         if isinstance(log_command[1], int)==False:
                             s="Date"
                             self.TM.delete(s,log_command[1])
                         elif isinstance(log_command[1], int):
                             s="ID"
                             self.TM.delete(s,log_command[1])


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
